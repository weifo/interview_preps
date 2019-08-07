# recursion usage
def cusum(l):
    return 0 if not l else  l[0] + cusum(l[1:])

# print(cusum([1,3,4,5,6,9,8]))

def rec_tree(L):
    tot=0
    for x in L:
        if not isinstance(x,list):
            tot+=x
        else:
            tot+=rec_tree(x)
    return tot

tree=[1,3,4,[8,9,4,[2,5,8,[3,2],1,1],1,2],1,3]
# print(rec_tree(tree))

def iter_tree(L):
    tot=0
    while L:
        cur=L.pop(0)
        if isinstance(cur,list):
            tot+=iter_tree(cur)
        else:
            tot+=cur
    return tot

print(iter_tree(tree))

