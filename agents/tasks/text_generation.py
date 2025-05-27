from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt: str):
    output = generator(prompt, max_length=100, num_return_sequences=1)
    return {"result": output[0]["generated_text"]}