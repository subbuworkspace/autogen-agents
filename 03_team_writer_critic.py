"""Example 3: a multi-agent team (writer + critic) using RoundRobinGroupChat."""
import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

from src.config import get_model_client


async def main() -> None:
    model_client = get_model_client()

    writer = AssistantAgent(
        name="writer",
        model_client=model_client,
        system_message="You write a short, clear LinkedIn post draft. Revise it using the critic's feedback.",
    )
    critic = AssistantAgent(
        name="critic",
        model_client=model_client,
        system_message=(
            "Review the writer's draft and give 2-3 concrete improvements. "
            "When the draft is good, reply with the single word APPROVE."
        ),
    )

    termination = TextMentionTermination("APPROVE") | MaxMessageTermination(8)
    team = RoundRobinGroupChat([writer, critic], termination_condition=termination)

    await Console(
        team.run_stream(task="Write a LinkedIn post about moving from Power BI to agentic AI.")
    )
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
