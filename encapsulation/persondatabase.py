from person import Person

class PersonDatabase:
    # In Python, attributes beginning with an _ (underscore) are said to
    # be "private". Private attributes should never be accessed from anywhere
    # other than within methods in the very same class in which the attribute
    # was declared.
    _people: list[Person] # If I changed this to a dictionary, that would break
    # every line of code where we call .append()

    def __init__(self) -> None:
        self._people = []

    def add_person(self, person: Person) -> None:
        self._people.append(person)
