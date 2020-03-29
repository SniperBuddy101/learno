# Working with class methods

class Humans:
    def __init__(self, number1, number2):
        self.body = {}
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return f"{(self.number1, self.number2)}"

    def __getitem__(self, body_part):
        return self.body.get(body_part, 0)

    def __setitem__(self, body_part, value):
        self.body[body_part] = value

    def __add__(self, other):
        return (self.number1 + other.number1, self.number2 + other.number2)

    def __gt__(self, other):
        return (self.number1 > other.number1) and (self.number2 > other.number2)


h1 = Humans(20, 70)
h2 = Humans(60, 80)
print(h1 + h2)
print(h2 > h1)
