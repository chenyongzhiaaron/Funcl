import unittest

import requests

from parameterized import parameterized
from Global_base import global_base


class OrderCreate(unittest.TestCase):

    def setUp(self):
        self.url = global_base.Base.url
        self.headers = global_base.Base.headers

    def tearDown(self):
        pass

    def test_create_order_success(self):
        payload = {"product_id": "", "product_count": "", "pay_type": "", "address_id": ""}
        result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "请求成功")


if __name__ == "__main__":
    unittest.main()