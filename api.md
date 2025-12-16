# Automate

Types:

```python
from tabstack.types import AutomateExecuteResponse
```

Methods:

- <code title="post /automate">client.automate.<a href="./src/tabstack/resources/automate.py">execute</a>(\*\*<a href="src/tabstack/types/automate_execute_params.py">params</a>) -> str</code>

# Extract

Types:

```python
from tabstack.types import ExtractCreateJsonResponse, ExtractCreateMarkdownResponse
```

Methods:

- <code title="post /extract/json">client.extract.<a href="./src/tabstack/resources/extract.py">create_json</a>(\*\*<a href="src/tabstack/types/extract_create_json_params.py">params</a>) -> <a href="./src/tabstack/types/extract_create_json_response.py">ExtractCreateJsonResponse</a></code>
- <code title="post /extract/markdown">client.extract.<a href="./src/tabstack/resources/extract.py">create_markdown</a>(\*\*<a href="src/tabstack/types/extract_create_markdown_params.py">params</a>) -> <a href="./src/tabstack/types/extract_create_markdown_response.py">ExtractCreateMarkdownResponse</a></code>

# Generate

Types:

```python
from tabstack.types import GenerateCreateJsonResponse
```

Methods:

- <code title="post /generate/json">client.generate.<a href="./src/tabstack/resources/generate.py">create_json</a>(\*\*<a href="src/tabstack/types/generate_create_json_params.py">params</a>) -> <a href="./src/tabstack/types/generate_create_json_response.py">GenerateCreateJsonResponse</a></code>
