from src.validator import validate_input, validate_output


def test_valid_input_returns_no_issues():
    notes = (
        "Customer portal returned intermittent errors "
        "affecting approximately 20 users."
    )

    assert validate_input(notes) == []


def test_empty_input_returns_issue():
    issues = validate_input("")

    assert "Source notes cannot be empty." in issues


def test_short_input_returns_issue():
    issues = validate_input("Short note")

    assert (
        "Source notes may be too short to generate reliable documentation."
        in issues
    )


def test_valid_output_returns_no_issues():
    output = (
        "Incident Summary: The customer portal experienced intermittent "
        "errors affecting users. Root cause remains under investigation."
    )

    assert validate_output(output) == []


def test_empty_output_returns_issue():
    issues = validate_output("")

    assert "The AI returned an empty response." in issues


def test_short_output_returns_issue():
    issues = validate_output("Too short")

    assert (
        "Generated documentation may be too short for meaningful review."
        in issues
    )