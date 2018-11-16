import unittest

import requests

from Global_base import global_base


class AuthInfo(unittest.TestCase):
    def setUp(self):
        self.h = global_base.Utils.token(self)
        self.url = global_base.DefTool.url(self, 'api/auth/me')

    def test_getInfo(self):
        self.r = requests.get(url=self.url, headers=self.h).json()
        self.assertEqual(self.r['status'], 200)
        self.assertEqual(self.r['message'], '请求成功')
        self.assertEqual(self.r['data']['brand'], 1000)
        self.assertEqual(self.r['data']['mobile'], 17727498114)

    def tearDown(self):
        print(self.r)


if __name__ == "__main__":
    unittest.main()
