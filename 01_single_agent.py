"""Example 1: a single assistant agent."""
import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console

from src.config import get_model_client


async def main() -> None:
    model_client = get_model_client()
    agent = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message="You are a helpful assistant. Keep answers short.",
    )
    await Console(agent.run_stream(task="Explain what an AI agent is in 3 sentences."))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
