"""Unit tests covering the triangle specification and its boundaries."""

import math

from triangle import classify_triangle, is_valid_triangle


def test_zero_side_is_invalid():
    assert classify_triangle(0, 4, 5) == "Invalid"


def test_negative_side_is_invalid():
    assert classify_triangle(-1, 4, 5) == "Invalid"


def test_triangle_inequality_failure_is_invalid():
    assert classify_triangle(1, 2, 8) == "Invalid"


def test_degenerate_triangle_is_invalid():
    # The strict inequality rules out 2 + 3 == 5.
    assert classify_triangle(2, 3, 5) == "Invalid"


def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_scalene_triangle_with_sides_out_of_order():
    assert classify_triangle(5, 3, 4) == "Right Scalene"


def test_right_isosceles_triangle_with_noninteger_side():
    # Exact equality of squared sides fails here due to rounding.
    assert (5 * math.sqrt(2)) ** 2 != 5 ** 2 + 5 ** 2
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_nearly_right_but_not_right_triangle():
    assert classify_triangle(3, 4, 5.1) == "Scalene"


def test_validity_function_returns_booleans():
    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(2, 3, 5) is False
    assert is_valid_triangle(0, 3, 4) is False


def test_non_finite_sides_are_invalid():
    assert classify_triangle(math.inf, 5, 6) == "Invalid"
    assert classify_triangle(math.nan, 5, 6) == "Invalid"


# Test that a triangle with sides 4, 0, and 5 is invalid
def test_zero_middle_side():
    assert classify_triangle(4, 0, 5) == "Invalid"


# Test a right isosceles triangle with a non-integer hypotenuse
def test_right_isosceles_float_copilot():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"