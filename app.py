import streamlit as st
from agents import launch_info_agent, weather_agent, summary_agent, news_agent
from agents.planner_agent import plan

st.title("🚀 Multi-Agent Launch Intelligence")

user_goal = st.text_input("🎯 Enter your goal:")

if user_goal:
    st.markdown("🧠 **Interpreting Goal...**")
    steps = plan(user_goal)
    st.markdown("🔧 **Plan generated:**")
    st.json(steps)

    memory = {}

    for step in steps:
        try:
            if step == "launch_info_agent":
                launch = launch_info_agent.get_next_launch()
                memory["launch"] = launch
                st.markdown("🚀 **Launch Info:**")
                st.json(launch)

            elif step == "weather_agent":
                if "launch" not in memory:
                    st.error("❌ Launch info missing. Cannot fetch weather.")
                    break

                city = memory["launch"]["location"]["city"]
                weather = weather_agent.get_weather(city)
                memory["weather"] = weather
                st.markdown("🌦 **Weather:**")
                st.json(weather)
                
            elif step == "news_agent":
                if "launch" not in memory:
                    st.error("❌ Launch info required to fetch news.")
                    break

                mission = memory["launch"]["mission"]
                news = news_agent.get_news(mission)
                st.markdown("📰 **Latest News**")
                st.text(news)


            elif step == "summary_agent":
                if "launch" not in memory or "weather" not in memory:
                    st.error("❌ Required data missing for summary.")
                    break

                summary = summary_agent.summarize(
                    memory["launch"],
                    memory["weather"]
                )
                st.markdown("📡 **Summary**")
                st.text(summary)

        except Exception as e:
            st.error(f"⚠️ Error in step `{step}`: {e}")
            break

