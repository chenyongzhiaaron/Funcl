import unittest

import requests
from parameterized import parameterized
from db_fixture import test_data
from Global_base import global_base


class FunCode(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/funCode/getInfo")
        self.h = global_base.DefTool.defaultHeaders(self)
        self.product_id = "j6WdKJEXOKmarZpA"
        self.status_fault = 400
        self.code1 = "MQZE1G57P3X72D9W"     # code 已激活，未到期，未使用
        self.code2 = "WOINFO193841N009"     # code 已激活，未到期，已使用
        self.code3 = "FWON9239J238J922"     # code 已激活，已到期，未使用
        self.code4 = "92389NJ2H19DE183"     # code 已激活，已到期，已使用
        self.code5 = "D12H872Y1010UJR0"     # code 未激活，未到期，未使用
        self.code6 = "1EJ91HJR891H8191"     # code 未激活，未到期，已使用

    def tearDown(self):
        print(self.result)

    def test_funCode_success(self):
        ''' funCode 已激活，未到期，未使用，获取可用状态成功'''
        payload = {"code": self.code1}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], "请求成功")
        self.assertEqual(self.result['data']['product_id'], self.product_id)

    def test_funCode_used(self):
        ''' funCode code 已激活，未到期，已使用，获取可用状态失败 '''
        payload = {"code": self.code2}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], self.status_fault)
        self.assertEqual(self.result['message'], '该码已被使用')

    def test_funCode_expired(self):
        ''' funCode code 已激活，已到期，未使用，获取可用状态失败 '''
        payload = {"code": self.code3}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], self.status_fault)
        self.assertEqual(self.result['message'], '该码已过期')

    def test_funCode_has_been_expired(self):
        ''' funCode code 已激活，已到期，已使用，获取可用状态失败 '''
        payload = {"code": self.code4}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], self.status_fault)
        self.assertEqual(self.result['message'], '该码已过期')

    def test_funCode_not_yet_due(self):
        ''' funCode code 未激活，未到期，未使用，获取可用状态失败 '''
        payload = {"code": self.code5}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], self.status_fault)
        self.assertEqual(self.result['message'], '该码未到使用时间')

    def test_funCode_not_yet_due(self):
        ''' funCode code 未激活，未到期，已使用，获取可用状态失败 '''
        payload = {"code": self.code6}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], self.status_fault)
        self.assertEqual(self.result['message'], '该码未到使用时间')



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


if __name__ == "__main__":

    unittest.main()
