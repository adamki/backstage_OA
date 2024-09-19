import pytest
from api.calculations import sum_of_squares, square_of_sum, calculate_difference


def test_sum_of_squares():
    # Smallest Valid N
    assert sum_of_squares(1) == 1
    assert sum_of_squares(3) == 14

    # Largest Valid N
    assert sum_of_squares(5) == 55
    assert sum_of_squares(10) == 385


def test_square_of_sum():
    # Smallest Valid N
    assert square_of_sum(1) == 1
    assert square_of_sum(3) == 36

    # Largest Valid N
    assert square_of_sum(5) == 225
    assert square_of_sum(10) == 3025


def test_calculate_difference():
    # Smallest Valid N
    assert calculate_difference(1) == 0
    assert calculate_difference(3) == 22

    # Largest Valid N
    assert calculate_difference(5) == 170
    assert calculate_difference(10) == 2640


def test_calculate_difference_invalid_n():
    # Invalid N
    with pytest.raises(ValueError, match="n must be between 1 and 100"):
        calculate_difference(0)  # Invalid: less than 1
    with pytest.raises(ValueError, match="n must be between 1 and 100"):
        calculate_difference(101)  # Invalid: greater than 100
