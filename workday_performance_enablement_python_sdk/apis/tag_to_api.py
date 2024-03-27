import typing_extensions

from workday_performance_enablement_python_sdk.apis.tags import TagValues
from workday_performance_enablement_python_sdk.apis.tags.workers_api import WorkersApi
from workday_performance_enablement_python_sdk.apis.tags.prompt_values_api import PromptValuesApi
from workday_performance_enablement_python_sdk.apis.tags.give_requested_feedback_events_api import GiveRequestedFeedbackEventsApi
from workday_performance_enablement_python_sdk.apis.tags.feedback_badges_api import FeedbackBadgesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WORKERS: WorkersApi,
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.GIVE_REQUESTED_FEEDBACK_EVENTS: GiveRequestedFeedbackEventsApi,
        TagValues.FEEDBACK_BADGES: FeedbackBadgesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WORKERS: WorkersApi,
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.GIVE_REQUESTED_FEEDBACK_EVENTS: GiveRequestedFeedbackEventsApi,
        TagValues.FEEDBACK_BADGES: FeedbackBadgesApi,
    }
)
