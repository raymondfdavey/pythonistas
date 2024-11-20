# Example if statements

x = 2

if x > 0:
    print('Greater than zero!')


x = 2

if x < 0:
    print('x is less than zero')
elif x == 0:
    print('x is equal to zero')
else:
    print('x is greater than zero')


x = 3
y = True

if (x == 3) and y:
    print('Both conditions satisfied!')
elif (x == 3) or y:
    print('One condition satisfied!')
else:
    print('Neither condition satisfied')

x = 3
y = True

if x == 3:
    if y:
        print('Both conditions satisfied!')

# print out the 8 times table
table = 8
x = 1

while x <= 12:
    answer = x * table
    print(f'{x} times {table} = {answer}')
    x += 1

# Emulating do ... while
# print out the 8 times table
# the loop is guaranteed to run at
# least one time. We use break to
# force the loop to end

table = 8
x = 1

while True:
    # We can do the calculation in the f-string
    print(f'{x} times {table} = {x * table}')
    x += 1
    if x > 12:
        break

# Iterating over a string...

x = 'Hello World!'
for c in x:
    print(c)

# Iterating over a range...
# Note i will be i the range

# 0 to 4 inclusive
# I.e. the range has 5 elements

for i in range(5):
    print(i)

# 5 to 9 inclusive
for i in range(5, 10):
    print(i)

# iterating over a list...
# Here words is a Python list...

words = ['cat', 'dog', 'giraffe']
for w in words:
    print(w)

zoo = ['tiger', 'penguin', 'elephant']
new_animals = ['ostrich', 'gnu', 'parrot']

zoo.append('llama')
zoo.extend(new_animals)
zoo.remove('ostrich')
zoo.insert(5, 'donkey')

for animal in zoo :
    print(animal)


# Stacks using lists
stack = ['apple', 'coconut', 'banana']
# To push, use append without an index...

stack.append('lime')
print(stack)

# to pop, use pop
item = stack.pop()
# item now has the value 'lime' and is
# no longer on the stack
print(stack)
