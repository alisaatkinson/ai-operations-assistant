import streamlit as st

from src.analyzer import generate_document
from src.prompts import DOCUMENT_PROMPTS
from src.validator import validate_input, validate_output


st.set_page_config(
    page_title="AI Operations Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("AI Documentation & Operations Assistant")

st.write(
    "Transform unstructured operational notes into structured, "
    "reviewable documentation."
)

st.info(
    "AI-generated content is a draft and requires human review "
    "before publication or distribution."
)

document_type = st.selectbox(
    "Document type",
    options=list(DOCUMENT_PROMPTS.keys()),
)

notes = st.text_area(
    "Operational notes",
    height=250,
    placeholder=(
        "Paste incident notes, meeting notes, technical observations, "
        "or other unstructured operational information here..."
    ),
)

if st.button("Analyze & Generate", type="primary"):

    input_issues = validate_input(notes)

    if input_issues:
        for issue in input_issues:
            st.warning(issue)

    else:
        try:
            with st.spinner("Analyzing operational notes..."):
                generated_document = generate_document(
                    notes=notes,
                    document_type=document_type,
                )

            output_issues = validate_output(generated_document)

            st.subheader("Generated Draft")
            st.markdown(generated_document)

            if output_issues:
                st.subheader("Validation Findings")

                for issue in output_issues:
                    st.warning(issue)

            st.divider()

            approved = st.checkbox(
                "I have reviewed this draft for accuracy."
            )

            if approved:
                st.success(
                    "Human review acknowledged. "
                    "Document is ready for the next workflow step."
                )

        except Exception as error:
            st.error(f"Generation failed: {error}")