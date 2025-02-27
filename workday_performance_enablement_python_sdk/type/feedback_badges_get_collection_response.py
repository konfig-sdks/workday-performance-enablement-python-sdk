# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from workday_performance_enablement_python_sdk.type.feedback_badge_detail9eab868ca81410001402525d054211f7 import FeedbackBadgeDetail9eab868ca81410001402525d054211f7

class RequiredFeedbackBadgesGetCollectionResponse(TypedDict):
    pass

class OptionalFeedbackBadgesGetCollectionResponse(TypedDict, total=False):
    data: typing.List[FeedbackBadgeDetail9eab868ca81410001402525d054211f7]

    total: int

class FeedbackBadgesGetCollectionResponse(RequiredFeedbackBadgesGetCollectionResponse, OptionalFeedbackBadgesGetCollectionResponse):
    pass
