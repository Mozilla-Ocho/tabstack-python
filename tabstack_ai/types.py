"""Type definitions and response models for TABStack AI SDK."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .schema import Schema


class Metadata:
    """Metadata extracted from a web page."""

    def __init__(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        author: Optional[str] = None,
        publisher: Optional[str] = None,
        image: Optional[str] = None,
        site_name: Optional[str] = None,
        url: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """Initialize metadata.

        Args:
            title: Page title
            description: Page description
            author: Author information
            publisher: Publisher information
            image: Featured image URL
            site_name: Site name
            url: Canonical URL
            type: Content type (e.g., article, website)
        """
        self.title = title
        self.description = description
        self.author = author
        self.publisher = publisher
        self.image = image
        self.site_name = site_name
        self.url = url
        self.type = type

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Metadata":
        """Create Metadata from dictionary.

        Args:
            data: Dictionary containing metadata fields

        Returns:
            Metadata instance
        """
        return cls(
            title=data.get("title"),
            description=data.get("description"),
            author=data.get("author"),
            publisher=data.get("publisher"),
            image=data.get("image"),
            site_name=data.get("site_name"),
            url=data.get("url"),
            type=data.get("type"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        result: Dict[str, Any] = {}
        if self.title is not None:
            result["title"] = self.title
        if self.description is not None:
            result["description"] = self.description
        if self.author is not None:
            result["author"] = self.author
        if self.publisher is not None:
            result["publisher"] = self.publisher
        if self.image is not None:
            result["image"] = self.image
        if self.site_name is not None:
            result["site_name"] = self.site_name
        if self.url is not None:
            result["url"] = self.url
        if self.type is not None:
            result["type"] = self.type
        return result


class MarkdownResponse:
    """Response from markdown extraction."""

    def __init__(self, url: str, content: str, metadata: Optional[Metadata] = None) -> None:
        """Initialize markdown response.

        Args:
            url: The URL that was converted
            content: The markdown content
            metadata: Optional extracted metadata
        """
        self.url = url
        self.content = content
        self.metadata = metadata

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MarkdownResponse":
        """Create MarkdownResponse from dictionary.

        Args:
            data: Dictionary containing response fields

        Returns:
            MarkdownResponse instance
        """
        metadata = None
        if "metadata" in data and data["metadata"]:
            metadata = Metadata.from_dict(data["metadata"])

        return cls(url=data["url"], content=data["content"], metadata=metadata)


class SchemaResponse:
    """Response from schema generation."""

    def __init__(self, schema: "Schema") -> None:
        """Initialize schema response.

        Args:
            schema: The generated Schema object
        """
        self.schema = schema

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SchemaResponse":
        """Create SchemaResponse from dictionary.

        Args:
            data: Dictionary containing the JSON schema

        Returns:
            SchemaResponse instance
        """
        # Import here to avoid circular import
        from .schema import Schema

        schema = Schema.from_json_schema(data)
        return cls(schema=schema)


class JsonResponse:
    """Response from JSON extraction or generation."""

    def __init__(self, data: Any) -> None:
        """Initialize JSON response.

        Args:
            data: The extracted or generated data
        """
        self.data = data

    @classmethod
    def from_dict(cls, data: Any) -> "JsonResponse":
        """Create JsonResponse from dictionary.

        Args:
            data: The response data

        Returns:
            JsonResponse instance
        """
        return cls(data=data)


class AutomateEvent:
    """Event from the automate streaming endpoint."""

    def __init__(self, type: str, data: Dict[str, Any]) -> None:
        """Initialize automate event.

        Args:
            type: Event type (e.g., 'start', 'task:completed', 'agent:extracted')
            data: Event data
        """
        self.type = type
        self.data = EventData(data)

    def __repr__(self) -> str:
        """String representation of event."""
        return f"AutomateEvent(type='{self.type}', data={self.data.raw})"


class EventData:
    """Event data with attribute access."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """Initialize event data.

        Args:
            data: Raw event data dictionary
        """
        self.raw = data

    def __getattr__(self, name: str) -> Any:
        """Get attribute from event data.

        Args:
            name: Attribute name (converts snake_case to camelCase for API)

        Returns:
            Attribute value

        Raises:
            AttributeError: If attribute doesn't exist
        """
        # Try exact match first
        if name in self.raw:
            return self.raw[name]

        # Try camelCase conversion for common patterns
        camel_name = self._to_camel_case(name)
        if camel_name in self.raw:
            return self.raw[camel_name]

        raise AttributeError(f"EventData has no attribute '{name}'")

    def _to_camel_case(self, snake_str: str) -> str:
        """Convert snake_case to camelCase.

        Args:
            snake_str: String in snake_case

        Returns:
            String in camelCase
        """
        components = snake_str.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    def get(self, key: str, default: Any = None) -> Any:
        """Get value from event data with default.

        Args:
            key: Key to retrieve
            default: Default value if key doesn't exist

        Returns:
            Value or default
        """
        return self.raw.get(key, default)

    def __repr__(self) -> str:
        """String representation of event data."""
        return f"EventData({self.raw})"
