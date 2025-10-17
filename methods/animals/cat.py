# This file represents the cat module
class Cat:
    name: str
    birth_year: int

def print_cat(cat: Cat) -> None:
    print(f'Cat\'s name: {cat.name}')
    print(f'The cat was born in {cat.birth_year}')

NUM_LEGS = 4
