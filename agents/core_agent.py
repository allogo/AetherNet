import yaml
from agents.tasks.text_generation import generate_text

class AetherAgent:
    def __init__(self, config_path="config/agent_config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def run_task(self, task_type: str, payload: dict):
        if task_type == "text_generation":
            return generate_text(payload.get("prompt", ""))
        return {"error": "Unsupported task type"}