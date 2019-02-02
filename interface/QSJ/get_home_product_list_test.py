import unittest
import requests
from Global_base import global_base


class GetHomeProductList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/loan/getHomeProductListV3.do')

    def tearDown(self):
        print(self.result)

    def test_get_home_product_list_success(self):
        r = requests.get(url=self.url)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.result = r.text
        self.assertIn('精灵口袋', self.result)
        self.assertIn('123395748146544640', self.result)


if __name__ == '__mani__':
    unittest.main()
