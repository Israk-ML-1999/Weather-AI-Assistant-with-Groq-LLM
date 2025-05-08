import streamlit as st
from app.models.llm_model import LLMModel, LLMRequest
from app.services.mcp_server import MCPServer
from app.config.mcp_config import MCPConfig
import time

# Set page config
st.set_page_config(
    page_title="Weather AI Assistant",
    page_icon="🌤️",
    layout="wide"
)

# Initialize MCP components
@st.cache_resource
def initialize_mcp():
    config = MCPConfig()
    mcp_server = MCPServer(config)
    model = LLMModel()
    return model, mcp_server

model, mcp_server = initialize_mcp()

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .response-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .weather-box {
        background-color: #e6f3ff;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .insights-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .context-info {
        font-size: 0.8em;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🌤️ Weather AI Assistant")
st.markdown("""
Get real-time weather data and AI-powered insights for any location.
""")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Weather", "Chat"])

with tab1:
    # Weather input
    location = st.text_input(
        "Enter location (city, country):",
        placeholder="Example: London, UK"
    )
    
    if st.button("Get Weather", type="primary"):
        if location:
            with st.spinner("Fetching weather data and generating insights..."):
                try:
                    # Get weather data and insights
                    response = mcp_server.process_weather_request(location)
                    weather_data = response["weather_data"]
                    insights = response["insights"]
                    
                    # Display weather data
                    st.markdown("### Current Weather")
                    st.markdown(f"""
                    <div class="weather-box">
                        <h3>{weather_data['location']}, {weather_data['country']}</h3>
                        <p>Temperature: {weather_data['temperature']}°C (Feels like: {weather_data['feels_like']}°C)</p>
                        <p>Weather: {weather_data['weather_description']}</p>
                        <p>Humidity: {weather_data['humidity']}%</p>
                        <p>Wind Speed: {weather_data['wind_speed']} m/s</p>
                        <p>Pressure: {weather_data['pressure']} hPa</p>
                        <p>Last Updated: {weather_data['timestamp']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display AI insights
                    st.markdown("### AI Insights")
                    st.markdown(f'<div class="insights-box">{insights}</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a location!")

with tab2:
    # Chat interface
    prompt = st.text_area(
        "Enter your question or prompt:",
        height=150,
        placeholder="Example: What's the weather like in New York?"
    )
    
    if st.button("Get Response", type="primary"):
        if prompt:
            with st.spinner("Generating response..."):
                try:
                    # Use MCP pattern to process the request
                    request = model.format_request(prompt)
                    response = mcp_server.process_request(request)
                    
                    if response.error:
                        st.error(f"Error: {response.error}")
                    else:
                        # Display response in a nice box
                        st.markdown("### Response:")
                        st.markdown(f'<div class="response-box">{response.content}</div>', unsafe_allow_html=True)
                        
                        # Show context info
                        st.markdown(f'<div class="context-info">Context length: {len(mcp_server.context_history)} messages</div>', 
                                  unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a prompt first!")

# Sidebar for MCP settings
with st.sidebar:
    st.header("MCP Settings")
    if st.button("Clear Context"):
        mcp_server.clear_context()
        st.success("Context cleared!")
    
    st.subheader("Context Summary")
    context_summary = mcp_server.get_context_summary()
    st.json(context_summary)

# Add footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit, OpenWeather API, and Groq LLM") 