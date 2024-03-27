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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from workday_performance_enablement_python_sdk.pydantic.badge_afd6ac52d62510001357f891ccfd0003 import BadgeAfd6ac52d62510001357f891ccfd0003
from workday_performance_enablement_python_sdk.pydantic.business_process_parameters_afd6ac52d6251000117d0a60ed8b0000 import BusinessProcessParametersAfd6ac52d6251000117d0a60ed8b0000
from workday_performance_enablement_python_sdk.pydantic.from_worker_afd6ac52d62510001357f891ccfd0001 import FromWorkerAfd6ac52d62510001357f891ccfd0001
from workday_performance_enablement_python_sdk.pydantic.get_workers_feedback_also_about3ab333661034100010b5635b2f7a0302 import GetWorkersFeedbackAlsoAbout3ab333661034100010b5635b2f7a0302
from workday_performance_enablement_python_sdk.pydantic.related_feedback_events9708c966f04f10000e1e9b7f9a5c0000 import RelatedFeedbackEvents9708c966f04f10000e1e9b7f9a5c0000
from workday_performance_enablement_python_sdk.pydantic.relates_to9d12ad407f0f10001c3949add7d40000 import RelatesTo9d12ad407f0f10001c3949add7d40000
from workday_performance_enablement_python_sdk.pydantic.to_worker_f4946919a39f10000f03207b1f230000 import ToWorkerF4946919a39f10000f03207b1f230000
from workday_performance_enablement_python_sdk.pydantic.workers_to_notify9e478586f65410001035b6c26a4c0000 import WorkersToNotify9e478586f65410001035b6c26a4c0000

FeedbackEventDetailAfd6ac52d62510001086b5c85cd50000 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
