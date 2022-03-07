'''
@create : lisa
@file :FAQ.py
@Date :2022/6/9
@desc :

'''
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
#---------------EBST FAQ----------------------
class FAQ(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/article/FAQ"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):
        #获取token
        token = Token().test_token ()

        payload = {"_gid": "GA1.2.474372163.1654678980","_ga":"GA1.2.2049571130.1654678969","_ga_8G02ZXM69R":"GS1.1.1654678969.1.1.1654680280.0",
                   "currency_code":"USD","PHPSESSID":"WBnWTaph261T76cUp8o1h7lajooyNHI8YF2FShos","R-18":"ebst.com"}

        result = requests.get ( self.Url, data=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()