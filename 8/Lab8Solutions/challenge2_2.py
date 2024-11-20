# Write a Python program that performs matrix operations using the numpy library.
# The program should ask the user to choose an operation (e.g., addition, subtraction, multiplication)
# and input the required matrices. You should write separate functions for each operation
# (e.g., matrix_addition, matrix_subtraction, matrix_multiplication) and call the appropriate function based
# on the user's choice.

import numpy as np

def matrix_addition(matrix_a, matrix_b):
    result = np.add(matrix_a, matrix_b)
    return result

def matrix_subtraction(matrix_a, matrix_b):
    result = np.subtract(matrix_a, matrix_b)
    return result

def matrix_multiplication(matrix_a, matrix_b):
    result = np.dot(matrix_a, matrix_b)
    return result

def main():
    operation = input("Choose a matrix operation (addition, subtraction, multiplication): ").lower()

    if operation not in ["addition", "subtraction", "multiplication"]:
        print("Invalid operation choice.")
        return

    rows_a = int(input("Enter the number of rows for matrix A: "))
    cols_a = int(input("Enter the number of columns for matrix A: "))
    matrix_a = np.random.rand(rows_a, cols_a)

    print(matrix_a)

    rows_b = int(input("Enter the number of rows for matrix B: "))
    cols_b = int(input("Enter the number of columns for matrix B: "))
    matrix_b = np.random.rand(rows_b, cols_b)

    print(matrix_b)

    if operation == "addition" or operation == "subtraction":
        if rows_a != rows_b or cols_a != cols_b:
            print("Matrix dimensions must match for addition and subtraction.")
            return

    if operation == "multiplication" and cols_a != rows_b:
        print("Number of columns in matrix A must match the number of rows in matrix B for multiplication.")
        return

    if operation == "addition":
        result = matrix_addition(matrix_a, matrix_b)
    elif operation == "subtraction":
        result = matrix_subtraction(matrix_a, matrix_b)
    else:
        result = matrix_multiplication(matrix_a, matrix_b)

    print(f"Result of {operation}:\n{result}")

if __name__ == "__main__":
    main()
