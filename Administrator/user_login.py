import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_db


class UserLogin(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/auth/login")
        self.h = global_base.DefTool.defHeaders(self)

    @parameterized.expand(
        [
            ("手机号正确，验证码错误，登录失败", 18127813600, 123456, 422, "验证失败"),
            ("手机号错误，验证码正确，登录失败", 18127813600, 123456, 422, "验证失败"),
            ("手机号最大值+1，验证码正确，登录失败", 181278136001, 123456, 422, "验证失败"),
            ("手机号-1，验证码正确，登录失败", 1812781360, 123456, 422, "验证失败"),
            ("所有参数为空，登录失败", "", "", 422, "验证失败",),
            ("手机号参数为空，登录失败", "", 1234, 422, "验证失败",),
            ("验证码参数为空，登录失败", 18127813600, "", 422, "验证失败",),
        ]
    )
    def test_user_login(self, case, mobile, verify_code, status, message):
        payload = {"mobile": mobile, "verify_code": verify_code}
        self.result1 = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result1["status"], status)
        self.assertEqual(self.result1["message"], message)
        print(self.result1)

    def test_login_success(self):
        headers1 = {'Accept': 'application/json', "Access-Token": '18127813600'}
        url1 = global_base.DefTool.url(self, "api/auth/captcha?mobile=18127813600")
        self.r1 = requests.get(url=url1, headers=headers1).json()
        number = test_db.T_DB.t_db(self)
        payload = {"mobile": 18127813600, "verify_code": number}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "请求成功")
        self.assertEqual(self.result["data"]["token_type"], "bearer")
        print(self.result)

    def tearDown(self):
        # print(self.r1)
        # print(self.result1)
        # print(self.result)
        print("测试完成")


if __name__ == "__main__":
    unittest.main()
