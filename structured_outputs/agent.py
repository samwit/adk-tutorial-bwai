import os
from google.genai import types
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

MODEL_NAME="gemini-2.0-flash"

## Structured Outputs
from pydantic import BaseModel, Field

## Output Schema
# --- Output Schema Definition ---
class TourInfo(BaseModel):
  """Information for a tour guide agent."""
  city: str = Field(description="The city for which the tour is designed.")
  points_of_interest: list[str] = Field(description="A list of attractions and points of interest for the tour.")
  duration_in_hours: float = Field(description="The total estimated duration of the tour in hours.")
  language: str = Field(description="The primary language for the tour.")

from google.adk.agents import LlmAgent

# --- Create Tour Guide Agent ---
root_agent = LlmAgent(
    name="tour_guide_agent",
    model="gemini-2.0-flash",
    instruction="""
        You are a Tour Design Assistant.
        Your task is to create personalized tour itineraries for cities based on the user's request.

        GUIDELINES:
        - Select appropriate points of interest based on the city and user preferences
        - Ensure the tour duration is realistic for visiting all suggested locations
        - Consider local culture and language for a better experience
        - Choose a diverse mix of attractions (historical sites, parks, museums, local cuisine spots)
        - Prioritize attractions based on their significance and visitor ratings
        - Ensure the tour is logistically feasible

        IMPORTANT: Your response MUST be valid JSON matching the TourInfo structure.

        DO NOT include any explanations or additional text outside the structured response.
    """,
    description="Designs personalized city tours with points of interest, duration, and language",
    output_schema=TourInfo,
    output_key="tour_info",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True
)