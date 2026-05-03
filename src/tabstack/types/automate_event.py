# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AutomateEvent",
    "V1AutomateEventAgentAction",
    "V1AutomateEventAgentActionData",
    "V1AutomateEventAgentExtracted",
    "V1AutomateEventAgentExtractedData",
    "V1AutomateEventAgentProcessing",
    "V1AutomateEventAgentProcessingData",
    "V1AutomateEventAgentReasoned",
    "V1AutomateEventAgentReasonedData",
    "V1AutomateEventAgentStatus",
    "V1AutomateEventAgentStatusData",
    "V1AutomateEventAgentStep",
    "V1AutomateEventAgentStepData",
    "V1AutomateEventAgentWaiting",
    "V1AutomateEventAgentWaitingData",
    "V1AutomateEventAIGeneration",
    "V1AutomateEventAIGenerationData",
    "V1AutomateEventAIGenerationDataUsage",
    "V1AutomateEventAIGenerationDataMessage",
    "V1AutomateEventAIGenerationDataMessageSystem",
    "V1AutomateEventAIGenerationDataMessageUser",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Text",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Image",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImage",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1Buffer",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageByteLength",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBuffer",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBufferBuffer",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1File",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileData",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1Buffer",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataByteLength",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBuffer",
    "V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBufferBuffer",
    "V1AutomateEventAIGenerationDataMessageAssistant",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Text",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1File",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileData",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1Buffer",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataByteLength",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBuffer",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBufferBuffer",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Reasoning",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolCall",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResult",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutput",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputText",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputJson",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputExecutionDenied",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorText",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorJson",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContent",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValue",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueText",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueMedia",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileData",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileURL",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileID",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageData",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageURL",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageFileID",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueCustom",
    "V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolApprovalRequest",
    "V1AutomateEventAIGenerationDataMessageTool",
    "V1AutomateEventAIGenerationDataMessageToolContent",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResult",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutput",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputText",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputJson",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputExecutionDenied",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorText",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorJson",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContent",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValue",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueText",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueMedia",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileData",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileURL",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileID",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageData",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageURL",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageFileID",
    "V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueCustom",
    "V1AutomateEventAIGenerationDataMessageToolContentToolApprovalResponse",
    "V1AutomateEventAIGenerationError",
    "V1AutomateEventAIGenerationErrorData",
    "V1AutomateEventBrowserActionCompleted",
    "V1AutomateEventBrowserActionCompletedData",
    "V1AutomateEventBrowserActionStarted",
    "V1AutomateEventBrowserActionStartedData",
    "V1AutomateEventBrowserNavigated",
    "V1AutomateEventBrowserNavigatedData",
    "V1AutomateEventBrowserReconnected",
    "V1AutomateEventBrowserReconnectedData",
    "V1AutomateEventBrowserScreenshotCaptured",
    "V1AutomateEventBrowserScreenshotCapturedData",
    "V1AutomateEventBrowserScreenshotCapturedImage",
    "V1AutomateEventBrowserScreenshotCapturedImageData",
    "V1AutomateEventCdpEndpointConnected",
    "V1AutomateEventCdpEndpointConnectedData",
    "V1AutomateEventCdpEndpointCycle",
    "V1AutomateEventCdpEndpointCycleData",
    "V1AutomateEventComplete",
    "V1AutomateEventCompleteData",
    "V1AutomateEventCompleteDataStats",
    "V1AutomateEventCompleteDataError",
    "V1AutomateEventDone",
    "V1AutomateEventError",
    "V1AutomateEventErrorData",
    "V1AutomateEventErrorDataError",
    "V1AutomateEventInteractiveFormDataError",
    "V1AutomateEventInteractiveFormDataErrorData",
    "V1AutomateEventInteractiveFormDataErrorDataField",
    "V1AutomateEventInteractiveFormDataRequest",
    "V1AutomateEventInteractiveFormDataRequestData",
    "V1AutomateEventInteractiveFormDataRequestDataField",
    "V1AutomateEventSystemDebugCompression",
    "V1AutomateEventSystemDebugCompressionData",
    "V1AutomateEventSystemDebugMessage",
    "V1AutomateEventSystemDebugMessageData",
    "V1AutomateEventTaskAborted",
    "V1AutomateEventTaskAbortedData",
    "V1AutomateEventTaskCompleted",
    "V1AutomateEventTaskCompletedData",
    "V1AutomateEventTaskMetrics",
    "V1AutomateEventTaskMetricsData",
    "V1AutomateEventTaskMetricsIncremental",
    "V1AutomateEventTaskMetricsIncrementalData",
    "V1AutomateEventTaskSetup",
    "V1AutomateEventTaskSetupData",
    "V1AutomateEventTaskStarted",
    "V1AutomateEventTaskStartedData",
    "V1AutomateEventTaskTraceContext",
    "V1AutomateEventTaskTraceContextData",
    "V1AutomateEventTaskValidated",
    "V1AutomateEventTaskValidatedData",
    "V1AutomateEventTaskValidationError",
    "V1AutomateEventTaskValidationErrorData",
]


class V1AutomateEventAgentActionData(BaseModel):
    """Event data for action execution"""

    action: str

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    ref: Optional[str] = None

    value: Optional[str] = None


class V1AutomateEventAgentAction(BaseModel):
    """Envelope for the "agent:action" event from /v1/automate."""

    data: V1AutomateEventAgentActionData
    """Event data for action execution"""

    event: Literal["agent:action"]


class V1AutomateEventAgentExtractedData(BaseModel):
    """Event data for extracted data"""

    extracted_data: str = FieldInfo(alias="extractedData")

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float


class V1AutomateEventAgentExtracted(BaseModel):
    """Envelope for the "agent:extracted" event from /v1/automate."""

    data: V1AutomateEventAgentExtractedData
    """Event data for extracted data"""

    event: Literal["agent:extracted"]


class V1AutomateEventAgentProcessingData(BaseModel):
    """Event data for when the agent is waiting for model generation"""

    has_screenshot: bool = FieldInfo(alias="hasScreenshot")

    iteration_id: str = FieldInfo(alias="iterationId")

    operation: str

    timestamp: float


class V1AutomateEventAgentProcessing(BaseModel):
    """Envelope for the "agent:processing" event from /v1/automate."""

    data: V1AutomateEventAgentProcessingData
    """Event data for when the agent is waiting for model generation"""

    event: Literal["agent:processing"]


class V1AutomateEventAgentReasonedData(BaseModel):
    """Event data for agent reasoning"""

    iteration_id: str = FieldInfo(alias="iterationId")

    reasoning: str

    timestamp: float


class V1AutomateEventAgentReasoned(BaseModel):
    """Envelope for the "agent:reasoned" event from /v1/automate."""

    data: V1AutomateEventAgentReasonedData
    """Event data for agent reasoning"""

    event: Literal["agent:reasoned"]


class V1AutomateEventAgentStatusData(BaseModel):
    """Event data for status messages"""

    iteration_id: str = FieldInfo(alias="iterationId")

    message: str

    timestamp: float


class V1AutomateEventAgentStatus(BaseModel):
    """Envelope for the "agent:status" event from /v1/automate."""

    data: V1AutomateEventAgentStatusData
    """Event data for status messages"""

    event: Literal["agent:status"]


class V1AutomateEventAgentStepData(BaseModel):
    """Event data for agent step tracking (each loop iteration)"""

    current_iteration: float = FieldInfo(alias="currentIteration")

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float


class V1AutomateEventAgentStep(BaseModel):
    """Envelope for the "agent:step" event from /v1/automate."""

    data: V1AutomateEventAgentStepData
    """Event data for agent step tracking (each loop iteration)"""

    event: Literal["agent:step"]


class V1AutomateEventAgentWaitingData(BaseModel):
    """Event data for waiting notifications"""

    iteration_id: str = FieldInfo(alias="iterationId")

    seconds: float

    timestamp: float


class V1AutomateEventAgentWaiting(BaseModel):
    """Envelope for the "agent:waiting" event from /v1/automate."""

    data: V1AutomateEventAgentWaitingData
    """Event data for waiting notifications"""

    event: Literal["agent:waiting"]


class V1AutomateEventAIGenerationDataUsage(BaseModel):
    input_tokens: Optional[float] = FieldInfo(alias="inputTokens", default=None)

    output_tokens: Optional[float] = FieldInfo(alias="outputTokens", default=None)

    total_tokens: Optional[float] = FieldInfo(alias="totalTokens", default=None)


class V1AutomateEventAIGenerationDataMessageSystem(BaseModel):
    """A system message. It can contain system information.

    Note: using the "system" part of the prompt is strongly preferred to increase the resilience against prompt injection attacks, and because not all providers support several system messages.
    """

    content: str

    role: Literal["system"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Text(BaseModel):
    """Text content part of a prompt. It contains a string of text."""

    text: str
    """The text content."""

    type: Literal["text"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1Buffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1Buffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageByteLength(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBufferBuffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBuffer(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBufferBuffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImage: TypeAlias = Union[
    str,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageUnionMember1,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageByteLength,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImageV1GlobalBuffer,
]


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Image(BaseModel):
    """Image content part of a prompt. It contains an image."""

    image: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1ImageImage
    """Image data. Can either be:

    - data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
    - URL: a URL that points to the image
    """

    type: Literal["image"]

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)
    """Optional IANA media type of the image."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1Buffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1Buffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataByteLength(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBufferBuffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBuffer(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBufferBuffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileData: TypeAlias = Union[
    str,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataUnionMember1,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataByteLength,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileDataV1GlobalBuffer,
]


class V1AutomateEventAIGenerationDataMessageUserContentUnionMember1File(BaseModel):
    """File content part of a prompt. It contains a file."""

    data: V1AutomateEventAIGenerationDataMessageUserContentUnionMember1FileData
    """File data. Can either be:

    - data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
    - URL: a URL that points to the image
    """

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type of the file."""

    type: Literal["file"]

    filename: Optional[str] = None
    """Optional filename of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


V1AutomateEventAIGenerationDataMessageUserContentUnionMember1: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Text,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1Image,
    V1AutomateEventAIGenerationDataMessageUserContentUnionMember1File,
]


class V1AutomateEventAIGenerationDataMessageUser(BaseModel):
    """A user message. It can contain text or a combination of text and images."""

    content: Union[str, List[V1AutomateEventAIGenerationDataMessageUserContentUnionMember1]]
    """Content of a user message.

    It can be a string or an array of text and image parts.
    """

    role: Literal["user"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Text(BaseModel):
    """Text content part of a prompt. It contains a string of text."""

    text: str
    """The text content."""

    type: Literal["text"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1Buffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1Buffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataByteLength(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBufferBuffer(BaseModel):
    byte_length: float = FieldInfo(alias="byteLength")


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBuffer(BaseModel):
    buffer: V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBufferBuffer

    byte_length: float = FieldInfo(alias="byteLength")

    byte_offset: float = FieldInfo(alias="byteOffset")

    bytes_per_element: float = FieldInfo(alias="BYTES_PER_ELEMENT")

    length: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, float] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> float: ...
    else:
        __pydantic_extra__: Dict[str, float]


V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileData: TypeAlias = Union[
    str,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataUnionMember1,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataByteLength,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileDataV1GlobalBuffer,
]


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1File(BaseModel):
    """File content part of a prompt. It contains a file."""

    data: V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1FileData
    """File data. Can either be:

    - data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
    - URL: a URL that points to the image
    """

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type of the file."""

    type: Literal["file"]

    filename: Optional[str] = None
    """Optional filename of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Reasoning(BaseModel):
    """Reasoning content part of a prompt. It contains a reasoning."""

    text: str
    """The reasoning text."""

    type: Literal["reasoning"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolCall(BaseModel):
    """Tool call content part of a prompt.

    It contains a tool call (usually generated by the AI model).
    """

    input: object
    """Arguments of the tool call.

    This is a JSON-serializable object that matches the tool's input schema.
    """

    tool_call_id: str = FieldInfo(alias="toolCallId")
    """ID of the tool call.

    This ID is used to match the tool call with the tool result.
    """

    tool_name: str = FieldInfo(alias="toolName")
    """Name of the tool that is being called."""

    type: Literal["tool-call"]

    provider_executed: Optional[bool] = FieldInfo(alias="providerExecuted", default=None)
    """Whether the tool call was executed by the provider."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputText(BaseModel):
    type: Literal["text"]
    """Text tool output that should be directly sent to the API."""

    value: str

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputJson(BaseModel):
    type: Literal["json"]

    value: Union[
        str,
        float,
        bool,
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, List[object], object]],
                List[Union[str, float, bool, List[object], object, None]],
            ],
        ],
        List[Union[str, float, bool, List[object], object, None]],
        None,
    ] = None
    """A JSON value can be a string, number, boolean, object, array, or null.

    JSON values can be serialized and deserialized by the JSON.stringify and
    JSON.parse methods.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputExecutionDenied(BaseModel):
    type: Literal["execution-denied"]
    """Type when the user has denied the execution of the tool call."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""

    reason: Optional[str] = None
    """Optional reason for the execution denial."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorText(BaseModel):
    type: Literal["error-text"]

    value: str

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorJson(BaseModel):
    type: Literal["error-json"]

    value: Union[
        str,
        float,
        bool,
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, List[object], object]],
                List[Union[str, float, bool, List[object], object, None]],
            ],
        ],
        List[Union[str, float, bool, List[object], object, None]],
        None,
    ] = None
    """A JSON value can be a string, number, boolean, object, array, or null.

    JSON values can be serialized and deserialized by the JSON.stringify and
    JSON.parse methods.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueText(BaseModel):
    text: str
    """Text content."""

    type: Literal["text"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueMedia(BaseModel):
    data: str

    media_type: str = FieldInfo(alias="mediaType")

    type: Literal["media"]
    """Deprecated. Use image-data or file-data instead."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileData(BaseModel):
    data: str
    """Base-64 encoded media data."""

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type."""

    type: Literal["file-data"]

    filename: Optional[str] = None
    """Optional filename of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileURL(BaseModel):
    type: Literal["file-url"]

    url: str
    """URL of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileID(BaseModel):
    file_id: Union[str, Dict[str, str]] = FieldInfo(alias="fileId")
    """ID of the file.

    If you use multiple providers, you need to specify the provider specific ids
    using the Record option. The key is the provider name, e.g. 'openai' or
    'anthropic'.
    """

    type: Literal["file-id"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageData(
    BaseModel
):
    data: str
    """Base-64 encoded image data."""

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type."""

    type: Literal["image-data"]
    """Images that are referenced using base64 encoded data."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageURL(BaseModel):
    type: Literal["image-url"]
    """Images that are referenced using a URL."""

    url: str
    """URL of the image."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageFileID(
    BaseModel
):
    file_id: Union[str, Dict[str, str]] = FieldInfo(alias="fileId")
    """Image that is referenced using a provider file id.

    If you use multiple providers, you need to specify the provider specific ids
    using the Record option. The key is the provider name, e.g. 'openai' or
    'anthropic'.
    """

    type: Literal["image-file-id"]
    """Images that are referenced using a provider file id."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueCustom(BaseModel):
    type: Literal["custom"]
    """Custom content part.

    This can be used to implement provider-specific content parts.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValue: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueText,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueMedia,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileData,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileURL,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueFileID,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageData,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageURL,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueImageFileID,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValueCustom,
]


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContent(BaseModel):
    type: Literal["content"]

    value: List[V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContentValue]


V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutput: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputText,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputJson,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputExecutionDenied,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorText,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputErrorJson,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutputContent,
]


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResult(BaseModel):
    """Tool result content part of a prompt.

    It contains the result of the tool call with the matching ID.
    """

    output: V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResultOutput
    """Result of the tool call. This is a JSON-serializable object."""

    tool_call_id: str = FieldInfo(alias="toolCallId")
    """ID of the tool call that this result is associated with."""

    tool_name: str = FieldInfo(alias="toolName")
    """Name of the tool that generated this result."""

    type: Literal["tool-result"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolApprovalRequest(BaseModel):
    """Tool approval request prompt part."""

    approval_id: str = FieldInfo(alias="approvalId")
    """ID of the tool approval."""

    tool_call_id: str = FieldInfo(alias="toolCallId")
    """ID of the tool call that the approval request is for."""

    type: Literal["tool-approval-request"]


V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Text,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1File,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1Reasoning,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolCall,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolResult,
    V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1ToolApprovalRequest,
]


class V1AutomateEventAIGenerationDataMessageAssistant(BaseModel):
    """An assistant message.

    It can contain text, tool calls, or a combination of text and tool calls.
    """

    content: Union[str, List[V1AutomateEventAIGenerationDataMessageAssistantContentUnionMember1]]
    """Content of an assistant message.

    It can be a string or an array of text, image, reasoning, redacted reasoning,
    and tool call parts.
    """

    role: Literal["assistant"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputText(BaseModel):
    type: Literal["text"]
    """Text tool output that should be directly sent to the API."""

    value: str

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputJson(BaseModel):
    type: Literal["json"]

    value: Union[
        str,
        float,
        bool,
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, List[object], object]],
                List[Union[str, float, bool, List[object], object, None]],
            ],
        ],
        List[Union[str, float, bool, List[object], object, None]],
        None,
    ] = None
    """A JSON value can be a string, number, boolean, object, array, or null.

    JSON values can be serialized and deserialized by the JSON.stringify and
    JSON.parse methods.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputExecutionDenied(BaseModel):
    type: Literal["execution-denied"]
    """Type when the user has denied the execution of the tool call."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""

    reason: Optional[str] = None
    """Optional reason for the execution denial."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorText(BaseModel):
    type: Literal["error-text"]

    value: str

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorJson(BaseModel):
    type: Literal["error-json"]

    value: Union[
        str,
        float,
        bool,
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, List[object], object]],
                List[Union[str, float, bool, List[object], object, None]],
            ],
        ],
        List[Union[str, float, bool, List[object], object, None]],
        None,
    ] = None
    """A JSON value can be a string, number, boolean, object, array, or null.

    JSON values can be serialized and deserialized by the JSON.stringify and
    JSON.parse methods.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueText(BaseModel):
    text: str
    """Text content."""

    type: Literal["text"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueMedia(BaseModel):
    data: str

    media_type: str = FieldInfo(alias="mediaType")

    type: Literal["media"]
    """Deprecated. Use image-data or file-data instead."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileData(BaseModel):
    data: str
    """Base-64 encoded media data."""

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type."""

    type: Literal["file-data"]

    filename: Optional[str] = None
    """Optional filename of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileURL(BaseModel):
    type: Literal["file-url"]

    url: str
    """URL of the file."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileID(BaseModel):
    file_id: Union[str, Dict[str, str]] = FieldInfo(alias="fileId")
    """ID of the file.

    If you use multiple providers, you need to specify the provider specific ids
    using the Record option. The key is the provider name, e.g. 'openai' or
    'anthropic'.
    """

    type: Literal["file-id"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageData(BaseModel):
    data: str
    """Base-64 encoded image data."""

    media_type: str = FieldInfo(alias="mediaType")
    """IANA media type."""

    type: Literal["image-data"]
    """Images that are referenced using base64 encoded data."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageURL(BaseModel):
    type: Literal["image-url"]
    """Images that are referenced using a URL."""

    url: str
    """URL of the image."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageFileID(BaseModel):
    file_id: Union[str, Dict[str, str]] = FieldInfo(alias="fileId")
    """Image that is referenced using a provider file id.

    If you use multiple providers, you need to specify the provider specific ids
    using the Record option. The key is the provider name, e.g. 'openai' or
    'anthropic'.
    """

    type: Literal["image-file-id"]
    """Images that are referenced using a provider file id."""

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueCustom(BaseModel):
    type: Literal["custom"]
    """Custom content part.

    This can be used to implement provider-specific content parts.
    """

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Provider-specific options."""


V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValue: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueText,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueMedia,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileData,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileURL,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueFileID,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageData,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageURL,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueImageFileID,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValueCustom,
]


class V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContent(BaseModel):
    type: Literal["content"]

    value: List[V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContentValue]


V1AutomateEventAIGenerationDataMessageToolContentToolResultOutput: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputText,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputJson,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputExecutionDenied,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorText,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputErrorJson,
    V1AutomateEventAIGenerationDataMessageToolContentToolResultOutputContent,
]


class V1AutomateEventAIGenerationDataMessageToolContentToolResult(BaseModel):
    """Tool result content part of a prompt.

    It contains the result of the tool call with the matching ID.
    """

    output: V1AutomateEventAIGenerationDataMessageToolContentToolResultOutput
    """Result of the tool call. This is a JSON-serializable object."""

    tool_call_id: str = FieldInfo(alias="toolCallId")
    """ID of the tool call that this result is associated with."""

    tool_name: str = FieldInfo(alias="toolName")
    """Name of the tool that generated this result."""

    type: Literal["tool-result"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


class V1AutomateEventAIGenerationDataMessageToolContentToolApprovalResponse(BaseModel):
    """Tool approval response prompt part."""

    approval_id: str = FieldInfo(alias="approvalId")
    """ID of the tool approval."""

    approved: bool
    """Flag indicating whether the approval was granted or denied."""

    type: Literal["tool-approval-response"]

    provider_executed: Optional[bool] = FieldInfo(alias="providerExecuted", default=None)
    """Flag indicating whether the tool call is provider-executed.

    Only provider-executed tool approval responses should be sent to the model.
    """

    reason: Optional[str] = None
    """Optional reason for the approval or denial."""


V1AutomateEventAIGenerationDataMessageToolContent: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageToolContentToolResult,
    V1AutomateEventAIGenerationDataMessageToolContentToolApprovalResponse,
]


class V1AutomateEventAIGenerationDataMessageTool(BaseModel):
    """A tool message. It contains the result of one or more tool calls."""

    content: List[V1AutomateEventAIGenerationDataMessageToolContent]
    """Content of a tool message. It is an array of tool result parts."""

    role: Literal["tool"]

    provider_options: Optional[
        Dict[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    Dict[str, Union[str, float, bool, List[object], object]],
                    List[Union[str, float, bool, List[object], object, None]],
                ],
            ],
        ]
    ] = FieldInfo(alias="providerOptions", default=None)
    """Additional provider-specific metadata.

    They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider.
    """


V1AutomateEventAIGenerationDataMessage: TypeAlias = Union[
    V1AutomateEventAIGenerationDataMessageSystem,
    V1AutomateEventAIGenerationDataMessageUser,
    V1AutomateEventAIGenerationDataMessageAssistant,
    V1AutomateEventAIGenerationDataMessageTool,
]


class V1AutomateEventAIGenerationData(BaseModel):
    """Event data when AI generation occurs"""

    finish_reason: Literal["stop", "length", "content-filter", "tool-calls", "error", "other"] = FieldInfo(
        alias="finishReason"
    )

    iteration_id: str = FieldInfo(alias="iterationId")

    prompt: str

    schema_: object = FieldInfo(alias="schema")

    timestamp: float

    usage: V1AutomateEventAIGenerationDataUsage

    messages: Optional[List[V1AutomateEventAIGenerationDataMessage]] = None

    object: Optional[builtins.object] = None

    provider_metadata: Optional[Dict[str, builtins.object]] = FieldInfo(alias="providerMetadata", default=None)

    temperature: Optional[float] = None

    warnings: Optional[List[builtins.object]] = None


class V1AutomateEventAIGeneration(BaseModel):
    """Envelope for the "ai:generation" event from /v1/automate."""

    data: V1AutomateEventAIGenerationData
    """Event data when AI generation occurs"""

    event: Literal["ai:generation"]


class V1AutomateEventAIGenerationErrorData(BaseModel):
    """Event data when AI generation error occurs"""

    error: str

    iteration_id: str = FieldInfo(alias="iterationId")

    prompt: str

    schema_: object = FieldInfo(alias="schema")

    timestamp: float

    messages: Optional[List[object]] = None


class V1AutomateEventAIGenerationError(BaseModel):
    """Envelope for the "ai:generation:error" event from /v1/automate."""

    data: V1AutomateEventAIGenerationErrorData
    """Event data when AI generation error occurs"""

    event: Literal["ai:generation:error"]


class V1AutomateEventBrowserActionCompletedData(BaseModel):
    """Event data for action results"""

    iteration_id: str = FieldInfo(alias="iterationId")

    success: bool

    timestamp: float

    error: Optional[str] = None


class V1AutomateEventBrowserActionCompleted(BaseModel):
    """Envelope for the "browser:action_completed" event from /v1/automate."""

    data: V1AutomateEventBrowserActionCompletedData
    """Event data for action results"""

    event: Literal["browser:action_completed"]


class V1AutomateEventBrowserActionStartedData(BaseModel):
    """Event data for action execution"""

    action: str

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    ref: Optional[str] = None

    value: Optional[str] = None


class V1AutomateEventBrowserActionStarted(BaseModel):
    """Envelope for the "browser:action_started" event from /v1/automate."""

    data: V1AutomateEventBrowserActionStartedData
    """Event data for action execution"""

    event: Literal["browser:action_started"]


class V1AutomateEventBrowserNavigatedData(BaseModel):
    """Event data when navigating to a page"""

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    title: str

    url: str


class V1AutomateEventBrowserNavigated(BaseModel):
    """Envelope for the "browser:navigated" event from /v1/automate."""

    data: V1AutomateEventBrowserNavigatedData
    """Event data when navigating to a page"""

    event: Literal["browser:navigated"]


class V1AutomateEventBrowserReconnectedData(BaseModel):
    """Event data when the browser reconnects after a mid-task disconnect"""

    endpoint_index: float = FieldInfo(alias="endpointIndex")
    """1-based index of the CDP endpoint now in use"""

    iteration_id: str = FieldInfo(alias="iterationId")

    starting_url: str = FieldInfo(alias="startingUrl")
    """The original starting URL the agent is restarting execution from"""

    timestamp: float

    total: float
    """Total number of configured CDP endpoints"""


class V1AutomateEventBrowserReconnected(BaseModel):
    """Envelope for the "browser:reconnected" event from /v1/automate."""

    data: V1AutomateEventBrowserReconnectedData
    """Event data when the browser reconnects after a mid-task disconnect"""

    event: Literal["browser:reconnected"]


class V1AutomateEventBrowserScreenshotCapturedData(BaseModel):
    """Event data for screenshot capture"""

    format: Literal["jpeg", "png"]

    iteration_id: str = FieldInfo(alias="iterationId")

    size: float

    timestamp: float


class V1AutomateEventBrowserScreenshotCaptured(BaseModel):
    """Envelope for the "browser:screenshot_captured" event from /v1/automate."""

    data: V1AutomateEventBrowserScreenshotCapturedData
    """Event data for screenshot capture"""

    event: Literal["browser:screenshot_captured"]


class V1AutomateEventBrowserScreenshotCapturedImageData(BaseModel):
    """
    Event data for screenshot image capture with full image data This event contains the complete screenshot and can be very large
    """

    image: str

    iteration_id: str = FieldInfo(alias="iterationId")

    media_type: Literal["image/jpeg", "image/png"] = FieldInfo(alias="mediaType")

    timestamp: float


class V1AutomateEventBrowserScreenshotCapturedImage(BaseModel):
    """Envelope for the "browser:screenshot_captured_image" event from /v1/automate."""

    data: V1AutomateEventBrowserScreenshotCapturedImageData
    """
    Event data for screenshot image capture with full image data This event contains
    the complete screenshot and can be very large
    """

    event: Literal["browser:screenshot_captured_image"]


class V1AutomateEventCdpEndpointConnectedData(BaseModel):
    """Event data when a CDP endpoint is successfully connected to"""

    endpoint_index: float = FieldInfo(alias="endpointIndex")
    """1-based index of the endpoint that connected"""

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    total: float
    """Total number of configured CDP endpoints"""


class V1AutomateEventCdpEndpointConnected(BaseModel):
    """Envelope for the "cdp:endpoint_connected" event from /v1/automate."""

    data: V1AutomateEventCdpEndpointConnectedData
    """Event data when a CDP endpoint is successfully connected to"""

    event: Literal["cdp:endpoint_connected"]


class V1AutomateEventCdpEndpointCycleData(BaseModel):
    """Event data when a CDP endpoint fails and the next one is being tried"""

    attempt: float
    """1-based index of the endpoint attempt that failed"""

    error: str
    """
    Sanitized error identifier from the failed connection attempt (error.name, not
    error.message — full messages may contain endpoint URLs)
    """

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    total: float
    """Total number of configured CDP endpoints"""


class V1AutomateEventCdpEndpointCycle(BaseModel):
    """Envelope for the "cdp:endpoint_cycle" event from /v1/automate."""

    data: V1AutomateEventCdpEndpointCycleData
    """Event data when a CDP endpoint fails and the next one is being tried"""

    event: Literal["cdp:endpoint_cycle"]


class V1AutomateEventCompleteDataStats(BaseModel):
    """Execution statistics"""

    actions: float

    duration_ms: float = FieldInfo(alias="durationMs")

    end_time: float = FieldInfo(alias="endTime")

    iterations: float

    start_time: float = FieldInfo(alias="startTime")


class V1AutomateEventCompleteDataError(BaseModel):
    """Structured error information for failed tasks"""

    code: Literal["TASK_ABORTED", "MAX_ITERATIONS", "MAX_ERRORS", "TASK_FAILED"]
    """Error codes for task failures"""

    message: str
    """Human-readable error message"""


class V1AutomateEventCompleteData(BaseModel):
    """Payload for the `complete` stream event.

    Structurally identical to TaskExecutionResult from webAgent.ts — the `complete` event's data is the agent's final TaskExecutionResult, stringified onto the SSE stream.
    """

    final_answer: Optional[str] = FieldInfo(alias="finalAnswer", default=None)
    """Final answer or result from the agent"""

    stats: V1AutomateEventCompleteDataStats
    """Execution statistics"""

    success: bool
    """Whether the task completed successfully"""

    error: Optional[V1AutomateEventCompleteDataError] = None
    """Structured error information for failed tasks"""


class V1AutomateEventComplete(BaseModel):
    """Envelope for the "complete" event from /v1/automate."""

    data: V1AutomateEventCompleteData
    """Payload for the `complete` stream event.

    Structurally identical to TaskExecutionResult from webAgent.ts — the `complete`
    event's data is the agent's final TaskExecutionResult, stringified onto the SSE
    stream.
    """

    event: Literal["complete"]


class V1AutomateEventDone(BaseModel):
    """Envelope for the "done" event from /v1/automate."""

    data: Dict[str, object]
    """Payload for the `done` stream terminator event.

    Empty today; reserved for future metadata.
    """

    event: Literal["done"]


class V1AutomateEventErrorDataError(BaseModel):
    code: str

    message: str

    timestamp: str
    """ISO-8601 timestamp"""


class V1AutomateEventErrorData(BaseModel):
    """Payload for the top-level `error` stream event.

    Emitted when an uncaught error escapes the task runner. Mirrors `ErrorResponse` from the server package's `taskRunner.ts` — kept structurally aligned so schema and runtime stay consistent. Distinct from agent-level error events like `ai:generation:error` and `task:validation_error`, which are emitted through the normal event emitter during the agent loop.
    """

    error: V1AutomateEventErrorDataError

    success: Literal[False]


class V1AutomateEventError(BaseModel):
    """Envelope for the "error" event from /v1/automate."""

    data: V1AutomateEventErrorData
    """Payload for the top-level `error` stream event.

    Emitted when an uncaught error escapes the task runner. Mirrors `ErrorResponse`
    from the server package's `taskRunner.ts` — kept structurally aligned so schema
    and runtime stay consistent. Distinct from agent-level error events like
    `ai:generation:error` and `task:validation_error`, which are emitted through the
    normal event emitter during the agent loop.
    """

    event: Literal["error"]


class V1AutomateEventInteractiveFormDataErrorDataField(BaseModel):
    """A single form field the agent needs data for."""

    field_type: Literal[
        "text", "email", "phone", "date", "number", "select", "checkbox", "radio", "textarea", "password", "other"
    ] = FieldInfo(alias="fieldType")
    """Semantic field type"""

    label: str
    """The field's visible label"""

    ref: str
    """Element ref from the accessibility tree (e.g., "E42")"""

    required: bool
    """Whether this field must be filled"""

    current_value: Optional[str] = FieldInfo(alias="currentValue", default=None)
    """Current value if already partially filled"""

    description: Optional[str] = None
    """Additional context (e.g., validation error message on re-request)"""

    options: Optional[List[str]] = None
    """Available options for select/radio fields"""


class V1AutomateEventInteractiveFormDataErrorData(BaseModel):
    """Event data when form validation fails and the agent re-requests data.

    Carries both the error context and the fields that need new values. Callers respond to this the same way as a request event.
    """

    field_errors: Dict[str, str] = FieldInfo(alias="fieldErrors")
    """Per-field error messages from validation (field ref -> error text)"""

    fields: List[V1AutomateEventInteractiveFormDataErrorDataField]

    form_description: str = FieldInfo(alias="formDescription")

    iteration_id: str = FieldInfo(alias="iterationId")

    page_title: str = FieldInfo(alias="pageTitle")

    page_url: str = FieldInfo(alias="pageUrl")

    request_id: str = FieldInfo(alias="requestId")

    timestamp: float


class V1AutomateEventInteractiveFormDataError(BaseModel):
    """Envelope for the "interactive:form_data:error" event from /v1/automate."""

    data: V1AutomateEventInteractiveFormDataErrorData
    """Event data when form validation fails and the agent re-requests data.

    Carries both the error context and the fields that need new values. Callers
    respond to this the same way as a request event.
    """

    event: Literal["interactive:form_data:error"]


class V1AutomateEventInteractiveFormDataRequestDataField(BaseModel):
    """A single form field the agent needs data for."""

    field_type: Literal[
        "text", "email", "phone", "date", "number", "select", "checkbox", "radio", "textarea", "password", "other"
    ] = FieldInfo(alias="fieldType")
    """Semantic field type"""

    label: str
    """The field's visible label"""

    ref: str
    """Element ref from the accessibility tree (e.g., "E42")"""

    required: bool
    """Whether this field must be filled"""

    current_value: Optional[str] = FieldInfo(alias="currentValue", default=None)
    """Current value if already partially filled"""

    description: Optional[str] = None
    """Additional context (e.g., validation error message on re-request)"""

    options: Optional[List[str]] = None
    """Available options for select/radio fields"""


class V1AutomateEventInteractiveFormDataRequestData(BaseModel):
    """Event data when the agent requests user data for form fields"""

    fields: List[V1AutomateEventInteractiveFormDataRequestDataField]

    form_description: str = FieldInfo(alias="formDescription")

    iteration_id: str = FieldInfo(alias="iterationId")

    page_title: str = FieldInfo(alias="pageTitle")

    page_url: str = FieldInfo(alias="pageUrl")

    request_id: str = FieldInfo(alias="requestId")

    timestamp: float


class V1AutomateEventInteractiveFormDataRequest(BaseModel):
    """Envelope for the "interactive:form_data:request" event from /v1/automate."""

    data: V1AutomateEventInteractiveFormDataRequestData
    """Event data when the agent requests user data for form fields"""

    event: Literal["interactive:form_data:request"]


class V1AutomateEventSystemDebugCompressionData(BaseModel):
    """Event data for compression debug info"""

    compressed_size: float = FieldInfo(alias="compressedSize")

    compression_percent: float = FieldInfo(alias="compressionPercent")

    iteration_id: str = FieldInfo(alias="iterationId")

    original_size: float = FieldInfo(alias="originalSize")

    timestamp: float


class V1AutomateEventSystemDebugCompression(BaseModel):
    """Envelope for the "system:debug_compression" event from /v1/automate."""

    data: V1AutomateEventSystemDebugCompressionData
    """Event data for compression debug info"""

    event: Literal["system:debug_compression"]


class V1AutomateEventSystemDebugMessageData(BaseModel):
    """Event data for message debug info"""

    iteration_id: str = FieldInfo(alias="iterationId")

    messages: List[object]

    timestamp: float


class V1AutomateEventSystemDebugMessage(BaseModel):
    """Envelope for the "system:debug_message" event from /v1/automate."""

    data: V1AutomateEventSystemDebugMessageData
    """Event data for message debug info"""

    event: Literal["system:debug_message"]


class V1AutomateEventTaskAbortedData(BaseModel):
    """Event data when a task is aborted"""

    final_answer: str = FieldInfo(alias="finalAnswer")

    iteration_id: str = FieldInfo(alias="iterationId")

    reason: str

    timestamp: float


class V1AutomateEventTaskAborted(BaseModel):
    """Envelope for the "task:aborted" event from /v1/automate."""

    data: V1AutomateEventTaskAbortedData
    """Event data when a task is aborted"""

    event: Literal["task:aborted"]


class V1AutomateEventTaskCompletedData(BaseModel):
    """Event data when a task is completed"""

    final_answer: Optional[str] = FieldInfo(alias="finalAnswer", default=None)

    iteration_id: str = FieldInfo(alias="iterationId")

    timestamp: float

    success: Optional[bool] = None


class V1AutomateEventTaskCompleted(BaseModel):
    """Envelope for the "task:completed" event from /v1/automate."""

    data: V1AutomateEventTaskCompletedData
    """Event data when a task is completed"""

    event: Literal["task:completed"]


class V1AutomateEventTaskMetricsData(BaseModel):
    ai_generation_count: float = FieldInfo(alias="aiGenerationCount")

    ai_generation_error_count: float = FieldInfo(alias="aiGenerationErrorCount")

    event_counts: Dict[str, float] = FieldInfo(alias="eventCounts")

    iteration_id: str = FieldInfo(alias="iterationId")

    step_count: float = FieldInfo(alias="stepCount")

    timestamp: float

    total_input_tokens: float = FieldInfo(alias="totalInputTokens")

    total_output_tokens: float = FieldInfo(alias="totalOutputTokens")


class V1AutomateEventTaskMetrics(BaseModel):
    """Envelope for the "task:metrics" event from /v1/automate."""

    data: V1AutomateEventTaskMetricsData

    event: Literal["task:metrics"]


class V1AutomateEventTaskMetricsIncrementalData(BaseModel):
    ai_generation_count: float = FieldInfo(alias="aiGenerationCount")

    ai_generation_error_count: float = FieldInfo(alias="aiGenerationErrorCount")

    event_counts: Dict[str, float] = FieldInfo(alias="eventCounts")

    iteration_id: str = FieldInfo(alias="iterationId")

    step_count: float = FieldInfo(alias="stepCount")

    timestamp: float

    total_input_tokens: float = FieldInfo(alias="totalInputTokens")

    total_output_tokens: float = FieldInfo(alias="totalOutputTokens")


class V1AutomateEventTaskMetricsIncremental(BaseModel):
    """Envelope for the "task:metrics_incremental" event from /v1/automate."""

    data: V1AutomateEventTaskMetricsIncrementalData

    event: Literal["task:metrics_incremental"]


class V1AutomateEventTaskSetupData(BaseModel):
    """Event data when a task is setup"""

    browser_name: str = FieldInfo(alias="browserName")

    iteration_id: str = FieldInfo(alias="iterationId")

    task: str

    timestamp: float

    data: Optional[object] = None

    guardrails: Optional[str] = None

    has_api_key: Optional[bool] = FieldInfo(alias="hasApiKey", default=None)

    key_source: Optional[Literal["global", "env", "not_set"]] = FieldInfo(alias="keySource", default=None)

    model: Optional[str] = None

    provider: Optional[str] = None

    proxy: Optional[str] = None

    pw_cdp_endpoint: Optional[str] = FieldInfo(alias="pwCdpEndpoint", default=None)

    pw_cdp_endpoint_count: Optional[float] = FieldInfo(alias="pwCdpEndpointCount", default=None)
    """Total number of CDP endpoints configured (index, not URLs)"""

    pw_cdp_endpoints: Optional[List[str]] = FieldInfo(alias="pwCdpEndpoints", default=None)

    pw_endpoint: Optional[str] = FieldInfo(alias="pwEndpoint", default=None)

    url: Optional[str] = None

    vision: Optional[bool] = None


class V1AutomateEventTaskSetup(BaseModel):
    """Envelope for the "task:setup" event from /v1/automate."""

    data: V1AutomateEventTaskSetupData
    """Event data when a task is setup"""

    event: Literal["task:setup"]


class V1AutomateEventTaskStartedData(BaseModel):
    """Event data when a task is started"""

    iteration_id: str = FieldInfo(alias="iterationId")

    plan: str

    success_criteria: str = FieldInfo(alias="successCriteria")

    task: str

    timestamp: float

    url: str

    action_items: Optional[List[str]] = FieldInfo(alias="actionItems", default=None)


class V1AutomateEventTaskStarted(BaseModel):
    """Envelope for the "task:started" event from /v1/automate."""

    data: V1AutomateEventTaskStartedData
    """Event data when a task is started"""

    event: Literal["task:started"]


class V1AutomateEventTaskTraceContextData(BaseModel):
    """Payload for the task:trace_context event.

    Carries the OpenTelemetry trace ID for this /v1/automate request so consumers can deep-link to distributed-tracing UIs (e.g. Cloud Trace, Cloud Logging) for the run.
    """

    trace_id: str = FieldInfo(alias="traceId")
    """W3C trace ID — 32-character lowercase hexadecimal string."""


class V1AutomateEventTaskTraceContext(BaseModel):
    """Envelope for the "task:trace_context" event from /v1/automate."""

    data: V1AutomateEventTaskTraceContextData
    """Payload for the task:trace_context event.

    Carries the OpenTelemetry trace ID for this /v1/automate request so consumers
    can deep-link to distributed-tracing UIs (e.g. Cloud Trace, Cloud Logging) for
    the run.
    """

    event: Literal["task:trace_context"]


class V1AutomateEventTaskValidatedData(BaseModel):
    """Event data for task validation"""

    completion_quality: Literal["failed", "partial", "complete", "excellent"] = FieldInfo(alias="completionQuality")

    final_answer: str = FieldInfo(alias="finalAnswer")

    iteration_id: str = FieldInfo(alias="iterationId")

    observation: str

    timestamp: float

    feedback: Optional[str] = None


class V1AutomateEventTaskValidated(BaseModel):
    """Envelope for the "task:validated" event from /v1/automate."""

    data: V1AutomateEventTaskValidatedData
    """Event data for task validation"""

    event: Literal["task:validated"]


class V1AutomateEventTaskValidationErrorData(BaseModel):
    """Event data for validation errors during action response processing"""

    errors: List[str]

    iteration_id: str = FieldInfo(alias="iterationId")

    raw_response: object = FieldInfo(alias="rawResponse")

    retry_count: float = FieldInfo(alias="retryCount")

    timestamp: float


class V1AutomateEventTaskValidationError(BaseModel):
    """Envelope for the "task:validation_error" event from /v1/automate."""

    data: V1AutomateEventTaskValidationErrorData
    """Event data for validation errors during action response processing"""

    event: Literal["task:validation_error"]


AutomateEvent: TypeAlias = Annotated[
    Union[
        V1AutomateEventAgentAction,
        V1AutomateEventAgentExtracted,
        V1AutomateEventAgentProcessing,
        V1AutomateEventAgentReasoned,
        V1AutomateEventAgentStatus,
        V1AutomateEventAgentStep,
        V1AutomateEventAgentWaiting,
        V1AutomateEventAIGeneration,
        V1AutomateEventAIGenerationError,
        V1AutomateEventBrowserActionCompleted,
        V1AutomateEventBrowserActionStarted,
        V1AutomateEventBrowserNavigated,
        V1AutomateEventBrowserReconnected,
        V1AutomateEventBrowserScreenshotCaptured,
        V1AutomateEventBrowserScreenshotCapturedImage,
        V1AutomateEventCdpEndpointConnected,
        V1AutomateEventCdpEndpointCycle,
        V1AutomateEventComplete,
        V1AutomateEventDone,
        V1AutomateEventError,
        V1AutomateEventInteractiveFormDataError,
        V1AutomateEventInteractiveFormDataRequest,
        V1AutomateEventSystemDebugCompression,
        V1AutomateEventSystemDebugMessage,
        V1AutomateEventTaskAborted,
        V1AutomateEventTaskCompleted,
        V1AutomateEventTaskMetrics,
        V1AutomateEventTaskMetricsIncremental,
        V1AutomateEventTaskSetup,
        V1AutomateEventTaskStarted,
        V1AutomateEventTaskTraceContext,
        V1AutomateEventTaskValidated,
        V1AutomateEventTaskValidationError,
    ],
    PropertyInfo(discriminator="event"),
]
