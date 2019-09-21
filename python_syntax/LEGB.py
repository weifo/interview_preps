'''
LEGB
local,enclosing,Global,bulit-in
'''
import builtins

x='global x'

def test(z):
    x='local x'
    print(z)
    global y
    y=123

# test('local z')

m=min([1,2,3,-92])
# print(dir(builtins))

def outer():
    x='outer x'

    def inner():
        nonlocal x
        x='inner x'
        print(x)
    
    inner()
    print(x)

outer()

(lambda x:print(x))(x)