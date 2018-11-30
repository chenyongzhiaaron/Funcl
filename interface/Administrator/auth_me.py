import unittest

import requests

from Global_base import global_base


class AuthMe(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, 'api/auth/me')
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    def test_auth_me_success(self):
        ''' 获取用户信息成功 '''
        self.result = requests.get(url=self.u, headers=self.h).json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], "请求成功")
        self.assertEqual(self.result['data']['brand'], 1000)
        self.assertEqual(self.result['data']['mobile'], "17727498114")


if __name__ == "__main__":
    unittest.main()
