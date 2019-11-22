def sort(data):
    l=len(data)
    for i in range(l-1):
        for j in range(l-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    print(data)
    return data

test=[
    [3,2,1,8,5],
    [10,2,6,4,8],
    [3,5,4,12,5]
]
for l in test:
    sort(l)

