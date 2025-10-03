def main() -> None:
    # int, float, bool, str

    my_cool_string = 'Hello, World!'
    print(my_cool_string)

    # Index is an integer between 0 and N-1, where N is the length of the string
    print(my_cool_string[0])
    
    # In Python, all strings are immutable
    # my_cool_string[0] = 'J' # I can't do this. Syntax error.

    # But I can do this
    my_cool_string = 'Jello, World!'

if __name__ == '__main__':
    main()
