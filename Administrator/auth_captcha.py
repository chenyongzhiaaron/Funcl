import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class Get_captcha(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/auth/captcha?mobile=18127813600")
        self.hearders = global_base.DefTool.defHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand(
        [
            ("输入正确手机号获取验证码成功", 200, "请求成功")
        ]
    )
    def test_get_captcha(self, case, status, message):
        self.result = requests.get(self.url, headers=self.hearders).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result['message'], message)


if __name__ == "__main__":
    unittest.main()
