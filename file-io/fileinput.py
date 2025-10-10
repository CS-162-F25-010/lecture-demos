from typing import TextIO
# Standard I/O: Standard input / output
# Every process has a standard output. Print() simply writes data to that file.
# Every process has a standard input. input() simply reads data from it.

# File I/O: File input / output. Write a program that reads data from files,
# and / or writes data to files.

def read_from_file(some_file: TextIO) -> list[int]:
    # Body goes here...

def main() -> None:
    # To read data from a file (i.e., file input), you first have to OPEN
    # the file for READING
    with open('people.csv', 'r') as f:
        # The body of the context manager goes here
        # You can read from the file, represented by f, inside this context
        # manager body.
        
        # read_from_file(f)

        last_names = []
        ages = []
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            # Tokenization: You take a string with many tokens, and you extract
            # those tokens from it.
            # line = 'Guyer,Alex,26'
            # tokens = ['Guyer', 'Alex', '26']
            tokens = line.split(',')
            last_names.append(tokens[0])
            ages.append(int(tokens[2]))
        
        # Here, the for loop is over

    # Here, you can no longer read from f.
    print(ages)
        

if __name__ == '__main__':
    main()
