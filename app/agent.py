from langchain_groq import ChatGroq
from langchain.agents import create_agent

from app.config import GROQ_API_KEY
from app.tools import (
    calculator,
    get_weather,
    web_search
)


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)


# --------------------------------------------------
# Tools
# --------------------------------------------------

tools = [
    calculator,
    get_weather,
    web_search
]


# --------------------------------------------------
# System Prompt
# --------------------------------------------------

SYSTEM_PROMPT = """
You are a helpful AI assistant with access to three tools.

TOOLS:

1. calculator
Use calculator for mathematical calculations.

2. get_weather
Use get_weather for weather information.
If the user asks about weather in a specific city,
always use get_weather.

3. web_search
Use web_search for general information that requires
external or up-to-date knowledge.

IMPORTANT ROUTING RULES:

- Weather questions → get_weather
- Mathematical calculations → calculator
- General current/external information → web_search
- You may use multiple tools when necessary.
- Do not invent information.
- Use tool results as the source of truth.

RESPONSE STYLE:

- Answer naturally and conversationally.
- Do not mention tools, APIs, agents, or internal steps.
- Do not show tool calls or technical details.
- Directly answer the user's question.
- Combine results naturally when multiple tools are used.
- Be concise unless the user asks for more detail.
"""


# --------------------------------------------------
# Agent
# --------------------------------------------------

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)