import unittest
import requests
from Global_base import global_base


class GetProductList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/plist/productList")

    def tearDown(self):
        print(self.result)

    def test_get_product_list_success(self):
        '''获取有借卡贷列表成功'''
        parma = {"cfgId": "NPL94820190117201810100"}
        r = requests.get(url=self.url, params=parma)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        # self.result = r.text
        # self.assertIn()


if __name__ == "__main__":
    unittest.main()
