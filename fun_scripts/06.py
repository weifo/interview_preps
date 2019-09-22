# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，
# 请统计出你认为每篇日记最重要的词。
import glob
import os
def count_word(article):
    word_map={}
    word_list=article.split()
    for word in word_list:
        if word not in word_map:
            word_map[word]=1
        else:
            word_map[word]+=1
    sorted_map=sorted(word_map.items(),key=lambda x:x[1],reverse=True)
    result=filter(lambda x: x[0] not in ['a','of','the','and','is'],sorted_map[:10])
    return list(result)[0]
    
    

def find_the_word(directary):
    files=glob.glob(directary)
    for file in files:
        with open(file) as f:
            result=count_word(f.read())
            print('in {},the highlight word is {}'.format(f.name,result[0]))

find_the_word('./files/*')