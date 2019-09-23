'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
则打印出 Freedom，否则打印出原数据。

程序员
码农
牛比
牛逼
草
屌丝
sex
'''
def check_user_input():
    with open('./files/filtered_words',encoding='utf-8') as f:
        words=[word.strip() for word in f.readlines()]
    
    data=input('type in something>> ')
    if any([True for word in words if word in data]):
        # [word in data for word in words]
        print('Freedom')
    else:
        print('your data >> ',data)


check_user_input()