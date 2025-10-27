class Person:
    name: str

def change_me(p: Person) -> None:
    p.name = 'Joe'

def change_list_value(l: list[int]) -> None:
    l[0] = 100

def main() -> None:
    jane = Person()
    # The dot operator reaches inside an object to retrieve / access one of
    # its attributes or methods
    jane.name = 'Jane'

    sally = Person()
    sally.name = 'Sally'

    # Now things get messy
    sally = jane

    print(id(jane))
    print(id(sally))

    sally.name = 'Sally'
    print(jane.name) # What does this print??? This prints Sally.

    change_me(jane)

    print(jane.name) # What does this print??? This prints Joe
    print(sally.name) # What does this print??? This prints Joe

    my_list = [1, 2, 3, 4, 5]
    change_list_value(my_list)
    print(my_list[0]) # What does this print??? This prints 100

if __name__ == '__main__':
    main()
