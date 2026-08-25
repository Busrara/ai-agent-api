
# AI Agent API

A production-ready AI Agent API built with **FastAPI, LangChain, and Groq**. It features intelligent tool calling for calculations, weather information, and web search for the users.

## Live Demo

**Live API:** https://ai-agent-api-6ax6.onrender.com

**Swagger UI:** https://ai-agent-api-6ax6.onrender.com/docs

The API is deployed on Render and can be tested directly through the interactive Swagger interface.

## Overview

This project shows how to build and deploy an AI agent that can analyze user requests and decide when external tools are needed.

The agent uses a Groq-powered LLM with LangChain to select and execute specialized tools based on the user's request.

### Available Tools

* 🧮 Calculator — mathematical calculations
* 🌤️ Weather — current weather information
* 🔎 Web Search — external and up-to-date information

## Architecture

```text
User
  │
  ▼
FastAPI /chat
  │
  ▼
AI Agent
LangChain + Groq
  │
  ├── Calculator
  │
  ├── Weather
  │
  └── Web Search
  │
  ▼
Tool Result
  │
  ▼
Agent Response
  │
  ▼
User
```

##  How It Works

1. The user sends a message to the `/chat` endpoint.
2. FastAPI validates the request.
3. The request is passed to the LangChain agent.
4. The Groq-powered LLM analyzes the request.
5. The agent decides whether a tool is required.
6. The selected tool is executed.
7. The tool result is returned to the agent.
8. The agent generates the final response.
9. FastAPI returns the response as JSON.

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* LangChain-Groq
* Groq
* Uvicorn
* Open-Meteo
* DDGS
* Pytest
* Render

## Tools

### Calculator

Performs mathematical calculations based on the user's request.

Example:

```text
User:
What is 15% of 240?

Agent:
15% of 240 is 36.
```

### Weather

Retrieves current weather information for a requested city.

The tool first geocodes the city and then retrieves weather data from Open-Meteo.

### Web Search

Searches the web when the agent determines that external or up-to-date information is required.

## Project Structure

```text
ai-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── schemas.py
│   └── tools.py
│
├── tests/
│   ├── test_api.py
│   └── test_tools.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

##  Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your real API key to GitHub.

The `.env` file is excluded using `.gitignore`.

##  Run Locally

Clone the repository:

```bash
git clone https://github.com/Busrara/ai-agent-api.git
cd ai-agent-api
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Add your Groq API key to `.env`.

Start the API:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

##  Testing

The project includes automated tests for API endpoints and tools.

Run:

```bash
python -m pytest -v
```

Current test result:

```text
7 passed
```

##  API Usage

### POST /chat

Request:

```json
{
  "message": "What is 15% of 240?"
}
```

Response:

```json
{
  "answer": "15% of 240 is 36."
}
```

##  Deployment

The application is deployed on Render and connected to the GitHub `main` branch.

**Production API:**
https://ai-agent-api-6ax6.onrender.com

**Swagger UI:**
https://ai-agent-api-6ax6.onrender.com/docs

Environment variables are configured separately from the source code to protect API credentials.

##  Future Improvements

* Streaming responses
* Conversation memory
* Additional tools
* Authentication and rate limiting
* Persistent conversation history
* Docker containerization
* GitHub Actions CI/CD
* Expanded integration tests
* Improved observability and logging

