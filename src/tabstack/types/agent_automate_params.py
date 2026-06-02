# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
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

    trusted_hostnames: SequenceNotStr[str]
    """
    TrustedHostnames lists hostnames where the action firewall is bypassed for fills
    and submissions. WARNING: on listed hosts, prompt injection from page content
    can drive the agent to fill and submit any field, including personal and
    credential data. Use only for sites you fully trust to receive your data.
    """

    unsafe_mode: bool
    """
    UnsafeMode disables the action firewall entirely. WARNING: prompt injection from
    page content can then cause the agent to submit your data, including
    credentials, personal information, and conversation context, to
    attacker-controlled forms. Only enable for trusted, controlled environments.
    """

    url: str
    """Starting URL for the task"""
