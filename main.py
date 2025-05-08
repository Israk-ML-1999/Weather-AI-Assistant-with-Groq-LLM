from fastapi import FastAPI
from app.controllers.llm_controller import LLMController
from app.presenters.response_presenter import ResponsePresenter
from app.services.groq_service import GroqService

app = FastAPI(title="MCP Project with Groq LLM")

# Initialize services
groq_service = GroqService()
response_presenter = ResponsePresenter()
llm_controller = LLMController(groq_service, response_presenter)

@app.get("/")
async def root():
    return {"message": "Welcome to MCP Project with Groq LLM"}

@app.post("/generate")
async def generate_text(prompt: str):
    return await llm_controller.generate_response(prompt) 