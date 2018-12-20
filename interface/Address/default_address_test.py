import unittest

import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from Global_base import global_base
from db_fixture import test_data


class DefaultAddress(unittest.TestCase):
    def setUp(self):
        # test_data.init_data()  # 初始化接口测试数据

        self.url = global_base.DefTool.url(self, 'api/user/default_address')
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    def test_get_default_address(self):
        '''获取用户默认地址成功'''
        status = 200
        message = "请求成功"
        # is_default = 1
        self.result = requests.get(url=self.url, headers=self.headers).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        # self.assertEqual(self.result['data']['is_default'], is_default)


if __name__ == "__main__":
    unittest.main()
