import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class Get_captcha(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/auth/captcha")
        self.hearders = global_base.DefTool.defHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand(
        [
            ("输入正确手机号获取验证码成功", 200, "请求成功")
        ]
    )
    def test_auth_captcha_success(self, case, status, message):
        '''数据正确，获取成功'''
        payload = {'mobile': 17727498114}
        self.result = requests.get(self.url, headers=self.hearders, params=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result['message'], message)

    @parameterized.expand([
        ('输入手机号少一位，获取验证码失败', 1380013800, 422, "验证失败", "手机号码 格式不对."),
        ('输入手机号多一位，获取验证码失败', 138001380000, 422, "验证失败", "手机号码 格式不对."),
        ('输入手机号为空，获取验证码失败', "", 422, "验证失败", "请填写 手机号码 ."),
        ('输入手机号为特殊字符，获取验证码失败', "189*(*9{:>as", 422, "验证失败", "手机号码 格式不对."),
    ])
    def test_auth_captcha_error(self, case, mobile, status, message, errors):
        ''' 数据错误获取验证码失败'''
        payload = {"mobile": mobile}
        self.result = requests.get(url=self.url, headers=self.hearders, params=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['errors']['mobile'][0], errors)

    def test_auth_acptcha_absent(self):
        ''' 输入的手机号码不符合大陆号码规则，获取验证码失败 '''
        payload = {'mobile': 12300138000}
        self.result = requests.get(url=self.url, headers=self.hearders, params=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无效的请求')


if __name__ == "__main__":
    unittest.main()
