from app.services.groq_service import GroqService
from app.presenters.response_presenter import ResponsePresenter

class LLMController:
    def __init__(self, groq_service: GroqService, response_presenter: ResponsePresenter):
        self.groq_service = groq_service
        self.response_presenter = response_presenter

    async def generate_response(self, prompt: str) -> dict:
        try:
            # Get completion from Groq service
            completion =  self.groq_service.generate_completion(prompt)
            
            # Format response using presenter
            return self.response_presenter.format_response(completion)
        except Exception as e:
            return self.response_presenter.format_error(str(e)) 