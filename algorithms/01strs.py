def sort(s):
    charlist=list(s)
    length=len(s)
    j=length-1
    answer=0
    for i in range(j):
        while(i<j and charlist[i]=='0'):
            i+=1
        while(i<j and charlist[j]=='1'):
            j-=1
        if i<j:
            answer+=1
            charlist[i],charlist[j]=charlist[j],charlist[i]
    print(f'交换次数为{answer}次')
    return ''.join(charlist)

s='001110110011'
print(sort(s))

