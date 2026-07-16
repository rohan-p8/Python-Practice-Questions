class Animals:

    def __init__(self, name):
        self.name = name
        print(f"Animal name: {self.name}")

class Pets(Animals):

    def __init__(self, name, belong):
        super().__init__(name)
        self.belong = belong
        print(f"Belong to: {self.belong}")

class Dog(Pets):

    def __init__(self, name, belong):
        super().__init__(name, belong)

    def bark(self):
        print(f"{self.name} is barking!")

p = Pets("Tokyo", "Pets family")
d = Dog("Motya", "Pets family")

d.bark()