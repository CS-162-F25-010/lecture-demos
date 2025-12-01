from isleapyear import is_leap_year

# Test-driven development (TDD) is a coding paradigm that is motivated / driven
# by automated testing. Very commonly, TDD  is implemented via the Red,
# Green, Refactor cycle.

# 1. Write a test for a behavior that has not yet been
#      implemented for a given component. Your codebase is now "red".
#      Currently, the tests fail.
# 2. Implement that behavior (and only that behavior) so that the test
#    passes. Importantly, you must not break the other tests in doing so.
#    Do this making the smallest number of changes possible. The codebase
#    is now "green".
# 3. Refactor. Zoom out, looking at your system as a whole, and determine
#    whether there are steps you could take to refactor it to improve the code.

# Tests should have high coverage

# Each individual test should be as simple as possible.
# Each test should test one thing.
# Each test should be simple so that they, themselves, don't have bugs.

def test_is_leap_year_with_year_indivisible_by_four() -> None:
    # Arrange: Arrange your inputs
    year_indivisible_by_four = 2001

    # Act
    result = is_leap_year(year_indivisible_by_four)

    # Assert
    assert not result
    
def test_is_leap_year_with_year_divisible_by_four_hundred() -> None:
    assert is_leap_year(2000), 'Error! 2000 is a leap year!'

def test_is_leap_year_with_year_divisible_by_one_hundred_but_not_four_hundred() -> None:
    assert not is_leap_year(2100), 'Error! 2100 is not a leap year!'
