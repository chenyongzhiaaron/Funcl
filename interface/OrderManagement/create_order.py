import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class OrderCreate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/create')
        self.headers = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("必填项输入正确，新建订单成功", "p0qgjlEQ0omz2eA8", 1, 4000, 68, 200, "请求成功"),
    ])
    def test_create_order_success(self, casename, product_id, product_count, pay_type, address_id, status, message):
        payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
                   "address_id": address_id}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

        @parameterized.expand([
            ("所有参数为空，新建订单失败", "", "", "", "", 400,),
            ("product_id 为空，新建订单失败", "p0qgjlEQ0omz2eA8", 1, 4000, 68, 400, "请求成功"),
            ("product_count 为空，新建订单失败", "p0qgjlEQ0omz2eA8", "", 4000, 68, 400, "请求成功"),
            ("pay_type 为空，新建订单失败", "p0qgjlEQ0omz2eA8", 1, "", 68, 400, "请求成功"),
            ("address_id 为空，新建订单失败", "p0qgjlEQ0omz2eA8", 1, 4000, "", 400, "请求成功"),
            ("product_id 不存在，新建订单失败", "p0qgjlEQ0omz2eA898876", 1, 4000, 68, 400, "请求成功"),
            ("product_count 不存在，新建订单失败", "p0qgjlEQ0omz2eA8", "abc1234*&123", 4000, 68, 400, "请求成功"),
            ("pay_type 不存在，新建订单失败", "p0qgjlEQ0omz2eA8", 1, 1234, 68, 400, "请求成功"),
            ("address_id 不存在，新建订单失败", "p0qgjlEQ0omz2eA8", 1, 4000, 9999, 400, "请求成功"),
            ("product_count 大于库存限制，新建订单失败", "p0qgjlEQ0omz2eA8", 101, 4000, 68, 400, "请求成功"),
        ])
        def test_order_create_error(self, casename, product_id, product_count, pay_type, address_id, status, message):
            payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
                       "address_id": address_id}
            self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
            self.assertEqual(self.result['status'], status)
            self.assertEqual(self.result['message'], message)


if __name__ == "__main__":
    unittest.main()

'''
新建订单接口
只会列出所属于当前用户的订单(s)
'''