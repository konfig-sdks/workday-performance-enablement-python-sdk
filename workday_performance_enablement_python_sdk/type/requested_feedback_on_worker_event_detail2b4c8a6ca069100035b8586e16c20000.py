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

from workday_performance_enablement_python_sdk.type.business_process_parameters2b4c8a6ca069100035b85907ae2c0000 import BusinessProcessParameters2b4c8a6ca069100035b85907ae2c0000
from workday_performance_enablement_python_sdk.type.feedback_about2b4c8a6ca069100035b85907ae2c0002 import FeedbackAbout2b4c8a6ca069100035b85907ae2c0002
from workday_performance_enablement_python_sdk.type.feedback_responders_ffdd5de32f7f100016dbb1b188d70000 import FeedbackRespondersFfdd5de32f7f100016dbb1b188d70000
from workday_performance_enablement_python_sdk.type.feedback_template2b4c8a6ca069100035b859a141200001 import FeedbackTemplate2b4c8a6ca069100035b859a141200001
from workday_performance_enablement_python_sdk.type.requested_feedback_question_ffdd5de32f7f1000144df0c21e640000 import RequestedFeedbackQuestionFfdd5de32f7f1000144df0c21e640000

RequestedFeedbackOnWorkerEventDetail2b4c8a6ca069100035b8586e16c20000 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
