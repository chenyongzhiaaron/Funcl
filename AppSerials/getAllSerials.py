import unittest

import requests

from Global_base import global_base


class GetAllSerials(unittest.TestCase):
    def setUp(self):
        self.r = global_base.DefTool.url(self, "api/serials/getAll")
        self.h = global_base.Utils.token(self)

    def tearDown(self):
        print(self.result)

    def test_getAllSerials_success(self):
        ''' 查询所有 serial 成功 '''
        self.result = requests.get(url=self.r, headers=self.h).json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "请求成功")
        self.assertEqual(self.result["data"][0]["id"], 1)
        self.assertEqual(self.result['data'][0]['serial_no'], 'C037A000FA22')


if __name__ == "__main__":
    unittest.main()
