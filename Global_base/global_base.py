import requests

from db_fixture import test_db


class Utils():
    def token(self):
        headers1 = {'Accept': 'application/json', "Access-Token": '18127813600'}
        url1 = DefTool.url(self, "api/auth/captcha?mobile=18127813600")
        url2 = DefTool.url(self, 'api/auth/login')
        re = requests.get(url=url1, headers=headers1).json()
        print(re)
        number = test_db.T_DB.t_db(self)
        payload = {"mobile": 18127813600, "verify_code": number}
        response = requests.post(url=url2, data=payload, headers=headers1).json()
        print(response)
        t = response['data']['access_token']
        b = "bearer "
        access_token = b + t
        h = {
            'Accept': 'application/json',
            'Authorization': access_token,
            "Access-Token": '18127813600'
        }
        print(h)
        return h


class DefTool():
    def url(self, patch):
        baseUrl = 'https://test.api.funcl.com.cn/'
        url = baseUrl + patch
        return url

    def defHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Access-Token": '18127813600'
        }
        return headers
