'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
'''
class noname:
    def get_str(self):
        info=input('type something please..')
        self.msg=info
    def show_str(self):
        print(self.msg.upper())

n1=noname()
n1.get_str()
n1.show_str()