# example2.py

import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from agent_core.models.base_model import BaseModel
from agent_core.models.model_registry import ModelRegistry
from models.gemini_15_flash_001 import Gemini15Flash001Model

from agent_core.agents import Agent


class Gemini15Flash001Model(BaseModel):
    def __init__(self):
        super().__init__()
        self.model_instance = ChatOpenAI(
            model_name="gemini-1.5-flash-001", temperature=0.1, verbose=True
        )
        os.getenv("openai_api_key")
        pass

    def process(self, request: str) -> str:
        messages = [
            HumanMessage(request),
        ]
        response = self.model_instance.invoke(messages)
        # Extract the 'content' attribute to return a string
        if hasattr(response, "content"):
            return response.content
        else:
            # Fallback in case 'content' is missing
            return str(response)

    def name(self) -> str:
        return "gemini-1.5-flash-001"


def main():

    ModelRegistry.register_model(Gemini15Flash001Model())

    agent = Agent(model_name="gemini-1.5-flash-001")
    agent.execute("Who are you?")
    print(f"Response: {agent.execution_responses}")


if __name__ == "__main__":
    main()
