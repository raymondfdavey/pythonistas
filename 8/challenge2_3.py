# Write a Python program that finds the inverse of a square matrix and solves a system of linear equations
# using the numpy library. The program should ask the user to input a square matrix and a column vector.
# You should find the inverse of the matrix and solve the equation Ax = B, where A is the matrix
# and B is the column vector.

import numpy as np


def find_inverse(matrix):
    # Find the inverse of the matrix and return it
    # Hint: use np.linalg.inv
    # If the matrix is singular, return None
    try:
        pass
    except np.linalg.LinAlgError:
        pass


def solve_system(matrix, vector):
    # Solve the system of equations Ax = B and return the solution vector
    # Hint: use np.dot (see the lecture slides for an example)
    pass


def main():
    n = int(input("Enter the size of the square matrix A: "))

    # Generate random values for matrix A and vector B
    matrix_a = np.random.rand(n, n)
    vector_b = np.random.rand(n, 1)

    inverse = find_inverse(matrix_a)

    if inverse is not None:
        solution = solve_system(matrix_a, vector_b)
        print(f"Matrix A:\n{matrix_a}")
        print(f"Vector B:\n{vector_b}")
        print(f"Inverse of A:\n{inverse}")
        print(f"Solution to Ax = B:\n{solution}")
    else:
        print("Matrix A is singular and does not have an inverse.")


if __name__ == "__main__":
    main()
