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
#---------------EBST 个人中心--取消订单----------------------
class member_orders_cancel(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/member/orders/20220615157782/cancel"


    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        #消息体
        payload = {"reason":"unpassed"}
        result = requests.post ( self.Url, json=payload,headers=headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 200, result['status_code'] )

if __name__ == '__main__':
    unittest.main()