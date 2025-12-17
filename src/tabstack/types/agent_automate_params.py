# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentAutomateParams"]


class AgentAutomateParams(TypedDict, total=False):
    task: Required[str]
    """The task description in natural language"""

    data: object
    """JSON data to provide context for form filling or complex tasks"""

    guardrails: str
    """Safety constraints for execution"""

    max_iterations: Annotated[int, PropertyInfo(alias="maxIterations")]
    """Maximum task iterations"""

    max_validation_attempts: Annotated[int, PropertyInfo(alias="maxValidationAttempts")]
    """Maximum validation attempts"""

    url: str
    """Starting URL for the task"""
