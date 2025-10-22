from person import Person
from persondatabase import PersonDatabase

# The interface of this function is as follows:
# Its name is add
# It accepts two parameters. The first is an int, the second is also an int
# It returns an integer
# It doesn't raise any exceptions
def add(x: int, y: int) -> int:
    # The implementation is the body
    return x + y

def main() -> None:
    person_database = PersonDatabase()
    joe = Person('Joe', 42)
    mohammad = Person('Mohammad', 24)
    person_database.add_person(joe)
    person_database.add_person(mohammad)

    # Now, the _ suggests that this is a mistake
    # person_database._people.append(joe)

    # Technically, in Python, there isn't REALLY such a thing as "private
    # attributes".


if __name__ == '__main__':
    main()
