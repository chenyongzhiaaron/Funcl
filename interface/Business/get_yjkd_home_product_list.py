import unittest
import requests
from Global_base import global_base


class GetHomeProdcutList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "app/loan/getHomeProductList.do")

    def tearDown(self):
        print(self.result)

    def test_get_home_product_list_success(self):
        '''获取有借卡贷Tab1首页成功'''
        pamras = {"id": "NPL56820190110110515100"}
        r = requests.get(url=self.url, params=pamras)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], "ok")
        self.result = r.text
        self.assertIn("米融", self.result)


if __name__ == "__main__":
    unittest.main()
