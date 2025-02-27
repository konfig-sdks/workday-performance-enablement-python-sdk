# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from workday_performance_enablement_python_sdk.paths.feedback_badges_id.get import GetById
from workday_performance_enablement_python_sdk.paths.feedback_badges.get import GetCollection
from workday_performance_enablement_python_sdk.apis.tags.feedback_badges_api_raw import FeedbackBadgesApiRaw


class FeedbackBadgesApi(
    GetById,
    GetCollection,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FeedbackBadgesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FeedbackBadgesApiRaw(api_client)
