import unittest

import requests

from Global_base import global_base
from db_fixture import test_data

from parameterized import parameterized


class DefaultAddress(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/user/default_address')
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取用户默认地址成功", 200, "请求成功", 88, 1)
    ])
    def test_get_default_address(self, case, status, message, address_id, is_default):
        self.result = requests.get(url=self.url, headers=self.headers).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['address_id'], address_id)
        self.assertEqual(self.result['data']['is_default'], is_default)


if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
