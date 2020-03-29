# Inheritance

class Cars:
    def __init__(self, tank_type, ac):
        self.wheels = 4
        self.tank_type = tank_type
        self.ac = ac


class Hatchback(Cars):
    def __init__(self, tank_type, ac):
        self.compartment = False
        super().__init__(tank_type, ac)

    def __str__(self):
        return f"A hatchback car with {self.wheels} wheels, {self.tank_type} tank and {self.ac} AC "


class Sedan(Cars):
    def __init__(self, tank_type, ac):
        self.compartment = True
        super().__init__(tank_type, ac)


car1 = Hatchback("Petrol", False)
print(car1)
