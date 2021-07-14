## Clases y objetos

class Robot:
    def __init__(self, name, color, weight):    ##constructor
        self.name = name
        self.color = color
        self.weight = weight
        
    def introduce_self(self):
        print("My name is "+ self.name) # this is in Java
"""
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30
r1.introduce_self()

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40
r2.introduce_self()
"""
r1 = Robot("Tom", "red", 30)        ## clean code is better
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, n, p, i):    ##constructor
        self.name = n
        self.personality = p
        self.is_sitting = i
        
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)        ## clean code is better
p2 = Person("Becky", "talkative", True)

## p1 owns r2

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()


r1.introduce_self()
r2.introduce_self()
