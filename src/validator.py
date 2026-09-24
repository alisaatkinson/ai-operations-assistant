from typing import List


def validate_input(notes: str) -> List[str]:
    """Validate source notes before sending them to the AI."""

    issues = []

    if not notes or not notes.strip():
        issues.append("Source notes cannot be empty.")
        return issues

    if len(notes.strip()) < 25:
        issues.append(
            "Source notes may be too short to generate reliable documentation."
        )

    return issues


def validate_output(output: str) -> List[str]:
    """Perform basic validation on AI-generated documentation."""

    issues = []

    if not output or not output.strip():
        issues.append("The AI returned an empty response.")
        return issues

    if len(output.strip()) < 50:
        issues.append(
            "Generated documentation may be too short for meaningful review."
        )

    return issues