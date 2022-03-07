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

#---------------EBST  购物车添加  ----------------------
class cart_add(unittest.TestCase):

    def setUp(self):
        self.Url = Url().test_url()+"/coreapi/cart/add"

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)
        # print(token)
        items = [
            {"product_id" : "2916","type": "normal","quantity":"1","checked":"true"}
        ]
        payload = {"items":items,"page":"cart"}
        result = requests.post( self.Url, data=json.dumps(payload),headers=headers)#或者直接json=payload
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()