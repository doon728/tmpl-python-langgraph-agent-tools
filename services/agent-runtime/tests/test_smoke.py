from src.graph.build_graph import run_graph

def test_graph_runs():
    assert run_graph("hello") == "hello"
