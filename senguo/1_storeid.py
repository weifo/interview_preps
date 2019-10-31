def verify_num(id):
    skip=[3,4,7]
    for num in skip:
        if str(num) in str(id):
            return False
    return True


def storeid():
    for i in range(100000000):
        if verify_num(i):
            yield str(i).zfill(8)


# 2 一共有 5764801 个id符合要求
def count():
    num=0
    for i in range(100000000):
        if verify_num(i):
            num+=1
    return num

print(f'一共有{count()}个可用id')

gen_id=storeid()
for i in range(50):
    print(next(gen_id))