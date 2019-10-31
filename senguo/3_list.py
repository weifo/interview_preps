def make_list(num):
    result_list=[num]
    while num>1:
        if num%2==0:
            result_list.insert(0,num//2)
            num//=2
        else:
            result_list[0:0]=[num//2,num//2+1]
            num//=2
    return len(result_list)


res=make_list(111)
print(res)


