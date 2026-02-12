from unittest.mock import patch
from src.graph.build_graph import run_graph

@patch("src.tools.bindings.requests.post")
def test_graph_runs(mock_post):
    mock_post.return_value.raise_for_status.return_value = None
    mock_post.return_value.json.return_value = {"results": ["ok"]}
    out = run_graph("hello")
    assert "RESULTS" in out
