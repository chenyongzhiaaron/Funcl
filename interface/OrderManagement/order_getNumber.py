import unittest

import requests

from Global_base import global_base


class GetNumber(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/order/getNumber")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    def test_get_number(self):
        self.result = requests.get(url=self.u, headers=self.h).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "请求成功")
        self.assertEqual(self.result["data"]["pending"], 0)
        self.assertEqual(self.result["data"]["un_finish"], 3)

if __name__ == "__main__":
    unittest.main()


'''
获取叮当详情接口
根据Order Number获取订单详细信息
'''