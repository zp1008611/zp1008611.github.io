# Agentic-RL

本章节探讨 Agentic 强化学习在大语言模型中的应用，包括理论动机、具体实现和代表性工作。

## 内容导航

### [绪论](agentic-rl-motivation/README.md)
探讨 Tool-integrated Reasoning Models 与 Agentic Systems 的定义、差异和发展动机。深入分析两种范式的优势与局限，以及为什么需要 Trainable Agentic Systems。

### [Search-R1](agentic-rl-search-r1/README.md)
Search-R1 是一个典型的 tool-integrated reasoning model，通过强化学习训练 LLMs 进行推理并利用搜索引擎。展示了在网页搜索场景下的优秀表现，同时也体现了这类模型在扩展性和泛化能力方面的局限。

### [AgentFlow](agentic-rl-agentflow/README.md)
AgentFlow 是 trainable agentic systems 的代表性工作，展示了如何通过在线强化学习优化模块化 agent 系统。在保持模块化架构优势的同时，实现了端到端的学习和优化。

### 工具轨迹数据合成
    - APIGen-MT: Agentic PIpeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay


### 工具轨迹后训练 
    - Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL


### 多轮对话动态环境训练 
    - Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning


### [使用sandbox训练codeagent]
    - https://lightning.ai/lightning-ai/environments/training-a-coding-agent-with-verl?section=featured&tab=overview
    - https://www.daytona.io/docs/en/trl-grpo-training/
---
