from fastapi import FastAPI, Request
from agents.core_agent import AetherAgent

app = FastAPI()
agent = AetherAgent()

@app.get("/")
def root():
    return {"status": "Agent running"}

@app.post("/run-task")
async def run_task(request: Request):
    data = await request.json()
    task_type = data.get("type")
    payload = data.get("payload", {})
    result = agent.run_task(task_type, payload)
    return result