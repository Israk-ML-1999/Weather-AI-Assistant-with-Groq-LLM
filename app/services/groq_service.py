import os
from groq import Groq
from dotenv import load_dotenv

class GroqService:
    def __init__(self):
        load_dotenv()
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama3-70b-8192"  # Using the correct model
        self.system_prompt = """You are an expert in Artificial Intelligence, Machine Learning, Deep Learning, and Natural Language Processing. 
        Provide detailed, accurate, and technical explanations while maintaining clarity. 
        Focus on practical applications and current state-of-the-art approaches."""

    def generate_completion(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=1024,
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")
