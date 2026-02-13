from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel


CONTRACT_VERSION = "v1"


app = FastAPI(title="Tool Gateway", version=CONTRACT_VERSION)


# -----------------------
# Request/Response Models
# -----------------------
class ToolInvokeRequest(BaseModel):
    contract_version: str = CONTRACT_VERSION
    tool_name: str
    input: Dict[str, Any]
    tenant_id: Optional[str] = None
    user_id: Optional[str] = None
    correlation_id: Optional[str] = None


class ToolError(BaseModel):
    code: str
    message: str


class ToolInvokeResponse(BaseModel):
    contract_version: str = CONTRACT_VERSION
    tool_name: str
    ok: bool
    output: Optional[Dict[str, Any]] = None
    error: Optional[ToolError] = None


# -----------------------
# Tool Implementations
# -----------------------
def search_kb(input_data: Dict[str, Any]) -> Dict[str, Any]:
    query = (input_data.get("query") or "").strip()
    if not query:
        return {"results": []}

    # Stubbed KB result (replace later with real KB/DB integration)
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


TOOL_REGISTRY = {
    "search_kb": search_kb,
}


# -----------------------
# Endpoints
# -----------------------
@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.post("/tools/invoke", response_model=ToolInvokeResponse)
def invoke_tool(req: ToolInvokeRequest) -> ToolInvokeResponse:
    # Contract version check (keeps agent + gateway in sync)
    if req.contract_version != CONTRACT_VERSION:
        return ToolInvokeResponse(
            contract_version=CONTRACT_VERSION,
            tool_name=req.tool_name,
            ok=False,
            error=ToolError(
                code="CONTRACT_VERSION_MISMATCH",
                message=f"Expected {CONTRACT_VERSION}, got {req.contract_version}",
            ),
        )

    handler = TOOL_REGISTRY.get(req.tool_name)
    if handler is None:
        return ToolInvokeResponse(
            contract_version=CONTRACT_VERSION,
            tool_name=req.tool_name,
            ok=False,
            error=ToolError(
                code="UNKNOWN_TOOL",
                message=f"Unknown tool: {req.tool_name}",
            ),
        )

    try:
        output = handler(req.input)
        return ToolInvokeResponse(
            contract_version=CONTRACT_VERSION,
            tool_name=req.tool_name,
            ok=True,
            output=output,
            error=None,
        )
    except Exception as e:
        return ToolInvokeResponse(
            contract_version=CONTRACT_VERSION,
            tool_name=req.tool_name,
            ok=False,
            error=ToolError(code="TOOL_EXECUTION_ERROR", message=str(e)),
        )
