import os
import subprocess

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

tools = [
    {
        "name": "run_black",
        "description": "Run Black formatter",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "run_ruff",
        "description": "Run Ruff linter",
        "input_schema": {"type": "object", "properties": {}},
    },
]


def run_black():
    subprocess.run(["black", "."], check=True)
    return "Black completed"


def run_ruff():
    subprocess.run(["ruff", "check", ".", "--fix"], check=True)
    return "Ruff completed"


response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    tools=tools,
    messages=[{"role": "user", "content": "Format and lint this Python project."}],
)

for block in response.content:
    if block.type == "tool_use":
        if block.name == "run_black":
            run_black()
        else:
            run_ruff()
