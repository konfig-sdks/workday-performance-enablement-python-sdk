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

from workday_performance_enablement_python_sdk.pydantic.job_profile_b8ac205877fd10000ea9174f73c500aa import JobProfileB8ac205877fd10000ea9174f73c500aa
from workday_performance_enablement_python_sdk.pydantic.job_type_b8ac205877fd10000ea91752f39c00ab import JobTypeB8ac205877fd10000ea91752f39c00ab
from workday_performance_enablement_python_sdk.pydantic.location_b8ac205877fd10000ea91737c7da00a5 import LocationB8ac205877fd10000ea91737c7da00a5
from workday_performance_enablement_python_sdk.pydantic.supervisory_organization_b8ac205877fd10000ea91743659800a7 import SupervisoryOrganizationB8ac205877fd10000ea91743659800a7
from workday_performance_enablement_python_sdk.pydantic.work_space426ac445037110001b3eb91ddf6f0100 import WorkSpace426ac445037110001b3eb91ddf6f0100

JobDataForWorkerB8ac205877fd10000ea91719a02a00a2 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
