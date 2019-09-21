# question
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 

def matrix():
    X,Y=input('enter two numbers please...').split(',')

    result=[[x*y for y in range(int(Y))] for x in range(int(X))]

    print(result)

matrix()

