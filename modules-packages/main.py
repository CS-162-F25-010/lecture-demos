#import dog as d
#from dog import Dog, print_dog as pdog

#import animals.dog as d

import animals

import animals.cat as kitty
from animals.dog import Dog, print_dog as pdog

def main() -> None:
    spot = Dog()
    spot.name = 'Spot'
    spot.birth_year = 1999

    pdog(spot)
    animals.print_dog(spot)
    
    princess = kitty.Cat()
    princess.name = 'Princess'
    princess.birth_year = 1999

    kitty.print_cat(princess)


if __name__ == '__main__':
    main()
