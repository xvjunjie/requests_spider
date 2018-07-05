# -*- coding:utf-8 -*-
import json
import sys

import requests

'''
    带请求参数
'''

query_string = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

post_data = {
    "query": query_string,
    "from": "zh",
    "to": "en",
}

post_url = "http://fanyi.baidu.com/basetrans"
resp = requests.post(post_url, data=post_data, headers=headers)
dict_ret = json.loads(resp.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is :", ret)
