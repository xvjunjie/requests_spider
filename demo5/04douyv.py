# -*- coding:utf-8 -*-
import time
from selenium import webdriver

'''
    斗鱼房间信息
    
'''


class DouYvspider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.PhantomJS()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")

        content_list = []
        for li in li_list:
            item = {}
            item["img"] = li.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            item["title"] = li.find_element_by_xpath("./a").get_attribute("title")
            item["anchor_name"] = li.find_element_by_xpath(".//span[@class='dy-name ellipsis fl']").text
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            content_list.append(item)

        # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url) > 0 else None

        print(content_list)

        return content_list, next_url


    def save_content(self, content_list):

        pass

    def run(self):
        self.driver.get(self.start_url)
        content_list, next_url = self.get_content_list()
        self.save_content(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyv = DouYvspider()
    douyv.run()
