# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from workday_performance_enablement_python_sdk.paths.give_requested_feedback_events.get import GetCollectionFeedbackEventsRaw
from workday_performance_enablement_python_sdk.paths.give_requested_feedback_events_id.get import GetInstanceRaw
from workday_performance_enablement_python_sdk.paths.give_requested_feedback_events_id.patch import UpdateEventRaw


class GiveRequestedFeedbackEventsApiRaw(
    GetCollectionFeedbackEventsRaw,
    GetInstanceRaw,
    UpdateEventRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
