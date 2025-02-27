# coding: utf-8

"""
    performanceEnablement

    The Performance Management service enables applications to access and create feedback about workers in the system.

    The version of the OpenAPI document: v5
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from workday_performance_enablement_python_sdk import WorkdayPerformanceEnablement

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        workdayperformanceenablement = WorkdayPerformanceEnablement(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(workdayperformanceenablement)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
