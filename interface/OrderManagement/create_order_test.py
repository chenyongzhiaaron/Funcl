import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_data, test_db


class OrderCreate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/create')
        self.headers = global_base.DefTool.defaultHeaders(self)
        self.product_id = "j6WdKJEXOKmarZpA"
        self.product_count = 1
        self.alipay_pay_type = 4000
        self.wxin_pay_type = 3000
        self.wxgz_pay_type = 3001
        self.address_id = test_db.T_DB().t_db2()
        self.status = 200
        self.message = "请求成功"

    def tearDown(self):
        print(self.result)

    def test_create_order_alipay_success(self):
        '''选择支付类型为支付宝支付新建订单成功'''
        payload = {"product_id": self.product_id, "product_count": self.product_count, "pay_type": self.alipay_pay_type,
                   "address_id": self.address_id}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], self.status)
        self.assertEqual(self.result["message"], self.message)

    def test_create_order_wxin_success(self):
        '''选择支付类型为微信支付新建订单成功'''
        payload = {"product_id": self.product_id, "product_count": self.product_count, "pay_type": self.wxin_pay_type,
                   "address_id": self.address_id}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], self.status)
        self.assertEqual(self.result["message"], self.message)

    def test_create_order_wxin_success(self):
        '''选择支付类型为微信支付（公众号）新建订单成功'''
        payload = {"product_id": self.product_id, "product_count": self.product_count, "pay_type": self.wxgz_pay_type,
                   "address_id": self.address_id}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], self.status)
        self.assertEqual(self.result["message"], self.message)






    # @parameterized.expand([
    #         ("所有参数为空，新建订单失败", "", "", "", "", 422, "验证失败"),
    #         ("product_id 为空，新建订单失败", "", 1, 4000, 76, 422, "验证失败"),
    #         ("product_count 为空，新建订单失败", "j6WdKJEXOKmarZpA", "", 4000, 76, 422, "验证失败"),
    #         ("pay_type 为空，新建订单失败", "j6WdKJEXOKmarZpA", 1, "", 76, 422, "验证失败"),
    #         ("address_id 为空，新建订单失败", "j6WdKJEXOKmarZpA", 1, 4000, "", 422, "验证失败"),
    #     ])
    # def test_order_create_error(self, case, product_id, product_count, pay_type, address_id, status, message):
    #         payload = {"product_id": product_id, "product_count": product_count, "pay_type": pay_type,
    #                    "address_id": address_id}
    #         self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
    #         self.assertEqual(self.result['status'], status)
    #         self.assertEqual(self.result['message'], message)


if __name__ == "__main__":
    unittest.main()

'''
新建订单接口
只会列出所属于当前 17727498114 用户的订单(s)
'''
