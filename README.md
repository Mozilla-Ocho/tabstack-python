# TABStack AI Python SDK

Python SDK for TABStack AI - Extract, Generate, and Automate web content using AI.

## Installation

### Using uv (recommended)
```bash
uv pip install tabstack-ai
```

Or add to your project:
```bash
uv add tabstack-ai
```

### Using pip
```bash
pip install tabstack-ai
```

### Using poetry
```bash
poetry add tabstack-ai
```

### Using pipenv
```bash
pipenv install tabstack-ai
```

## Quick Start

```python
import os
from tabstack_ai import TABStack
from tabstack_ai.schema import Schema, String, Number, Object, Array

# Initialize the client
tabs = TABStack(api_key=os.getenv('TABSTACK_API_KEY'))
tabs = TABStack(api_key="a9bd2978f7d52c25c7661ad751a106e10a767565d566d5128ca5fb90b26425f4")

# Extract markdown from a URL
result = tabs.extract.markdown(
    url="https://news.ycombinator.com",
    metadata=True
)
print(result.content)
print(result.metadata.title)

# Extract structured JSON data
schema = Schema(
    stories=Array(
        Object(
            title=String,
            points=Number,
            author=String,
        )
    )
)

data = tabs.extract.json(
    url="https://news.ycombinator.com",
    schema=schema
)

# Generate transformed content with AI
summary_schema = Schema(
    summaries=Array(
        Object(
            title=String,
            category=String,
            summary=String,
        )
    )
)

summaries = tabs.generate.json(
    url="https://news.ycombinator.com",
    schema=summary_schema,
    instructions="For each story, categorize it and write a one-sentence summary"
)

# Automate web tasks (streaming)
for event in tabs.automate.execute(
    task="Find the top 3 trending repositories and extract their details",
    url="https://github.com/trending",
    guardrails="browse and extract only"
):
    if event.type == "task:completed":
        print(f"Result: {event.data.final_answer}")
    elif event.type == "agent:extracted":
        print(f"Extracted: {event.data.extracted_data}")
```

## Features

- **Extract**: Convert web content to markdown or structured JSON
- **Generate**: Transform and enhance web data with AI
- **Automate**: Execute complex web automation tasks using natural language
- **Fully Typed**: Complete type hints for better IDE support
- **Custom Schema DSL**: Intuitive schema definition for data extraction
- **Zero Dependencies**: Built using only Python standard library
- **Comprehensive Error Handling**: Custom exceptions for all API errors

## API Reference

### Extract

#### `extract.markdown(url, metadata=False, nocache=False)`
Convert URL content to Markdown format.

#### `extract.schema(url, instructions=None, nocache=False)`
Generate a schema from URL content.

#### `extract.json(url, schema, nocache=False)`
Extract structured JSON data from a URL using a schema.

### Generate

#### `generate.json(url, schema, instructions, nocache=False)`
Generate transformed JSON with AI based on custom instructions.

### Automate

#### `automate.execute(task, url=None, data=None, guardrails=None, max_iterations=50, max_validation_attempts=3)`
Execute AI-powered browser automation tasks (returns streaming iterator).

## Schema DSL

Define schemas using the intuitive Schema DSL:

```python
from tabstack_ai.schema import Schema, String, Number, Object, Array, Boolean

schema = Schema(
    title=String,
    price=Number,
    in_stock=Boolean,
    tags=Array(String),
    details=Object(
        weight=Number,
        dimensions=String,
    )
)
```

## Error Handling

The SDK provides custom exceptions for different error types:

```python
from tabstack_ai.exceptions import (
    TABStackError,
    BadRequestError,
    UnauthorizedError,
    InvalidURLError,
    ServerError,
    ServiceUnavailableError,
)

try:
    result = tabs.extract.markdown(url="https://example.com")
except UnauthorizedError:
    print("Invalid API key")
except InvalidURLError:
    print("Invalid or inaccessible URL")
except ServerError as e:
    print(f"Server error: {e}")
```

## License

MIT License

## Support

- Documentation: https://docs.tabstack.ai
- Issues: https://github.com/tabstack/tabs-python/issues
- Email: support@tabstack.ai
