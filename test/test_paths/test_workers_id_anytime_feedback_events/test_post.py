# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import workday_performance_enablement_python_sdk
from workday_performance_enablement_python_sdk.paths.workers_id_anytime_feedback_events import post
from workday_performance_enablement_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWorkersIDAnytimeFeedbackEvents(ApiTestMixin, unittest.TestCase):
    """
    WorkersIDAnytimeFeedbackEvents unit test stubs
        Creates a single feedback given event instance about the specified worker.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
