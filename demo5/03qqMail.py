# -*- coding:utf-8 -*-
from selenium import webdriver
import time

"""
包含iframe  ， frame的要切换

"""


driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")

#切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("12312312312")


time.sleep(3)
driver.quit()