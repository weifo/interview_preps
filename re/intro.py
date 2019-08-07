import re
'''
re.search() return 匹配对象或 None
re.findall() return a list 
re.split()
'''
t=open('../basic/re.txt')
for line in t:
    line=line.strip()
    # if line.find('expression')>=0:
    #     print(line)
    #     # break

    # if re.search('better',line):
    #     print(line)

r1=r'\w+'
r2='^F.+?'

ex1=re.findall(r1,'123+=-a456bcd78')
ex2=re.compile(r2).match('Fabcd')
# ex3=r1.match('1234')
res=re.search(re.compile('abc+'),'abccc')
print(res)
print(ex1,ex2.groups)