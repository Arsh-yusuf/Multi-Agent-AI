# 🚀 Multi-Agent Launch Intelligence

A modular multi-agent system that interprets user goals and uses public APIs (SpaceX, WeatherAPI, NewsAPI) to deliver launch-related insights.

## Features

- 🤖 Planner Agent: Interprets user goals and plans agent execution
- 📡 Launch Info Agent: Fetches the next space launch
- 🌦 Weather Agent: Gets forecast for the launch site
- 📰 News Agent: Pulls mission-related news
- 🧠 Summary Agent: Provides a final decision or report

## Setup

1. Clone the repo or unzip:
   ```bash
   git clone https://github.com/your-username/multi_agent_system.git
   cd multi_agent_system


2. Install dependencies
   pip install -r requirements.txt


3. Create a .env file with your keys:
   WEATHERAPI_KEY=your_key
   NEWSAPI_KEY=your_key

4. Run the app
   streamlit run app.py

