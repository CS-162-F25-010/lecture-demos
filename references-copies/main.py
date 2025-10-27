# References / copies / Python's object model

def main() -> None:
    # In Python, an object is basically any value
    
    # As it turns out, a variable is not a value. A variable is not an object.

    # What is a variable???
    # A variable is a reference to an object.

    x = 5
    
    # In Python, every object has a unique identifier. It can be retrieved
    # via the id() function.
    # print(id(x))

    # the assignment operator takes a variable on the left, and an object on
    # the right (or a reference to an object on the right), and it sets up
    # the variable to refer to the given object.
    y = x

    # print(id(y)) # Question: Will this print the same id as above, or a different one?

    
    x = 1
    print(x)
    print(y) # This still prints 5. Why?
    
    print(id(x))
    print(id(y))


    x += 2 # This is equivalent to x = x + 2
    print(id(x))

    # In the context of primitives (int, float, bool), none of this
    # really matters that much.

    # In the context of more complicated objects, this REALLY matters.



if __name__ == '__main__':
    main()
