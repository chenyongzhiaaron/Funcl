import unittest

import requests

from Global_base import global_base


class SerialsStore(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, 'api/serials/store')
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    # def test_serials_store_success(self):
    #     ''' serials no. 绑定成功'''
    #     payload = {'serial_no': "C037A000FA22", 'confirm': 'true'}
    #     self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
    #     self.assertEqual(self.result['status'], 200)
    #     self.assertEqual(self.result['message'], '请求成功')
    #     self.assertEqual(self.result['data']['serial_no'], 'C037A000FA22')

    def test_serials_store_sn_exist(self):
        ''' serial no. 已存在，注册失败 '''
        payload = {'serial_no': 'C037A000FA22', 'confirm': "true"}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '当前用户已绑定该产品.')

    def test_serials_store_all_null(self):
        ''' 所有参数为空，注册失败'''
        payload = {'serial_no': '', 'confirm': ''}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无效的产品记录.')

    def test_serials_store_sn_error(self):
        ''' serial no. 错误，注册失败'''
        payload = {'serial_no': "c009错~@!@90lkzXK", "confirm": 'true'}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无效的产品记录.')

    def test_serials_store_sn_null(self):
        ''' SN 为空，注册失败 '''
        payload = {'serial_no': "", 'confirm': "true"}
        self.result = requests.post(url=self.u, headers=self.h, data=payload).json()
        self.assertEqual(self.result['status'], 400)
        self.assertEqual(self.result['message'], '无效的产品记录.')
    

if __name__ == '__main__':
    unittest.main()
