# Write a Python program that calculates the area of geometric shapes.
# The program should ask the user to choose a shape (e.g., circle, rectangle) and input the required parameters.
# You should write separate functions for each shape (e.g., calculate_circle_area, calculate_rectangle_area)
# and call the appropriate function based on the user's choice.

import math


def calculate_circle_area(radius):
    # Calculate and return the area of a circle
    pass


def calculate_rectangle_area(length, width):
    # Calculate and return the area of a rectangle
    pass


def main():
    shape = input("Choose a shape (circle, rectangle): ").lower()

    if shape == "circle":
        radius = float(input("Enter the radius: "))
        area = calculate_circle_area(radius)
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = calculate_rectangle_area(length, width)
    else:
        print("Invalid shape choice.")
        return

    print(f"The area of the {shape} is {area:.2f}")


if __name__ == "__main__":
    main()