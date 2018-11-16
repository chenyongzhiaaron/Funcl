import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class OrderPay(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/pay')
        self.headers = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ('选择正确的订单号，选择支付类型为支付宝，唤起支付成功', 11201811160740393823, 4000, 200, '请求成功'),
        ('选择正确的订单号，选择支付类型为微信，唤起支付成功', 11201811160740393823, 3000, 200, '请求成功'),
    ])
    def test_order_pay_success(self, case, order_number, pay_type, status, message):
        payload = {'order_number': order_number, 'pay_type': pay_type}
        self.result = requests.put(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)


if __name__ == "__main__":
    unittest.main()


'''
已有叮当唤起支付接口
3000位微信支付，3001位微信二维码，4000位支付宝
'''