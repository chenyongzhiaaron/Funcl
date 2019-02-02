import unittest
import requests
from Global_base import global_base


class GetCreditHelper(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/credit/getCreditHelper.do')

    def tearDown(self):
        print(self.result)

    def test_get_credit_helper_success(self):
        r = requests.get(url=self.url)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.result = r.text
        self.assertIn('拼多多', self.result)
        self.assertIn('贷前检查', self.result)
        self.assertIn('拒贷诊断', self.result)
        self.assertIn('信用卡提现', self.result)
        self.assertIn('算一卦', self.result)
        self.assertIn('otherBanner', self.result)
        self.assertIn('creditFindBanner', self.result)


if __name__ == "__main__":
    unittest.main()
