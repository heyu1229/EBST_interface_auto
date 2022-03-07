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
#---------------EBST 文章列表页----------------------
class article_channels_articles(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/article-channel/articles"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        payload = {"per_page":"20","url":"E-Cigarette-ABC","page":"1"}

        result = requests.get ( self.Url, json=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()