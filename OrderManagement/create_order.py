import unittest

import requests

from parameterized import parameterized
from Global_base import global_base


class OrderCreate(unittest.TestCase):

    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/create')
        self.headers = global_base.Utils.token(self)

    def tearDown(self):
        pass

    @parameterized.expand([
            ("必填项输入正确，新建订单成功", "lYaDb7EjKK3LONk5", 1, 4000, 1, 200, "请求成功"),
    ])
    def test_create_order_success(self, casename,product_id, product_count, pay_type, address_id, status, message):
        payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type, "address_id": address_id}
        result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(result["status"], status)
        self.assertEqual(result["message"], message)


if __name__ == "__main__":
    unittest.main()