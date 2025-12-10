"""Tests for shared utilities."""

from tabstack._shared import build_automate_request


class TestBuildAutomateRequest:
    """Tests for build_automate_request function."""

    def test_minimal_request(self) -> None:
        """Test building request with only task."""
        result = build_automate_request(task="Find repositories")
        assert result == {"task": "Find repositories"}

    def test_with_url(self) -> None:
        """Test building request with url."""
        result = build_automate_request(task="Find repositories", url="https://github.com/trending")
        assert result == {
            "task": "Find repositories",
            "url": "https://github.com/trending",
        }

    def test_with_schema(self) -> None:
        """Test building request with schema."""
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        result = build_automate_request(task="Extract data", schema=schema)
        assert result == {"task": "Extract data", "schema": schema}

    def test_with_data(self) -> None:
        """Test building request with data for form filling."""
        data = {"name": "Alex", "email": "alex@example.com"}
        result = build_automate_request(task="Fill form", data=data)
        assert result == {"task": "Fill form", "data": data}

    def test_with_guardrails(self) -> None:
        """Test building request with guardrails."""
        result = build_automate_request(
            task="Browse site", guardrails="read-only, no form submissions"
        )
        assert result == {
            "task": "Browse site",
            "guardrails": "read-only, no form submissions",
        }

    def test_with_max_iterations(self) -> None:
        """Test building request with max_iterations."""
        result = build_automate_request(task="Complex task", max_iterations=20)
        assert result == {"task": "Complex task", "maxIterations": 20}

    def test_with_max_validation_attempts(self) -> None:
        """Test building request with max_validation_attempts."""
        result = build_automate_request(task="Validate task", max_validation_attempts=5)
        assert result == {"task": "Validate task", "maxValidationAttempts": 5}

    def test_with_all_parameters(self) -> None:
        """Test building request with all parameters."""
        schema = {"type": "object", "properties": {"items": {"type": "array"}}}
        data = {"query": "python"}
        result = build_automate_request(
            task="Search and extract",
            url="https://example.com",
            schema=schema,
            data=data,
            guardrails="browse only",
            max_iterations=30,
            max_validation_attempts=2,
        )
        assert result == {
            "task": "Search and extract",
            "url": "https://example.com",
            "schema": schema,
            "data": data,
            "guardrails": "browse only",
            "maxIterations": 30,
            "maxValidationAttempts": 2,
        }

    def test_max_iterations_zero_not_included(self) -> None:
        """Test that max_iterations=0 is included (it's valid, just not truthy)."""
        # Note: 0 is a valid value but Python's 'if max_iterations is not None' handles this
        result = build_automate_request(task="Test", max_iterations=0)
        assert result == {"task": "Test", "maxIterations": 0}

    def test_empty_string_guardrails_not_included(self) -> None:
        """Test that empty string guardrails is not included."""
        result = build_automate_request(task="Test", guardrails="")
        assert result == {"task": "Test"}

    def test_empty_dict_data_not_included(self) -> None:
        """Test that empty dict data is not included."""
        result = build_automate_request(task="Test", data={})
        assert result == {"task": "Test"}
