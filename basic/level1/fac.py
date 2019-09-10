# question
# Write a program which can compute the factorial of a given number.

def facnum():
    try:
        receive_num=int(input())
        if receive_num<=0:
            raise ValueError('This num should be positive')
        else:
            result=1
            for num in range(2,receive_num+1):
                result*=num
            print(result)
    except Exception as e:
        print(e)

facnum()