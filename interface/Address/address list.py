import unittest

import requests
from parameterized import parameterized
from db_fixture import test_data
from Global_base import global_base


class AddressList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/user/address_list")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("获取当前用户全部地址成功", 200, "请求成功", "修改用户", '测试工作者', 17, 16, 1, 0),
    ])
    def test_get_address_list(self, case, status, message, deliver_name_0, deliver_name_1,
                              address_id_0, address_id_1, is_default_0, is_default_1):
        self.result = requests.get(url=self.url, headers=self.headers).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data'][0]['deliver_name'], deliver_name_0)
        self.assertEqual(self.result['data'][1]['deliver_name'], deliver_name_1)
        self.assertEqual(self.result['data'][0]['address_id'], address_id_0)
        self.assertEqual(self.result['data'][1]['address_id'], address_id_1)
        self.assertEqual(self.result['data'][0]['is_default'], is_default_0)
        self.assertEqual(self.result['data'][1]['is_default'], is_default_1)


if __name__ == '__main__':
    unittest.main()
