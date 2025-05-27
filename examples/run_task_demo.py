import requests, json

resp = requests.post("http://localhost:8000/run-task",
                     json={"type": "text_generation",
                           "payload": {"prompt": "Hello world"}})
print(resp.json())