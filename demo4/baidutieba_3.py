# -*- coding:utf-8 -*-

from lxml import etree
import requests


class TiebaSpider():
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=" + self.tieba_name + "&pn={}"
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse_url(self, url):
        '''获取页面内容'''
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_content_list(self, html_str):
        '''提取页面数据'''
        print(html_str)

        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class,'i')]")  # 提取div列表进行分组

        content_list = []
        for div in div_list:
            item = {}
            # 获取贴吧标题
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            # 获取标题对应的详情地址
            item["href"] = self.part_url + div.xpath(".a/@href")[0] if len(div.xpath("./a/@href")) > 0 else None

            item["img_list"] = self.get_img_list(item["href"], [])

            content_list.append(item)
            print(content_list)

    def get_img_list(self, detail_url, total_img_list):
        '''获取'''
        detail_htlm_str = self.part_url(detail_url)
        detail_html = etree.HTML(detail_htlm_str)

        img_list = detail_html.xpath("img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)
        print(total_img_list)

        return total_img_list

    def run(self):
        # 1.获取页面返回的内容html
        # 2.传给etree.Html(html)
        # 3.使用xpath获取要抓取的字段数据

        html_str = self.parse_url(self.url_temp)
        content_list = self.get_content_list(html_str)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("世界杯")
    tieba_spider.run()
