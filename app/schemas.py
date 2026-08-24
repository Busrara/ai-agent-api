from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for the chat endpoint.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="User message"
    )


class ChatResponse(BaseModel):
    """
    Response model returned by the chat endpoint.
    """

    answer: str