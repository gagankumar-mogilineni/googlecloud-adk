from google.adk.agents import Agent
from google.adk.tools import google_search

# root_agent = Agent(
#     name="my_first_agent",
#     model="gemini-2.0-flash",
#     description="Agent will answer users query related to google cloud",
#     instruction="""
#     You are the AI Assistant that will answer queries related to google cloud
#     """,
#     tools = [google_search]
# )

def morning_greet(name: str) -> str:
    return f"Good Morning, {name} How Can i assit you today? My mood is amazing"

def evening_greet(name: str) -> str:
    return f"Good Morning, {name} How Can i assit you today? I am tired"

root_agent = Agent(
    name="my_first_agent",
    model="gemini-2.0-flash",
    description="Agent will answer users query related to google cloud",
    instruction="""
    First ask user a Name &  start converstation by greeting based on users Greet
    If user says Good Morning, use morning_greet tool to greet user.
    If user says Good Evening, use evening_greet tool to greet user.
    """,
    tools = [evening_greet, morning_greet]
)