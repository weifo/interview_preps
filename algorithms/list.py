import sys
list1=[12,15,19,21,4,6]
l2=list1[3:5]
# l2[0]=12
print(list1,l2)
# print('size of two lists are {} and {}'.format(sys.getsizeof(list1),sys.getsizeof(l2)))
n=12
l=[]
for i in range(n):
    a=len(l)
    b=sys.getsizeof(l)

    print('the length is {0:3d},the bytes are {1:4d}'.format(a,b))
    l.append(i)