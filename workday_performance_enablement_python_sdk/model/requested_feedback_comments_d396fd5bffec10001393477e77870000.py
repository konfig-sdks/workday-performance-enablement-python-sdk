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


class RequestedFeedbackCommentsD396fd5bffec10001393477e77870000(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    feedbackDeclined = schemas.BoolSchema
                    feedbackDeclineReason = schemas.StrSchema
                    
                    
                    class possibleMultipleChoiceAnswers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000']:
                                return PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000'], typing.List['PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'possibleMultipleChoiceAnswers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def questionType() -> typing.Type['QuestionType544916c1cd75100006c4f105d3f60000']:
                        return QuestionType544916c1cd75100006c4f105d3f60000
                    
                    
                    class multipleChoiceAnswers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000']:
                                return MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000'], typing.List['MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'multipleChoiceAnswers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000':
                            return super().__getitem__(i)
                    numericAnswer = schemas.IntSchema
                    dateAnswer = schemas.DateSchema
                    response = schemas.StrSchema
                    
                    
                    class relatesTo(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['RelatesToC836a10b43ed10000beb5b92b4c10000']:
                                return RelatesToC836a10b43ed10000beb5b92b4c10000
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['RelatesToC836a10b43ed10000beb5b92b4c10000'], typing.List['RelatesToC836a10b43ed10000beb5b92b4c10000']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'relatesTo':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'RelatesToC836a10b43ed10000beb5b92b4c10000':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def feedbackQuestion() -> typing.Type['FeedbackQuestionD396fd5bffec10001393481822cd0007']:
                        return FeedbackQuestionD396fd5bffec10001393481822cd0007
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "feedbackDeclined": feedbackDeclined,
                        "feedbackDeclineReason": feedbackDeclineReason,
                        "possibleMultipleChoiceAnswers": possibleMultipleChoiceAnswers,
                        "questionType": questionType,
                        "multipleChoiceAnswers": multipleChoiceAnswers,
                        "numericAnswer": numericAnswer,
                        "dateAnswer": dateAnswer,
                        "response": response,
                        "relatesTo": relatesTo,
                        "feedbackQuestion": feedbackQuestion,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["feedbackDeclined"]) -> MetaOapg.properties.feedbackDeclined: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["feedbackDeclineReason"]) -> MetaOapg.properties.feedbackDeclineReason: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["possibleMultipleChoiceAnswers"]) -> MetaOapg.properties.possibleMultipleChoiceAnswers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["questionType"]) -> 'QuestionType544916c1cd75100006c4f105d3f60000': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["multipleChoiceAnswers"]) -> MetaOapg.properties.multipleChoiceAnswers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["numericAnswer"]) -> MetaOapg.properties.numericAnswer: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dateAnswer"]) -> MetaOapg.properties.dateAnswer: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["response"]) -> MetaOapg.properties.response: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["relatesTo"]) -> MetaOapg.properties.relatesTo: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["feedbackQuestion"]) -> 'FeedbackQuestionD396fd5bffec10001393481822cd0007': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["feedbackDeclined", "feedbackDeclineReason", "possibleMultipleChoiceAnswers", "questionType", "multipleChoiceAnswers", "numericAnswer", "dateAnswer", "response", "relatesTo", "feedbackQuestion", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["feedbackDeclined"]) -> typing.Union[MetaOapg.properties.feedbackDeclined, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["feedbackDeclineReason"]) -> typing.Union[MetaOapg.properties.feedbackDeclineReason, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["possibleMultipleChoiceAnswers"]) -> typing.Union[MetaOapg.properties.possibleMultipleChoiceAnswers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["questionType"]) -> typing.Union['QuestionType544916c1cd75100006c4f105d3f60000', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["multipleChoiceAnswers"]) -> typing.Union[MetaOapg.properties.multipleChoiceAnswers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["numericAnswer"]) -> typing.Union[MetaOapg.properties.numericAnswer, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dateAnswer"]) -> typing.Union[MetaOapg.properties.dateAnswer, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> typing.Union[MetaOapg.properties.response, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["relatesTo"]) -> typing.Union[MetaOapg.properties.relatesTo, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["feedbackQuestion"]) -> typing.Union['FeedbackQuestionD396fd5bffec10001393481822cd0007', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["feedbackDeclined", "feedbackDeclineReason", "possibleMultipleChoiceAnswers", "questionType", "multipleChoiceAnswers", "numericAnswer", "dateAnswer", "response", "relatesTo", "feedbackQuestion", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                feedbackDeclined: typing.Union[MetaOapg.properties.feedbackDeclined, bool, schemas.Unset] = schemas.unset,
                feedbackDeclineReason: typing.Union[MetaOapg.properties.feedbackDeclineReason, str, schemas.Unset] = schemas.unset,
                possibleMultipleChoiceAnswers: typing.Union[MetaOapg.properties.possibleMultipleChoiceAnswers, list, tuple, schemas.Unset] = schemas.unset,
                questionType: typing.Union['QuestionType544916c1cd75100006c4f105d3f60000', schemas.Unset] = schemas.unset,
                multipleChoiceAnswers: typing.Union[MetaOapg.properties.multipleChoiceAnswers, list, tuple, schemas.Unset] = schemas.unset,
                numericAnswer: typing.Union[MetaOapg.properties.numericAnswer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                dateAnswer: typing.Union[MetaOapg.properties.dateAnswer, str, date, schemas.Unset] = schemas.unset,
                response: typing.Union[MetaOapg.properties.response, str, schemas.Unset] = schemas.unset,
                relatesTo: typing.Union[MetaOapg.properties.relatesTo, list, tuple, schemas.Unset] = schemas.unset,
                feedbackQuestion: typing.Union['FeedbackQuestionD396fd5bffec10001393481822cd0007', schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    feedbackDeclined=feedbackDeclined,
                    feedbackDeclineReason=feedbackDeclineReason,
                    possibleMultipleChoiceAnswers=possibleMultipleChoiceAnswers,
                    questionType=questionType,
                    multipleChoiceAnswers=multipleChoiceAnswers,
                    numericAnswer=numericAnswer,
                    dateAnswer=dateAnswer,
                    response=response,
                    relatesTo=relatesTo,
                    feedbackQuestion=feedbackQuestion,
                    id=id,
                    descriptor=descriptor,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestedFeedbackCommentsD396fd5bffec10001393477e77870000':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_performance_enablement_python_sdk.model.feedback_question_d396fd5bffec10001393481822cd0007 import FeedbackQuestionD396fd5bffec10001393481822cd0007
from workday_performance_enablement_python_sdk.model.multiple_choice_answers06c0300303a9100019828d5ca44a0000 import MultipleChoiceAnswers06c0300303a9100019828d5ca44a0000
from workday_performance_enablement_python_sdk.model.possible_multiple_choice_answers4c60c128c16510000a59980041610000 import PossibleMultipleChoiceAnswers4c60c128c16510000a59980041610000
from workday_performance_enablement_python_sdk.model.question_type544916c1cd75100006c4f105d3f60000 import QuestionType544916c1cd75100006c4f105d3f60000
from workday_performance_enablement_python_sdk.model.relates_to_c836a10b43ed10000beb5b92b4c10000 import RelatesToC836a10b43ed10000beb5b92b4c10000
