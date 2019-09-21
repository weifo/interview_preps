'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50, H is 30
D is the variable whose
values should be input to your program in a comma-separated sequence.
'''
import math
def calculate():
    raw_list=input('enter nums please...').split(',')
    data=[int(x) for x in raw_list]
    fn=lambda x:math.sqrt(2*50*x/30)

    result=[fn(x) for x in data]
    print(result)

calculate()


