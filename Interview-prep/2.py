# multilevel inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Fish(Dog):
    def swim(self):
        print("Swimming")

fish = Fish()

fish.eat()
fish.bark()
fish.swim()
