from traceback import print_exc # Gives you access to the print_exc function

def a() -> None:
    my_list = [1, 12, -1]
    
    # To catch exceptions, first wrap the offending code in a try block
    i = int(input('Enter an index: '))
    try:
        print(my_list[i]) # What does this do?
        # This body can be as big as you want
    except IndexError as e: # You additionally need an except block.
        # Except block body goes here
        # This code will be executed if and only if the above try block
        # throws an IndexError
        print(e) # This prints the error message associated with the exception
        
        # You can manually print a traceback
        print_exc() # Prints the traceback, but does NOT crash the program
        print('Hello')
    except ValueError as e:
        # Deal with the value error somehow
        print(e)
    
    # When an exception is thrown into a function, that function may:
    # 1. Catch the exception
    # 2. Re-throw, or propagate, the exception

    # 2. is what happens by default.

def b() -> None:
    a()

def c() -> None:
    b()

def main() -> None:
    c()

if __name__ == '__main__':
    main()
    # If the exception is thrown to module scope and it's not caught, the
    # program crashes and prints a traceback
