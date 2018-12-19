import unittest

import requests

from Global_base import global_base

a = '''asd'''
print(a)

class GetOne(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, "api/serials/getOne")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    def test_getOne_snId_exist(self):
        ''' serial_id 存在，查询成功 '''
        payload = {'serial_id': 1}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '请求成功')
        self.assertEqual(self.result['data']['id'], 1)
        self.assertEqual(self.result['data']['serial_no'], 'C037A000FA22')

    def test_getOne_snId_null(self):
        ''' serial_id 为空 查询失败'''
        payload = {'serial_id': ""}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无该产品记录.')

    def test_getOne_snId_error(self):
        ''' serial_id 错误，查询失败 '''
        payload = {'serial_id': "ww测试39*"}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无该产品记录.')

    def test_getOne_snId_absent(self):
        ''' serial_io 不存，查询失败 '''
        payload = {'serial_id': 2}
        self.result = requests.get(url=self.u, headers=self.h, params=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无该产品记录.')


if __name__ == '__main__':
    unittest.main()
