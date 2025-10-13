# It's possible to create your own types in Python
# In most cases, you create composite types / aggregate types

# Convention: Custom class names should begin with a Capital letter

# This class defines a custom data type
# This particular class is known as a POD (plain-old data) type.
class City:
    # Attribute declarations. These inform Mypy that every City SHOULD have
    # an attribute `name` and another attribute `population`.
    name: str
    population: int


def print_city(city: City) -> None:
    # Prints the given city's data to the terminal
    print(f'City name: {city.name}')
    print(f'City population: {city.population}')


def parse_city(line: str) -> City:
    tokens = line.split(',')
    result = City()
    result.name = tokens[0]
    result.population = int(tokens[1])
    return result


def main() -> None:
    cities = []
    with open('cities.csv', 'r') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            cities.append(parse_city(line))
    print_city(cities[1])

if __name__ == '__main__':
    main()
