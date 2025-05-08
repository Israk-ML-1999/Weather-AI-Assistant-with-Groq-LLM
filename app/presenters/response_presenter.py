


from datetime import datetime

class ResponsePresenter:
    def format_response(self, completion: str) -> dict:
        return {
            "status": "success",
            "data": {
                "completion": completion,
                "timestamp": datetime.utcnow().isoformat()
            }
        }

    def format_error(self, error_message: str) -> dict:
        return {
            "status": "error",
            "error": {
                "message": error_message,
                "timestamp": datetime.utcnow().isoformat()
            }
        } 