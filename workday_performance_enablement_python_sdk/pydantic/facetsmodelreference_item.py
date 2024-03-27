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

from workday_performance_enablement_python_sdk.pydantic.facetsmodelreference_item_values import FACETSMODELREFERENCEItemValues

class FACETSMODELREFERENCEItem(BaseModel):
    # A description of the facet
    descriptor: typing.Optional[str] = Field(None, alias='descriptor')

    # The alias used to select the facet
    facet_parameter: typing.Optional[str] = Field(None, alias='facetParameter')

    values: typing.Optional[FACETSMODELREFERENCEItemValues] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
