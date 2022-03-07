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
#---------------EBST 首页轮播图 ----------------------
class scroll_banners(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/index/scroll-banners"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):
        timestamp = str(int(time.time()))
        #获取token
        token = Token().test_token ()
        # print(token)
        payload = {"token": token,"R-18":timestamp,"PHPSESSID":"YAFF6PcHh2B4lJ7XPZZI4OKm4OvBIjCavWnvI32V","product-viewed":"280%2C5434%2C5409%2C3632%2C5426%2C4471%2C981%2C5432%2C2580%2C5428",
                    "_atuvc":"1%7C6","_ga":"GA1.2.1697023960.1637747204","_ga_8G02ZXM69R":"GS1.1.1644543548.19.0.1644543548.0","currency_code":"USD"}

        result = requests.get ( self.Url, data=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()