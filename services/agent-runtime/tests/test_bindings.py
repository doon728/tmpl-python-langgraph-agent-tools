from unittest.mock import MagicMock, patch

from src.tools.bindings import CONTRACT_VERSION, search_kb


@patch("src.tools.bindings.requests.post")
def test_search_kb(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {
        "contract_version": CONTRACT_VERSION,
        "tool_name": "search_kb",
        "ok": True,
        "output": {"results": ["a", "b"]},
        "error": None,
    }
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    out = search_kb("hi")
    assert out == ["a", "b"]
