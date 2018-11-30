import unittest
import requests
from Global_base import global_base


class UpdateDefaultAddress(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/user/default_address')
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    def test_update_default_address(self):
        payload = {"default_address_id": ""}

