import requests

# class Utils():
#     #   用于单一操作
#     def token(self):
#         headers1 = {'Accept': 'application/json', "Access-Token": ''}
#         url1 = DefTool.url(self, "api/auth/captcha?mobile=")
#         url2 = DefTool.url(self, 'api/auth/login')
#         re = requests.get(url=url1, headers=headers1).json()
#         number = test_db.T_DB.t_db(self)
#         payload = {"mobile": 17727475174, "verify_code": number}
#         response = requests.post(url=url2, data=payload, headers=headers1).json()
#         t = response['data']['access_token']
#         b = "bearer "
#         access_token = b + t
#         h = {
#             'Accept': 'application/json',
#             'Authorization': access_token,
#             "Access-Token": '17727475174'
#         }
#         print(h)
#         return h


class DefTool():
    #   用户多次操作
    def url(self, patch):
        baseUrl = 'http://k8s-qsj-test.jie.iask.cn/'  # 这个是测试服用户中心
        url = baseUrl + patch
        return url

    def defBaseParmsGetCode(self):
        headers = {
            "type": 2,
            "ver": "2.5.0",
            "verno": 13,
            "deviceId": "A0000087B98608",
            "deviceType": 1,
            "productId": 1003,
            "channelId": "anzhi",
            "deviceToken": "6418235f5d18aae5c7c6f1513f8c3839",
            "sign": "32f563c16c56a30694ff720b8e74a9c2"
        }
        return headers

    def defBaseParmsGetPassword(self):
            headers = {
                "ver": "2.5.0",
                "verno": 13,
                "deviceId": "A0000087B98608",
                "deviceType": 1,
                "productId": 1003,
                "channelId": "anzhi",
                "deviceToken": "6418235f5d18aae5c7c6f1513f8c3839",
                "sign": "32f563c16c56a30694ff720b8e74a9c2"
            }
            return headers

    def defaultHeaders(self):
        headers = {
            'Accept': 'application/json',
            "Authorization": "bearer ",
            "Access-Token": '',
            'Accept-Language': "cn",
            # "Content encoding": 'UTF-8'
        }
        return headers
