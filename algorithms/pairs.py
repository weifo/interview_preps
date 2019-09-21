def find_match(data,target):
    map={}

    for num in data:
        other=target-num
        if other in map:
            return other,num
        else:
            map[num]=True
    return 'no match!'

l1=[1,3,5,6,8,12]
l2=[5]
print(find_match(l1,20))
print(find_match(l2,10))