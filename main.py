from fastapi import FastAPI, HTTPException

from app.agent import agent
from app.schemas import ChatRequest, ChatResponse


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="AI Agent API",
    description="A production-oriented tool-using AI agent",
    version="1.0.0"
)


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
def health_check():
    """
    Check whether the API is running.
    """

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Chat Endpoint
# --------------------------------------------------

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):
    """
    Process a user message using the AI agent.
    """

    try:

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.message
                    }
                ]
            }
        )

        answer = result["messages"][-1].content

        return ChatResponse(
            answer=answer
        )

    except Exception as e:

        # Log the actual error for developers
        print(f"Agent error: {e}")

        # Do not expose internal error details to users
        raise HTTPException(
            status_code=500,
            detail="Agent failed to process the request."
        )