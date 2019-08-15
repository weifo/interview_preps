'''
  find the largest  continuous sum of a list
  the element can be negative or positive
'''
def sum(l):
    if len(l)==0:
        return 'too short'
    
    max_sum=current_sum=l[0]

    for num in l[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(max_sum,current_sum)
        print(max_sum)

    return max_sum

l=[-13,-8,2,4,-2,-4,7,-10,7,3,-1]
print(sum(l))