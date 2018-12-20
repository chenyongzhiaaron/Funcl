import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_data


class NewAddress(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/user/address")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("传入正确必填项，新建默认地址成功", "测试收货人名称", 17727475174, 11, 1101, 110105, "测试地址名称", 518110, 1, 200, '请求成功'),
        ("传入正确必填项，新建非默认地址成功", "测试收货人名称", 17727475174, 11, 1101, 110105, "测试地址名称", 518110, 0, 200, '请求成功'),
    ])
    def test_new_address_success(self, case, deliver_name, deliver_phone, deliver_address_province_id,
                                 deliver_address_city_id, deliver_address_district_id, deliver_address, zip_code,
                                 is_default,
                                 status, message):
        '''新建默认地址及非默认地址成功'''
        payload = {"deliver_name": deliver_name, "deliver_phone": deliver_phone,
                   "deliver_address_province_id": deliver_address_province_id,
                   "deliver_address_city_id": deliver_address_city_id,
                   "deliver_address_district_id": deliver_address_district_id, "deliver_address": deliver_address,
                   "is_default": is_default, "zip_code": zip_code}
        self.result = requests.post(url=self.url, headers=self.headers, data=payload).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    # test_data.init_data()
    unittest.main()

'''
deliver_name                        必填|max:20
华安
deliver_phone                       必填|max:20
15812749031
deliver_address_province_id         必填|integer|max:100
11
deliver_address_city_id             必填|integer|max:10000
1101
deliver_address_district_id         必填|integer|max:999999999
110105
deliver_address                      必填|String|max:255
朝阳十八路2031
zip_code                            必填|String|max:15
518000
is_default                          必填|是否设定为默认地址，1为是，0为否
0
'''
