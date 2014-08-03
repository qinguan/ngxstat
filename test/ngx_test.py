__author__ = 'xuguojun'

import unittest


class MyTestCase(unittest.TestCase):
    def test_ngx_regex(self):
        from ngx_regex import LOG_PATTEN
        import re

        str1='60.9.11.168 - - [02/Aug/2014:12:20:54 +0800] ' \
             '"GET /apis/msg/hasnew.action?count=5&agent_type=1&callback=window.Q.__callbacks__.cbkc79h1 ' \
             'HTTP/1.1" 200 101 "http://so.iqiyi.com/so/q_%E4%B8%AD%E5%9B%BD%E5%A5%BD%E5%A3%B0%E9%9F%B3?source=suggest&r=1278964811233" ' \
             '"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)" "-" 865 0.001 0.001 10.153.74.212:8080'
        str2='10.15.177.149 - - [02/Aug/2014:12:20:48 +0800] ' \
             '"GET /apis/msg/send_ugc_recommend.action?device_id=152f46d48b8a45e795dd9388c45e9b81&related_uid=243977833&agent_type=1 ' \
             'HTTP/1.1" 200 28 "-" "Java/1.7.0_09" "-" 315 0.0035 0.005 10.153.74.203:8080'
        str3='10.15.177.149 - - [02/Aug/2014:12:20:48 +0800] ' \
             '"GET /apis/msg/send_ugc_recommend.action?device_id=152f46d48b8a45e795dd9388c45e9b81&related_uid=243977833&agent_type=1 ' \
             'HTTP/1.1" 200 28 "-" "Java/1.7.0_09" "-" 315 0.005 0.005 10.153.74.203:8080'

        self.assertIsNotNone(re.search(LOG_PATTEN, str1), "ngx_regex_test_1 failed")
        self.assertIsNotNone(re.search(LOG_PATTEN, str2), "ngx_regex_test_2 failed")
        self.assertIsNotNone(re.search(LOG_PATTEN, str3), "ngx_regex_test_3 failed")

        self.assertEqual(len(re.search(LOG_PATTEN, str1).groups()), 13, "ngx_regex_test_4 number is not matching.")


if __name__ == '__main__':
    unittest.main()
