# Allow the user to enter a number. Use an if statement to display
# whether the number is negative, equal to zero or positive.

x = int(input('Enter a number: '))

if x < 0:
    print('Negative number')
elif x == 0:
    print('Equal to zero')
else:
    print('Positive number')

# The range() function can be used to create a sequence of numbers
# (see the code for this). Allow the user to enter a number and
# then iterate over the range to determine whether the number
# the user entered is present in the sequence.
# Note: the returned range does not include the end value.
# See the documentation for more details: 
# https://docs.python.org/3/library/functions.html#func-range

x1 = range(0, 10)
x2 = range(15, 5, -1)  # steps of -1
x3 = range(0, 30, 3)  # steps of 3

a = int(input('Enter a number: '))

for x in x1:
    if a == x:
        print('Number in generated range sequence')
        break

for x in x2:
    if a == x:
        print('Number in generated range sequence')
        break

for x in x3:
    if a == x:
        print('Number in generated range sequence')
        break

# This can be done more simply and pythonicly using the "in" operator e.g.:
if a in x1:
    print('Number in generated range sequence')


# An arithmetic series of numbers is defined by an initial value
# and a common difference. For example, if the starting value is 2 and
# the common difference is 5, the arithmetic sequence would begin:
# 2, 5, 8, 11, 14, ...
# Allow the user to enter values for the initial value and common difference.
# Write code to determine the sum of the first 10 elements in the
# arithmetic sequence.

initial_value = int(input('Enter initial value: '))
common_diff = int(input('Enter common dfference: '))

# Obvious approach - use a loop
x = initial_value
i = 0
my_sum = 0
while i < 10:
    print(x)
    my_sum += x
    x += common_diff
    i += 1
print(f'Sum is: {my_sum}')

# Alternative approach - use a range...

x = range(initial_value, initial_value + (10 * common_diff), common_diff)
print(f'Sum is {sum(x)}')


# Write code to simulate the simple children’s game “Fuzz Buzz”.
# The rules are simple; start counting upwards from 1 in single increments.
# If the number is divisible by 5, display “Fuzz”. if the number is
# divisible by 6, display “Buzz". If the number is divisible by both,
# display “Fuzz Buzz”. Otherwise just display the number.
# Play the game from 1 through to 50 inclusive.

v1 = 1   # current number value
while v1 <= 50:
    if v1 % 5 == 0 and v1 % 6 != 0 :
        print('Fuzz')
    elif v1 % 6 == 0 and v1 % 5 != 0:
        print('Buzz')
    elif v1 % 6 == 0 and v1 % 5 == 0:
        print('Fuzz Buzz')
    else:
        print(v1, ' ')
    v1 += 1
