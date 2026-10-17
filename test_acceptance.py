"""Customer-facing acceptance test for a stained-glass studio."""

from triangle import classify_triangle


def test_stained_glass_customer_requirements():
    # AC1: Unbuildable inputs return Invalid without crashing.
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"

    # AC2: Buildable inputs return their correct named shapes.
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(3, 3, 3) == "Equilateral"

    # AC3: Right-angle pieces are clearly flagged for reinforcement.
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * (2 ** 0.5)) == "Right Isosceles"
