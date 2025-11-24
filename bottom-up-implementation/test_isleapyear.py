from isleapyear import is_leap_year

def test_is_leap_year_with_year_indivisible_by_four() -> None:
    assert not is_leap_year(2001),\
        ('Error! 2001 is not a leap year!')
