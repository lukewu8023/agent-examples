# example2.py

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from models.model_registry import ModelRegistry
from models.base_model import BaseModel

from agents import Agent


class Gemini15PRO002Model(BaseModel):
    def __init__(self):
        super().__init__(name="gemini-1.5-pro-002")
        self.model_instance = ChatOpenAI(
            model="gemini-1.5-pro-002", temperature=0.1, verbose=True
        )

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


def main():

    ModelRegistry.register_model(Gemini15PRO002Model())

    agent = Agent(model="gemini-1.5-pro-002")
    agent.execute("Who are you?")
    print(f"Response: {agent.execution_responses}")


if __name__ == "__main__":
    main()
