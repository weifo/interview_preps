

l=[1,5,6,3,12,3,5,4,7,11,2,4,8,8,4,2,2,2,2,2]

def fun(l,k):
    seen=set()
    output=list()
    for num in l:
        target=k-num

        if target not in seen:
            seen.add(num)
        else:
            output.append((num,target))
            seen.discard(target)

    print(output)

fun(l,10)