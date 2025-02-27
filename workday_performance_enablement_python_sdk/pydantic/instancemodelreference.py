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


class INSTANCEMODELREFERENCE(BaseModel):
    # wid / id / reference id
    id: str = Field(alias='id')

    # A description of the instance
    descriptor: typing.Optional[str] = Field(None, alias='descriptor')

    # A link to the instance
    href: typing.Optional[str] = Field(None, alias='href')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
