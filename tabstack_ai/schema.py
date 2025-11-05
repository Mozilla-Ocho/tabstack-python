"""Schema definition system for TABStack AI SDK.

This module provides a DSL for defining JSON schemas in a Pythonic way.
"""

from typing import Any, Dict, Optional, Union


class SchemaType:
    """Base class for schema types."""

    def to_json_schema(self) -> Dict[str, Any]:
        """Convert to JSON Schema format."""
        raise NotImplementedError


class StringType(SchemaType):
    """String type."""

    def __init__(self, description: Optional[str] = None) -> None:
        self.description = description

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {"type": "string"}
        if self.description:
            schema["description"] = self.description
        return schema


class NumberType(SchemaType):
    """Number type."""

    def __init__(self, description: Optional[str] = None) -> None:
        self.description = description

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {"type": "number"}
        if self.description:
            schema["description"] = self.description
        return schema


class BooleanType(SchemaType):
    """Boolean type."""

    def __init__(self, description: Optional[str] = None) -> None:
        self.description = description

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {"type": "boolean"}
        if self.description:
            schema["description"] = self.description
        return schema


class ObjectType(SchemaType):
    """Object type with properties."""

    def __init__(self, description: Optional[str] = None, **properties: SchemaType) -> None:
        self.description = description
        self.properties = properties

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {
            "type": "object",
            "properties": {key: prop.to_json_schema() for key, prop in self.properties.items()},
            "required": list(self.properties.keys()),
            "additionalProperties": False,
        }
        if self.description:
            schema["description"] = self.description
        return schema


class ArrayType(SchemaType):
    """Array type with item schema."""

    def __init__(self, items: SchemaType, description: Optional[str] = None) -> None:
        self.items = items
        self.description = description

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {"type": "array", "items": self.items.to_json_schema()}
        if self.description:
            schema["description"] = self.description
        return schema


# Convenience instances for simple types
String = StringType()
Number = NumberType()
Boolean = BooleanType()


# Factory functions for types with parameters
def Object(description: Optional[str] = None, **properties: SchemaType) -> ObjectType:
    """Create an object type with properties.

    Args:
        description: Optional description of the object
        **properties: Keyword arguments mapping property names to their schema types

    Returns:
        ObjectType instance

    Example:
        >>> Object(
        ...     title=String,
        ...     count=Number
        ... )
    """
    return ObjectType(description=description, **properties)


def Array(items: SchemaType, description: Optional[str] = None) -> ArrayType:
    """Create an array type.

    Args:
        items: Schema type for array items
        description: Optional description of the array

    Returns:
        ArrayType instance

    Example:
        >>> Array(String)
        >>> Array(Object(title=String, count=Number))
    """
    return ArrayType(items=items, description=description)


class Schema:
    """Root schema definition.

    This class provides a convenient DSL for defining JSON schemas.

    Example:
        >>> schema = Schema(
        ...     name=String,
        ...     age=Number,
        ...     tags=Array(String),
        ...     address=Object(
        ...         street=String,
        ...         city=String,
        ...     )
        ... )
    """

    def __init__(self, **properties: SchemaType) -> None:
        """Initialize a schema with properties.

        Args:
            **properties: Keyword arguments mapping property names to their schema types
        """
        self.properties = properties

    def to_json_schema(self) -> Dict[str, Any]:
        """Convert to JSON Schema format.

        Returns:
            Dictionary representing a JSON Schema
        """
        return {
            "type": "object",
            "properties": {key: prop.to_json_schema() for key, prop in self.properties.items()},
            "required": list(self.properties.keys()),
            "additionalProperties": False,
        }

    def to_dict(self) -> Dict[str, Any]:
        """Alias for to_json_schema for backwards compatibility."""
        return self.to_json_schema()

    @classmethod
    def from_json_schema(cls, json_schema: Dict[str, Any]) -> "Schema":
        """Create a Schema from a JSON Schema dictionary.

        Args:
            json_schema: JSON Schema dictionary

        Returns:
            Schema instance

        Example:
            >>> json_schema = {
            ...     "type": "object",
            ...     "properties": {
            ...         "name": {"type": "string"},
            ...         "age": {"type": "number"}
            ...     }
            ... }
            >>> schema = Schema.from_json_schema(json_schema)
        """
        if json_schema.get("type") != "object":
            raise ValueError("Root schema must be of type 'object'")

        properties_dict = json_schema.get("properties", {})
        properties = {}

        for key, prop_schema in properties_dict.items():
            properties[key] = _parse_schema_type(prop_schema)

        return cls(**properties)


def _parse_schema_type(schema: Dict[str, Any]) -> SchemaType:
    """Parse a JSON schema property into a SchemaType.

    Args:
        schema: JSON schema property dictionary

    Returns:
        SchemaType instance
    """
    schema_type = schema.get("type")
    description = schema.get("description")

    if schema_type == "string":
        return StringType(description=description)
    elif schema_type == "number":
        return NumberType(description=description)
    elif schema_type == "boolean":
        return BooleanType(description=description)
    elif schema_type == "array":
        items_schema = schema.get("items", {})
        items_type = _parse_schema_type(items_schema)
        return ArrayType(items=items_type, description=description)
    elif schema_type == "object":
        properties_dict = schema.get("properties", {})
        properties = {}
        for key, prop_schema in properties_dict.items():
            properties[key] = _parse_schema_type(prop_schema)
        return ObjectType(description=description, **properties)
    else:
        # Fallback to string type for unknown types
        return StringType(description=description)


# Type alias for convenience
SchemaInput = Union[Schema, Dict[str, Any]]
