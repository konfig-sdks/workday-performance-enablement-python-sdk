# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

from workday_performance_enablement_python_sdk.paths.values_workers_to_notify_workers_to_notify.get import GetInstances
from workday_performance_enablement_python_sdk.paths.values_feedback_template_feedback_template.get import GetInstances0
from workday_performance_enablement_python_sdk.paths.values_feedback_on_worker_feedback_on_worker.get import GetInstances1
from workday_performance_enablement_python_sdk.paths.values_feedback_responder_feedback_responder.get import GetInstances2
from workday_performance_enablement_python_sdk.paths.values_relates_to_relates_to.get import GetInstances3
from workday_performance_enablement_python_sdk.apis.tags.prompt_values_api_raw import PromptValuesApiRaw


class PromptValuesApi(
    GetInstances,
    GetInstances0,
    GetInstances1,
    GetInstances2,
    GetInstances3,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PromptValuesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PromptValuesApiRaw(api_client)
