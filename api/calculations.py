def sum_of_squares(n: int) -> int:
    """Calculate the sum of the squares of the first n natural numbers."""
    return sum(i**2 for i in range(1, n + 1))


def square_of_sum(n: int) -> int:
    """Calculate the square of the sum of the first n natural numbers."""
    total_sum = sum(range(1, n + 1))
    return total_sum**2


def calculate_difference(n: int) -> int:
    """Calculate the difference between the square of the sum and the sum of the squares."""
    if n < 1 or n > 100:
        raise ValueError("n must be between 1 and 100")

    return square_of_sum(n) - sum_of_squares(n)
