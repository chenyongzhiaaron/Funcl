import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class OrderCreate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/create')
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("选择支付类型为支付宝支付新建订单成功", "j6WdKJEXOKmarZpA", 1, 4000, 76, 200, "请求成功"),
        ("选择支付类型为微信支付新建订单成功", "j6WdKJEXOKmarZpA", 1, 3000, 76, 200, "请求成功"),
        ("选择支付类型为微信支付（公众号）新建订单成功", "j6WdKJEXOKmarZpA", 1, 3001, 76, 200, "请求成功"),
    ])
    def test_create_order_success(self, case, product_id, product_count, pay_type, address_id, status, message):
        payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
                   "address_id": address_id}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
            ("所有参数为空，新建订单失败", "", "", "", "", 422, "验证失败"),
            ("product_id 为空，新建订单失败", "", 1, 4000, 76, 422, "验证失败"),
            ("product_count 为空，新建订单失败", "j6WdKJEXOKmarZpA", "", 4000, 76, 422, "验证失败"),
            ("pay_type 为空，新建订单失败", "j6WdKJEXOKmarZpA", 1, "", 76, 422, "验证失败"),
            ("address_id 为空，新建订单失败", "j6WdKJEXOKmarZpA", 1, 4000, "", 422, "验证失败"),
        ])
    def test_order_create_error(self, case, product_id, product_count, pay_type, address_id, status, message):
            payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
                       "address_id": address_id}
            self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
            self.assertEqual(self.result['status'], status)
            self.assertEqual(self.result['message'], message)


if __name__ == "__main__":
    unittest.main()

'''
新建订单接口
只会列出所属于当前 17727498114 用户的订单(s)
'''
