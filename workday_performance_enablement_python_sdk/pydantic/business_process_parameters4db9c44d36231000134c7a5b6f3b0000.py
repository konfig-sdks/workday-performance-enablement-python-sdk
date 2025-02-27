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

from workday_performance_enablement_python_sdk.pydantic.business_process_parameters_afd6ac52d6251000117be546cb060000 import BusinessProcessParametersAfd6ac52d6251000117be546cb060000

BusinessProcessParameters4db9c44d36231000134c7a5b6f3b0000 = typing.Union[BusinessProcessParametersAfd6ac52d6251000117be546cb060000,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
