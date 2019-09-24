# 第 0013 题： 用 Python 写一个爬图片的程序
from lxml import etree
import time
# import requests
# try:
#     r=requests.get('https://music.163.com')
# except Exception as e:
#     print(e)
# else:
#     if r.status_code==200:
#         html=etree.HTML(r.text)
#         lis=html.xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li[1]')
#         print(len(lis))
#         print('okkkk')
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://music.163.com')
time.sleep(5)
code=etree.HTML(driver.page_source)
lis=code.xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li[1]')
print(len(lis))

