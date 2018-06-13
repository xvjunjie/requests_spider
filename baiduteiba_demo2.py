# -*- coding:utf-8 -*-
import requests
# https://tieba.baidu.com/f?kw=世界杯&ie=utf-8&pn=50


class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def get_url_list(self):
        '''构造url'''
        return [self.url_temp.format(i*50) for i in range(50)]

    def request_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def run(self):
        #构造url
        url_list = self.get_url_list()
        # 根据url请求
        for url in url_list:
            content  = self.request_url(url)





