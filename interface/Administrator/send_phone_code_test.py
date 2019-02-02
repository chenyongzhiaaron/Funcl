import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class GetCaptcha(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "usercenter/sys/sendPhoneCode")
        self.parms = global_base.DefTool.defBaseParmsGetCode(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand(
        [
            ("输入正确手机号获取验证码成功", 200, "ok"),
        ]
    )
    def test_auth_captcha_success(self, case, code, msg):
        '''数据正确，获取成功'''
        p1 = {'phone': 18127813600}
        payload = dict(self.parms, **p1)
        print(payload)
        self.result = requests.get(self.url, params=payload).json()
        self.assertEqual(self.result["code"], code)
        self.assertEqual(self.result['msg'], msg)


if __name__ == "__main__":
    unittest.main()
