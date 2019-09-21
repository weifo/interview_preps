# MCD:greatest comon divisor
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

# lowest common multiple
def lcm(x,y):
    _mcd=gcd(x,y)
    return x*y//_mcd


print(lcm(47,60))
