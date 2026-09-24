import os

from dotenv import load_dotenv
from openai import OpenAI

from src.prompts import DOCUMENT_PROMPTS, SYSTEM_PROMPT


load_dotenv()


def get_client() -> OpenAI:
    """Create an OpenAI client using the API key from the environment."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found. "
            "Add it to your local .env file."
        )

    return OpenAI(api_key=api_key)


def generate_document(notes: str, document_type: str) -> str:
    """Generate documentation from unstructured operational notes."""

    if document_type not in DOCUMENT_PROMPTS:
        raise ValueError(f"Unsupported document type: {document_type}")

    client = get_client()

    instructions = f"""
{SYSTEM_PROMPT}

DOCUMENT TYPE INSTRUCTIONS:
{DOCUMENT_PROMPTS[document_type]}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=instructions,
        input=f"""
SOURCE NOTES:

{notes}
""",
    )

    return response.output_text