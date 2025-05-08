import os
import requests
from datetime import datetime
from typing import Dict, Any, Optional
from dotenv import load_dotenv

class WeatherService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
    def get_weather_data(self, location: str) -> Dict[str, Any]:
        """Fetch weather data for a given location"""
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'  # For Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Format the weather data
            weather_info = {
                "location": data['name'],
                "country": data['sys']['country'],
                "temperature": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "humidity": data['main']['humidity'],
                "pressure": data['main']['pressure'],
                "weather_description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed'],
                "timestamp": datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return weather_info
            
        except Exception as e:
            raise Exception(f"Error fetching weather data: {str(e)}")
            
    def format_weather_prompt(self, weather_data: Dict[str, Any]) -> str:
        """Format weather data into a prompt for the LLM"""
        return f"""Based on the following weather data for {weather_data['location']}, {weather_data['country']}:
        - Temperature: {weather_data['temperature']}°C
        - Feels like: {weather_data['feels_like']}°C
        - Weather: {weather_data['weather_description']}
        - Humidity: {weather_data['humidity']}%
        - Wind Speed: {weather_data['wind_speed']} m/s
        - Pressure: {weather_data['pressure']} hPa
        - Time: {weather_data['timestamp']}
        
        Please provide a natural, conversational summary of the current weather conditions and some relevant advice or insights.""" 