# -*- coding:utf-8 -*-

from PIL import Image
import pytesseract

file_path = "/home/python/Desktop/Projects/requests_spider/imgs/c.jpg"

img = Image.open(file_path)
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)
