from person import Person

class PersonDatabase:
    people: list[Person] # If I changed this to a dictionary, that would break
    # every line of code where we call .append()

    def __init__(self) -> None:
        self.people = []

    def add_person(self, person: Person) -> None:
        self.people.append(person)
