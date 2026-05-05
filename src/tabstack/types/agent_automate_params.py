# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.geotarget_geo_target import GeotargetGeoTarget

__all__ = ["AgentAutomateParams"]


class AgentAutomateParams(TypedDict, total=False):
    task: Required[str]
    """The task description in natural language"""

    data: object
    """JSON data to provide context for form filling or complex tasks"""

    geo_target: GeotargetGeoTarget
    """Optional geotargeting parameters for proxy requests"""

    guardrails: str
    """Safety constraints for execution"""

    interactive: bool
    """Enable interactive mode to allow human-in-the-loop input during task execution"""

    max_iterations: Annotated[int, PropertyInfo(alias="maxIterations")]
    """Maximum task iterations"""

    max_validation_attempts: Annotated[int, PropertyInfo(alias="maxValidationAttempts")]
    """Maximum validation attempts"""

    url: str
    """Starting URL for the task"""
