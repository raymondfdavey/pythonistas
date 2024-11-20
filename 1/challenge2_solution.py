# Allow the user to enter an integer number. Determine if the number is prime
# or not. A number is prime if it is only divisible exactly by 1 and itself,
# e.g. 3, 7, 11 and 17. Note, 2 is the only even prime number. 1 is not
# generally regarded as prime.
# Display the answer “prime” or not prime as appropriate.

x = int(input('Enter the number to test: '))
is_prime = True  # boolean data type - note the capital 'T' in 'True

y = x - 1
while y > 1:
    if x % y == 0:
        # x is divisible exactly by y...
        is_prime = False
        break  # exits the while loop
    else:
        y -= 1

if is_prime:
    print(f'Number {x} is a prime number')
else:
    print(f'Number {x} is not a prime number')
