'''
@create : lisa
@file :login.py
@Date :2022/6/10
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
#---------------EBST 登录----------------------
class login(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/auth/login"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):

        #消息体
        payload = {"username": "eva_zhang","password":"123456","captcha":"coreapi",}

        result = requests.post( self.Url, data=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()