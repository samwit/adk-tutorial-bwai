import os
from google.genai import types
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search

import yfinance as yf

def stock_price(stock_ticker: str) -> dict:
    """This tool returns the last known price for a given stock ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "NVDA"

    Returns:
        str:"Ticker: Last Price"
        Example Respnse "NVDA: $100.21"
        """
    # Specify stock ticker
    stock_data = yf.Ticker(stock_ticker)
    # Get historical prices
    prices = stock_data.history(period='1d')
    # Filter on closes only
    last_close = prices['Close']
    return {
        "stock_price" : str(f"Stock price for {stock_ticker}: {last_close}")
        }


MODEL_NAME="gemini-2.0-flash"

from re import search
from google.adk.tools import google_search

# Worker Agents
stock_agent = Agent(
    model=MODEL_NAME,
    name='stock_agent',
    description = "An agent to be able to get real-time stock information",
    instruction='get stock prices',
    tools=[stock_price]
)
print(f"Agent '{stock_agent.name}' defined.")


finance_specialist = Agent(
    name="FinanceAgent",
    model=MODEL_NAME,
    description="A specialist for answering basic questions about personal finance, like savings, budgeting, or understanding general investment concepts. Do not give specific financial advice.",
    instruction="You are FinanceBot. Explain basic personal finance concepts clearly and simply. You must not provide specific investment recommendations or personalized financial advice. Stick to general knowledge."
)
print(f"Agent '{finance_specialist.name}' defined.")

search_specialist = Agent(
    name="SearchAgent",
    model=MODEL_NAME,
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[google_search]
)
print(f"Agent '{search_specialist.name}' defined.")

cooking_specialist = Agent(
    name="CookingAgent",
    model=MODEL_NAME,
    description="A specialist for providing simple recipes or cooking tips. Use this agent if the user asks for a recipe, cooking instructions, or culinary advice.",
    instruction="You are ChefBot. Provide a simple recipe or a helpful cooking tip based on the user's query. Keep recipes brief, with clear steps, and use common ingredients."
)
print(f"Agent '{cooking_specialist.name}' defined.")

from google.adk.tools.agent_tool import AgentTool

coordinator_agent = Agent(
    name="CoordinatorAgent",
    model=MODEL_NAME, # This model needs to be good at function calling/delegation
    description="I am the main coordinator. I will analyze your request and delegate it to the appropriate specialist agent: JokeAgent, FinanceAgent, or CookingAgent.",
    instruction=f"""
    You are a helpful AI assistant that coordinates tasks by delegating to specialist agents.
    You have access to the following specialist agents:
    1. "{search_specialist.name}": {search_specialist.description}
    2. "{finance_specialist.name}": {finance_specialist.description}
    3. "{cooking_specialist.name}": {cooking_specialist.description}
    4. "{stock_agent.name}": {stock_agent.description}

    When the user makes a request:
    - If the request is about finding a stock price, delegate to "{stock_agent.name}".
    - If the request is about general personal finance (savings, budget, general investments), delegate to "{finance_specialist.name}".
    - If the request is about cooking, recipes, or food preparation, delegate to "{cooking_specialist.name}".
    - If the request is very general (e.g., "hello"), or you are unsure which specialist to use, try to answer it yourself briefly or ask for clarification.

    To delegate, you will internally use a function call to transfer control. The user will see the response from the specialist.

    You also have access to the following tools:
    1. "{search_specialist.name}": {search_specialist.description}
    """,
    sub_agents=[
        finance_specialist,
        cooking_specialist,
        stock_agent
    ],
    tools=[
        AgentTool(search_specialist),
    ],
)
print(f"Agent '{coordinator_agent.name}' defined with sub_agents: {[sa.name for sa in coordinator_agent.sub_agents]}.")

root_agent = coordinator_agent