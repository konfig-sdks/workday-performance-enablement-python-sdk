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

from workday_performance_enablement_python_sdk.type.instancemodelreference import INSTANCEMODELREFERENCE

class RequiredMULTIPLEINSTANCEMODELREFERENCE(TypedDict):
    pass

class OptionalMULTIPLEINSTANCEMODELREFERENCE(TypedDict, total=False):
    total: int

    data: typing.List[INSTANCEMODELREFERENCE]

class MULTIPLEINSTANCEMODELREFERENCE(RequiredMULTIPLEINSTANCEMODELREFERENCE, OptionalMULTIPLEINSTANCEMODELREFERENCE):
    pass
