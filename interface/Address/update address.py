import unittest

import requests
from parameterized import parameterized
from db_fixture import test_db
from Global_base import global_base
from db_fixture import test_data


class UpdatedAddress(unittest.TestCase):
    def setUp(self):
        address_id = test_db.T_DB.t_db2(self)
        print("api/user/address/" + str(address_id))
        self.url = global_base.DefTool.url(self, "api/user/address/" + str(address_id))
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("address_id 为单前用户所有，修改成功过", '修改用户', 13800138001, 44, 4419, 441900003, "修改测试地址", 1, 200, "请求成功"),

    ])
    def test_update_address(self, case, deliver_name, deliver_phone, deliver_address_province_id,
                            deliver_address_city_id, deliver_address_district_id,
                            deliver_address, is_default, status, message):
        payload = {"deliver_name": deliver_name, "deliver_phone": deliver_phone,
                   "deliver_address_province_id": deliver_address_province_id,
                   "deliver_address_city_id": deliver_address_city_id,
                   "deliver_address_district_id": deliver_address_district_id, "deliver_address": deliver_address,
                   "is_default": is_default}
        self.result = requests.put(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
