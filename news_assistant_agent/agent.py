import datetime
import os

from zoneinfo import ZoneInfo
from google.adk.agents import Agent

# 1. Setup Environment Variables (Best practice for ADK in 2026)
# This ensures the ADK knows to use Vertex AI and your specific project
# These 2 below lines are only required to run the agent locally using command 
# 'uv run python main.py' 
# because if we deploy to Cloud Run, then we are passing these 2 parameters in the 
# gcloud run command itself.
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = os.environ.get("GOOGLE_CLOUD_PROJECT", "vjindal-project-ai-basic")

def get_news(city: str) -> dict:
   """Retrieves the news of a particular city.
   Args:
       city (str): The name of the city for which to retrieve the news.

   Returns:
       dict: headline and content of the news, or error message.
   """
   if city.lower() == "bengaluru" or city.lower() == "bangalore":
       return {
           "headline": "Upto 6 hour long traffic Jams in Bengaluru on 9th September",
           "content": "Due to extremely heavy rainfall, parts of Bengaluru, including Whitefield and MG Road experienced long traffic jams due to waterlogging.",
       }
   else:
       return {
           "error_message": f"News for '{city}' is not available.",
       }

root_agent = Agent(
   name="news_assistant_agent",
   model="gemini-2.0-flash",
   description=(
       "Agent to retrieve news for any particular city."
   ),

   instruction=(
       "You are a helpful agent who can answer user questions related to news of any city."
   ),
   tools=[get_news],
)
