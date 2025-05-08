from dataclasses import dataclass
from typing import Optional

@dataclass
class LLMRequest:
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 1024
    model: str = "llama3-70b-8192"

@dataclass
class LLMResponse:
    content: str
    error: Optional[str] = None
    timestamp: Optional[str] = None

class LLMModel:
    def __init__(self):
        self.system_prompt = """You are a weather expert and meteorologist who provides accurate, helpful, and natural explanations about weather conditions.
        Focus on providing practical insights, weather safety tips, and relevant recommendations based on current weather conditions."""
    
    def format_request(self, prompt: str) -> LLMRequest:
        """Format the user's prompt into a structured request"""
        return LLMRequest(prompt=prompt)
    
    def format_response(self, content: str, error: str = None) -> LLMResponse:
        """Format the LLM's response into a structured response"""
        return LLMResponse(content=content, error=error) 