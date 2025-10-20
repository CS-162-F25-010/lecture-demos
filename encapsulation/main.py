from person import Person
from persondatabase import PersonDatabase

def main() -> None:
    person_database = PersonDatabase()
    joe = Person('Joe', 42)
    mohammad = Person('Mohammad', 24)
    person_database.add_person(joe)
    person_database.add_person(mohammad)


if __name__ == '__main__':
    main()
