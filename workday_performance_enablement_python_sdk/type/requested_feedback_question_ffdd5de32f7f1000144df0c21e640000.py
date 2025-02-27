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

from workday_performance_enablement_python_sdk.type.feedback_response2f703c317dc910001bd2de83d1590000 import FeedbackResponse2f703c317dc910001bd2de83d1590000
from workday_performance_enablement_python_sdk.type.question_multiple_choice_ffdd5de32f7f100016c2c1e768f40000 import QuestionMultipleChoiceFfdd5de32f7f100016c2c1e768f40000
from workday_performance_enablement_python_sdk.type.question_type_ffdd5de32f7f1000144df15bb77b0001 import QuestionTypeFfdd5de32f7f1000144df15bb77b0001
from workday_performance_enablement_python_sdk.type.talent_tag_ffdd5de32f7f100016c88e016ad20000 import TalentTagFfdd5de32f7f100016c88e016ad20000

RequestedFeedbackQuestionFfdd5de32f7f1000144df0c21e640000 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
