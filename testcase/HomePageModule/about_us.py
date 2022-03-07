'''
@create : lisa
@file :EBST
@Date :2022/2/15
@desc :

'''

# -*- coding:UTF-8 -*-
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
from public.get_token import Token
from public.get_url import Url
from public.get_headers import Headers
#---------------EBST 关于我们 ----------------------
class about_us(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/index/about-us"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        # print(token)
        payload = {}

        result = requests.get ( self.Url, json=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()