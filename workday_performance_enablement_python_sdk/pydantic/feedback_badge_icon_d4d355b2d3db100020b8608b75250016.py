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

from workday_performance_enablement_python_sdk.pydantic.instancemodelreference import INSTANCEMODELREFERENCE

FeedbackBadgeIconD4d355b2d3db100020b8608b75250016 = typing.Union[INSTANCEMODELREFERENCE,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
