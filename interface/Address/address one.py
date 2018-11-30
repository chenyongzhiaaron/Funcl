import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_data
from db_fixture import test_db


class AddressOne(unittest.TestCase):
    def setUp(self):
        id = test_db.T_DB().t_db2()
        self.url = global_base.DefTool.url(self, "api/user/address/" + str(id))
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        pass

    @parameterized.expand([
        ("正确的地址ID，查询成功", 200, "请求成功", 16, '测试工作者', '13800138000', '测试办公室'),
    ])
    def test_get_address_one_success(self, case, status, message, data_address_id, data_deliver_name,
                                     data_deliver_phone, data_deliver_address):
        self.result = requests.get(url=self.url, headers=self.headers).json()
        print(self.result)
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['address_id'], data_address_id)
        self.assertEqual(self.result['data']['deliver_name'], data_deliver_name)
        self.assertEqual(self.result['data']['deliver_phone'], data_deliver_phone)
        self.assertEqual(self.result['data']['deliver_address'], data_deliver_address)


if __name__ == '__main__':
    # test_data.init_data()   # c初始化接口测试数据
    unittest.main()
