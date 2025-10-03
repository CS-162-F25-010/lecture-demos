# Importing an entire module or package
# import math

# Importing a small number of things from a module or package
from math import sqrt, pi

def main() -> None:
    # The period (.) is referred to as the dot operator
    #print(math.sqrt(25))
    #print(math.pi)
    print(sqrt(25))
    print(pi)

if __name__ == '__main__':
    main()
