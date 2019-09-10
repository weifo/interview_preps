# question
# input a num string that is seperated by comma,convert it into tuple and list restpectly

raw=input('enter you num string...')
raw_list=raw.split(',')

l=[int(x) for x in raw_list]
t=tuple(l)

print(l,t,sep='\n')