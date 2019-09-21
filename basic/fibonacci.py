# two ways to generate a fibonacci squence
def gen_fib(n):
    if n<=1:
        return n
    else:
        return gen_fib(n-1)+gen_fib(n-2)

# print(gen_fib(12))

def fib(max):
    a,b=0,1
    n=0
    while n<max:
        yield b
        a,b=b,a+b
        n+=1

# gen=fib(20)
# for i in range(10):
#     cur=gen.__next__()
# else:
#     print(cur)
gen=fib(5)
for i in gen:
    print(i,end=' , ')