import typing_extensions

from workday_performance_enablement_python_sdk.paths import PathValues
from workday_performance_enablement_python_sdk.apis.paths.feedback_badges import FeedbackBadges
from workday_performance_enablement_python_sdk.apis.paths.workers_id_requested_feedback_on_self_events_subresource_id import WorkersIDRequestedFeedbackOnSelfEventsSubresourceID
from workday_performance_enablement_python_sdk.apis.paths.give_requested_feedback_events import GiveRequestedFeedbackEvents
from workday_performance_enablement_python_sdk.apis.paths.feedback_badges_id import FeedbackBadgesID
from workday_performance_enablement_python_sdk.apis.paths.workers_id_goals import WorkersIDGoals
from workday_performance_enablement_python_sdk.apis.paths.workers_id_requested_feedback_on_self_events import WorkersIDRequestedFeedbackOnSelfEvents
from workday_performance_enablement_python_sdk.apis.paths.workers_id_requested_feedback_on_worker_events_subresource_id import WorkersIDRequestedFeedbackOnWorkerEventsSubresourceID
from workday_performance_enablement_python_sdk.apis.paths.workers_id_goals_subresource_id import WorkersIDGoalsSubresourceID
from workday_performance_enablement_python_sdk.apis.paths.workers_id_anytime_feedback_events_subresource_id import WorkersIDAnytimeFeedbackEventsSubresourceID
from workday_performance_enablement_python_sdk.apis.paths.workers_id import WorkersID
from workday_performance_enablement_python_sdk.apis.paths.workers_id_requested_feedback_on_worker_events import WorkersIDRequestedFeedbackOnWorkerEvents
from workday_performance_enablement_python_sdk.apis.paths.workers import Workers
from workday_performance_enablement_python_sdk.apis.paths.workers_id_anytime_feedback_events import WorkersIDAnytimeFeedbackEvents
from workday_performance_enablement_python_sdk.apis.paths.give_requested_feedback_events_id import GiveRequestedFeedbackEventsID
from workday_performance_enablement_python_sdk.apis.paths.values_workers_to_notify_workers_to_notify import ValuesWorkersToNotifyWorkersToNotify
from workday_performance_enablement_python_sdk.apis.paths.values_feedback_template_feedback_template import ValuesFeedbackTemplateFeedbackTemplate
from workday_performance_enablement_python_sdk.apis.paths.values_feedback_on_worker_feedback_on_worker import ValuesFeedbackOnWorkerFeedbackOnWorker
from workday_performance_enablement_python_sdk.apis.paths.values_feedback_responder_feedback_responder import ValuesFeedbackResponderFeedbackResponder
from workday_performance_enablement_python_sdk.apis.paths.values_relates_to_relates_to import ValuesRelatesToRelatesTo

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.FEEDBACK_BADGES: FeedbackBadges,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS_SUBRESOURCE_ID: WorkersIDRequestedFeedbackOnSelfEventsSubresourceID,
        PathValues.GIVE_REQUESTED_FEEDBACK_EVENTS: GiveRequestedFeedbackEvents,
        PathValues.FEEDBACK_BADGES_ID: FeedbackBadgesID,
        PathValues.WORKERS_ID_GOALS: WorkersIDGoals,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS: WorkersIDRequestedFeedbackOnSelfEvents,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS_SUBRESOURCE_ID: WorkersIDRequestedFeedbackOnWorkerEventsSubresourceID,
        PathValues.WORKERS_ID_GOALS_SUBRESOURCE_ID: WorkersIDGoalsSubresourceID,
        PathValues.WORKERS_ID_ANYTIME_FEEDBACK_EVENTS_SUBRESOURCE_ID: WorkersIDAnytimeFeedbackEventsSubresourceID,
        PathValues.WORKERS_ID: WorkersID,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS: WorkersIDRequestedFeedbackOnWorkerEvents,
        PathValues.WORKERS: Workers,
        PathValues.WORKERS_ID_ANYTIME_FEEDBACK_EVENTS: WorkersIDAnytimeFeedbackEvents,
        PathValues.GIVE_REQUESTED_FEEDBACK_EVENTS_ID: GiveRequestedFeedbackEventsID,
        PathValues.VALUES_WORKERS_TO_NOTIFY_WORKERS_TO_NOTIFY: ValuesWorkersToNotifyWorkersToNotify,
        PathValues.VALUES_FEEDBACK_TEMPLATE_FEEDBACK_TEMPLATE: ValuesFeedbackTemplateFeedbackTemplate,
        PathValues.VALUES_FEEDBACK_ON_WORKER_FEEDBACK_ON_WORKER: ValuesFeedbackOnWorkerFeedbackOnWorker,
        PathValues.VALUES_FEEDBACK_RESPONDER_FEEDBACK_RESPONDER: ValuesFeedbackResponderFeedbackResponder,
        PathValues.VALUES_RELATES_TO_RELATES_TO: ValuesRelatesToRelatesTo,
    }
)

path_to_api = PathToApi(
    {
        PathValues.FEEDBACK_BADGES: FeedbackBadges,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS_SUBRESOURCE_ID: WorkersIDRequestedFeedbackOnSelfEventsSubresourceID,
        PathValues.GIVE_REQUESTED_FEEDBACK_EVENTS: GiveRequestedFeedbackEvents,
        PathValues.FEEDBACK_BADGES_ID: FeedbackBadgesID,
        PathValues.WORKERS_ID_GOALS: WorkersIDGoals,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_SELF_EVENTS: WorkersIDRequestedFeedbackOnSelfEvents,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS_SUBRESOURCE_ID: WorkersIDRequestedFeedbackOnWorkerEventsSubresourceID,
        PathValues.WORKERS_ID_GOALS_SUBRESOURCE_ID: WorkersIDGoalsSubresourceID,
        PathValues.WORKERS_ID_ANYTIME_FEEDBACK_EVENTS_SUBRESOURCE_ID: WorkersIDAnytimeFeedbackEventsSubresourceID,
        PathValues.WORKERS_ID: WorkersID,
        PathValues.WORKERS_ID_REQUESTED_FEEDBACK_ON_WORKER_EVENTS: WorkersIDRequestedFeedbackOnWorkerEvents,
        PathValues.WORKERS: Workers,
        PathValues.WORKERS_ID_ANYTIME_FEEDBACK_EVENTS: WorkersIDAnytimeFeedbackEvents,
        PathValues.GIVE_REQUESTED_FEEDBACK_EVENTS_ID: GiveRequestedFeedbackEventsID,
        PathValues.VALUES_WORKERS_TO_NOTIFY_WORKERS_TO_NOTIFY: ValuesWorkersToNotifyWorkersToNotify,
        PathValues.VALUES_FEEDBACK_TEMPLATE_FEEDBACK_TEMPLATE: ValuesFeedbackTemplateFeedbackTemplate,
        PathValues.VALUES_FEEDBACK_ON_WORKER_FEEDBACK_ON_WORKER: ValuesFeedbackOnWorkerFeedbackOnWorker,
        PathValues.VALUES_FEEDBACK_RESPONDER_FEEDBACK_RESPONDER: ValuesFeedbackResponderFeedbackResponder,
        PathValues.VALUES_RELATES_TO_RELATES_TO: ValuesRelatesToRelatesTo,
    }
)
