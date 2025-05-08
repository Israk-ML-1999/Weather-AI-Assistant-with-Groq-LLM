import requests
import json

def test_generate(prompt):
    url = "http://localhost:8000/generate"
    
    print(f"\nTesting prompt: {prompt}")
    print("-" * 80)
    
    response = requests.post(url, json={"prompt": prompt})
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))

def run_tests():
    test_prompts = [
        # AI Fundamentals
        "Explain the difference between narrow AI and general AI with examples",
        
        # Machine Learning
        "Compare and contrast supervised, unsupervised, and reinforcement learning with real-world applications",
        
        # Deep Learning
        "Explain the architecture of a transformer model and its role in modern NLP",
        
        # NLP Specific
        "What are the key challenges in natural language understanding and how are they being addressed?",
        
        # Practical Applications
        "How is deep learning being used in computer vision applications?",
        
        # Advanced Topics
        "Explain the concept of transfer learning in deep neural networks with examples",
        
        # Current Trends
        "What are the latest developments in large language models and their applications?"
    ]
    
    for prompt in test_prompts:
        test_generate(prompt)

if __name__ == "__main__":
    run_tests() 