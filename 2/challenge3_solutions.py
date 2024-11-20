# Create a list comprehension that displays only the even numbers in a given list.

list1 = [1, 6, 3, 4, 2, 5, 7, 18, 9]
even_only = [a for a in list1 if a % 2 == 0]
print(even_only)

# Create a list comprehension that produces a new list b from a given list of
# strings a consisting of only those elements in a that have 3 or fewer characters.

list2 = ['gnu', 'penguin', 'horse', 'fox', 'elephant', 'emu']
a2 = [a for a in list2 if len(a) <= 3]
print(a2)

# Create a list comprehension that produces a new list b from a given list of
# strings a consisting of only those elements in a that begin with a specific letter.
list3 = ['gnu', 'penguin', 'horse', 'fox', 'elephant', 'emu', 'goat']
first_letter = 'g'
a3 = [a for a in list3 if a[0] == first_letter]
print(a3)

# Create a list comprehension that produces a new list b from a given list of
# strings a consisting of only those elements in a that begin with a specific letter
# and have 3 of fewer characters.
list4 = ['gnu', 'penguin', 'horse', 'fox', 'elephant', 'emu', 'goat', 'giraffe']
first_letter = 'g'
a4 = [a for a in list3 if a[0] == first_letter if len(a) <= 3]
print(a4)
