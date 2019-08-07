# bubblesort
def bubblesort(list):
    l=list.copy()
    for iter_num in range(len(l)-1,0,-1):
        for idx in range(iter_num):
            if(l[idx]>l[idx+1]):
                l[idx],l[idx+1]=l[idx+1],l[idx]

    return l

data=[1,2,3,4,2,6,9,5,7,3,4]
# print(bubblesort(data))


def merge(a,b):
    # la,lb=len(a),len(b)
    # print(a,b)
    x,ia,ib=0,0,0
    sl=[]
    while a or b:
        if a==[]:
            sl.extend(b)
            return sl
        elif b==[]:
            sl.extend(a)
            return sl
        elif a[0]<b[0]:
            sl.append(a.pop(0))
        else:
            sl.append(b.pop(0))
    
    return sl

def merge_sort(list):
    l=list
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=merge_sort(l[:mid])
    right=merge_sort(l[mid:])

    return merge(left,right)

print(merge_sort(data))
