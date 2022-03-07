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
#---------------EBST 注册----------------------
class register(unittest.TestCase):

    def setUp(self):

        self.Url = Url().test_url()+"/coreapi/account/register"
        self.headers = Headers().test_get_headers()

    def testcase_001(self):
        timenow =str(int(time.time()))
        #消息体
        payload = {"login_name": "lisa"+timenow,
                    "display_name": "lisa20220617",
                    "email": timenow+"@qq.com",
                    "password_shadow": "Heyu123456",
                    "password_shadow_repeat": "Heyu123456",
                    "password_hint": "",
                    "business_type": 1,
                    "company_name": "dddddddddd",
                    "business_license": "members/202206/1655431322_13882.jpg",
                    "monthly_purchase": 1,
                    "phone": "18888052583",
                    "skype_id": "",
                    "whatsapp_name": "",
                    "country_id": 3341,
                    "province": "2222222",
                    "province_id": "",
                    "captcha": "coreapi",
                    "captcha_key": "$2y$10$p7j.Hr2Hc0MCRna0MsMSteNHm1xWV2401iHNb3Ps8l9dV7/O9A8f.",
                    "request_reseller": "false",
                    "description": "",
                    "individual_name": "",
                    "company_website": "",
                    "city": "222222",
                    "street": "22222222",
                    "post_code": "222222222222",
                    "id_card": "",
                    "license_file_name": "12.jpg",
                    "id_file_name": "",
                    "contact_person": "22222222"
                   }

        result = requests.post( self.Url, json=payload,headers=self.headers )
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()