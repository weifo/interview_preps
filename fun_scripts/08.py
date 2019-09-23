# 第 0008 题： 一个HTML文件，找出里面的正文。
from lxml import etree

html=etree.parse('./files/网易云音乐.html',etree.HTMLParser())
body=html.xpath('//body')
print(etree.tostring(body[0]))