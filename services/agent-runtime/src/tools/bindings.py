import os
import requests

TOOL_GATEWAY_URL = os.getenv("TOOL_GATEWAY_URL", "http://localhost:8080")

def search_kb(query: str) -> list[str]:
    r = requests.post(
        f"{TOOL_GATEWAY_URL}/tools/search_kb",
        json={"query": query},
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()
    return data.get("results", [])
