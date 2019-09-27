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
driver.get('https://music.163.com/')
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
elem=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[1]/ul/li[1]/p/a')
# code=etree.HTML(driver.page_source)
# print(driver.page_source)
# with open('test.html','w',encoding='utf-8') as f:
#     f.write(driver.page_source)

# lis=code.xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li[1]')
# print(len(lis))
def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

imgs=driver.find_elements_by_xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li/div/img')
# text=get_text_excluding_children(driver,elem)
print(elem.text)
for img in imgs:
    print(img.get_attribute('src'))

