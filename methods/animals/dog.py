# What is an object?
# Definition 1: An object is an instance of a class
# Definition 2: An object is a variable that has data and behavior (and identity)
# Python's Definition: Any value.

# For our purposes, we're going to use definition 1

# Object-oriented programming. Very loosely, OOP is a way of programming
# that's centered around classes and objects.

# A class can have attributes. Attributes establish "has-a" relationships.
# Methods establish "can" relationships.

# This file represents the dog module
class Dog:
    name: str
    birth_year: int

    # A constructor is a very special method in a class that's automatically
    # called on a variable of that class the moment it's created. The purpose
    # of a constructor is to "set up" the variable.
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year

    # A method is basically just a function that's defined within a class
    def print(self) -> None:
        print(f'Dog\'s name: {self.name}')
        print(f'The dog was born in {self.birth_year}')

NUM_LEGS = 4
