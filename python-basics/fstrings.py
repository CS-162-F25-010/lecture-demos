def main() -> None:
    number_of_strawberries = 100
    number_of_people = 1.5
    alex_likes_spaghetti = True

    print(f'Alex has {number_of_strawberries} strawberries, and Alex '
        f'has {number_of_people + 1} friends, and does alex like spaghetti? '
        f'{alex_likes_spaghetti}')

    # Type casting
    number_of_people = float(number_of_strawberries)

    print(number_of_people)

    print(int(2.9)) # Prints 2, truncation

if __name__ == '__main__':
    main()
