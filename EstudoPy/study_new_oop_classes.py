from time import *


class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    def _my_private_hello(self):
        return print("My private Hello")

    def my_public_hello(self):
        return print("My public Hello")

    # No need to instantiate a variable, use the class it self instead.
    @classmethod
    def num_dogs(cls):
        return print(len(cls.dogs))

    @staticmethod
    def bark(n):
        for _ in range(n):
            print("Bark")


Tim = Dog("Tim")
Fim = Dog("Fim")
Jim = Dog("Jim")
# print(Dog.num_dogs())
# t = Tim.num_dogs()
# print(t)
Dog.num_dogs()

# print(Dog.num_dogs())


# Tim.my_public_hello()
# Tim._my_private_hello()
