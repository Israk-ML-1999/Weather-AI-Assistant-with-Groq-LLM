import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.services.mcp_server import MCPServer
from app.config.mcp_config import MCPConfig
from app.models.llm_model import LLMRequest

app = FastAPI(title="Weather AI Assistant with Groq LLM")

# Initialize MCP server
config = MCPConfig()
mcp_server = MCPServer(config)

class WeatherRequest(BaseModel):
    location: str

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to Weather AI Assistant",
        "endpoints": {
            "/weather": "Get weather data and insights for a location",
            "/chat": "Chat with the AI assistant"
        }
    }

@app.post("/weather")
async def get_weather(request: WeatherRequest) -> Dict[str, Any]:
    try:
        response = mcp_server.process_weather_request(request.location)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest) -> Dict[str, Any]:
    try:
        llm_request = LLMRequest(prompt=request.prompt)
        response = mcp_server.process_request(llm_request)
        return {
            "content": response.content,
            "error": response.error
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/context")
async def get_context():
    """Get the current context summary"""
    return mcp_server.get_context_summary()

@app.delete("/context")
async def clear_context():
    """Clear the conversation context"""
    mcp_server.clear_context()
    return {"message": "Context cleared successfully"} 