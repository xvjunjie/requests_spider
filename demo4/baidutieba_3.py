# -*- coding:utf-8 -*-
import json

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

        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class,'i')]")  # 提取div列表进行分组

        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            item["href"] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")) > 0 else None

            item["img_list"] = self.get_img_list(item["href"], [])
            item["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in item["img_list"]]
            content_list.append(item)

        next_url = self.part_url+html.xpath("//a[text()='下一页']/@href")[0]  if len(html.xpath("//a[text()='下一页']/@href"))>0 else None

        return content_list, next_url

    def get_img_list(self, detail_url, total_img_list):
        '''获取'''
        # 3.2请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)

        # 3.3提取详情页第一页的图片，提取下一页的地址
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)

        # 3.4请求详情页下一页的地址，进入循环3.2-3.4
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url) > 0:
            detail_next_url = self.part_url + detail_next_url[0]
            return self.get_img_list(detail_next_url, total_img_list)

        return total_img_list


    def save_content_list(self,content_list):
        file_path = self.tieba_name+".txt"
        with open(file_path,"a",encoding="utf-8") as f :
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
        print("保存成功")




    def run(self):
        # 1.获取页面返回的内容html
        # 2.传给etree.Html(html)
        # 3.使用xpath获取要抓取的字段数据

        html_str = self.parse_url(self.url_temp)
        content_list = self.get_content_list(html_str)
        self.save_content_list(content_list)

if __name__ == '__main__':
    tieba_spider = TiebaSpider("世界杯")
    tieba_spider.run()
