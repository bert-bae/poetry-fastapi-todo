from pydantic import BaseModel


class PromptAgentInput(BaseModel):
    prompt: str
