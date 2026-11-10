import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def ask_model(prompt: str) -> str:
    """Send a prompt to an LLM and return its response."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Check .env file."
        )

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are a helpful AI assistant.",
        input=prompt,
    )

    return response.output_text