import os
import requests
import logging
from config.settings import get_config
logger = logging.getLogger(__name__)

def search_kb(query: str) -> list[str]:
    """
    Search knowledge base using configuration-driven approach
    """
    # Get tool gateway URL from configuration
    tool_gateway_url = get_config('tool_gateway.url', 'http://localhost:8080')
    timeout = get_config('tool_gateway.timeout', 10)

    try:
        r = requests.post(
            f"{tool_gateway_url}/tools/search_kb",
            json={"query": query},
            timeout=timeout
        )
        r.raise_for_status()
        data = r.json()
        return data.get("results", [])
    except requests.RequestException as e:
        # Log the error using our new logging system
        logger.error(f"Tool gateway call failed: {e}")
        return []
