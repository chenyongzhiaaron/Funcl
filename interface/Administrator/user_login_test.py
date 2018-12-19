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
            ("手机号正确，验证码错误，登录失败", 17727498114, 1233, 422, "验证失败", 'The 手机号码 已变更.', 'The verify code 不正确.'),
            ("手机号错误，验证码正确，登录失败", 13800138009, 123456, 422, "验证失败", 'The 手机号码 已变更.', 'The verify code 不正确.'),
            ("手机号最大值+1，验证码正确，登录失败", 181278136001, 123456, 422, "验证失败", '手机号码 格式不对.', 'The verify code 不正确.'),
            ("手机号-1，验证码正确，登录失败", 1812781360, 123456, 422, "验证失败", '手机号码 格式不对.', 'The verify code 不正确.'),
            ("所有参数为空，登录失败", "", "", 422, "验证失败", '请填写 手机号码 .', '请填写 verify code .'),
            ("手机号参数为空，登录失败", "", 1234, 422, "验证失败", '请填写 手机号码 .', 'The verify code 不正确.'),
            ("验证码参数为空，登录失败", 17727498114, "", 422, "验证失败", 'The 手机号码 已变更.', '请填写 verify code .'),
        ]
    )
    def test_user_login(self, case, mobile, verify_code, status, message, errors_mobile, errors_verify_code):
        payload = {"mobile": mobile, "verify_code": verify_code}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result['errors']['mobile'][0], errors_mobile)
        self.assertEqual(self.result['errors']['verify_code'][0], errors_verify_code)

    def test_login_success(self):
        headers1 = {'Accept': 'application/json', "Access-Token": '17727498114'}
        url1 = global_base.DefTool.url(self, "api/auth/captcha?mobile=17727498114")
        self.r1 = requests.get(url=url1, headers=headers1).json()
        number = test_db.T_DB.t_db(self)
        payload = {"mobile": 17727498114, "verify_code": number}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "请求成功")
        self.assertEqual(self.result["data"]["token_type"], "bearer")

    def tearDown(self):
        print(self.result)


if __name__ == "__main__":
    unittest.main()
