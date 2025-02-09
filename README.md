# PhAENix Agent Examples

Welcome to the **PhAENix Agent Examples** repository! This project contains **comprehensive examples** demonstrating how to use [PhAENix](https://github.com/lukewu8023/agent-core) in various scenarios. Each example showcases different features, configurations, or integrations—ranging from basic step-based planning to advanced validation loops and external tool usage.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Examples Overview](#examples-overview)
3. [Example Documentation Template](#example-documentation-template)
4. [Contributing](#contributing)

---

## Introduction

PhAENix is designed to simplify building robust LLM-based agents by providing:

- Multiple **planner** options (step-based or graph-based)
- A sophisticated **validation** system
- **Customizable** LLM configurations
- **Tool & API Integrations** for dynamic, real-time data processing

This repository demonstrates these capabilities through **12 hands-on examples**, ranging from minimal single-step queries (Example 1) to advanced multi-step planning with external tools and validations (Examples 5, 6, and beyond). Each example includes:

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

| **Example #** | **Example Title**                        | **Short Description**                                                                                                           | **Code Link**       | **Details (Sub-README)**      |
| ------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------- |
| 1             | Minimal Single-Step Execution            | Showcases a basic Agent creation with a custom model and a single-step query (`agent.execute("Who are you?")`).                 | [Code](./example1)  | [Docs](./example1/README.md)  |
| 2             | Basic Step-Based Planning                | Demonstrates using a `GenericPlanner` to break a task into multiple steps (e.g., “3 steps draw a flower.”).                     | [Code](./example2)  | [Docs](./example2/README.md)  |
| 3             | Multiple Agents & Different Models       | Illustrates running two agents simultaneously, each with distinct model and planner configurations.                             | [Code](./example3)  | [Docs](./example3/README.md)  |
| 4             | Retrieving Execution History & Summaries | Shows how to retrieve and summarize multi-step execution via `agent.get_execution_result_summary()`.                            | [Code](./example4)  | [Docs](./example4/README.md)  |
| 5             | Using GraphPlanner with Validation       | Introduces the `GraphPlanner` along with validators, demonstrating an advanced planning approach and debugging logs.            | [Code](./example5)  | [Docs](./example5/README.md)  |
| 6             | Tool Integration & Graph Planner         | Highlights using built-in tools (e.g., event, metric, log, trace) with `GraphPlanner` to analyze external data and root causes. | [Code](./example6)  | [Docs](./example6/README.md)  |
| 7             | Agent Knowledge & Background Setup       | Demonstrates embedding domain knowledge and background context (e.g., a professional artist) for specialized task execution.    | [Code](./example7)  | [Docs](./example7/README.md)  |
| 8             | Configuring Log Levels & Planner         | Shows how to set log levels (via environment variables or in code) and use a `GenericPlanner` for multi-step tasks.             | [Code](./example8)  | [Docs](./example8/README.md)  |
| 9             | Overriding Default Prompts               | Explores customizing prompts for validators, single-step execution, multi-step planning, and final summaries.                   | [Code](./example9)  | [Docs](./example9/README.md)  |
| 10            | Using Context for Role-Based Execution   | Demonstrates adding context (e.g., “digital artist” role) to guide the Agent’s behavior and outputs.                            | [Code](./example10) | [Docs](./example10/README.md) |
| 11            | Advanced Validator Management            | Showcases enabling, adding, and updating multiple validators to refine agent outputs and handle specific tasks.                 | [Code](./example11) | [Docs](./example11/README.md) |
| 12            | Advanced LLM Chat & Summarization        | Utilizes `agent.llm_chat` for direct text processing and summarizes the entire execution history in one prompt.                 | [Code](./example12) | [Docs](./example12/README.md) |

## Contributing

Interested in contributing a new example or improving an existing one? Please follow these steps:

1. Fork & Clone this repository.
2. Create a new branch for your feature or fix.
3. Add or update the relevant files (including the Examples Overview table above if you’re adding a new example).
4. Submit a Pull Request (PR) with a concise description of your changes.

We appreciate all contributions—whether it’s a bug fix, documentation improvement, or a brand-new example!
