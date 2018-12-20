import unittest

import requests

from Global_base import global_base
from db_fixture import test_data, test_db


class UpdateDefaultAddress(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'api/user/default_address')
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)
        print(self.result2)


    def test_update_default_address_success(self):
        '''输入正确并存在的地址 id 修改默认地址成功'''
        aid = test_db.T_DB().t_db2()
        payload = {"default_address_id": aid}
        self.result = requests.put(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result['message'], "请求成功")
        '''获取用户默认地址查看是否修改默认地址成功'''
        url = global_base.DefTool.url(self, "api/user/default_address")
        self.result2 = requests.get(url=url, headers=self.headers).json()
        self.assertEqual(self.result2['status'], 200)
        self.assertEqual(self.result2['message'], "请求成功")
        self.assertEqual(self.result2['data']['address_id'], aid)
        self.assertEqual(self.result2['data']['is_default'], 1)


if __name__ == '__main__':
    # test_data.init_data()
    unittest.main()


'''
PUT 修改默认地址
default_address_id  74
必填|integer|max:10
'''