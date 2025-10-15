import animals.cat

# This file represents the dog module
class Dog:
    name: str
    birth_year: int

def print_dog(dog: Dog) -> None:
    print(f'Dog\'s name: {dog.name}')
    print(f'The dog was born in {dog.birth_year}')

NUM_LEGS = 4
