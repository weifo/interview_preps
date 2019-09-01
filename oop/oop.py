class Robot:
    __counter = 0
    
    def __init__(self,name='Robot'):
        self.name=name
        type(self).__counter += 1
        
    def hi(self):
        print(f'hi,I am {self.name}',self)

    @staticmethod
    def RobotInstances():
        return Robot.__counter

    @classmethod
    def some_class_func(f):
        return f
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(y.RobotInstances())
    print(Robot.RobotInstances())
    print(Robot.some_class_func())
    x.hi()