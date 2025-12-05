from pydantic import BaseModel, Field


class GreetingRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500, description="Greeting text from user")


class GreetingResponse(BaseModel):
    status: str = Field(default="ok")
    echoed: str = Field(..., description="Echo of the submitted message")
