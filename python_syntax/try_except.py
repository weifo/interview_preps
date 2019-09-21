try:
    f=open('test.txt')
    if f.name=='test.txt':
        raise ValueError
    # var=not_define
    # var=13/0
except FileNotFoundError as e:
    print(e)
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('can not divided by zero')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

finally:
    print('I have to print this before exit')
