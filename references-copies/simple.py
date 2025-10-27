def change_me(x: int) -> None:
    x = 100

def main() -> None:
    y = 1
    change_me(y)
    print(y) # What does this print??? This prints 1

if __name__ == '__main__':
    main()
