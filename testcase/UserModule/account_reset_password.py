'''
@create : lisa
@file :article_privacy_policy.py
@Date :2022/6/9
@desc :

'''
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
from public.get_token import Token
from public.get_url import Url
from public.get_headers import Headers
#---------------EBST 重置密码保存------------------------
class account_reset_password(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/account/reset-password"

    def testcase_001(self):
        #获取token
        # token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers()

        #消息体
        payload = {
            "code": "7f01cb04e67f23b09458fcd0511af1b1",
            "password_shadow": "123456"
        }
        result = requests.get ( self.Url, json=payload,headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()