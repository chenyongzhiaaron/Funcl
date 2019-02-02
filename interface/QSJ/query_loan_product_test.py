import unittest
import requests
from Global_base import global_base


class QueryLoanProduct(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/loan/queryLoanProductByListIdV2.do')

    def tearDown(self):
        print(self.result)

    def test_query_loan_product_success(self):
        r = requests.get(url=self.url)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.result = r.text
        # self.assertIn('精灵口袋', self.result)


if __name__ == '__main__':
    unittest.main()
