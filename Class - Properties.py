class Dogs:
    def __init__(self, breed, age):
        self.__breed = breed
        self.age = age

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        self.__breed = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    age_property = property(get_age, set_age)


pup1 = Dogs("Labrador", 2)

pup1.age_property = 66

print(pup1.age_property)

print(pup1.breed)
