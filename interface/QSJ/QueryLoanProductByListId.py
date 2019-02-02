import unittest
import requests
from Global_base import global_base


class QueryLoanProductByListId(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/loan/queryLoanProductByListId.do')

    def tearDown(self):
        print(self.result)

    def test_query_loan_product_by_listId_success(self):
        '''获取轻松借列表/首页极速下款URL不带参数成功'''
        params = {"id": "NPL51420190110153458100"}
        r = requests.get(url=self.url, params=params)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.result = r.text
        self.assertIn('极速下款', self.result)
        self.assertIn('auto4', self.result)
        self.assertIn('auto2', self.result)


if __name__ == '__main__':
    unittest.main()
