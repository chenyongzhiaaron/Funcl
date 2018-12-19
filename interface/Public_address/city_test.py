import unittest
import requests
from db_fixture import test_db
from Global_base import global_base

class City(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "api/common/area/city")
        self.headers = global_base.DefTool.defaultHeaders(self)

    def tearDown(self):
        print(self.result)

    def test_get_city(self):
        payload = {"province_id": 21}
        self.result = requests.get(url=self.url, headers=self.headers,params=payload).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result['message'], "请求成功")
        # self.assertEquals(self.result['message'], "请求成功")


if __name__ == "__main__":
    unittest.main()



