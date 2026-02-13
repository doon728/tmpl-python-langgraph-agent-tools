from fastapi import FastAPI, HTTPException
from src.contracts.envelope import ToolRequest, ToolResponse
from src.tools.search_kb import search_kb

app = FastAPI(title="Tool Gateway")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/tools/invoke", response_model=ToolResponse)
def invoke_tool(req: ToolRequest):
    try:
        if req.tool_name == "search_kb":
            query = str(req.input.get("query", ""))
            out = search_kb(query)
            return {"contract_version": "v1", "tool_name": tool_name, "ok": True, "output": output, "error": None}

        raise HTTPException(status_code=404, detail=f"Unknown tool: {req.tool_name}")

    except HTTPException:
        raise
    except Exception as e:
        return {"contract_version": "v1", "tool_name": tool_name, "ok": False, "output": None, "error": {"code":"TOOL_FAILED","message": str(e), "details": {}}}

