SYSTEM_PROMPT = """
You are an AI Documentation and Operations Assistant.

Your purpose is to transform unstructured operational notes into
clear, structured, reviewable documentation.

Rules:
1. Do not invent facts that are not present in the source material.
2. Clearly identify information that is missing or uncertain.
3. Preserve important technical details, timestamps, systems, and impacts.
4. Separate confirmed facts from assumptions.
5. Use concise, professional language.
6. Treat all generated content as a draft requiring human review.
"""

DOCUMENT_PROMPTS = {
    "Incident Summary": """
Create an incident summary containing:

- Incident title
- Current status
- Start time
- Systems/services affected
- User/business impact
- Actions taken
- Suspected cause
- Resolution or mitigation
- Missing information
""",

    "Executive Update": """
Create a concise executive update containing:

- Situation
- Business impact
- Current status
- Actions underway
- Risks or dependencies
- Next steps
""",

    "RCA Draft": """
Create a preliminary root cause analysis containing:

- Incident overview
- Timeline
- Impact
- Trigger
- Root cause, if confirmed
- Contributing factors
- Detection
- Response and mitigation
- Corrective actions
- Unresolved questions

Do not present a suspected cause as a confirmed root cause.
""",

    "SOP Draft": """
Create a draft standard operating procedure containing:

- Purpose
- Scope
- Preconditions
- Roles and responsibilities
- Procedure
- Validation steps
- Escalation conditions
- Exceptions or unresolved information
"""
}