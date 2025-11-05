# TABStack AI Python SDK - Quick Start Guide

## Installation

Choose your preferred package manager:

### pip
```bash
cd /Users/tbeauvais/workspace/tabs-python
pip install -e .
```

### poetry
```bash
cd /Users/tbeauvais/workspace/tabs-python
poetry install
```

### pipenv
```bash
cd /Users/tbeauvais/workspace/tabs-python
pipenv install -e .
```

### setuptools
```bash
cd /Users/tbeauvais/workspace/tabs-python
python setup.py install
```

## Basic Usage

### Initialize the Client

```python
import os
from tabstack_ai import TABStack

tabs = TABStack(api_key=os.getenv('TABSTACK_API_KEY'))
```

### Extract Markdown

```python
result = tabs.extract.markdown(
    url="https://example.com/article",
    metadata=True
)
print(result.content)
print(result.metadata.title)
```

### Extract Structured JSON

```python
from tabstack_ai.schema import Schema, String, Number, Array, Object

schema = Schema(
    stories=Array(
        Object(
            title=String,
            points=Number,
            author=String,
        )
    )
)

result = tabs.extract.json(
    url="https://news.ycombinator.com",
    schema=schema
)
print(result.data)
```

### Generate Schema

```python
result = tabs.extract.schema(
    url="https://news.ycombinator.com",
    instructions="extract top stories with title and points"
)
# result.schema is a Schema object
print(result.schema.to_json_schema())
# Can be used directly with extract.json()
data = tabs.extract.json(url="https://news.ycombinator.com", schema=result.schema)
```

### Generate Transformed Content

```python
from tabstack_ai.schema import Schema, String, Array, Object

schema = Schema(
    summaries=Array(
        Object(
            title=String,
            category=String,
            summary=String,
        )
    )
)

result = tabs.generate.json(
    url="https://news.ycombinator.com",
    schema=schema,
    instructions="Categorize each story and write a summary"
)
print(result.data)
```

### Automate Web Tasks

```python
for event in tabs.automate.execute(
    task="Find the top 3 trending repositories",
    url="https://github.com/trending",
    guardrails="browse and extract only"
):
    if event.type == "task:completed":
        print(f"Result: {event.data.final_answer}")
    elif event.type == "agent:extracted":
        print(f"Extracted: {event.data.extracted_data}")
```

## Schema DSL

The SDK provides an intuitive DSL for defining schemas:

```python
from tabstack_ai.schema import (
    Schema,
    String,
    Number,
    Boolean,
    Array,
    Object
)

# Simple schema
schema = Schema(
    name=String,
    age=Number,
    active=Boolean
)

# Nested schema
schema = Schema(
    user=Object(
        name=String,
        email=String,
        age=Number
    ),
    tags=Array(String),
    scores=Array(Number)
)

# Complex nested schema
schema = Schema(
    products=Array(
        Object(
            name=String,
            price=Number,
            in_stock=Boolean,
            categories=Array(String),
            details=Object(
                weight=Number,
                dimensions=String
            )
        )
    )
)
```

## Error Handling

```python
from tabstack_ai.exceptions import (
    TABStackError,
    BadRequestError,
    UnauthorizedError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError
)

try:
    result = tabs.extract.markdown(url="https://example.com")
except UnauthorizedError:
    print("Invalid API key")
except InvalidURLError:
    print("Invalid or inaccessible URL")
except ServerError as e:
    print(f"Server error: {e.message}")
except TABStackError as e:
    print(f"API error: {e.message} (status: {e.status_code})")
```

## Features

✓ **Fully Typed**: Complete type hints for IDE support and type checking
✓ **Zero Dependencies**: Built using only Python standard library (http.client)
✓ **Custom Schema DSL**: Intuitive schema definition system
✓ **Comprehensive Error Handling**: Custom exceptions for all API error types
✓ **Streaming Support**: Server-Sent Events (SSE) for automate endpoint
✓ **Multiple Package Managers**: Works with pip, poetry, pipenv, and setuptools
✓ **Python 3.8+**: Compatible with Python 3.8 through 3.12

## Testing

Run the included test suite:

```bash
python test_sdk.py
```

Run the example file:

```bash
export TABSTACK_API_KEY="your-api-key"
python example.py
```

## API Reference

Full documentation: [README.md](README.md)

## Support

- Documentation: https://docs.tabstack.ai
- Issues: https://github.com/tabstack/tabs-python/issues
- Email: support@tabstack.ai
