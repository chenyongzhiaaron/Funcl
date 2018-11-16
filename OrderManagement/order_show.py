import unittest

import requests

from Global_base import global_base


class OrderShow(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/order/show')
        self.headers = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    def test_order_show_success(self):
        ''' order number 存在，查询成功 '''
        payload = [{'order_number': 11201809270847162209}, {'order_number': 11201811160740393823}]
        for i in payload:
            self.result = requests.get(url=self.url, headers=self.headers, params=i).json()
            self.assertEqual(self.result['status'], 200)
            self.assertEqual(self.result['message'], '请求成功')

    # def test_order_show_order_number_absent(self):
    #     ''' 订单号不存在，查询失败 '''


if __name__ == '__main__':
    unittest.main()


''''
获取订单详情接口
根据Order Number获取订单详细信息
'''


# def testlistg(i):
#     self.result = requests.get(url=self.url, headers=self.headers, params=i).json()
#     self.assertEqual(self.result['status'], 200)
#     self.assertEqual(self.result['message'], '请求成功')