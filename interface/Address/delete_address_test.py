import unittest

import requests

from Global_base import global_base
from db_fixture import test_db, test_data


class DeleteAddress(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/user/address")
        self.url2 = global_base.DefTool.url(self, "api/user/address_list")

        self.headers = global_base.DefTool.defaultHeaders(self)
        self.address_id = test_db.T_DB().t_db2()

    def tearDown(self):
        print(self.result)
        print(self.result2)

    def test_delete_address_success(self):
        '''地址id存在且正确，删除地址成功'''
        status = 200
        message = "请求成功"
        address_id = 88
        deliver_name = '固定用户'
        deliver_address = '固定测试地址'
        payload = {"delete_address_id": self.address_id}
        self.result = requests.delete(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result["message"], message)
        '''调用查询用户地址接口断言是否真正删除地址成功，若查询id == 固定地址di，怎成功'''
        self.result2 = requests.get(url=self.url2, headers=self.headers).json()
        self.assertEqual(self.result2['data'][0]['address_id'], address_id)
        self.assertEqual(self.result2['data'][0]['deliver_name'], deliver_name)
        self.assertEqual(self.result2['data'][0]['deliver_address'], deliver_address)


if __name__ == "__main__":
    test_data.init_data()
    unittest.main()
