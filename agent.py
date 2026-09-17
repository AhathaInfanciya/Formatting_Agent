import os
import subprocess

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

PROMPT = """
You are a Python formatting agent.

Available tools:
1. black
2. ruff

Your job is to decide which tools should be run.

Respond only with tool names.

Examples:
black
ruff
black, ruff

For Python projects that require formatting and linting,
respond with:

black, ruff
"""


def run_black():
    print("Running Black...")

    subprocess.run(
        ["black", "."],
        check=True,
    )

    print("Black completed.\n")


def run_ruff():
    print("Running Ruff...")

    subprocess.run(
        ["ruff", "check", ".", "--fix"],
        check=True,
    )

    print("Ruff completed.\n")


def ask_claude():
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not found in environment variables."
        )

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": PROMPT,
            }
        ],
    )

    decision = response.content[0].text.lower().strip()

    print(f"Claude Decision: {decision}\n")

    return decision


def main():
    print("Starting Formatting Agent...\n")

    decision = ask_claude()

    if "black" in decision:
        run_black()

    if "ruff" in decision:
        run_ruff()

    print("Formatting Agent Completed Successfully.")


if __name__ == "__main__":
    main()
