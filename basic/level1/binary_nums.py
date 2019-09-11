# 
def check_bi():
    raw_list=input('enter some binary strings...').split(',')
    # intnums=[int(x,2) for x in raw_list]
    
    result=filter(lambda x: int(x,2)%5==0,raw_list)
    print(*result,sep=',')

check_bi()
