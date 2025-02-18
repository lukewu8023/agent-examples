# evaluators_management.py

from agent_core.agents import Agent
from agent_core.planners.generic_planner import GenericPlanner
from agent_core.evaluators import GenericEvaluator


def main():
    agent = Agent()
    agent.planner = GenericPlanner()

    # 1) Enable evaluation
    agent.enable_evaluators()

    # 2) See default evaluator mapping
    print("Default evaluator:", agent.evaluators)

    # 3) Add a new evaluator
    writing_evaluator = GenericEvaluator(agent.model_name)
    agent.add_evaluator("writing", writing_evaluator)

    # 4) Update existing category
    coding_evaluator = GenericEvaluator(agent.model_name)
    agent.update_evaluator("coding", coding_evaluator)

    print("evaluators after updates:", agent.evaluators)

    # 5) Execute a simple task
    task = "3 steps to draw a flower"
    agent.execute(task)

    # 6) Summarize the execution
    execution_result = agent.get_execution_result_summary()
    print(f"Execution Result: {execution_result}")


if __name__ == "__main__":
    main()
