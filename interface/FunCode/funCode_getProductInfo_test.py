import unittest

import requests
from parameterized import parameterized

from Global_base import global_base
from db_fixture import test_data


class FunCodeProductInfo(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/funCode/getProductInfo")
        self.h = global_base.DefTool.defaultHeaders(self)
        self.status = 200
        self.message = "请求成功"
        self.code = 'MQZE1G57P3X72D9W'
        self.product_id = 'j6WdKJEXOKmarZpA'
        self.name = 'Funcl W1'
        self.product_code = 'H18D'
        self.color_text = 'white'

    def tearDown(self):
        print(self.result)

    def test_getFunCodeProdcutInfo(self):
        '''参数正确，请求成功'''
        payload = {'code': self.code, 'product_id': self.product_id}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], self.status)
        self.assertEqual(self.result['message'], self.message)
        self.assertEqual(self.result['data']['id'], self.product_id)
        self.assertEqual(self.result['data']['name'], self.name)
        self.assertEqual(self.result['data']['product_code'], self.product_code)
        self.assertEqual(self.result['data']['color_text'], self.color_text)


if __name__ == "__main__":
    unittest.main()
