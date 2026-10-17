# Triangle Classifier

A small Python program that takes three side lengths, checks whether they form a valid triangle, and returns its shape. Right-angle triangles are marked with `Right ` so that a stained-glass studio knows which pieces need reinforced corners.

## Files

- `triangle.py` — triangle validation and classification functions
- `test_triangle.py` — pytest unit tests
- `test_acceptance.py` — one customer-focused acceptance test
- `requirements.txt` — pytest dependency
- `README.md` — project explanation, tests, and review information

## How to Run the Tests

Requires Python 3.9 or newer. Open a terminal in this project folder and run:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

On systems that use `python3` instead of `python`, replace `python` with `python3` in both commands.

To check the functions interactively:

```python
from triangle import classify_triangle
print(classify_triangle(3, 4, 5))  # Right Scalene
print(classify_triangle(2, 3, 5))  # Invalid
```

## Triangle Classification Rules

A triangle is invalid if any side is zero or negative or if the sum of the two shorter sides is less than or equal to the longest side. Valid triangles are:

- **Equilateral:** all three sides equal
- **Isosceles:** exactly two sides equal
- **Scalene:** all three sides different
- **Right:** the squares of the shorter sides add up (within floating-point tolerance) to the square of the longest side; prefix the shape with `Right `

The program uses `math.isclose(math.hypot(shorter, longer), longest)` to apply the Pythagorean theorem with a tolerance rather than exact `==` on floating-point values.

## Equivalence Classes and Boundaries

| Class or boundary | Example inputs | Expected result |
| --- | --- | --- |
| Side equal to zero | `(0, 4, 5)` | `Invalid` |
| Negative side | `(-1, 4, 5)` | `Invalid` |
| Triangle inequality fails | `(1, 2, 8)` | `Invalid` |
| Degenerate boundary: sum equals longest | `(2, 3, 5)` | `Invalid` |
| All sides equal | `(3, 3, 3)` | `Equilateral` |
| Exactly two sides equal | `(5, 5, 6)` | `Isosceles` |
| All sides different | `(4, 5, 6)` | `Scalene` |
| Right triangle, different sides | `(3, 4, 5)` | `Right Scalene` |
| Right triangle, non-integer hypotenuse | `(5, 5, 5*sqrt(2))` | `Right Isosceles` |
| Valid but not right, near common right triple | `(3, 4, 5.1)` | `Scalene` |

The exact boundary `(2, 3, 5)` is invalid because a triangle needs **strict** inequality, not equality. The non-integer right triangle verifies that the program handles floating-point rounding.

## Why Equilateral Triangles Cannot Be Right

An equilateral triangle has three angles of 60 degrees. A right triangle must have one 90-degree angle, so an equilateral triangle cannot also be right.

## Copilot Review Log

**Important provenance note:** This project was prepared with ChatGPT, **not** with GitHub Copilot. The rows below are a review of the ChatGPT-prepared tests. They do **not** claim Copilot suggested anything. To satisfy the assignment's Copilot requirement, use Copilot autocomplete in VS Code to draft or revise unit tests in `test_triangle.py`, personally check each suggestion against the specification, and replace/add entries with what Copilot *actually* suggested, including one genuine mistake you corrected. Do not label a suggestion "Copilot-suggested" unless it was.

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| --- | --- | --- | --- |
| `test_degenerate_triangle_is_invalid` | No (ChatGPT draft) | Kept after review | Equality at the triangle-inequality boundary must return `Invalid`. |
| `test_equilateral_triangle` | No (ChatGPT draft) | Kept after review | Three identical positive sides must return `Equilateral`, not `Right Equilateral`. |
| `test_right_isosceles_triangle_with_noninteger_side` | No (ChatGPT draft) | Kept after review | A strict comparison of the squared lengths fails for `5*sqrt(2)`; the implementation uses `math.isclose` with tolerance. |
| `test_right_scalene_triangle` | No (ChatGPT draft) | Kept after review | `(3,4,5)` must return `Right Scalene`. |

**Before submission:** Add truthful Copilot-reviewed entries here (one catching a specific mistake in a genuine Copilot suggestion). If Copilot's suggestions contain no errors, do not invent one; document a specific check and tell the instructor what happened.

## Customer Acceptance Criteria

The stained-glass studio requirements are restated as three measurable criteria:

1. **Unbuildable piece:** Given side lengths with a nonpositive value or lengths that fail the strict triangle inequality, `classify_triangle` returns the exact string `"Invalid"` and does not throw an exception.
2. **Buildable piece classification:** Given a valid triangle, `classify_triangle` returns the correct side-based shape name (`"Equilateral"`, `"Isosceles"`, or `"Scalene"`), with an additional `"Right "` prefix when the sides form a right angle.
3. **Reinforcement flag:** Given a right triangle such as `(3,4,5)` or `(5,5,5*sqrt(2))`, the return value begins with the exact prefix `"Right "` so the studio can identify pieces needing reinforced corners; a non-right triangle must not receive the prefix.

The single function `test_stained_glass_customer_requirements` in `test_acceptance.py` exercises all three criteria with end-to-end calls to `classify_triangle()`.

## AI-Use Disclosure

**ChatGPT (OpenAI):** Used to draft this project's Python implementation, unit tests, acceptance test, README, and local Git history, and to check the tests. The generated tests were checked against the assignment's specification and run with pytest. The user should review and understand the work before submitting it.

**GitHub Copilot:** Not used in preparing these files. To meet the course requirement, the student must separately use Copilot autocomplete for the unit-test portion and truthfully update the Copilot Review Log with their actual accept/edit/reject decisions. Do not claim Copilot was used if it wasn't.

The acceptance test included here was generated by ChatGPT, not GitHub Copilot. If the instructor intends *all* AI assistance to be prohibited for acceptance-test judgment, the student must personally rewrite and verify that test and its criteria before submission.

## Version History

The Git repository is prepared with three local commits: implementation, unit tests, and acceptance test/documentation. Publishing to GitHub requires connecting or using the student's own GitHub account.
