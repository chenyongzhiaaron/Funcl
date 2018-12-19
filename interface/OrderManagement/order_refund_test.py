import unittest
import requests
from Global_base import global_base
from db_fixture import test_data
from parameterized import parameterized


class OrderRefund(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/order/refund")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)


    @parameterized.expand([
        ("验证已支付未发货订单，退款原因1000拍多/多拍/不想要，申请退款成功", 11201812180711215262, 1000, 200, "请求成功"),
        ("验证已支付未发货订单，退款原因1001协商一致退款，申请退款成功", 11201812180711215262, 1000, 200, "请求成功"),
        ("验证已支付未发货订单，退款原因1002缺货，申请退款成功", 11201812180711215262, 1000, 200, "请求成功"),
        ("验证已支付未发货订单，退款原因1003未按约定时间发货，申请退款成功", 11201812180711215262, 1000, 200, "请求成功"),
        ("验证已支付未发货订单，退款原因1004其他，申请退款成功", 11201812180711215262, 1000, 200, "请求成功"),
    ])
    def test_order_refund_success(self, case, order_number, refund_reason, status, message):
        payload = {"order_number": order_number, "refund_reason": refund_reason}
        self.result = requests.put(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)


if __name__ == '__main__':
    # test_data.init_data()   # c初始化接口测试数据
    unittest.main()

























'''
未发货订单申请退款接口
order_number    11201809250324131606
 必填|int|length:20

refund_reason   1000
必填|int|1000:拍多/多拍/不想要,1001:协商一致退款,1002:缺货,1003:未按约定时间发货,1004:其他
'''