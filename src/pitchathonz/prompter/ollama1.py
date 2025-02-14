import ollama

def generate_response(prompt, model="llama2"):
    response = ollama.generate(model=model, prompt=prompt)
    return response['content']
