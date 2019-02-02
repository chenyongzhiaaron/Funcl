import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_db


class UserLogin(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "usercenter/sys/loginByPass")
        self.p = global_base.DefTool.defBaseParmsGetPassword(self)

    def test_login_success(self):
        '''参数正确，登录成功'''
        p1 = {"username": 18127813600, "password": 111111}
        payload = dict(self.p, **p1)
        print(payload)
        self.result = requests.post(url=self.u, data=payload).json()
        self.assertEqual(self.result["code"], 200)
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["data"]["username"], 18127813600)
        self.assertEqual(self.result['data']['mobile'], 18127813600)
        # self.assertEqual(self.result['token'], )

    def tearDown(self):
        print(self.result)


if __name__ == "__main__":
    unittest.main()
