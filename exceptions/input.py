def main() -> None:
    valid_input = False
    while not valid_input:
        try:
            age = int(input('How old are you?: '))
            if age >= 0:
                valid_input = True
            else:
                print('Error. Please enter a NON-NEGATIVE number.')
        except ValueError as e:
            print('Error. Bad input. Please enter a NUMBER.')

if __name__ == '__main__':
    main()
