# -*- coding:utf-8 -*-
import requests


class TiebaSpider():
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=" + self.tieba_name + "&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse_url(self, url):
        '''获取页面内容'''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self):
        '''提取页面数据'''




    def get_url_list(self):
        '''获取'''



    def run(self):
        content = self.parse_url(self.url_temp)




if __name__ == '__main__':
    tieba_spider = TiebaSpider("世界杯")
    tieba_spider.run()
