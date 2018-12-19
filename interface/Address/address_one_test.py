import unittest

import requests
from Global_base import global_base
from db_fixture import test_data
from db_fixture import test_db


class AddressOne(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/user/address/88")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    def test_get_address_one_success(self):
        '''正确的地址ID，查询成功'''
        self.result = requests.get(url=self.url, headers=self.headers).json()
        status = 200
        message = "请求成功"
        deliver_name = "固定用户"
        deliver_phone = "13800138001"
        deliver_address = "固定测试地址"
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['deliver_name'], deliver_name)
        self.assertEqual(self.result['data']['deliver_phone'], deliver_phone)
        self.assertEqual(self.result['data']['deliver_address'], deliver_address)


if __name__ == '__main__':
    test_data.init_data()  # c初始化接口测试数据
    unittest.main()
