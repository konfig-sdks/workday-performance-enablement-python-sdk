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

from workday_performance_enablement_python_sdk.pydantic.supervisory_organization_job_view_fab4a151b24810000d29746fb7e21259 import SupervisoryOrganizationJobViewFab4a151b24810000d29746fb7e21259

SupervisoryOrganizationB8ac205877fd10000ea91743659800a7 = typing.Union[SupervisoryOrganizationJobViewFab4a151b24810000d29746fb7e21259,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
