# distinct_model_setup.py

from agent_core.agents import Agent
from agent_core.planners import GenericPlanner


def main():
    agent1 = Agent()
    agent1.execute("Who are you?")

    agent2 = Agent(model_name="gemini-1.5-flash-002")
    agent2.planner = GenericPlanner(model_name="gemini-1.5-pro-002")
    task = "3 steps draw a flower"
    agent2.execute(task)


if __name__ == "__main__":
    main()
