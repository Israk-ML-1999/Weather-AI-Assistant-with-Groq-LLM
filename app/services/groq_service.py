import os
from groq import Groq
from dotenv import load_dotenv
from typing import List, Dict, Any, Union

class GroqService:
    def __init__(self):
        load_dotenv()
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama3-70b-8192"  # Using the correct model
        self.system_prompt = """You are a weather expert and meteorologist who provides accurate, helpful, and natural explanations about weather conditions.
        Focus on providing practical insights, weather safety tips, and relevant recommendations based on current weather conditions."""

    def generate_completion(self, prompt: Union[str, List[Dict[str, str]]], **kwargs) -> str:
        try:
            # Handle both string prompts and message lists
            if isinstance(prompt, str):
                messages = [
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            else:
                messages = prompt

            completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=kwargs.get('temperature', 0.7),
                max_tokens=kwargs.get('max_tokens', 1024),
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")
