import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class FunCode(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/funCode/getInfo")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("code 正确，请求成功", "FJ2U89H198H928H9", 200, "请求成功", "wONZeKmv0R3Gkb9r"),
        ("code 正确，起始前加空格，请求成功", " FJ2U89H198H928H9", 200, "请求成功", "wONZeKmv0R3Gkb9r"),
        ("code 正确，结束后加空格，请求成功", "FJ2U89H198H928H9 ", 200, "请求成功", "wONZeKmv0R3Gkb9r")
    ])
    def test_funCode_success(self, case, code, status, message, data):
        ''' funCode 正确，获取可用状态成功'''
        payload = {"code": code, "status": status, "message": message, "data": data}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['product_id'], data)

    def test_funCode_disable(self):
        ''' funCode 已使用，获取可用状态失败 '''
        payload = {'code': 'WOINFO193841N009'}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '该码已被使用')

    @parameterized.expand([
        ("funCode，符合长度，数据错误，获取状态失败", "FJ2U89H198H928H8", 400, "Fun码错误，请重新再试!"),
        ("funCode，长度17位，获取状态失败", "FJ2U89H198H928H81", 400, "Fun码错误，请重新再试!"),
        ("funCode，长度15位，获取状态失败", "FJ2U89H198H928H", 400, "Fun码错误，请重新再试!"),
        ("funCode，长度1位，获取状态失败", "F", 400, "Fun码错误，请重新再试!"),
        ("funCode，特殊字符，获取状态失败", "=-=中文@!#(*", 400, "Fun码错误，请重新再试!"),
        # ("funCode==空格", " ", 400, "Fun码错误，请重新再试!"),
    ])
    def test_funCode_error(self, case, code, status, message):
        ''' funCode 错误，获取可用状态失败 '''
        payload = {"code": code, "status": status, "message": message}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result['message'], message)

    def test_funCode_absent(self):
        ''' funCode 不传，获取可用状态失败 '''
        self.result = requests.post(url=self.u, headers=self.h).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], "")

if __name__ == "__main__":
    unittest.main()
