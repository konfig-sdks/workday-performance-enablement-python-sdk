# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from workday_performance_enablement_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    FEEDBACK_BADGES = "/feedbackBadges"
    WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS_SUBRESOURCE_ID = "/workers/{ID}/requestedFeedbackOnSelfEvents/{subresourceID}"
    GIVE_REQUESTED_FEEDBACK_EVENTS = "/giveRequestedFeedbackEvents"
    FEEDBACK_BADGES_ID = "/feedbackBadges/{ID}"
    WORKERS_ID_GOALS = "/workers/{ID}/goals"
    WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS = "/workers/{ID}/requestedFeedbackOnSelfEvents"
    WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS_SUBRESOURCE_ID = "/workers/{ID}/requestedFeedbackOnWorkerEvents/{subresourceID}"
    WORKERS_ID_GOALS_SUBRESOURCE_ID = "/workers/{ID}/goals/{subresourceID}"
    WORKERS_ID_ANYTIME_FEEDBACK_EVENTS_SUBRESOURCE_ID = "/workers/{ID}/anytimeFeedbackEvents/{subresourceID}"
    WORKERS_ID = "/workers/{ID}"
    WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS = "/workers/{ID}/requestedFeedbackOnWorkerEvents"
    WORKERS = "/workers"
    WORKERS_ID_ANYTIME_FEEDBACK_EVENTS = "/workers/{ID}/anytimeFeedbackEvents"
    GIVE_REQUESTED_FEEDBACK_EVENTS_ID = "/giveRequestedFeedbackEvents/{ID}"
    VALUES_WORKERS_TO_NOTIFY_WORKERS_TO_NOTIFY = "/values/workersToNotify/workersToNotify"
    VALUES_FEEDBACK_TEMPLATE_FEEDBACK_TEMPLATE = "/values/feedbackTemplate/feedbackTemplate"
    VALUES_FEEDBACK_ON_WORKER_FEEDBACK_ON_WORKER = "/values/feedbackOnWorker/feedbackOnWorker"
    VALUES_FEEDBACK_RESPONDER_FEEDBACK_RESPONDER = "/values/feedbackResponder/feedbackResponder"
    VALUES_RELATES_TO_RELATES_TO = "/values/relatesTo/relatesTo"
