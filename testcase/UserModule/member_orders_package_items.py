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
#---------------EBST 个人中心--获取单个订单单个包裹明细----------------------
class member_orders_package_items(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/member/orders/20220429106786/package/items"


    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        #消息体
        payload = {"logistic_no":"1234567890"}
        result = requests.get ( self.Url, json=payload,headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()