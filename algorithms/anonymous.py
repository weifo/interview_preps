def gets():
    cmds=input().split('\n')
    print(cmds)
    init=cmds[0]
    num=int(cmds[1])
    
    for i in range(2,2+num):
        h,l=map(int,cmds[i].split(' '))
        t=h+l
        frag=init[h,t]
        init+=str(reversed(frag))
    return init

gets()