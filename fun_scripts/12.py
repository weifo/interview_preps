# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def censor_input():
    with open('./files/filtered_words',encoding='utf-8') as f:
        words=[word.strip() for word in f.readlines()]

    data=input('type something here')
    for word in words:
        if word in data:
            data=data.replace(word,'**')
    print(data)

censor_input()