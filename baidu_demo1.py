# -*- coding:utf-8 -*-
import requests

url_temp = "https://www.baidu.com/s"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
p = {"wd": "知乎"}

response = requests.get(url_temp, headers=headers, params=p)
context = response.content.decode()
print(context)
