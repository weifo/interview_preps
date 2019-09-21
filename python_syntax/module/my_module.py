print('importing my_module')

def find_index(to_search,target):

    for i,value in enumerate(to_search):
        '''find the index of a value in a sequence'''
        if value==target:
            return i
    return -1

square=[x**2 for x in [2,3,4,5,6,7,8,9] if x%2==0 ]
