"""Example 2: an agent that calls tools."""
import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console

from src.config import get_model_client
from src.tools import calculate, get_current_time


async def main() -> None:
    model_client = get_model_client()
    agent = AssistantAgent(
        name="tool_agent",
        model_client=model_client,
        tools=[get_current_time, calculate],
        system_message="Use the tools when needed, then answer clearly.",
        reflect_on_tool_use=True,
    )
    await Console(
        agent.run_stream(task="What time is it now, and what is 1234 * 56?")
    )
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
