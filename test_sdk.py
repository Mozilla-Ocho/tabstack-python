"""Test script to verify SDK functionality."""
import sys

sys.path.insert(0, ".")

from tabstack_ai import (
    TABStack,
    BadRequestError,
    UnauthorizedError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError,
    TABStackError,
)
from tabstack_ai.schema import Schema, String, Number, Boolean, Array, Object


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        from tabstack_ai import (
            Extract,
            Generate,
            Automate,
            MarkdownResponse,
            SchemaResponse,
            JsonResponse,
            Metadata,
            AutomateEvent,
            EventData,
        )

        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_schema():
    """Test Schema DSL functionality."""
    print("\nTesting Schema DSL...")
    try:
        # Test simple schema
        simple_schema = Schema(name=String, age=Number, active=Boolean)
        assert simple_schema.to_json_schema()["type"] == "object"
        assert "name" in simple_schema.to_json_schema()["properties"]

        # Test nested schema
        nested_schema = Schema(
            user=Object(name=String, email=String),
            tags=Array(String),
            scores=Array(Number),
        )
        json_schema = nested_schema.to_json_schema()
        assert json_schema["properties"]["user"]["type"] == "object"
        assert json_schema["properties"]["tags"]["type"] == "array"
        assert json_schema["properties"]["tags"]["items"]["type"] == "string"

        # Test complex nested schema
        complex_schema = Schema(
            stories=Array(
                Object(
                    title=String,
                    points=Number,
                    author=String,
                    comments=Array(Object(text=String, user=String)),
                )
            )
        )
        json_schema = complex_schema.to_json_schema()
        assert "stories" in json_schema["properties"]

        # Test Schema.from_json_schema
        json_schema_dict = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
                "active": {"type": "boolean"},
                "tags": {"type": "array", "items": {"type": "string"}},
            },
        }
        reconstructed_schema = Schema.from_json_schema(json_schema_dict)
        assert "name" in reconstructed_schema.properties
        assert "age" in reconstructed_schema.properties
        assert "active" in reconstructed_schema.properties
        assert "tags" in reconstructed_schema.properties
        # Verify round-trip
        assert reconstructed_schema.to_json_schema()["type"] == "object"

        print("✓ Schema DSL tests passed")
        return True
    except AssertionError as e:
        print(f"✗ Schema test failed: {e}")
        return False


def test_client_init():
    """Test client initialization."""
    print("\nTesting client initialization...")
    try:
        # Test valid initialization
        tabs = TABStack(api_key="test-key")
        assert hasattr(tabs, "extract")
        assert hasattr(tabs, "generate")
        assert hasattr(tabs, "automate")

        # Test custom base URL
        tabs_custom = TABStack(api_key="test-key", base_url="https://custom.api.com")
        assert "custom.api.com" in repr(tabs_custom)

        # Test that empty API key raises error
        try:
            TABStack(api_key="")
            print("✗ Should have raised ValueError for empty API key")
            return False
        except ValueError:
            pass  # Expected

        print("✓ Client initialization tests passed")
        return True
    except Exception as e:
        print(f"✗ Client initialization test failed: {e}")
        return False


def test_exceptions():
    """Test exception hierarchy."""
    print("\nTesting exceptions...")
    try:
        # Test exception hierarchy
        assert issubclass(BadRequestError, TABStackError)
        assert issubclass(UnauthorizedError, TABStackError)
        assert issubclass(InvalidURLError, TABStackError)
        assert issubclass(ServerError, TABStackError)
        assert issubclass(ServiceUnavailableError, TABStackError)

        # Test exception creation
        err = BadRequestError("test error")
        assert err.status_code == 400
        assert err.message == "test error"

        err2 = UnauthorizedError()
        assert err2.status_code == 401

        print("✓ Exception tests passed")
        return True
    except AssertionError as e:
        print(f"✗ Exception test failed: {e}")
        return False


def test_response_models():
    """Test response model creation."""
    print("\nTesting response models...")
    try:
        from tabstack_ai.types import (
            MarkdownResponse,
            Metadata,
            SchemaResponse,
            JsonResponse,
            AutomateEvent,
        )
        from tabstack_ai.schema import Schema

        # Test Metadata
        metadata = Metadata.from_dict(
            {"title": "Test Title", "author": "Test Author", "url": "https://example.com"}
        )
        assert metadata.title == "Test Title"
        assert metadata.author == "Test Author"

        # Test MarkdownResponse
        md_response = MarkdownResponse.from_dict(
            {"url": "https://example.com", "content": "# Test", "metadata": {"title": "Test"}}
        )
        assert md_response.url == "https://example.com"
        assert md_response.content == "# Test"
        assert md_response.metadata.title == "Test"

        # Test SchemaResponse
        schema_response = SchemaResponse.from_dict(
            {"type": "object", "properties": {"name": {"type": "string"}}}
        )
        assert isinstance(schema_response.schema, Schema)
        assert schema_response.schema.to_json_schema()["type"] == "object"

        # Test JsonResponse
        json_response = JsonResponse.from_dict({"key": "value", "count": 42})
        assert json_response.data["key"] == "value"
        assert json_response.data["count"] == 42

        # Test AutomateEvent
        event = AutomateEvent(type="task:completed", data={"finalAnswer": "Success"})
        assert event.type == "task:completed"
        assert event.data.get("finalAnswer") == "Success"

        print("✓ Response model tests passed")
        return True
    except Exception as e:
        print(f"✗ Response model test failed: {e}")
        return False


def test_package_metadata():
    """Test package metadata."""
    print("\nTesting package metadata...")
    try:
        import tabstack_ai

        assert hasattr(tabstack_ai, "__version__")
        assert hasattr(tabstack_ai, "__all__")
        assert len(tabstack_ai.__all__) > 0
        print(f"✓ Package metadata tests passed (version: {tabstack_ai.__version__})")
        return True
    except Exception as e:
        print(f"✗ Package metadata test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("TABStack AI SDK Test Suite")
    print("=" * 60)

    tests = [
        test_imports,
        test_schema,
        test_client_init,
        test_exceptions,
        test_response_models,
        test_package_metadata,
    ]

    results = [test() for test in tests]

    print("\n" + "=" * 60)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)

    if all(results):
        print("\n✓ All tests passed! SDK is ready to use.")
        return 0
    else:
        print("\n✗ Some tests failed. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
