from sled import Sled
from dog import Dog
from husky import Husky

def main() -> None:
    spot = Dog('Jeff', 'Spot')
    spot.vocalize()
    spot.print()

    fluffy = Husky('Jill', 'Fluffy')
    # When you call vocalize() on a Husky, by default, it calls
    # the Husky class's vocalize() method (this calls the override)
    fluffy.vocalize()
    fluffy.print()

    santas_sleigh = Sled()
    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)
    print(f'The sled has traveled {santas_sleigh.distance_traveled} miles')
    
    # spot.pull_sled(santas_sleigh) # This is a syntax error

if __name__ == '__main__':
    main()
