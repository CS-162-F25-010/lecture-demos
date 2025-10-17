from animals.dog import Dog
from animals.cat import Cat, print_cat

def main() -> None:
    spot = Dog('Spot', 1999) # This is actually a constructor call
    #spot.name = 'Spot'
    #spot.birth_year = 1999

    spot.print()

    fluffy = Dog('Fluffy', 2017)
    
    fluffy.print()
    
    princess = Cat()
    princess.name = 'Princess'
    princess.birth_year = 1999

    print_cat(princess)


if __name__ == '__main__':
    main()
