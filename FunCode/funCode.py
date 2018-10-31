import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class FunCode(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/funCode/getInfo")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        # print(self.result)
        print(self.result_f)

    @parameterized.expand([
            ("code 正确，请求成功", "FJ2U89H198H928H9", 200, "请求成功", "wONZeKmv0R3Gkb9r"),
            ("code 正确，起始前加空格，请求成功", " FJ2U89H198H928H9", 200, "请求成功", "wONZeKmv0R3Gkb9r"),
            ("code 正确，结束后加空格，请求成功", "FJ2U89H198H928H9 ", 200, "请求成功", "wONZeKmv0R3Gkb9r")
    ])
    def test_funCode_success(self, case, code, status, message, data):
        payload = {"code": code, "status": status, "message": message, "data": data}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['product_id'], data)

    @parameterized.expand([
        ("funCode 错误", "FJ2U89H198H928H8", 400, "Fun码错误，请重新再试!"),
        ("funCode==16位+1", "FJ2U89H198H928H81", 400, "Fun码错误，请重新再试!"),
        ("funCode==16位-1", "FJ2U89H198H928H", 400, "Fun码错误，请重新再试!"),
        # ("funCode为空", "", 400, "Fun码错误，请重新再试!"),
        ("funCode==1位", "F", 400, "Fun码错误，请重新再试!"),
        ("funCode==特殊字符", "=-=中文@!#(*", 400, "Fun码错误，请重新再试!"),
        # ("funCode==空格", " ", 400, "Fun码错误，请重新再试!"),
        # ("funCode起始数值前+空格", " FJ2U89H198H928H9", 400, "Fun码错误，请重新再试!"),
        # ("funCode数值后+空格", "FJ2U89H198H928H9 ", 400, "Fun码错误，请重新再试!"),
    ])
    def test_funCode_fail(self, case, code, status, message):
        payload = {"code": code, "status": status, "message": message}
        self.result_f = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result_f["status"], status)
        self.assertEqual(self.result_f['message'], message)


if __name__ == "__main__":
    unittest.main()
