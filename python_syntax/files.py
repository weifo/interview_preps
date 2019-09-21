# 1 read file
with open('focus.txt','r+') as f:
    # for line in f.readlines():
    #     print(line)
    # print(f.read())

    # for line in f:
    #     print(line,end='')
    
    print(f.read(40))
    # set read position
    f.seek(0)
    print(f.read(10))


# write
with open('focus.txt','r') as rf:
    with open('test.txt','w') as wf:
        for line in rf:
            wf.write(line)
