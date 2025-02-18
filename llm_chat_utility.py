# llm_chat_utility.py

from agent_core.agents import Agent
from agent_core.planners.generic_planner import GenericPlanner


def main():
    agent = Agent()
    agent.planner = GenericPlanner()

    print(agent.evaluate_text_prompt)
    print(agent.process("Who are you?"))

    task = "3 steps to write a poem about flower"
    agent.execute(task)

    execution_history = agent.execution_history
    print(f"Execution History: {execution_history}")
    execution_result = agent.process(
        f"Summarize the execution history: {execution_history}"
    )
    print(f"Execution Result: {execution_result}")


if __name__ == "__main__":
    main()
