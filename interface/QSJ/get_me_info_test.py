import requests
import unittest
from Global_base import global_base


class GetMeInfo(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, 'app/profile/getMeInfo.do')

    def tearDown(self):
        print(self.result)

    def test_get_me_info_success(self):
        '''用户未登录查看个人中心成功'''
        r = requests.get(url=self.url)
        self.result = r.json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')
        self.assertEqual(self.result['data']['recommendInfo']['productMoreUrl'],
                         "http://k8s-qsj-test.jie.iask.cn/pg/qsjAppV2/query.html?cfgId=16&hsinaifNeedFullWin=2")
        self.assertEqual(self.result['data']['userInfo']['login'], False)


if __name__ == '__main__':
    unittest.main()
