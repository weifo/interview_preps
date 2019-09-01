l1=[1,3,5,7]
# []
print(l1[10:])

def pass_val(someval=None):
    if someval is None:
        someval=[]
    else:
        someval=someval.copy()
    someval.append(15)
    return someval

res=pass_val()
print(res)

res=list(filter(lambda x:x%2,[15,7,8,12,16]))
print(res)