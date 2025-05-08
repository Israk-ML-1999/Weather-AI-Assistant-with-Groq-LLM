from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class MCPConfig:
    """MCP Server Configuration"""
    model_name: str = "llama2-70b-4096"
    max_tokens: int = 1024
    temperature: float = 0.7
    context_window: int = 4096
    tools_enabled: bool = True
    
    # Tool configurations
    available_tools: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.available_tools is None:
            self.available_tools = {
                "code_generation": True,
                "data_analysis": True,
                "web_search": False,
                "file_operations": False
            }
    
    @property
    def model_settings(self) -> Dict[str, Any]:
        return {
            "model": self.model_name,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "context_window": self.context_window
        } 