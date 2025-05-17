import os
from google.genai import types
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search

builtintools_agent   = Agent(
    name="builtintools_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)

print(f"Agent '{builtintools_agent.name}' defined.")

root_agent = builtintools_agent