import ollama
import json

def generate_html_from_prompt(prompt, config):
    model = config.get("model", "llama2")
    response = ollama.generate(model=model, prompt=prompt)
    html_content = f"<html><body><h1>{prompt}</h1><p>{response['content']}</p></body></html>"
    output_path = "/tmp/pitchathonz.html"
    with open(output_path, "w") as f:
        f.write(html_content)
    return output_path
