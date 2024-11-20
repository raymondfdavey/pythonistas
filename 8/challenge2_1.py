"""Numpy Exercises"""

import time
import numpy as np


# Besides having lots of useful methods for scientific computing, numpy arrays
# are also generally much faster than Python lists.

# The following class is a context manager that can be used to time blocks of
# code. It is used like this:
#
# with Timer() as t:
#     run code...
#
# It will automatically print the time it took to run the code block when the
# block is finished executing, e.g.:
# Execution took <t>s
#
# The Timer class is not important for this challenge, but you can use it to
# time your code if you want to (or feel free to write your own timer).


class Timer:
    """
    Class for timing blocks of code.
    
    Examples
    --------
    >>> with Timer() as t:
    >>>    run code...
    Execution took <t>s)
    """

    def __init__(self, message=None):
        self.start = 0
        self.end = 0
        self.interval = 0
        if message:
            print(message, end=': ')

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
        print(f'{self.interval:.3g}s')

    def __str__(self):
        return f'{self.interval:.3g}s'

    def reset(self):
        """Reset timer to 0"""
        self.start = 0
        self.end = 0
        self.interval = 0


### Speed comparison between Python lists and numpy arrays ###

# Create a list of the first 100_000_000 integers
# Hint: use range
with Timer("List creation") as t:
    python_list = ...

# Create a numpy array of the first 100_000_000 integers
# Hint: use np.arange
with Timer("Array creation") as t:
    numpy_array = ...

# Add 5 to each element in the Python list
# Hint: use a for loop
with Timer("List addition") as t:
    python_list_result = ...

# Add 5 to each element in the numpy array
with Timer("Array addition") as t:
    numpy_array_result = ...

# Add 5 to each element in the numpy array again but use np.add
with Timer("Array addition with np.add") as t:
    numpy_array_result = ...


### Array operation exercises ###

# Create a vector full of ones of size 12
# Hint: use np.ones
ones_vector = ...

# Divide each element in the ones vector by 12
scaled_vector = ...

# Reshape the scaled vector to size (2, 6)
# Hint: use np.reshape or the .reshape method
reshaped_vector = ...

# Confirm that the reshaped vector is of size (2, 6)
# Hint: use assert

# Create a null vector (full of zeros) of size (4, 3)
# Hint: use np.zeros
null_vector = ...

# Create a vector with values ranging from 10 to 32 in steps of 2 (inclusive)
# Hint: use np.arange
ranged_vector = ...

# Prinnt the last 3 elements of the ranged vector
# Hint: use print(f"{variable=}") to print the variable name and value

# Add 5 to each element in the ranged vector
added_vector = ...

# Multiply each element in the added vector by 2.5
multiplied_vector = ...

# Reverse the order of the multiplied vector
# Hint: use np.flip
reversed_vector = ...

# Print the third, fourth, and fifth elements of the reversed vector

# Reshape the reversed vector then multiply it by the reshaped vector
product_vector = ...

# Print the last row of the product vector

# Create a 3x3 random matrix
# Hint: use np.random.random
random_matrix = ...

# Create a 3x3 identity matrix
# Hint: use np.eye
identity_matrix = ...

# Print the middle column of the identity matrix

# Multiply the random matrix by the identity matrix
# Hint: use np.dot or the @ operator
product_matrix = ...

# Print the product matrix

# Print the sum of the product matrix
# Hint: use np.sum

# Print the mean of the product matrix
# Hint: use np.mean

# Print the standard deviation of the product matrix
# Hint: use np.std

# Print the minimum and maximum values in the product matrix
# Hint: use np.min and np.max

# Find the indices of values greater than 0.5 in the product matrix
# Hint: use np.where

# Use the indices to set the values greater than 0.5 to 1 and print the matrix
# Hint: use np.where

# Create a random vector of size 10 and sort it in ascending order and print it
# Hint: use np.sort
random_vector = ...

# Clip the values in the random vector between 0.25 and 0.75 and print it
# Hint: use np.clip
clipped_vector = ...

# Calculate the cumulative sum of the clipped vector
# Hint: use np.cumsum
cumulative_sum = ...

# Take the natural log of each element in the cumulative sum vector and print it
# Hint: use np.log
log_vector = ...

# Calculate the dot product of the log vector and the clipped vector and print it
# Hint: use np.dot
dot_product = ...

# Round the dot product to 2 decimal places and print it
# Hint: use np.round
