import unittest
import requests
from Global_base import global_base


class GetNewLoanProduct(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/loan/getNewLoanProduct.do')

    def tearDown(self):
        print(self.result)

    def test_get_new_loan_product_success(self):
        '''获取新口子列表成功'''
        self.result = requests.get(url=self.url).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.assertEqual(self.result['data']['productList'][0]['pname'], '自动下线产品验证')


if __name__ == '__main__':
    unittest.main()
