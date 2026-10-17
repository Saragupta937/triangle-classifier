"""Validate triangles and classify them by their sides and angles."""

import math


def is_valid_triangle(a, b, c) -> bool:
    """Return True only if the three lengths can form a triangle."""
    if not all(math.isfinite(side) and side > 0 for side in (a, b, c)):
        return False

    # For sorted sides, only the two shorter sides need checking.
    shortest, middle, longest = sorted((a, b, c))
    return shortest + middle > longest


def classify_triangle(a, b, c) -> str:
    """Return the triangle type, prefixed with 'Right ' when appropriate."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    shorter, longer, longest = sorted((a, b, c))
    # hypot(shorter, longer) is sqrt(shorter**2 + longer**2).
    # isclose avoids incorrect results from floating-point rounding.
    if math.isclose(math.hypot(shorter, longer), longest, rel_tol=1e-9):
        return "Right " + triangle_type

    return triangle_type
