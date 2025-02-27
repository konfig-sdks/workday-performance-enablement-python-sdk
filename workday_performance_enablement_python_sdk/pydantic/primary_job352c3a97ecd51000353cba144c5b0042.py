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

from workday_performance_enablement_python_sdk.pydantic.job_data_for_worker_b8ac205877fd10000ea91719a02a00a2 import JobDataForWorkerB8ac205877fd10000ea91719a02a00a2

PrimaryJob352c3a97ecd51000353cba144c5b0042 = typing.Union[JobDataForWorkerB8ac205877fd10000ea91719a02a00a2,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
