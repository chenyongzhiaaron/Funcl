import unittest

import requests
from parameterized import parameterized

from Global_base import global_base


class Subscribe(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/newsletter/subscribe")
        self.h = global_base.DefTool.defHeaders(self)

    def tearDown(self):
        pass

    @parameterized.expand([
        # ("输入正确且数据库不存在的邮箱，新增订阅成功", "262667641@qq.com", "funcl_global", "us", 200, "请求成功", "Welcome! Please check your mailbox. :)"),
        ("输入正确但数据库存在的邮箱，提示不能重复订阅", "aaron@crazybaby.com", "funcl_golbal", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),
        (
        "邮箱格式错误，订阅失败", "aa21ro3n@crazyb.1234", "funcl_golbal", "us", 422, "验证失败", 'The email address is unacceptable.'),
        ("locale 为US", "aaron@crazybaby.com", "funcl_golbal", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),
        ("locale 为CN", "aaron@crazybaby.com", "funcl_golbal", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),
        ("locale 为JP", "aaron@crazybaby.com", "funcl_golbal", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),
        ("scope 不存在", "aaron@crazybaby.com", "funcl_golbal1245", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),
        ("scope 存在", "aaron@crazybaby.com", "funcl_w1", "us", 200, "请求成功",
         " It seems like you were already on the list! :)"),

    ])
    def test_subscribe_success(self, case, email, scope, locale, status, message, data):
        playload = {"email": email, "scope": scope, "locale": locale}
        self.result = requests.post(url=self.u, headers=self.h, data=playload).json()
        print(self.result)
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertIn(self.result["data"], data)

    @parameterized.expand([
        ("邮箱为空，订阅失败", "", "funcl_global", "us", 422, "验证失败", ['请填写 email .']),
        ("邮箱格式错误，订阅失败", "aaron@crazyb", "funcl_golbal", "us", 422, "验证失败", ["Oops! Something's wrong with your email."]),
        ("邮箱格式错误，订阅失败", "aaroncrazyb", "funcl_golbal", "us", 422, "验证失败", ["Oops! Something's wrong with your email."]),
        ("邮箱格式错误，订阅失败", "@crazyb", "funcl_golbal", "us", 422, "验证失败", ["Oops! Something's wrong with your email."]),
        ("locale 不存在", "aaron@crazybaby.com", "funcl_golbal", "902", 422, "验证失败", ['The locale 限指定参数']),
        ("locale 为空", "aaron@crazybaby.com", "funcl_golbal", "", 422, "验证失败", ['请填写 locale .']),
        ("scope 为空", "aaron@crazybaby.com", "", "us", 422, "验证失败", ['请填写 scope .']),
    ])
    def test_subscribe_fail(self, case, email, scope, locale, status, message, errors):
        playload = {'email': email, 'scope': scope, 'locale': locale, 'status': status, 'message': message,
                    'error': errors}
        self.result_f = requests.post(url=self.u, headers=self.h, data=playload).json()
        print(self.result_f)
        self.assertEqual(self.result_f["status"], status)
        self.assertEqual(self.result_f['message'], message)
        if (case == "locale 不存在") | (case == "locale 为空"):
            self.assertEqual(self.result_f['errors']['locale'], errors)
        elif (case == "scope 为空") | (case == "scope 不存在"):
            self.assertEqual(self.result_f['errors']['scope'], errors)
        else:
            self.assertEqual(self.result_f['errors']['email'], errors)


if __name__ == "__main__":
    unittest.main()
