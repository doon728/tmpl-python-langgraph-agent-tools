from __future__ import annotations

from typing import Any, Dict, Optional, Callable

from fastapi import FastAPI, Request
from pydantic import BaseModel

from src.contract import (
    CONTRACT_VERSION,
    ok_response,
    err_response,
)

app = FastAPI(title="Tool Gateway", version=CONTRACT_VERSION)


# -----------------------
# Request/Response Models
# -----------------------
class ToolInvokeRequestModel(BaseModel):
    contract_version: str = CONTRACT_VERSION
    tool_name: str
    input: Dict[str, Any]
    tenant_id: Optional[str] = None
    user_id: Optional[str] = None
    correlation_id: Optional[str] = None


# -----------------------
# Minimal auth/context middleware (stub)
# -----------------------
@app.middleware("http")
async def log_context(request: Request, call_next: Callable):
    # Prefer headers if present; fall back to body fields (handled in endpoint)
    tenant_id = request.headers.get("x-tenant-id")
    user_id = request.headers.get("x-user-id")
    correlation_id = request.headers.get("x-correlation-id")

    # Log is intentionally minimal; later you can swap to structured logging / OTel
    print(
        f"[tool-gateway] {request.method} {request.url.path} "
        f"tenant={tenant_id} user={user_id} corr={correlation_id}"
    )

    response = await call_next(request)
    return response


# -----------------------
# Tool Implementations
# -----------------------
def search_kb(input_data: Dict[str, Any]) -> Dict[str, Any]:
    query = (input_data.get("query") or "").strip()
    if not query:
        return {"results": []}

    return {
        "results": [
            {
                "id": "doc-001",
                "title": "Sample KB Doc",
                "score": 0.87,
                "snippet": f"Matched on: {query}",
            }
        ]
    }


def get_member(input_data: Dict[str, Any]) -> Dict[str, Any]:
    member_id = (input_data.get("member_id") or "").strip()
    if not member_id:
        return {"member": None}

    # Stubbed member record
    return {
        "member": {
            "member_id": member_id,
            "first_name": "Jane",
            "last_name": "Doe",
            "dob": "1990-01-01",
            "plan": "SamplePlan",
        }
    }


def write_case_note(input_data: Dict[str, Any]) -> Dict[str, Any]:
    case_id = (input_data.get("case_id") or "").strip()
    note = (input_data.get("note") or "").strip()

    if not case_id or not note:
        return {"written": False, "note_id": None}

    # Stubbed “write” response
    return {"written": True, "note_id": "note-001"}


TOOL_REGISTRY: Dict[str, Any] = {
    "search_kb": search_kb,
    "get_member": get_member,
    "write_case_note": write_case_note,
}


# -----------------------
# Endpoints
# -----------------------
@app.get("/health")
def health() -> dict:
    # Keep this stable for liveness probes + tests
    return {"ok": True, "contract_version": CONTRACT_VERSION}


@app.post("/tools/invoke")
def invoke_tool(req: ToolInvokeRequestModel) -> dict:
    # Contract version check (agent + gateway must match)
    if req.contract_version != CONTRACT_VERSION:
        return err_response(
            tool_name=req.tool_name,
            code="CONTRACT_VERSION_MISMATCH",
            message=f"Expected {CONTRACT_VERSION}, got {req.contract_version}",
        )

    handler = TOOL_REGISTRY.get(req.tool_name)
    if handler is None:
        return err_response(
            tool_name=req.tool_name,
            code="UNKNOWN_TOOL",
            message=f"Unknown tool: {req.tool_name}",
        )

    try:
        output = handler(req.input)
        return ok_response(req.tool_name, output)
    except Exception as e:
        return err_response(
            tool_name=req.tool_name,
            code="TOOL_EXECUTION_ERROR",
            message=str(e),
        )
