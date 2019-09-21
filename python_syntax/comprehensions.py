raw=[1,3,4,5,7,9,12,24]

# map usage
list1=[n-2 for n in raw]

list2=map(lambda x: x+2,raw)

# filter usage
list1=[n for n in raw if n %2==0]

list2=filter(lambda x: x%2==0,raw)
# print(list1,list(list2))

my_list=[(letter,num) for letter in 'abcd' for num in range(4)]

# dictionary comprehension
cities=['wuhu','hefei','jinan','nanchang','xuzhou']
provinces=['anhui','anhui','shandong','jiangxi','jiangsu']

my_dict={}
for city,pro in zip(cities, provinces):
    my_dict[pro]=city

my_dict={pro:city for pro,city in zip(provinces,cities)}

# set comprehension
my_set={n for n in raw}

# generator comprehension
def gen_func(nums):
    for n in nums:
        yield  n*n
my_gen=gen_func(raw)

my_gen=(n*n for n in raw)

for i in my_gen:
    print(i)
# print(my_set)
