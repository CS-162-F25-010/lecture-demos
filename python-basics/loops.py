def main() -> None:
    # There are two main kinds of loops in Python:
    # for loops
    # while loops
    
    # Python does not have do-while loops

    # While loops are exactly like if statements, except you write
    # the word "while" instead of the word "if"

    i = 0
    while True:
        print('Hello')
        i += 1
        # While loop body goes here

        # You can only use a break statement inside a loop.
        # It immediately "ends" the loop.
        if i >= 10:
            break
    
    # How many times does this program print "Hello"? 10 times

    # For loops in Python
    # Some examples of iterables include lists, ranges, tuples
    # range(n) constructs a range that represents all the whole numbers
    #   from 0 through n-1
    # range(a, b) constructs a range that represents all the whole numbers
    #   from a through b-1   [a, b)
    for i in range(10):
        # For loop body goes here
        print(i)

if __name__ == '__main__':
    main()
