from numberofdaysinyear import number_of_days_in_year

def test_number_of_days_in_year_with_leap_year() -> None:
    # Arrange
    leap_year = 2000

    # Act
    result = number_of_days_in_year(leap_year)

    # Assert
    assert result == 366

def test_number_of_days_in_year_with_non_leap_year() -> None:
    # Arrange
    non_leap_year = 2001

    # Act
    result = number_of_days_in_year(non_leap_year)

    # Assert
    assert result == 365
