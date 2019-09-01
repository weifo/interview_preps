import random
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health_level = random.random() 
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False
        
class PhysicianRobot(Robot):
    def say_hi(self):
        super().say_hi()
        print(self.name + " takes care of you!")
    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")

doc = PhysicianRobot("Dr. Moo")        
doc.say_hi()
rob_list = []
for i in range(5):
    x = Robot("Marvin" + str(i))
    if x.needs_a_doctor():
        print("health_level of " + x.name + " before healing: ", x.health_level)
        doc.heal(x)
        print("health_level of " + x.name + " after healing: ", x.health_level)
    rob_list.append((x.name, x.health_level))
    
# print(rob_list)