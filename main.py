from agents import planner_agent, launch_info_agent, weather_agent, summary_agent

def main():
    print("🔍 User Goal: Find next SpaceX launch and assess delay risk from weather.")
    
    # Step 1: Planning
    steps = planner_agent.create_plan("next SpaceX launch weather delay prediction")

    # Step 2: Launch Info
    launch = launch_info_agent.get_next_launch()
    site_name, city = launch_info_agent.get_launchpad_location(launch["launchpad_id"])

    # Step 3: Weather
    weather = weather_agent.get_weather(city)

    # Step 4: Summary
    location = {"name": site_name, "city": city}
    result = summary_agent.summarize(launch, location, weather)

    print("\n📢 FINAL RESULT\n" + result)

if __name__ == "__main__":
    main()
