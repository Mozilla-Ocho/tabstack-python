# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["V1ResearchQuestionAssessment"]


class V1ResearchQuestionAssessment(BaseModel):
    """Assessment of a single research question"""

    findings: str
    """What we learned (if answered/partial) or what's missing (if unanswered)"""

    question: str
    """The research question being assessed"""

    status: Literal["answered", "partial", "unanswered"]
    """
    Status: answered (clear info), partial (some info, gaps remain), unanswered (no
    relevant info)
    """
