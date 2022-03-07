'''
@create : lisa
@file :article_privacy_policy.py
@Date :2022/6/9
@desc :

'''
'''
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
from public.get_token import Token
from public.get_url import Url
from public.get_headers import Headers
#---------------EBST 保存修改密码(security)-----------------------
class member_security(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/member/security"

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        #消息体
        payload = {"old_password":"123456","new_password":"Heyu123456","rep_password":"Heyu123456"}
        result = requests.post ( self.Url, json=payload,headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()
'''