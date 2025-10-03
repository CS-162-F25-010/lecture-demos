# Python does not have constants
# However, it has a convention. If you want a variable to never be changed,
# name it in ALL_CAPS

# Global constants are fine.
# PI = 3.1415

def main() -> None:
    # This is a single-line comment

    # Expressions: Pieces of code with types and values

    # Primitive types in Python:
    # int (integer). 12
    # float (floating point number, typically 64-bit)
    # bool (boolean). True or False.
    # str (string). A sequence of zero or more characters.

    '''
    everything
    in
    the
    middle
    is
    part
    of
    the
    comment
    '''
    
    # Literal: A hardcoded value.
    # int literals: Just write the number (e.g., 12)
    # float literals: Just write the number, and make sure there's a decimal
    #   point somewhere (e.g., 3.14)
    # bool literals: True or False (yes, with capital T / F)
    # str literals: Enclose in single quotes or double quotes (e.g., 'Hello',
    #    or "Hello")

    # Arithmetic operations
    # + (plus)
    # -
    # *
    # /
    # % (remainder after division
    # ** (exponentiation)
    #   e.g., 2**5 is read as "two to the power of five"

    print(2**5) # Prints 32

    # (For now) A variable is a named location in memory where
    # a value can be stored

    # To create a variable, write its name, followed by an
    # assignment operator (=), followed by its initial value
    x = 2**5

    print(x) # Prints 32

    # To change the value of a variable, use the exact same
    # syntax
    x = 3

    print(x) # Prints 3

    # Python says this is legal. But Mypy says it isn't (Mypy doesn't allow
    # a variable's type to change!). Running `mypy variables.py` will print
    # an error message to the terminal. This is a bad idea!
    x = 3.14

    print(x) # Technically works and prints 3.14. Again, a bad idea!

    #x = x + 1 # x is now 4.14
    x += 1 # x is now 4.14

    print(x) # Prints 4.14


if __name__ == '__main__':
    main()
