# With a given integral number n, write a program to generate a dictionary whose key-value is i-->i*i 

def some_dict():
    num=int(input('give a num that you like...'))
    dict1={}
    for n in range(1,num+1):
        dict1[n]=n*n
    print(dict1.items())
    return dict1

some_dict()
