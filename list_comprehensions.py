# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th
#
# ------------------------------

# ------------------------------
# List Comprehensions
# ------------------------------

print('Standard List Comprehension')
some_list = [element for element in range(10)]
print(some_list)

# ------------------------------


# ------------------------------
# Dictionary Comprehensions
# ------------------------------

print('\nStandard Dict Comprehension')
some_dict = {i: element for i, element in enumerate(range(10))}
print(some_dict)

# ------------------------------


# ------------------------------
# List Comprehensions with conditionals
# ------------------------------

print('\nList Comprehension with Conditional')
print('Even numbers:')
some_list_cond = [element for element in range(10) if element % 2 == 0]
print(some_list_cond)

# ------------------------------


# ------------------------------
# List Comprehension with nested loops
# ------------------------------

print('\nList Comprehension with Nested Loops')
z = [[1, 2, 3, 4, 5], [6, 7, 8], [9]]
some_list_nest = [col for row in z for col in row]
print(some_list_nest)

# ------------------------------



