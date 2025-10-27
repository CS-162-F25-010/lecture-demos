from copy import deepcopy

class Person:
    name: str

def main() -> None:
    jane = Person()
    jane.name = 'Jane'

    sally = deepcopy(jane)
    print(sally.name)

    sally.name = 'Sally'
    print(sally.name) # Prints Sally
    print(jane.name) # Prints Jane

if __name__ == '__main__':
    main()
