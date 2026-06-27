# ✈️ AI Travel Concierge

An intelligent, autonomous travel agent built with **LangGraph**, **Streamlit**, and **Google Gemini** for the Google & Kaggle AI Capstone Project. 

## 🌟 Overview
The AI Travel Concierge takes your dream destination and personal interests, searches the web for current, real-world data, and automatically generates a highly structured, day-by-day luxury travel itinerary.

Unlike standard chatbots, this is a true **Agent** that is equipped with a Web Search tool. It verifies its recommendations and provides you with ratings, reviews, and clickable links for every restaurant and attraction it suggests!

## 🚀 Features
- **Intelligent Web Search**: Uses the `duckduckgo-search` API to find real-time data instead of hallucinating.
- **Beautiful UI**: Built on Streamlit with a clean, dark-mode native aesthetic and a premium travel banner.
- **Structured Output**: Generates clean, day-by-day Markdown itineraries.
- **Actionable Links**: Provides Google Maps/Website links for every recommendation.

## 🛠️ Tech Stack
- **Python**
- **Streamlit**: For the frontend user interface.
- **LangGraph**: To handle the complex Agent reasoning and tool-calling loop.
- **Google Gemini (gemini-2.5-flash)**: The core LLM engine powering the agent.
- **DuckDuckGo Search (`ddgs`)**: For real-time web scraping.

## 💻 How to Run Locally

### Prerequisites
1. Get a **Free Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Ensure you have Python installed.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ThattisettiPriyanshu/AI-Agent.git
   cd AI-Agent
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Open your browser to `http://localhost:8501`, enter your API key, and start planning your next trip!
