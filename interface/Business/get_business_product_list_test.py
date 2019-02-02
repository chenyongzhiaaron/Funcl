import requests
import unittest
from Global_base import global_base


class GetBusinessProductList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "/app/dwdk/getBusinessProductList.do")

    def tearDown(self):
        print(self.result)

    def test_get_business_product_list_success(self):
        '''查询大王贷款列表成功'''
        parms = {"cfgId": "NPL81820181011105344100"}
        self.result = requests.get(url=self.url, params=parms).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], "ok")


if __name__ == "__main__":
    unittest.main()
