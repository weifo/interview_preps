def spam():
    yield 45
    return 'generator'

s=spam()
next(s)