import math
def add(x,y):
    return x+y

def divide(x,y):
    return x/y

def power(x,y):
    # return math.pow(x,y)
    if y==0:
        raise  ValueError
    return x**y

def cos(x):
    x=math.radians(x)
    return math.cos(x)