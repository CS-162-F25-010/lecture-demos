# Determines whether a given year is a leap year
def is_leap_year(y: int) -> bool:
    # A leap year occurs every year that's a multiple of 4,
    # except for years that are divisible by 100 but not 400.
    # (Yes, this is a true fact. See the below reference.)
    # https://en.wikipedia.org/wiki/Leap_year

    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return True
        else:
            return True
    else:
        return False # Not divisible by 4

def main() -> None:
    # An assertion is a line of code that "asserts" that a certain condition
    # must be True. If that condition is not True (i.e., False), then
    # an AssertionError is automatically raised.
    
    
    assert is_leap_year(2000), 'Error! 2000 is a leap year!'

    assert not is_leap_year(2100), 'Error! 2100 is not a leap year!'

# Pytest is an automated testing framework for Python.

if __name__ == '__main__':
    main()
