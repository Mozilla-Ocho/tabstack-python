# Contributing to TABStack AI Python SDK

## Development Setup

### Prerequisites
- Python 3.8 or higher
- uv, pip, poetry, or pipenv

### Installation for Development

#### Using uv (recommended)
```bash
# Clone the repository
git clone https://github.com/tabstack/tabs-python.git
cd tabs-python

# Create a virtual environment and install in development mode
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install package with dev dependencies
uv pip install -e ".[dev]"
```

#### Using pip
```bash
# Clone the repository
git clone https://github.com/tabstack/tabs-python.git
cd tabs-python

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

#### Using poetry
```bash
# Clone the repository
git clone https://github.com/tabstack/tabs-python.git
cd tabs-python

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

#### Using pipenv
```bash
# Clone the repository
git clone https://github.com/tabstack/tabs-python.git
cd tabs-python

# Install dependencies
pipenv install --dev

# Activate virtual environment
pipenv shell
```

### Running Tests

```bash
# Run the test suite
python test_sdk.py

# Run example file (requires API key)
export TABSTACK_API_KEY="your-api-key"
python example.py
```

### Type Checking

```bash
# With uv (if dev dependencies installed)
uv run mypy tabstack_ai

# Or with pip-installed mypy
mypy tabstack_ai
```

### Code Formatting

```bash
# With uv (if dev dependencies installed)
uv run black tabstack_ai

# Or with pip-installed black
black tabstack_ai
```

### Linting

```bash
# With uv (if dev dependencies installed)
uv run ruff check tabstack_ai

# Or with pip-installed ruff
ruff check tabstack_ai
```

## Project Structure

```
tabs-python/
├── tabstack_ai/           # Main package directory
│   ├── __init__.py        # Package exports
│   ├── client.py          # Main TABStack client
│   ├── _http_client.py    # Internal HTTP client
│   ├── schema.py          # Schema DSL
│   ├── types.py           # Response models
│   ├── exceptions.py      # Custom exceptions
│   ├── extract.py         # Extract operator
│   ├── generate.py        # Generate operator
│   ├── automate.py        # Automate operator
│   └── py.typed           # Type hints marker
├── setup.py               # Setuptools configuration
├── setup.cfg              # Setuptools metadata
├── pyproject.toml         # Modern Python project config
├── Pipfile                # Pipenv configuration
├── README.md              # User documentation
├── CONTRIBUTING.md        # Development documentation
├── LICENSE                # MIT License
├── example.py             # Usage examples
└── test_sdk.py            # Test suite
```

## Code Style Guidelines

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Write docstrings for all public classes and methods (Google style)
- Keep functions focused and single-purpose
- Maximum line length: 100 characters

## Adding New Features

1. Create a new branch for your feature
2. Implement the feature with type hints
3. Add docstrings with examples
4. Update tests if needed
5. Run the test suite to ensure everything passes
6. Submit a pull request

## Release Process

1. Update version in `pyproject.toml`, `setup.py`, and `tabstack_ai/__init__.py`
2. Update CHANGELOG.md
3. Create a git tag: `git tag v1.0.0`
4. Build the package:
   - With uv: `uv build`
   - Or with build: `python -m build`
5. Upload to PyPI: `uv publish` or `twine upload dist/*`

## Questions or Issues?

- Documentation: https://docs.tabstack.ai
- Issues: https://github.com/tabstack/tabs-python/issues
- Email: support@tabstack.ai
