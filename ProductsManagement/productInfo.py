import unittest

import requests

from Global_base import global_base


class ProductInfo(unittest.TestCase):
    def setUp(self):
        self.u = global_base.DefTool.url(self, 'api/product/getInfo/H18D')
        self.h = global_base.DefTool.defHeaders(self)
        self.u2 = global_base.DefTool.url(self, 'api/product/getInfo/H18E')

    def tearDown(self):
        print(self.result)
        print(self.r)

    def test_get_product_info(self):
        self.result = requests.get(url=self.u, headers=self.h).json()
        self.assertEqual(self.result['data'][0]['name'], "Funcl W1")
        self.assertEqual(self.result['data'][0]['id'], "lYaDb7EjKK3LONk5")
        self.assertEqual(self.result['data'][0]['product_code'], 'H18D')
        self.assertEqual(self.result['data'][0]['color_code'], '1000')
        self.assertEqual(self.result['data'][0]['color_text'], 'black')
        self.assertEqual(self.result['data'][1]['name'], 'Funcl W1')
        self.assertEqual(self.result['data'][1]['color_code'], '2000')
        self.assertEqual(self.result['data'][1]['product_code'], 'H18D')
        self.assertEqual(self.result['data'][1]['color_text'], 'white')
        self.assertEqual(self.result['data'][1]['id'], 'p0qgjlEQ0omz2eA8')
        self.r = requests.get(url=self.u2, headers=self.h).json()
        self.assertEqual(self.r['data'][0]['name'], "Funcl AI")
        self.assertEqual(self.r['data'][0]['id'], "j6WdKJEXOKmarZpA")
        self.assertEqual(self.r['data'][0]['product_code'], 'H18E')
        self.assertEqual(self.r['data'][0]['color_code'], '1000')
        self.assertEqual(self.r['data'][0]['color_text'], 'black')
        self.assertEqual(self.r['data'][1]['name'], 'Funcl AI')
        self.assertEqual(self.r['data'][1]['color_code'], '2000')
        self.assertEqual(self.r['data'][1]['product_code'], 'H18E')
        self.assertEqual(self.r['data'][1]['color_text'], 'white')
        self.assertEqual(self.r['data'][1]['id'], 'wONZeKmv0R3Gkb9r')

if __name__ == "__main__":
    unittest.main()