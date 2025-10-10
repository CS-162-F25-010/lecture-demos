def main() -> None:
    name_of_file = input('Name of file: ')
    try:
        with open(name_of_file, 'r') as f:
            print('success')
    except FileNotFoundError as e:
        print('fail')


if __name__ == '__main__':
    main()
