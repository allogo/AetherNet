from agents.core_agent import AetherAgent

def test_text_generation():
    agent = AetherAgent()
    res = agent.run_task("text_generation", {"prompt": "test"})
    assert "result" in res