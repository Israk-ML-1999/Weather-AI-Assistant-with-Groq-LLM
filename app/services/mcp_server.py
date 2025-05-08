from typing import Dict, Any, Optional
from app.config.mcp_config import MCPConfig
from app.models.llm_model import LLMRequest, LLMResponse
from app.services.groq_service import GroqService
from app.services.weather_service import WeatherService

class MCPServer:
    def __init__(self, config: Optional[MCPConfig] = None):
        self.config = config or MCPConfig()
        self.groq_service = GroqService()
        self.weather_service = WeatherService()
        self.context_history = []
        self.max_history_length = 10

    def add_to_context(self, message: Dict[str, Any]):
        """Add a message to the context history"""
        self.context_history.append(message)
        if len(self.context_history) > self.max_history_length:
            self.context_history.pop(0)

    def clear_context(self):
        """Clear the context history"""
        self.context_history = []

    def process_weather_request(self, location: str) -> Dict[str, Any]:
        """Process a weather request and generate insights"""
        try:
            # Get weather data
            weather_data = self.weather_service.get_weather_data(location)
            
            # Format weather data into a prompt
            weather_prompt = self.weather_service.format_weather_prompt(weather_data)
            
            # Get LLM insights
            insights = self.groq_service.generate_completion(
                prompt=weather_prompt,
                temperature=self.config.model_settings.get('temperature', 0.7),
                max_tokens=self.config.model_settings.get('max_tokens', 1024)
            )
            
            # Combine weather data and insights
            response = {
                "weather_data": weather_data,
                "insights": insights
            }
            
            return response
            
        except Exception as e:
            raise Exception(f"Error processing weather request: {str(e)}")

    def process_request(self, request: LLMRequest) -> LLMResponse:
        """Process an MCP request with context"""
        try:
            # Add request to context
            self.add_to_context({
                "role": "user",
                "content": request.prompt
            })

            # Get completion from Groq
            completion = self.groq_service.generate_completion(
                prompt=request.prompt,
                temperature=self.config.model_settings.get('temperature', 0.7),
                max_tokens=self.config.model_settings.get('max_tokens', 1024)
            )

            # Add response to context
            self.add_to_context({
                "role": "assistant",
                "content": completion
            })

            return LLMResponse(content=completion)

        except Exception as e:
            return LLMResponse(content="", error=str(e))

    def get_context_summary(self) -> Dict[str, Any]:
        """Get a summary of the current context"""
        return {
            "history_length": len(self.context_history),
            "available_tools": self.config.available_tools,
            "model_settings": self.config.model_settings
        } 