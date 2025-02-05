# example1.py

from agents import Agent


def main():

    agent = Agent(model="gpt-4o-mini")
    agent.execute("Who are you?")
    print(f"Response: {agent.execution_responses}")


if __name__ == "__main__":
    main()
