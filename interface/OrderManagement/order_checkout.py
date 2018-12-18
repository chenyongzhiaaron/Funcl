import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class OrderCheckout(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/order/checkout")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("使用微信原生支付生成订单并跳转支付成功", "j6WdKJEXOKmarZpA", 1, 3000, 76, 200, "请求成功",
         'https://open.weixin.qq.com'),
        ("使用微信二维码生成订单并跳转支付成功", "j6WdKJEXOKmarZpA", 1, 3001, 76, 200, "请求成功",
         'http://api.funcl.com/api/order/pay/wxpay/wap/pay'),
        ("使用支付宝成订单并跳转支付成功", "j6WdKJEXOKmarZpA", 1, 4000, 76, 200, "请求成功",
         'https://openapi.alipay.com'),
        ("购买白色 AI 生成订单并跳转支付成功", "dAP8BNMgva3q59wv", 1, 4000, 76, 200, "请求成功",
         'https://openapi.alipay.com'),
        ("购买黑色 AI 生成订单并跳转支付成功", "ZpAG05MV5W3JdwxO", 1, 4000, 76, 200, "请求成功",
         'https://openapi.alipay.com'),
        ("购买黑色AI数量达到前端限制最大数量生成订单并跳转支付成功", "dAP8BNMgva3q59wv", 5, 4000, 76, 200, "请求成功",
         'https://openapi.alipay.com'),
        ("验证来源 funcCode 生成订单并跳转成功", "dAP8BNMgva3q59wv", 1, 4000, 76, "FJ2U89H198H928H9", 200, "请求成功",
         'https://openapi.alipay.com'),
    ])
    def test_order_checkout_success(self, case, product_id, product_count, pay_type, address_id, fun_code, status,
                                    message, data):
        payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
                   "address_id": address_id, "fun_code": fun_code}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertIn(data, self.result['data'])


if __name__ == '__main__':
    unittest.main()
