# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
# 找出出现次数最多的5个词
word_num={}
with open('README.md') as f:
    txt=f.read()
    for word in txt.split(' '):
        if word in word_num:
            word_num[word]+=1
        else:
            word_num[word]=1

word_map=word_num.items()
sorted_map=sorted(word_map,key=lambda word: word[1],reverse=1)

sorted_dict=dict(sorted_map)
print(sorted_map[:5])
