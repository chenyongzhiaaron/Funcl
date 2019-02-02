import unittest

import requests

from Global_base import global_base


class AuthLogout(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, 'usercenter/sys/logout')
        self.h = global_base.DefTool.defBaseParmsGetCode(self)

    def tearDown(self):
        print(self.result)

    def test_logout(self):
        '''验证退出登录成功'''
        p = {}
        self.result = requests.post(url=self.u, headers=self.h).json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '请求成功')


if __name__ == '__main__':
    unittest.main()
