# -*- coding:utf-8 -*-
import requests
from selenium import webdriver
from utils.yundama.dama import indetify

'''
登录豆瓣
'''

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get("https://www.douban.com/")
    driver.find_element_by_id("form_email").send_keys("784542623@qq.com")
    driver.find_element_by_id("form_password").send_keys("zhoudawei123")

    # 识别验证码

    captcha_img = driver.find_element_by_id("captcha_image").get_attribute("src")
    content = requests.get(captcha_img).content
    code  = indetify(content)


    #输入验证码
    driver.find_element_by_id("captcha_field").send_keys(code)
    driver.find_element_by_class_name("bn-submit").click()

