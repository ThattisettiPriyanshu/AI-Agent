import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Define the Search Tool
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 2. Streamlit UI Setup
st.set_page_config(page_title="Wanderlust AI", page_icon="✈️", layout="centered")

# Inject beautiful, responsive background image with a dark overlay to maintain perfect readability
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=2000&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: transparent;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("✈️ Wanderlust AI")
st.markdown("Your personal AI travel agent. Tell me where you want to go, and I'll search the web to build your perfect itinerary.")

# Sidebar for API Key configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
st.sidebar.markdown("[Get a free Gemini API key here](https://aistudio.google.com/app/apikey)")

# Input Form
with st.form("travel_form"):
    destination = st.text_input("Where do you want to go?", placeholder="e.g. Tokyo, Japan")
    days = st.number_input("How many days?", min_value=1, max_value=14, value=3)
    interests = st.text_input("What are your interests?", placeholder="e.g. Food, Museums, Hidden Gems")
    submitted = st.form_submit_button("Build My Itinerary 🚀")

if submitted:
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar first!")
    elif not destination:
        st.warning("Please enter a destination.")
    else:
        # 3. Agent Initialization
        os.environ["GOOGLE_API_KEY"] = api_key
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
        
        system_message = """You are a highly experienced, luxury Travel Concierge Agent.
        Your job is to build a highly structured, day-by-day travel itinerary for the user based on their destination and interests.
        
        Instructions:
        1. SPEED REQUIREMENT: You must execute exactly ONE search query combining the destination and interests. Do not do multiple searches. After your first search, immediately write the final itinerary.
        2. Do not hallucinate places that don't exist. Verify them using your one search.
        3. Create a day-by-day itinerary. For each day, provide a Morning, Afternoon, and Evening activity with specific restaurant recommendations.
        4. CRITICAL: For every restaurant or attraction you suggest, you MUST include its star rating/reviews (if found) and a clickable Markdown link to its website or a Google Maps search link.
        5. Format your final output cleanly using Markdown headers and bullet points. Make it look beautiful and easy to read.
        """

        agent_executor = create_react_agent(llm, tools)

        with st.spinner(f"Searching the web for the best things to do in {destination}..."):
            try:
                prompt_text = f"I am going to {destination} for {days} days. My interests are: {interests}. Please build my itinerary."
                messages = [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt_text}
                ]
                
                # Run the agent
                response = agent_executor.invoke({"messages": messages})
                
                # Display the response
                st.markdown("### Your Custom Itinerary 🗺️")
                
                # LangGraph sometimes returns content as a list of JSON blocks. We extract the text here:
                final_content = response["messages"][-1].content
                if isinstance(final_content, list):
                    final_text = "".join(block.get("text", "") for block in final_content if block.get("type") == "text")
                else:
                    final_text = final_content
                    
                st.markdown(final_text)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
