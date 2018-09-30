# import requests
# import unittest
#
# from db_fixture import test_db
#
#
# class TokenClass(unittest.TestCase):
#     # token = ""
#
#     def setUp(self):
#         self.headers = {'Accept': 'application/json'}
#         self.url = Url.url(self,'api/auth/login')
#
#     def getToken(self):
#         number = test_db.T_DB.t_db(self)
#         payload = {"mobile": 18127813600, "verify_code": number}
#         response = requests.post(url=self.url, data=payload, headers=self.headers).json()
#         # print(res)
#         t =response['data']['access_token']
#         b = "bearer "
#         access_token = b + t
#         return access_token
#
#     def test_getInfo(self):
#         # token =self.getToken()
#         headers = Headers.headers(self)
#         self.r = requests.post(url=self.url + '/auth/me', headers=headers)
#         print(self.r)
#
#     def tearDown(self):
#         pass
#
#     # def defHeader(self, heade={}):
#     #     access_token =
#     #     headers = {'Accept': 'application/json',
#     #                'Authorization': access_token}
#     #     # d3 = dict(headers.items(), heade.items())
#     #     print(headers, heade,)
#     #     return dict(headers, **heade)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# class Url():
#     def url(self, patch):
#         baseUrl = 'http://api.funcl.local/'
#         url = baseUrl + patch
#         return url
#
# class Headers():
#     def headers(self):
#         access_token = TokenClass.getToken(self)
#         headers = {
#             'Accept': 'application/json',
#             'Authorization': access_token
#         }
#         return headers
