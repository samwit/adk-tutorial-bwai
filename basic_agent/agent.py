import os
from google.genai import types
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService


basic_agent = Agent(
    model="gemini-2.0-flash",
    name='basic_agent',
    instruction='tells a joke for a provided subject which the user will provide',
)


root_agent = basic_agent

