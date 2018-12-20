import requests

from db_fixture import test_db


class Utils():
    #   用于单一操作
    def token(self):
        headers1 = {'Accept': 'application/json', "Access-Token": '17727475174'}
        url1 = DefTool.url(self, "api/auth/captcha?mobile=17727475174")
        url2 = DefTool.url(self, 'api/auth/login')
        re = requests.get(url=url1, headers=headers1).json()
        # print(re)
        number = test_db.T_DB.t_db(self)
        # print(number)
        payload = {"mobile": 17727475174, "verify_code": number}
        response = requests.post(url=url2, data=payload, headers=headers1).json()
        # print(response)
        t = response['data']['access_token']
        # print(t)
        b = "bearer "
        access_token = b + t
        h = {
            'Accept': 'application/json',
            'Authorization': access_token,
            "Access-Token": '17727475174'
        }
        print(h)
        return h


class DefTool():
    #   用户多次操作
    def url(self, patch):
        # baseUrl = 'https://test.api.funcl.com.cn/'    # 这个是 测试服
        baseUrl = 'http://api.funcl.com/'  # 这个是田科本地
        # baseUrl = 'http://api.funcl.com'
        url = baseUrl + patch
        return url

    def defHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Access-Token": '17727475174'
        }
        return headers

    def defaultHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmZ1bmNsLmNvbS9hcGkvY"
                             "XV0aC9sb2dpbiIsImlhdCI6MTU0NTI5NTM3MSwiZXhwIjoxNTQ1MzgxNzcxLCJuYmYiOjE1NDUyOTUzNzEsImp0a"
                             "SI6IlVhVVI3Qm1FckxiQU8xWFkiLCJzdWIiOjM1MiwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMT"
                             "RlMGIwNDc1NDZhYSJ9.O2Ubr1oBtS-dQOYFoAFd8vuUmFEfVURYIX2_ig19CMA",
            "Access-Token": '17727475174',
            'Accept-Language': "cn",
            # "Content encoding": 'UTF-8'
        }
        return headers
