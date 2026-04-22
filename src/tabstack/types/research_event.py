# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResearchEvent",
    "V1ResearchEventAnalyzingEnd",
    "V1ResearchEventAnalyzingEndData",
    "V1ResearchEventAnalyzingEndDataSample",
    "V1ResearchEventAnalyzingStart",
    "V1ResearchEventAnalyzingStartData",
    "V1ResearchEventComplete",
    "V1ResearchEventCompleteData",
    "V1ResearchEventCompleteDataMetadata",
    "V1ResearchEventCompleteDataMetadataCitedPage",
    "V1ResearchEventCompleteDataMetadataGapEvaluation",
    "V1ResearchEventCompleteDataMetadataGapEvaluationQuestionAssessment",
    "V1ResearchEventCompleteDataMetadataJudgment",
    "V1ResearchEventCompleteDataMetadataMetrics",
    "V1ResearchEventCompleteDataMetadataMetricsPhases",
    "V1ResearchEventCompleteDataMetadataMetricsSuccessRates",
    "V1ResearchEventCompleteDataMetadataMetricsTokens",
    "V1ResearchEventCompleteDataMetadataOutline",
    "V1ResearchEventCompleteDataMetadataURLSources",
    "V1ResearchEventError",
    "V1ResearchEventErrorData",
    "V1ResearchEventErrorDataError",
    "V1ResearchEventEvaluatingEnd",
    "V1ResearchEventEvaluatingEndData",
    "V1ResearchEventEvaluatingEndDataQuestionAssessment",
    "V1ResearchEventEvaluatingStart",
    "V1ResearchEventEvaluatingStartData",
    "V1ResearchEventFollowingEnd",
    "V1ResearchEventFollowingEndData",
    "V1ResearchEventFollowingEndDataSample",
    "V1ResearchEventFollowingStart",
    "V1ResearchEventFollowingStartData",
    "V1ResearchEventIterationEnd",
    "V1ResearchEventIterationEndData",
    "V1ResearchEventIterationStart",
    "V1ResearchEventIterationStartData",
    "V1ResearchEventJudgingEnd",
    "V1ResearchEventJudgingEndData",
    "V1ResearchEventJudgingStart",
    "V1ResearchEventJudgingStartData",
    "V1ResearchEventOutliningEnd",
    "V1ResearchEventOutliningEndData",
    "V1ResearchEventOutliningStart",
    "V1ResearchEventOutliningStartData",
    "V1ResearchEventPlanningEnd",
    "V1ResearchEventPlanningEndData",
    "V1ResearchEventPlanningStart",
    "V1ResearchEventPlanningStartData",
    "V1ResearchEventPrefetchingEnd",
    "V1ResearchEventPrefetchingEndData",
    "V1ResearchEventPrefetchingStart",
    "V1ResearchEventPrefetchingStartData",
    "V1ResearchEventSearchingEnd",
    "V1ResearchEventSearchingEndData",
    "V1ResearchEventSearchingStart",
    "V1ResearchEventSearchingStartData",
    "V1ResearchEventStart",
    "V1ResearchEventStartData",
    "V1ResearchEventWritingEnd",
    "V1ResearchEventWritingEndData",
    "V1ResearchEventWritingStart",
    "V1ResearchEventWritingStartData",
]


class V1ResearchEventAnalyzingEndDataSample(BaseModel):
    """Page sample - lightweight representation for event payloads"""

    domain: str

    title: str

    url: str

    url_source: Literal["user-input", "search-result", "extracted-link"] = FieldInfo(alias="urlSource")
    """URL source tracking - where a URL came from"""

    relevance: Optional[Literal["low", "medium", "high"]] = None

    reliability: Optional[Literal["low", "medium", "high"]] = None

    summary: Optional[str] = None


class V1ResearchEventAnalyzingEndData(BaseModel):
    analyzed: float

    failed: float

    iteration: float

    message: str

    samples: List[V1ResearchEventAnalyzingEndDataSample]

    timestamp: float


class V1ResearchEventAnalyzingEnd(BaseModel):
    """Envelope for the "analyzing:end" event from /v1/research."""

    data: V1ResearchEventAnalyzingEndData

    event: Literal["analyzing:end"]


class V1ResearchEventAnalyzingStartData(BaseModel):
    iteration: float

    message: str

    page_count: float = FieldInfo(alias="pageCount")

    timestamp: float


class V1ResearchEventAnalyzingStart(BaseModel):
    """Envelope for the "analyzing:start" event from /v1/research."""

    data: V1ResearchEventAnalyzingStartData

    event: Literal["analyzing:start"]


class V1ResearchEventCompleteDataMetadataCitedPage(BaseModel):
    id: str

    claims: List[str]

    source_queries: List[str] = FieldInfo(alias="sourceQueries")

    url: str

    depth: Optional[float] = None

    full_text: Optional[str] = FieldInfo(alias="fullText", default=None)
    """Full page text (fetched markdown or search excerpts).

    Only populated when `includeFullText: true` in ResearchOptions.

    - Fast mode: Parallel API excerpts (~5000 chars)
    - Other modes: Fetched page markdown
    """

    parent_url: Optional[str] = FieldInfo(alias="parentUrl", default=None)

    relevance: Optional[Literal["low", "medium", "high"]] = None

    reliability: Optional[Literal["low", "medium", "high"]] = None

    summary: Optional[str] = None
    """LLM-generated summary. Undefined in fast mode (no content analysis)."""

    title: Optional[str] = None

    url_source: Optional[Literal["user-input", "search-result", "extracted-link"]] = FieldInfo(
        alias="urlSource", default=None
    )
    """URL source tracking - where a URL came from"""


class V1ResearchEventCompleteDataMetadataGapEvaluationQuestionAssessment(BaseModel):
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


class V1ResearchEventCompleteDataMetadataGapEvaluation(BaseModel):
    """Gap evaluation results from research strategist"""

    gap_description: str = FieldInfo(alias="gapDescription")
    """
    Based on unanswered/partial questions, what specific information is still
    needed?
    """

    question_assessments: List[V1ResearchEventCompleteDataMetadataGapEvaluationQuestionAssessment] = FieldInfo(
        alias="questionAssessments"
    )
    """Assessment of each research question's status and findings"""

    research_coverage: Literal["Light", "Moderate", "Solid", "Comprehensive"] = FieldInfo(alias="researchCoverage")
    """Research coverage level - assesses quality across all questions.

    Hierarchy: Light < Moderate < Solid < Comprehensive

    - **Light**: Basic info on some questions, most need more depth → Continue
    - **Moderate**: Multiple questions answered, some remain partial → Continue
    - **Solid**: Most questions well-answered with validated sources → Sufficient to
      stop
    - **Comprehensive**: All questions thoroughly answered, exceptional depth →
      Definitely stop
    """

    should_continue_research: bool = FieldInfo(alias="shouldContinueResearch")
    """Explicit decision: should research continue with another iteration?

    - Considers: how many questions unanswered/partial, coverage for mode, remaining
      iterations
    - Drives query generation: true → generate queries, false → stop researching
    """

    new_research_questions: Optional[List[str]] = FieldInfo(alias="newResearchQuestions", default=None)
    """New research questions to add (optional, use sparingly)

    - Only if original decomposition missed something critical
    - Maximum 2-3 new questions total across all iterations
    - Most iterations should return empty array or omit this field
    """

    search_queries: Optional[List[str]] = FieldInfo(alias="searchQueries", default=None)
    """
    Search queries to address identified gaps (only when shouldContinueResearch is
    true)

    - Target unanswered questions first, then partial questions
    - 3-10 targeted queries if shouldContinueResearch is true
    - Omit or provide empty array if shouldContinueResearch is false
    """


class V1ResearchEventCompleteDataMetadataJudgment(BaseModel):
    """Judgment result from research judge"""

    approved: bool

    observation: str

    score: float

    feedback: Optional[str] = None


class V1ResearchEventCompleteDataMetadataMetricsPhases(BaseModel):
    duration: float


class V1ResearchEventCompleteDataMetadataMetricsSuccessRates(BaseModel):
    """Success rates (0-1) for various operations"""

    analyzes: float

    fetches: float

    searches: float


class V1ResearchEventCompleteDataMetadataMetricsTokens(BaseModel):
    """Token usage for a specific model"""

    input: float

    output: float


class V1ResearchEventCompleteDataMetadataMetrics(BaseModel):
    """Complete research metrics"""

    cached_fetches: float = FieldInfo(alias="cachedFetches")
    """Cached fetch count (subset of fetches)"""

    cached_searches: Dict[str, float] = FieldInfo(alias="cachedSearches")
    """Cached search count by provider name (subset of searches)"""

    fetches: float
    """Fetch count (number of pages fetched)"""

    iterations: float
    """Number of research iterations performed"""

    phases: Dict[str, V1ResearchEventCompleteDataMetadataMetricsPhases]
    """Phase timings with duration in milliseconds"""

    robots_blocked: float = FieldInfo(alias="robotsBlocked")
    """Number of URLs blocked by robots.txt"""

    searches: Dict[str, float]
    """Search count by provider name (e.g., "bright-data", "parallel")"""

    success_rates: V1ResearchEventCompleteDataMetadataMetricsSuccessRates = FieldInfo(alias="successRates")
    """Success rates (0-1) for various operations"""

    tokens: Dict[str, V1ResearchEventCompleteDataMetadataMetricsTokens]
    """Token usage by model ID (e.g., "gemini-2.5-flash")"""

    total_duration: float = FieldInfo(alias="totalDuration")
    """Total duration in milliseconds"""


class V1ResearchEventCompleteDataMetadataOutline(BaseModel):
    """Report outline from research writer"""

    direct_answer: str = FieldInfo(alias="directAnswer")

    key_takeaways: List[str] = FieldInfo(alias="keyTakeaways")

    outline: str

    relevant_source_ids: List[str] = FieldInfo(alias="relevantSourceIds")


class V1ResearchEventCompleteDataMetadataURLSources(BaseModel):
    extracted_links: float = FieldInfo(alias="extractedLinks")

    search_results: float = FieldInfo(alias="searchResults")

    user_provided: float = FieldInfo(alias="userProvided")


class V1ResearchEventCompleteDataMetadata(BaseModel):
    """Research metadata

    Note: citedPages, gapEvaluations, outline, and judgments are optional to support fast mode, which skips these phases for maximum speed.
    """

    executed_queries: List[List[str]] = FieldInfo(alias="executedQueries")

    mode: Literal["fast", "balanced", "deep", "max", "ultra"]
    """Research mode determines depth, thinking budget, and quality controls

    Modes (in order of cost/thoroughness):

    - **fast**: Quick answers with minimal validation (~$2, 1 iteration, no judge)
    - **balanced**: Standard research with moderate depth (~$8, 3 iterations, Flash
      models, no judge)
    - **deep**: Thorough research with judge review (~$15, 5 iterations, Flash
      models, with judge)
    - **max**: Maximum quality with Pro models (~$40, 5 iterations, Pro models, with
      judge)
    - **ultra**: Ultimate tier - all Pro models, 10 iterations (expensive, for when
      accuracy is paramount)
    """

    prompt: str

    query_complexity: Literal["simple", "moderate", "complex"] = FieldInfo(alias="queryComplexity")

    research_objective: str = FieldInfo(alias="researchObjective")

    research_plan: str = FieldInfo(alias="researchPlan")

    research_questions: List[str] = FieldInfo(alias="researchQuestions")

    total_pages_analyzed: float = FieldInfo(alias="totalPagesAnalyzed")
    """Total pages analyzed across all iterations"""

    cited_pages: Optional[List[V1ResearchEventCompleteDataMetadataCitedPage]] = FieldInfo(
        alias="citedPages", default=None
    )
    """Pages cited in the report, ordered by first citation appearance"""

    gap_evaluations: Optional[List[V1ResearchEventCompleteDataMetadataGapEvaluation]] = FieldInfo(
        alias="gapEvaluations", default=None
    )

    judgments: Optional[List[V1ResearchEventCompleteDataMetadataJudgment]] = None

    metrics: Optional[V1ResearchEventCompleteDataMetadataMetrics] = None
    """Complete research metrics"""

    outline: Optional[V1ResearchEventCompleteDataMetadataOutline] = None
    """Report outline from research writer"""

    url_sources: Optional[V1ResearchEventCompleteDataMetadataURLSources] = FieldInfo(alias="urlSources", default=None)


class V1ResearchEventCompleteData(BaseModel):
    """complete - Research finished successfully"""

    message: str

    metadata: V1ResearchEventCompleteDataMetadata
    """Research metadata

    Note: citedPages, gapEvaluations, outline, and judgments are optional to support
    fast mode, which skips these phases for maximum speed.
    """

    report: str

    timestamp: float


class V1ResearchEventComplete(BaseModel):
    """Envelope for the "complete" event from /v1/research."""

    data: V1ResearchEventCompleteData
    """complete - Research finished successfully"""

    event: Literal["complete"]


class V1ResearchEventErrorDataError(BaseModel):
    message: str

    name: str

    stack: Optional[str] = None


class V1ResearchEventErrorData(BaseModel):
    """error - Research failed"""

    error: V1ResearchEventErrorDataError

    message: str

    timestamp: float

    activity: Optional[
        Literal[
            "prefetching",
            "planning",
            "iteration",
            "searching",
            "analyzing",
            "following",
            "evaluating",
            "outlining",
            "writing",
            "judging",
        ]
    ] = None
    """Activity types for research workflow"""

    iteration: Optional[float] = None


class V1ResearchEventError(BaseModel):
    """Envelope for the "error" event from /v1/research."""

    data: V1ResearchEventErrorData
    """error - Research failed"""

    event: Literal["error"]


class V1ResearchEventEvaluatingEndDataQuestionAssessment(BaseModel):
    """Question assessment for evaluating:end payload"""

    findings: str
    """What we learned (if answered/partial) or what's missing (if unanswered)"""

    question: str
    """The research question being assessed"""

    status: Literal["answered", "partial", "unanswered"]
    """
    Status: answered (clear info), partial (some info, gaps remain), unanswered (no
    relevant info)
    """


class V1ResearchEventEvaluatingEndData(BaseModel):
    coverage: Literal["Light", "Moderate", "Solid", "Comprehensive"]

    gaps: str

    iteration: float

    message: str

    next_queries: List[str] = FieldInfo(alias="nextQueries")

    question_assessments: List[V1ResearchEventEvaluatingEndDataQuestionAssessment] = FieldInfo(
        alias="questionAssessments"
    )

    should_continue: bool = FieldInfo(alias="shouldContinue")

    timestamp: float


class V1ResearchEventEvaluatingEnd(BaseModel):
    """Envelope for the "evaluating:end" event from /v1/research."""

    data: V1ResearchEventEvaluatingEndData

    event: Literal["evaluating:end"]


class V1ResearchEventEvaluatingStartData(BaseModel):
    iteration: float

    message: str

    pages_analyzed: float = FieldInfo(alias="pagesAnalyzed")
    """Total pages analyzed so far (including this iteration)"""

    question_count: float = FieldInfo(alias="questionCount")
    """Number of research questions being assessed"""

    timestamp: float


class V1ResearchEventEvaluatingStart(BaseModel):
    """Envelope for the "evaluating:start" event from /v1/research."""

    data: V1ResearchEventEvaluatingStartData

    event: Literal["evaluating:start"]


class V1ResearchEventFollowingEndDataSample(BaseModel):
    """Page sample - lightweight representation for event payloads"""

    domain: str

    title: str

    url: str

    url_source: Literal["user-input", "search-result", "extracted-link"] = FieldInfo(alias="urlSource")
    """URL source tracking - where a URL came from"""

    relevance: Optional[Literal["low", "medium", "high"]] = None

    reliability: Optional[Literal["low", "medium", "high"]] = None

    summary: Optional[str] = None


class V1ResearchEventFollowingEndData(BaseModel):
    failed: float

    followed: float

    iteration: float

    message: str

    samples: List[V1ResearchEventFollowingEndDataSample]

    timestamp: float


class V1ResearchEventFollowingEnd(BaseModel):
    """Envelope for the "following:end" event from /v1/research."""

    data: V1ResearchEventFollowingEndData

    event: Literal["following:end"]


class V1ResearchEventFollowingStartData(BaseModel):
    iteration: float

    link_count: float = FieldInfo(alias="linkCount")

    message: str

    timestamp: float


class V1ResearchEventFollowingStart(BaseModel):
    """Envelope for the "following:start" event from /v1/research."""

    data: V1ResearchEventFollowingStartData

    event: Literal["following:start"]


class V1ResearchEventIterationEndData(BaseModel):
    is_last: bool = FieldInfo(alias="isLast")
    """Whether this is the final iteration"""

    iteration: float

    message: str

    timestamp: float

    stop_reason: Optional[Literal["max_iterations", "coverage_sufficient"]] = FieldInfo(
        alias="stopReason", default=None
    )
    """Why research iterations stopped (only present when isLast is true)"""


class V1ResearchEventIterationEnd(BaseModel):
    """Envelope for the "iteration:end" event from /v1/research."""

    data: V1ResearchEventIterationEndData

    event: Literal["iteration:end"]


class V1ResearchEventIterationStartData(BaseModel):
    iteration: float

    max_iterations: float = FieldInfo(alias="maxIterations")
    """Maximum iterations for this research mode"""

    message: str

    queries: List[str]
    """Search queries to execute in this iteration"""

    timestamp: float


class V1ResearchEventIterationStart(BaseModel):
    """Envelope for the "iteration:start" event from /v1/research."""

    data: V1ResearchEventIterationStartData

    event: Literal["iteration:start"]


class V1ResearchEventJudgingEndData(BaseModel):
    approved: bool

    attempt: float

    message: str

    score: float

    timestamp: float

    feedback: Optional[str] = None


class V1ResearchEventJudgingEnd(BaseModel):
    """Envelope for the "judging:end" event from /v1/research."""

    data: V1ResearchEventJudgingEndData

    event: Literal["judging:end"]


class V1ResearchEventJudgingStartData(BaseModel):
    attempt: float

    max_attempts: float = FieldInfo(alias="maxAttempts")
    """Maximum attempts allowed (1 + maxRevisions)"""

    message: str

    timestamp: float


class V1ResearchEventJudgingStart(BaseModel):
    """Envelope for the "judging:start" event from /v1/research."""

    data: V1ResearchEventJudgingStartData

    event: Literal["judging:start"]


class V1ResearchEventOutliningEndData(BaseModel):
    message: str

    sources_selected: float = FieldInfo(alias="sourcesSelected")

    timestamp: float


class V1ResearchEventOutliningEnd(BaseModel):
    """Envelope for the "outlining:end" event from /v1/research."""

    data: V1ResearchEventOutliningEndData

    event: Literal["outlining:end"]


class V1ResearchEventOutliningStartData(BaseModel):
    message: str

    pages_analyzed: float = FieldInfo(alias="pagesAnalyzed")
    """Total pages analyzed across all iterations"""

    quality_page_count: float = FieldInfo(alias="qualityPageCount")
    """Pages that meet quality threshold (medium+ relevance and reliability)"""

    timestamp: float


class V1ResearchEventOutliningStart(BaseModel):
    """Envelope for the "outlining:start" event from /v1/research."""

    data: V1ResearchEventOutliningStartData

    event: Literal["outlining:start"]


class V1ResearchEventPlanningEndData(BaseModel):
    complexity: Literal["simple", "moderate", "complex"]

    message: str

    objective: str

    plan: str

    queries: List[str]

    questions: List[str]

    timestamp: float


class V1ResearchEventPlanningEnd(BaseModel):
    """Envelope for the "planning:end" event from /v1/research."""

    data: V1ResearchEventPlanningEndData

    event: Literal["planning:end"]


class V1ResearchEventPlanningStartData(BaseModel):
    has_prefetched_context: bool = FieldInfo(alias="hasPrefetchedContext")
    """Whether prefetched user-provided URLs exist for context"""

    message: str

    timestamp: float


class V1ResearchEventPlanningStart(BaseModel):
    """Envelope for the "planning:start" event from /v1/research."""

    data: V1ResearchEventPlanningStartData

    event: Literal["planning:start"]


class V1ResearchEventPrefetchingEndData(BaseModel):
    failed: float

    fetched: float

    message: str

    timestamp: float


class V1ResearchEventPrefetchingEnd(BaseModel):
    """Envelope for the "prefetching:end" event from /v1/research."""

    data: V1ResearchEventPrefetchingEndData

    event: Literal["prefetching:end"]


class V1ResearchEventPrefetchingStartData(BaseModel):
    message: str

    timestamp: float

    url_count: float = FieldInfo(alias="urlCount")

    urls: List[str]


class V1ResearchEventPrefetchingStart(BaseModel):
    """Envelope for the "prefetching:start" event from /v1/research."""

    data: V1ResearchEventPrefetchingStartData

    event: Literal["prefetching:start"]


class V1ResearchEventSearchingEndData(BaseModel):
    iteration: float

    message: str

    timestamp: float

    urls_found: float = FieldInfo(alias="urlsFound")

    urls_new: float = FieldInfo(alias="urlsNew")


class V1ResearchEventSearchingEnd(BaseModel):
    """Envelope for the "searching:end" event from /v1/research."""

    data: V1ResearchEventSearchingEndData

    event: Literal["searching:end"]


class V1ResearchEventSearchingStartData(BaseModel):
    iteration: float

    message: str

    queries: List[str]

    timestamp: float


class V1ResearchEventSearchingStart(BaseModel):
    """Envelope for the "searching:start" event from /v1/research."""

    data: V1ResearchEventSearchingStartData

    event: Literal["searching:start"]


class V1ResearchEventStartData(BaseModel):
    """start - Research begins"""

    message: str

    timestamp: float


class V1ResearchEventStart(BaseModel):
    """Envelope for the "start" event from /v1/research."""

    data: V1ResearchEventStartData
    """start - Research begins"""

    event: Literal["start"]


class V1ResearchEventWritingEndData(BaseModel):
    attempt: float

    message: str

    timestamp: float


class V1ResearchEventWritingEnd(BaseModel):
    """Envelope for the "writing:end" event from /v1/research."""

    data: V1ResearchEventWritingEndData

    event: Literal["writing:end"]


class V1ResearchEventWritingStartData(BaseModel):
    attempt: float

    is_revision: bool = FieldInfo(alias="isRevision")
    """Whether this is a revision attempt (attempt > 1)"""

    max_attempts: float = FieldInfo(alias="maxAttempts")
    """Maximum attempts allowed (1 + maxRevisions)"""

    message: str

    timestamp: float

    previous_score: Optional[float] = FieldInfo(alias="previousScore", default=None)
    """Previous judgment score if this is a revision"""


class V1ResearchEventWritingStart(BaseModel):
    """Envelope for the "writing:start" event from /v1/research."""

    data: V1ResearchEventWritingStartData

    event: Literal["writing:start"]


ResearchEvent: TypeAlias = Annotated[
    Union[
        V1ResearchEventAnalyzingEnd,
        V1ResearchEventAnalyzingStart,
        V1ResearchEventComplete,
        V1ResearchEventError,
        V1ResearchEventEvaluatingEnd,
        V1ResearchEventEvaluatingStart,
        V1ResearchEventFollowingEnd,
        V1ResearchEventFollowingStart,
        V1ResearchEventIterationEnd,
        V1ResearchEventIterationStart,
        V1ResearchEventJudgingEnd,
        V1ResearchEventJudgingStart,
        V1ResearchEventOutliningEnd,
        V1ResearchEventOutliningStart,
        V1ResearchEventPlanningEnd,
        V1ResearchEventPlanningStart,
        V1ResearchEventPrefetchingEnd,
        V1ResearchEventPrefetchingStart,
        V1ResearchEventSearchingEnd,
        V1ResearchEventSearchingStart,
        V1ResearchEventStart,
        V1ResearchEventWritingEnd,
        V1ResearchEventWritingStart,
    ],
    PropertyInfo(discriminator="event"),
]
