# 第 0009 题： 一个HTML文件，找出里面的链接。
from lxml import etree

html=etree.parse('./files/网易云音乐.html',etree.HTMLParser())

anchors=html.xpath('//a')
print(len(anchors))