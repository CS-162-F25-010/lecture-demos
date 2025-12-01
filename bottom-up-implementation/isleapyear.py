# Determines whether a given year is a leap year
def is_leap_year(y: int) -> bool:
    # A leap year occurs every year that's a multiple of 4,
    # except for years that are divisible by 100 but not 400.
    # (Yes, this is a true fact. See the below reference.)
    # https://en.wikipedia.org/wiki/Leap_year

    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    else:
        return False # Not divisible by 4
