# PhAENix Agent Examples

Welcome to the **PhAENix Agent Examples** repository! This project contains **comprehensive examples** demonstrating how to use [PhAENix](https://github.com/lukewu8023/agent-core) in various scenarios. Each example showcases different features, configurations, or integrations—ranging from basic step-based planning to advanced validation loops and external tool usage.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Examples Overview](#examples-overview)
3. [Contributing](#contributing)

---

## Introduction

PhAENix is designed to simplify building robust LLM-based agents by providing:

- Multiple **planner** options (step-based or graph-based)
- A sophisticated **validation** system
- **Customizable** LLM configurations
- **Tool & API Integrations** for dynamic, real-time data processing

This repository demonstrates these capabilities through **14 hands-on examples**, ranging from minimal single-step queries (Example 1) to advanced multi-step planning with external tools and validations (Examples 5, 6, and beyond). Each example includes:

- A **concise summary** of the use case
- **Links to the code** within this repository
- **Links to a sub-README** for deeper details (e.g., parameter definitions, alternative approaches, and scenario variations)

By exploring these examples, you’ll learn how to:

- Configure and switch between **various LLM models**
- Implement **step-based** and **graph-based** planning flows
- Retrieve and summarize execution outputs (e.g., **history and results**)
- Integrate **external tools or APIs** for dynamic data access
- Override **default prompts** and validation logic for specialized behaviors
- Manage context or background knowledge to fine-tune the agent’s perspective

Whether you’re a first-time user or an advanced developer, these examples will guide you in building your own robust LLM-based agent using PhAENix.

---

## Examples Overview

Below is a high-level summary of the 12 examples. Click on each **Example Title** to jump to the documentation template below or directly view the corresponding code and sub-README.

| **Example #** | **Example Title**        | **Short Description**                                                                                                                                                      | **Code Link**                         | **Details Documentation**                  |
| ------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------ |
| 1             | Minimal Agent Creation   | Creates a basic agent with just two lines of code. Quickly demonstrates a single-step query to confirm the agent is functioning.                                           | [Code](./minimal_agent_creation.py)   | [Docs](./docs/minimal_agent_creation.md)   |
| 2             | Step-Based Planning      | Specifies a planner to break a task into multiple steps. The agent plans first, then executes each step in sequence.                                                       | [Code](./step-based_planning.py)      | [Docs](./docs/step-based_planning.md)      |
| 3             | Distinct Model Setup     | Assigns distinct models to different components (e.g., agent, planner). This enables flexible, specialized capabilities across the entire workflow.                        | [Code](./distinct_model_setup.py)     | [Docs](./docs/distinct_model_setup.md)     |
| 4             | Execution Summaries      | Tracks and prints the execution history for each step. Also demonstrates summarizing results and displaying AI responses.                                                  | [Code](./execution_summaries.py)      | [Docs](./docs/execution_summaries.md)      |
| 5             | Graph-Based Planner      | Introduces `GraphPlanner` to structure tasks as nodes in a graph. The agent arranges and executes each node-based step for advanced planning.                              | [Code](./graph-based_planner.py)      | [Docs](./docs/graph-based_planner.md)      |
| 6             | Tools Integration        | Uses langchain tools to enhance the agent’s capabilities. Demonstrates how the agent can interact with external data to diagnose or analyze complex events.                | [Code](./tools_integration.py)        | [Docs](./docs/tools_integration.md)        |
| 7             | Knowledge & Background   | Injects human knowledge and system background to guide the agent’s perspective. Improves accuracy for specialized tasks by focusing its domain context.                    | [Code](./knowledge_background.py)     | [Docs](./docs/knowledge_background.md)     |
| 8             | Configurable Log Levels  | Shows how to set log levels (e.g., DEBUG, INFO, ERROR) for each entity (agent, planner, evaluator). Multiple approaches are demonstrated, including environment variables. | [Code](./configurable_log_levels.py)  | [Docs](./docs/configurable_log_levels.md)  |
| 9             | Override Default Prompts | Prints and customizes the default prompts for validators, agents, and planners. Illustrates how altering prompts can reshape agent behavior on the fly.                    | [Code](./override_default_prompts.py) | [Docs](./docs/override_default_prompts.md) |
| 10            | Precise Context Control  | Ensures the LLM receives only relevant context for each task. Prevents unrelated or incorrect information from influencing the agent’s output.                             | [Code](./precise_context_control.py)  | [Docs](./docs/precise_context_control.md)  |
| 11            | Evaluators Management    | Demonstrates adding and updating evaluators (e.g., writing, coding) for dynamic task validation. Failed steps trigger re-execution or replanning to ensure success.        | [Code](./evaluators_management.py)    | [Docs](./docs/evaluators_management.md)    |
| 12            | LLM Chat Utility         | Shows how to perform standalone LLM requests through `agent.process()`. Includes ready-made methods for evaluating or summarizing text without a full agent cycle.         | [Code](./llm_chat_utility.py)         | [Docs](./docs/llm_chat_utility.md)         |
| 13            | Code Evaluator           | Introduces a specialized `CodingEvaluator` for assessing code generation steps. Ensures quality control and error handling when the agent produces code.                   | [Code](./code_evaluator.py)           | [Docs](./docs/code_evaluator.md)           |
| 14            | LangGraph Integration    | Demonstrates synergy between PhAENix and LangGraph. Uses a state graph to orchestrate custom message flows and agent execution.                                            | [Code](./langgraph_integration.py)    | [Docs](./docs/langgraph_integration.md)    |

## Installation

### Debug Mode

#### A1. Clone the core repository

```bash
git clone https://github.com/lukewu8023/agent-core.git
```

#### A2. Clone the examples project

```bash
git clone https://github.com/lukewu8023/agent-examples.git
cd agent-examples
```

#### A3. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### A4. Install the project as a library

```bash
pip install -e path/to/agent-core
```

### Production Mode

#### B1. Clone the examples project

```bash
git clone https://github.com/lukewu8023/agent-examples.git
cd agent-examples
```

#### B2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### B3. Install the project as a library

```bash
pip install agent-core
```

This will make the agents, planners, models, etc. available in your Python environment.

## Contributing

Interested in contributing a new example or improving an existing one? Please follow these steps:

1. Fork & Clone this repository.
2. Create a new branch for your feature or fix.
3. Add or update the relevant files (including the Examples Overview table above if you’re adding a new example).
4. Submit a Pull Request (PR) with a concise description of your changes.

We appreciate all contributions—whether it’s a bug fix, documentation improvement, or a brand-new example!
