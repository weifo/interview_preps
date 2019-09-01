class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()

d1=Dog()
print(d1._class_info,Pet._class_info,sep=' , ')
Pet._class_info='info has been changed'
print(Pet._class_info)