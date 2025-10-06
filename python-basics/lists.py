def average(list_of_numbers: list[float]) -> float:
    sum_of_numbers = 0.0
    for x in list_of_numbers:
        sum_of_numbers += x
    return sum_of_numbers / len(list_of_numbers)

def main() -> None:
    # Lists in Python
    
    # A list is sort of like an array.
    # A list is a homogeneous sequence of things.
    #   Homogeneous: Everything in it is of the same type.
    #       Technically, Python lets lists be heterogeneous. But Mypy does not.
    #   Sequence: An ordered list of things.
    #   Element: A thing within a list.

    # An array is of a fixed size. In Python, a list can be expanded.
    # An array is homogeneous.

    # empty_list = []
    # empty_list.append(5)
    cool_numbers = [3.14, 9.81, 2.71]
    
    # An index is an integer that specifies a position within a list
    # In python, most everything is indexed by 0.
    print(cool_numbers[2])

    cool_numbers[2] = 10.5

    print(cool_numbers[2])

    print(cool_numbers)

    # Slicing / slices / slice indexing

    # To get the length of a list, write len(the list goes here)

    print(len(cool_numbers)) # Prints 3

    # You can add stuff to lists
    # To append stuff to a list (add stuff to the end of it), you  can do
    # this:
    cool_numbers.append(2.71)

    print(cool_numbers)

    # TO insert stuff into the middle of a list, you can do this:
    cool_numbers.insert(1, -1.5)

    print(cool_numbers)

    # You can remove stuff from lists
    del cool_numbers[3]

    print(cool_numbers)

    # You can iterate through a list using a for loop
    average_of_numbers = average(cool_numbers)
    print(f'Average is: {average_of_numbers}')

    my_list = [x ** 2 for x in cool_numbers]

    print(my_list)

    empty_list: list[float] = []
    empty_list.append(3.14)
    

if __name__ == '__main__':
    main()
