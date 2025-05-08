# MCP Project with Groq LLM Integration

This project implements a Model-Controller-Presenter (MCP) architecture pattern with Groq LLM integration.

## Project Structure
```
mcp_project/
├── app/
│   ├── models/         # Data models and business logic
│   ├── controllers/    # Request handling and business logic coordination
│   ├── presenters/     # Response formatting and view logic
│   └── services/       # External service integrations (Groq API)
├── config/            # Configuration files
├── tests/             # Test files
└── main.py           # Application entry point
```

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## Features
- MCP Architecture implementation
- Groq LLM integration
- FastAPI backend
- Environment-based configuration
- Modular and extensible design