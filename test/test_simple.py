# coding: utf-8

"""
    Data API

    Serves the Clever Data API

    The version of the OpenAPI document: 3.1.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from clever_python_sdk import Clever

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        clever = Clever(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(clever)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
