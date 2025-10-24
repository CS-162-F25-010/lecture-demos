# None and Optionals
from typing import Optional

class Person:
    name: str
    age: int
    
    phone_number: Optional[str]

def find_age_of_person(people: list[Person], name: str) -> Optional[int]:
    found_age = None # This creates the found_age variable and binds it to None
    for person in people:
        if person.name == name:
            found_age = person.age
            break
    return found_age


def main() -> None:
    # None, in python, can be used to represent the absence of a value
    people = [
        Person(),
        Person(),
        Person(),
        Person()
    ]
    people[0].name = 'Joe'
    people[0].age = 26
    people[1].name = 'Mohammad'
    people[1].age = 24
    people[2].name = 'Aditya'
    people[2].age = 30
    people[3].name = 'Jane'
    people[3].age = 19

    x: Optional[int] = 5
    x = None

    # At some point, later, I want to find the age of the person named
    # X, where X is provided by the user
    # Mypy decides that the type of this variable is Optional[int]
    
    user_input = input('Who would you like to search for?: ')
    found_age = find_age_of_person(people, user_input)
    if found_age is None:
        print('Failed to find a person with that name!')
    else:
        print(f'The person\'s age is {found_age}')

    my_list: list[Optional[int]] = []

if __name__ == '__main__':
    main()
