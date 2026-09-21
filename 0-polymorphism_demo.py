#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(dog.speak)
print(cat.speak)
