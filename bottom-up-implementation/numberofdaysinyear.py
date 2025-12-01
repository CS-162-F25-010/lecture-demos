from isleapyear import is_leap_year

def number_of_days_in_year(y: int) -> int:
    if is_leap_year(y):
        return 366
    else:
        return 365
