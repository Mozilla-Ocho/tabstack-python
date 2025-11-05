# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-04

### Added
- Initial release of TABStack AI Python SDK
- `TABStack` client class for API interaction
- `Extract` operator with three methods:
  - `markdown()` - Convert URLs to markdown
  - `schema()` - Generate schemas from URL content (returns Schema object)
  - `json()` - Extract structured JSON using schemas
- `Generate` operator with `json()` method for AI-powered content transformation
- `Automate` operator with `execute()` method for streaming web automation
- Custom Schema DSL for intuitive schema definition
- `Schema.from_json_schema()` class method to convert JSON schemas to Schema objects
- Fully typed response models:
  - `MarkdownResponse`
  - `SchemaResponse` (contains Schema object)
  - `JsonResponse`
  - `AutomateEvent` and `EventData`
- Custom exceptions for all API errors:
  - `TABStackError` (base)
  - `BadRequestError`
  - `UnauthorizedError`
  - `InvalidURLError`
  - `ServerError`
  - `ServiceUnavailableError`
  - `APIError`
- Zero third-party dependencies (uses stdlib `http.client`)
- Support for multiple package managers (pip, poetry, pipenv, setuptools)
- Complete type hints throughout
- Comprehensive test suite
- Full documentation (README, QUICKSTART, CONTRIBUTING)

### Changed
- N/A (initial release)

### Deprecated
- N/A (initial release)

### Removed
- N/A (initial release)

### Fixed
- N/A (initial release)

### Security
- Bearer token authentication via Authorization header
- No credentials stored in codebase
