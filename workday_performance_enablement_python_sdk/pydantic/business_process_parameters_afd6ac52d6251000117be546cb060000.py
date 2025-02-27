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

from workday_performance_enablement_python_sdk.pydantic.action38ff08ab6736100010816009079d0126 import Action38ff08ab6736100010816009079d0126
from workday_performance_enablement_python_sdk.pydantic.comments86093b8a932f10001499f356ff83012e import Comments86093b8a932f10001499f356ff83012e
from workday_performance_enablement_python_sdk.pydantic.event_attachments_for_toolbar43b30ba735b8100011ee4767246d0143 import EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143
from workday_performance_enablement_python_sdk.pydantic.for5d688bd57bb910001815ab3dd10024a9 import For5d688bd57bb910001815ab3dd10024a9
from workday_performance_enablement_python_sdk.pydantic.overall_business_process5d688bd57bb910001815ab49927724aa import OverallBusinessProcess5d688bd57bb910001815ab49927724aa
from workday_performance_enablement_python_sdk.pydantic.transaction_status7457adcbe0fa1000089b63ab3a510000 import TransactionStatus7457adcbe0fa1000089b63ab3a510000

BusinessProcessParametersAfd6ac52d6251000117be546cb060000 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
