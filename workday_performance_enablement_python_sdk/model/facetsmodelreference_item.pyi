# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from workday_performance_enablement_python_sdk import schemas  # noqa: F401


class FACETSMODELREFERENCEItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    This object represents the possible facets for this resource
    """


    class MetaOapg:
        
        class properties:
            descriptor = schemas.StrSchema
            facetParameter = schemas.StrSchema
        
            @staticmethod
            def values() -> typing.Type['FACETSMODELREFERENCEItemValues']:
                return FACETSMODELREFERENCEItemValues
            __annotations__ = {
                "descriptor": descriptor,
                "facetParameter": facetParameter,
                "values": values,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["facetParameter"]) -> MetaOapg.properties.facetParameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> 'FACETSMODELREFERENCEItemValues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["descriptor", "facetParameter", "values", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["facetParameter"]) -> typing.Union[MetaOapg.properties.facetParameter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union['FACETSMODELREFERENCEItemValues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["descriptor", "facetParameter", "values", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
        facetParameter: typing.Union[MetaOapg.properties.facetParameter, str, schemas.Unset] = schemas.unset,
        values: typing.Union['FACETSMODELREFERENCEItemValues', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FACETSMODELREFERENCEItem':
        return super().__new__(
            cls,
            *args,
            descriptor=descriptor,
            facetParameter=facetParameter,
            values=values,
            _configuration=_configuration,
            **kwargs,
        )

from workday_performance_enablement_python_sdk.model.facetsmodelreference_item_values import FACETSMODELREFERENCEItemValues
