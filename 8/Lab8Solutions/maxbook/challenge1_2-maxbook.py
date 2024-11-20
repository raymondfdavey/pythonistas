# Write a Python program that solves a quadratic equation of the form ax^2 + bx + c = 0.
# The program should ask the user to input the coefficients a, b, and c, and then solve the equation.
# You should handle cases with real and complex roots and print the solutions.

import math
import cmath

def solve_quadratic(a, b, c):
    # The formula for solving a quadratic equation is:
    # x = (-b +/- sqrt(b^2 - 4ac)) / 2a
    # The +/- means that there are two solutions, one with a plus and one with a minus
    # Start by calculating the discriminant, which is b^2 - 4ac
    # If the discriminant is greater than 0, there are two real solutions
    # If the discriminant is equal to 0, there is one real solution (repeated)
    # If the discriminant is less than 0, there are two complex solutions
    # Hint: use math.sqrt for real solutions and cmath.sqrt for complex solutions
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real solution (repeated)
        root1 = -b / (2*a)
        return root1,
    else:
        # Complex solutions
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2


def main():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    roots = solve_quadratic(a, b, c)

    if len(roots) == 1:
        print(f"The equation has one real solution: x = {roots[0]}")
    elif len(roots) == 2:
        print(f"The equation has two real solutions: x1 = {roots[0]}, x2 = {roots[1]}")
    else:
        print(f"The equation has complex solutions: x1 = {roots[0]}, x2 = {roots[1]}")

if __name__ == "__main__":
    main()
