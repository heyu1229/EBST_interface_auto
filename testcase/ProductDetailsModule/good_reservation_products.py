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

#---------------EBST  商品详情页  ----------------------
class index_about_us(unittest.TestCase):

    def setUp(self):

        # 文档相关接口：http://beta-api.elfbar.com/member/reservation-products

        # 实际地址：https://beta-store.elfbar.com/coreapi/member/reservation-products

        self.Url = Url().test_url()+"/coreapi/member/reservation-products"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)
        # print(token)
        items = [
            {"product_bn" : "110104331450000","quantity": "2"},
            {"product_bn" : "110104331451000","quantity": "1"}
        ]
        payload = {"items":items}
        result = requests.post( self.Url, data=json.dumps(payload),headers=headers)#或者直接json=payload
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()