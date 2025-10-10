def main() -> None:
    # File output: Write data into a file
    # 'w' opens in truncate mode. Overwrites contents of the file.
    # 'a' opens in append mode. Appends contents to the END of the file.
    with open('results.txt', 'a') as f:
        f.write('Hello, World!\n')
        f.write('Hello, World!\n')

if __name__ == '__main__':
    main()
