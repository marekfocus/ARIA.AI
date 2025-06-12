import requests
import json

def send_to_mistral(prompt):
    response = requests.post(
        "http://localhost:5000/mistral",
        json={"prompt": prompt}
    )
    return response.json()

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return send_to_mistral(f"Analyze this legal content:\n\n{content}")
