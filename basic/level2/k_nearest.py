import math
points=[[1,3],[2,5],[4,8],[-1,-2],[2,0],[1,1],[2,1],[2,2]]
vertex=[2,2]
k=3

def find_points(points,vertex,k):
    fn=lambda p1,p2:math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    # fn=lambda p1,p2:math.sqrt(sum([(a-b)**2] for a,b in zip(p1,p2)))

    dis_list,result=[],[]
    for p in points:
        dis_list.append(round(fn(p,vertex),5))
    dis_sorted=sorted(dis_list)
    for i in range(k):
        idx=dis_list.index(dis_sorted[i])
        result.append(points[idx])
    return result

# res=find_points(points,vertex,k)

def methond2(points,K):
    fn=lambda p1:(p1[0]-vertex[0])**2+(p1[1]-vertex[1])**2

    points=sorted(points,key=fn)
    return points[:K]

res=methond2(points,k)
print(res)
print(points)

    