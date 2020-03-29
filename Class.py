# Working with classes

# class Monkey:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def a_class_method(cls):
#         return cls(2, 5)
#
#     def left(self):
#         print("Yaha se left")
#         print(self.x, self.y)
#
#     def right(self):
#         print("Yaha se right, mere dost")
#
#
# pappu = Monkey.a_class_method()
# pappu.left()

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"Hi, my name is {self.name}. I'm {self.color} colored with a weight of {self.weight}")


r1 = Robot("Jerry", "blue", 50)
r2 = Robot("Tom", "red", 40)
r1.introduce_self()
r2.introduce_self()


class Person:
    default_color = "red"

    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

print(p1.isSitting)
print(p2.isSitting)

print("Class method of making everyone sit begins..")

Person.stand_up()
print(p2.isSitting, p1.isSitting)

#
# p1.robot_owned = r2
# p2.robot_owned = r1
#
# r1.name = "Himakat Ali"
#
# print(p1.robot_owned.name, p2.robot_owned.name)
