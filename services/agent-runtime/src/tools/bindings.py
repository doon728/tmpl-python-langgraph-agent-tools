import os
import requests

TOOL_GATEWAY_URL = os.getenv("TOOL_GATEWAY_URL", "http://localhost:8080")

def search_kb(query: str) -> list[dict]:
    payload = {
        "tool_name": "search_kb",
        "input": {"query": query},
        "tenant_id": os.getenv("TENANT_ID"),
        "user_id": os.getenv("USER_ID"),
        "correlation_id": os.getenv("CORRELATION_ID"),
    }

    r = requests.post(f"{TOOL_GATEWAY_URL}/tools/invoke", json=payload, timeout=10)
    r.raise_for_status()
    body = r.json()

    if not body.get("ok"):
        raise RuntimeError(body.get("error", {}).get("message", "Tool call failed"))

    return body["output"]["results"]
