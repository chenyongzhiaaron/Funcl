import unittest
import requests
from Global_base import global_base
from db_fixture import test_db


class LoginByCode(unittest.TestCase):
    def setUp(self):
        self.url_send_code = global_base.DefTool.url(self, 'usercenter/sys/sendPhoneCode')
        self.url = global_base.DefTool.url(self, 'usercenter/sys/loginByCode')
        self.parms = global_base.DefTool.defBaseParmsGetCode(self)
        self.p = global_base.DefTool.defBaseParmsGetCode(self)

    def tearDown(self):
        print(self.result)
        print(self.re)

    def test_login_by_code_success(self):
        '''输入正确手机号及验证码，登陆成功'''
        # 获取验证码
        p1 = {'phone': 18570000000}
        payload = dict(self.parms, **p1)
        print(payload)
        self.re = requests.get(self.url, params=payload).json()
        # 使用获取的验证码进行登陆
        code = test_db.T_DB().t_db2()
        p2 = {"username": 18570000000, "code": code}
        params = dict(p2, **self.p)
        self.result = requests.post(url=self.url, data=params).json()
        self.assertEqual(self.result['code'], '200')
        self.assertEqual(self.result['msg'], 'ok')


if __name__ == "__main__":
    unittest.main()
