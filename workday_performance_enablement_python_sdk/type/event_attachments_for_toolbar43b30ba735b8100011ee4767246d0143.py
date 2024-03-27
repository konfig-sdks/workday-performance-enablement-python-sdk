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

from workday_performance_enablement_python_sdk.type.category43b30ba735b8100011ee4781a9d50146 import Category43b30ba735b8100011ee4781a9d50146
from workday_performance_enablement_python_sdk.type.content_type43b30ba735b8100011ee47993f11014a import ContentType43b30ba735b8100011ee47993f11014a
from workday_performance_enablement_python_sdk.type.uploaded_by_b32ff437243510000e22e06470370160 import UploadedByB32ff437243510000e22e06470370160

EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
