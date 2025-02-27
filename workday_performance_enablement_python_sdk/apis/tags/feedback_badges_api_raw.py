# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from workday_performance_enablement_python_sdk.paths.feedback_badges_id.get import GetByIdRaw
from workday_performance_enablement_python_sdk.paths.feedback_badges.get import GetCollectionRaw


class FeedbackBadgesApiRaw(
    GetByIdRaw,
    GetCollectionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
