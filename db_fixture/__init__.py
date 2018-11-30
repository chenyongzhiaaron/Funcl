import unittest
import requests

class ProductInfo(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        print(self.result)
        print(self.r)

    def test_get_product_info(self):
        self.r = requests.get(url='https://api.github.com/events')
        self.result = self.r.json()
        self.assertEqual(self.result[0]["id"], "8660437067")

if __name__ == "__main__":
    unittest.main()