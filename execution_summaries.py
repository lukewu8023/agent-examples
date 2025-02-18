# execution_summaries.py

from agent_core.agents import Agent
from agent_core.planners import GenericPlanner


def main():

    agent = Agent()
    agent.planner = GenericPlanner()

    task = "3 steps draw a digital flower using computer characters."
    agent.execute(task)

    execution_responses = agent.execution_responses
    print(f"Execution Response: {agent.execution_responses}")
    execution_history = agent.execution_history
    print(f"Execution History: {execution_history}")
    execution_result = agent.get_execution_result_summary()
    print(f"Execution Result: {execution_result}")


if __name__ == "__main__":
    main()
