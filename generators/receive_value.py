def receiver():
    while True:
        item=yield
        print('Got',item)

recv=receiver()
# next(recv)

recv.send('Hello')
recv.send('Weifo')