import unittest
import requests

from Global_base import global_base
from parameterized import parameterized

class GetList(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, 'api/order/getList')
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        # print(self.result)
        print(self.res)

#     @parameterized.expand([
#         # ("status 不填，获取全部状态成功", "", 200, "请求成功"),
#         ("status 为0，获取未支付状态成功", 0, 200, "请求成功"),
#         ("status 为1000，获取待收货订单成功", 1000, 200, "请求成功"),
#         ("status 为3000，获取已完成状态成功", 3000, 200, "请求成功"),
#         ("status 为4000，获取已取消状态成功", 4000, 200, "请求成功"),
#         ("status 为5000，获取已关闭状态成功", 5000, 200, "请求成功"),
#     ])
# # status 选填，不填为获取全部状态，支付状态:0: 未支付 |1000:待收货|3000:已完成|4000:已取消|5000:已关闭
#     def test_get_list_success(self, casename, status, s, message):
#         payload = {"status": status}
#         self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
#         self.assertEqual(self.result["status"], s)
#         self.assertEqual(self.result["message"], message)

    # @parameterized.expand([
    #     ("status 为中文，请求失败", "中文输入", 200, "请求成功"),
    #     ("status 为字母，请求失败", "abc", 200, "请求成功"),
    #     ("status 为特殊字符，请求失败", "_#&*", 200, "请求成功"),
    #     ("status 为小数，请求失败", 3000.01, 200, "请求成功"),
    #     ("status 为空，请求失败", "", 200, "请求成功"),
    # ])
    # def test_get_list_fail(self, casename, status, s, message):
    #     payload = {"status": status}
    #     self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
    #     self.assertEqual(self.result["status"], s)
    #     self.assertEqual(self.result["message"], message)

#   status 参数不传，请求成功
    def test_getList_fail(self):
        self.res = requests.get(url=self.u, headers=self.h).json()
        self.assertEqual(self.res['status'], 200)



if __name__ == "__main__":
    unittest.main()
