# coding=utf-8
import unittest
import requests
from Global_base import global_base
from parameterized import parameterized


class AppInit(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, "usercenter/sys/init")
        self.p2 = global_base.DefTool.defBaseParmsGetCode(self)
    def tearDown(self):
        print(self.result)

    def test_app_init_success(self):
        p1 = {"androidid": "affb199d7d46d386", "availablespace": 110513348608, "brand": "OPPO", "imsi": 000000, "mac": "78:36:CC:9A:05:C3", "memory": 5850380, "serialnumber": "", "totalspace": 116502671360}
        payload = dict(p1, **self.p2)
        self.result = requests.post(url=self.url, data=payload).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)
        # self.assertIn(first_name, self.result)
        # self.assertIn(second_name, self.result)
        # self.assertIn(third_name, self.result)
        # self.assertIn(fourth_name, self.result)


if __name__ == "__main__":
    unittest.main()
