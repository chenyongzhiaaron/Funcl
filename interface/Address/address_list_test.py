import unittest

import requests

from Global_base import global_base
from db_fixture import test_data, test_db


class AddressList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/user/address_list")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    def test_get_address_list(self):
        ''' 获取当前用户全部地址成功'''
        status = 200
        message = "请求成功"
        deliver_name = "固定用户"
        deliver_name_init = "初始化用户名"
        address_id_init = test_db.T_DB().t_db2()
        deliver_phone_init = '17727475174'
        deliver_phone = '13800138001'
        deliver_address = '固定测试地址'
        deliver_address_init = "初始化用户地址"
        self.result = requests.get(url=self.url, headers=self.headers).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data'][1]['deliver_name'], deliver_name)
        self.assertEqual(self.result['data'][0]['deliver_name'], deliver_name_init)
        self.assertEqual(self.result['data'][0]['address_id'], address_id_init)
        self.assertEqual(self.result['data'][0]['deliver_phone'], deliver_phone_init)
        self.assertEqual(self.result['data'][1]['deliver_phone'], deliver_phone)
        self.assertEqual(self.result['data'][1]['deliver_address'], deliver_address)
        self.assertEqual(self.result['data'][0]['deliver_address'], deliver_address_init)


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
