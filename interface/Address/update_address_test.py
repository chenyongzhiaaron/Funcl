import os
import sys
import unittest

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import requests
from db_fixture import test_db
from Global_base import global_base
from db_fixture import test_data


class UpdatedAddress(unittest.TestCase):
    def setUp(self):
        self.address_id = test_db.T_DB.t_db2(self)
        print("api/user/address/" + str(self.address_id))
        self.url = global_base.DefTool.url(self, "api/user/address/" + str(self.address_id))
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)
        print(self.result2)

    def test_update_address(self):
        '''address_id 为单前用户所有，修改成功过'''
        status = 200
        message = "请求成功"
        deliver_name = '修改用户'
        deliver_phone = 13800138001
        deliver_address_province_id = 44
        deliver_address_district_id = 441900003
        deliver_address_city_id = 4419
        deliver_address = '修改测试地址'
        is_default = 1
        payload = {"deliver_name": deliver_name, "deliver_phone": deliver_phone,
                   "deliver_address_province_id": deliver_address_province_id,
                   "deliver_address_city_id": deliver_address_city_id,
                   "deliver_address_district_id": deliver_address_district_id, "deliver_address": deliver_address,
                   "is_default": is_default}
        self.result = requests.put(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        ''' 调用查询当前用户个人地址接口，断言是否真正修改用户地址成功'''
        self.result2 = requests.get(url=self.url, headers=self.headers).json()
        self.assertEqual(self.result2["status"], status)
        self.assertEqual(self.result2['message'], message)
        self.assertEqual(self.result2['data']['address_id'], self.address_id)
        self.assertEqual(self.result2['data']['deliver_name'], deliver_name)
        self.assertEqual(self.result2['data']['deliver_phone'], deliver_phone)
        self.assertEqual(self.result2['data']['deliver_address'], deliver_address)
        self.assertEqual(self.result2['data']['is_default'], is_default)
        self.assertEqual(self.result2['data']['deliver_address_province']['province_id'], deliver_address_province_id)
        self.assertEqual(self.result2['data']['deliver_address_city']['city_id'], deliver_address_city_id)
        self.assertEqual(self.result2['data']['deliver_address_district']['district_id'], deliver_address_district_id)


if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
