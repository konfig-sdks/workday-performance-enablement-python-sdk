# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from workday_performance_enablement_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    WORKERS = "workers"
    PROMPT_VALUES = "Prompt Values"
    GIVE_REQUESTED_FEEDBACK_EVENTS = "giveRequestedFeedbackEvents"
    FEEDBACK_BADGES = "feedbackBadges"
