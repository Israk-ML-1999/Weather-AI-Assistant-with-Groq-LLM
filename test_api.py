import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_root():
    """Test the root endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print("\n=== Root Endpoint ===")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_weather():
    """Test the weather endpoint"""
    # Example weather request
    weather_data = {
        "location": "London, UK"
    }
    
    print("\n=== Weather Endpoint ===")
    print("Request Body:", json.dumps(weather_data, indent=2))
    
    response = requests.post(
        f"{BASE_URL}/weather",
        json=weather_data
    )
    
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_chat():
    """Test the chat endpoint"""
    # Example chat request
    chat_data = {
        "prompt": "What's the weather like in New York?"
    }
    
    print("\n=== Chat Endpoint ===")
    print("Request Body:", json.dumps(chat_data, indent=2))
    
    response = requests.post(
        f"{BASE_URL}/chat",
        json=chat_data
    )
    
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_context():
    """Test the context endpoints"""
    # Get context
    print("\n=== Get Context Endpoint ===")
    response = requests.get(f"{BASE_URL}/context")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))
    
    # Clear context
    print("\n=== Clear Context Endpoint ===")
    response = requests.delete(f"{BASE_URL}/context")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    print("Testing Weather AI Assistant API")
    print("Make sure the server is running at http://localhost:8000")
    
    try:
        test_root()
        test_weather()
        test_chat()
        test_context()
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Make sure it's running at http://localhost:8000")
    except Exception as e:
        print(f"\nError: {str(e)}") 