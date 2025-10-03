def main() -> None:
    # Standard output is a special file that every process has.
    #       A process is a running instance of a program

    # By default, standard output is linked to the terminal.
    # print() simply writes stuff to standard output.

    # There is also a standard input. By default, it's also linked to the
    # terminal.

    # input() simply reads stuff from standard input.

    # This prints "What is your favorite number?: ". And then it PAUSES
    # until the user types something in and presses enter. It then RETURNS
    # the string that the user typed in
    favorite_number = float(input('What is your favorite number?: '))

    print(f'Your number, doubled, is {favorite_number * 2}')


    

if __name__ == '__main__':
    main()
