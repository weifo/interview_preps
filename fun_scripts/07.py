# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
# 包括空行和注释，但是要分别列出来。
import glob,os
os.chdir('../weifo_blog')

files=glob.glob("*.py")
result={
    'code':0,
    'empty':0,
    'comment':0
}

for file in files:
    lines=open(file,encoding='utf-8').readlines()
    for line in lines:
        if line.startswith('#'):
            result['comment']+=1
        elif line.strip()=='':
            result['empty']+=1
        else:
            result['code']+=1
    print('summary:\n {code} lines code \n {empty} lines empty \n {comment} lines comment \n {name}'.
        format(**result,name=file)) 
print(len(files))
# for file in glob.glob("*.py")
