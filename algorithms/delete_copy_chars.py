'''
in a str ,if char is 'a',delete it
          if char is 'b',copy it
'''
def func(s):
    charlist=list(s)
    n,numb=0,0
    for i in range(len(charlist)):
        if charlist[i] !='a':
            charlist[n]=charlist[i]
            n+=1
        if charlist[i]=='b':
            numb+=1
    charlist=charlist[0:n]
    j,k=len(charlist)+numb-1,len(charlist)-1
    result=[None]*(j+1)

    while(k>=0):
        result[j]=charlist[k]
        j-=1
        if charlist[k]=='b':
            result[j]='b'
            j-=1
        k-=1

    return ''.join(result)

    # return s.replace('a','').replace('b','bb')

s='abbcdahafbdab'
print(func(s))


