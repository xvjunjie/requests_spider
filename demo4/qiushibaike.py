# -*- coding:utf-8 -*-
'''
    糗事百科 热门
'''
import json

import requests
from lxml import etree


class QiuShi():
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def get_url_list(self):
        return [self.start_url.format(i) for i in range(0, 14)]

    def parse_url(self, url):
        req = requests.get(url, headers=self.headers)
        return req.content.decode()

    def get_data(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")

        context_list = []
        for div in div_list:
            item = {}
            # 头像
            item["avatar_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["avatar_img"] = "https:" + item["avatar_img"][0] if len(item["avatar_img"]) > 0 else None

            # 昵称
            item["nickname"] = div.xpath("./a[2]/h2/text()")

            # 内容
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.replace("\n", "") for i in item["content"]]

            # 内容图片
            item["content_img"] = div.xpath(".//div[@class='thumb']//img/@scr")
            item["content_img"] = "https:" + item["content_img"][0] if len(item["content_img"]) else None

            context_list.append(item)
        return context_list

    def save_data(self, content_list):
        file_path = "糗事百科.txt"
        with open(file_path, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            content = self.parse_url(url)
            content_list = self.get_data(content)
            self.save_data(content_list)


if __name__ == '__main__':
    qiushi = QiuShi()
    qiushi.run()
