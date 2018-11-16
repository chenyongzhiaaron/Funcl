import unittest
import requests

from Global_base import global_base
from parameterized import parameterized
from db_fixture import test_db


class FunCodeProductInfo(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self,"api/funCode/getProductInfo")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ('参数正确，请求成功', 'FJ2U89H198H928H9', 'wONZeKmv0R3Gkb9r', 200, '请求成功', 'wONZeKmv0R3Gkb9r'),
        ('code 正确，product_id 错误，请求失败', 'FJ2U89H198H928H9', 'wONZeKmv0R3Gkb9r=-21344', 422, '请求成功', 'wONZeKmv0R3Gkb9r'),
        ('code 正确，product_id 为空，请求失败', 'FJ2U89H198H928H9', 'wONZeKmv0R3Gkb9r=-21344', 200, '请求成功', 'wONZeKmv0R3Gkb9r'),
        ('code 错误，product_id 正确，请求失败', 'FJ2U89H198H928H932', 'wONZeKmv0R3Gkb9r', 200, '请求成功', 'wONZeKmv0R3Gkb9r'),
    ])
    def test_getFunCodeProdcutInfo(self, case, code, product, status, message, data):
        payload = {'code': code, 'product_id': product, 'status': status, 'message': message, 'data': data}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['data']['id'], data)


if __name__=="__main__":
    unittest.main()

#  这个接口还没有完善,api 有问题。
