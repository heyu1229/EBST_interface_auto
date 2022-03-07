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
#---------------EBST 根据国家获取国家下的州/省/郡------------------------
class countries_provinces(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/countries/3388/provinces"

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        #消息体
        payload = {}
        result = requests.get ( self.Url, data=payload,headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()