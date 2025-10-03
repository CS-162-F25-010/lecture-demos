def main() -> None:
    password = input("What's the password?: ")

    # If statements / else statements
    # = assignment
    # Relational operator.
    # == equality
    # < less than
    # > greater than
    # <= less than or equal to
    # >= greater than or equal to
    # != not equal to

    # Logical operators: Given two booleans, produce one new boolean
    # or
    # and
    # not

    if password == 'Open Sesame' or password == 'Abrakadabra':
        # If statement body goes here
        print("You're in!")
        x = 100
    elif password == 'Admin':
        # Elif body goes here
        print("You're an admin!")
    else:
        # Else body goes here
        print("No! Bad password!")

    print(x) # This print 100 if the first if statement triggered
    # Otherwise, the above print statement throws an exception.

   

if __name__ == '__main__':
    main()
