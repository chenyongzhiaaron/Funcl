import requests

from db_fixture import test_db


class Utils():
    def token(self):
        headers1 = {'Accept': 'application/json', "Access-Token": '17727498114'}
        url1 = DefTool.url(self, "api/auth/captcha?mobile=17727498114")
        url2 = DefTool.url(self, 'api/auth/login')
        re = requests.get(url=url1, headers=headers1).json()
        # print(re)
        number = test_db.T_DB.t_db(self)
        # print(number)
        payload = {"mobile": 17727498114, "verify_code": number}
        response = requests.post(url=url2, data=payload, headers=headers1).json()
        # print(response)
        t = response['data']['access_token']
        # print(t)
        b = "bearer "
        access_token = b + t
        h = {
            'Accept': 'application/json',
            'Authorization': access_token,
            "Access-Token": '17727498114'
        }
        # print(h)
        return h


class DefTool():
    def url(self, patch):
        # baseUrl = 'https://test.api.funcl.com.cn/'    # 这个是 测试服
        baseUrl = 'http://api.funcl.com/'  # 这个是田科本地
        # baseUrl = 'http://api.funcl.com'
        url = baseUrl + patch
        return url

    def defHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Access-Token": '17727498114'
        }
        return headers

    def defaultHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8"
                             "vYXBpLmZ1bmNsLmNvbS9hcGkvYXV0aC9sb2dpbiIsImlhdCI6MTU0MzQ3OTM4NywiZXhwIjo"
                             "xNTQzNTY1Nzg3LCJuYmYiOjE1NDM0NzkzODcsImp0aSI6IlJRblJyVEZSQVpRV0lwY0ciLCJzdWIiOjM"
                             "zMywicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.6fxYQB9Ey5nbnFNzz"
                             "JvpYaSoXEJiKzp_1zx7GehVVd4",
            "Access-Token": '18127813600'
        }
        return headers
