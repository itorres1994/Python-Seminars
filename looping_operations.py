# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th
#
# ------------------------------

from collections import Iterable

# ------------------------------
# Using a For Comprehension loop
# ------------------------------

print('Looping using For loops\n')

# ------------------------------
# For loop using a range object
# ------------------------------

x = [1, 2, 3, 4, 5, 6, 7]

print('Looping using range as index:')
for i in range(len(x)):
    print('Range element:', i, ' | element:', x[i])

# ------------------------------


# ------------------------------
# For loop using an iterable object
# ------------------------------

print('\nLooping using an iterable object:')
for element in x:
    print('Object element:', element)

# ------------------------------


# ------------------------------
# For loop using enumeration
# ------------------------------

print('\nLooping using an enumeration:')
for i, element in enumerate(x):
    print('index:', i, ' | element:', element)

# ------------------------------


# ------------------------------
# For loop using zip (an iterable object...)
# ------------------------------

limit = 5
print('\nLooping using an enumeration:')
for i, element in zip(range(limit), x):
    print('zipped element:', i, ' | element:', element)

# ------------------------------


# ------------------------------


# ------------------------------
# Using While loops
# ------------------------------

print('Looping using While loops\n')

# ------------------------------
# Regular While loop
# ------------------------------

y = [('I', 'love'), 'crepes']
print('\nWhile Loop:')
index = 0
length = len(y)
while index < length:
    print('Index:', index, ' | ', y[index])
    index += 1

# ------------------------------


# ------------------------------
# Regular While loop with nested for loop
# ------------------------------

y = [('I', 'love'), 'crepes']
print('\nWhile Loop with nested for loop:')
index = 0
length = len(y)
while index < length:
    print('Index:', index, ' | ', y[index])

    # Check the instance of the object we are
    # iterating over: is it an iterable object
    if isinstance(y[index], Iterable) and not isinstance(y[index], str):
        for element in y[index]:
            print('Nested element:', element)

    index += 1

# ------------------------------

# ------------------------------


# ------------------------------
# Recursion
# ------------------------------

print('\nRecursion with an iterable object:')
x = [1, 2, 3, 4, 5, 6]


def product(s):

    def prodhelp(a, j, l):
        print('element:', a[j])
        if j < l:
            return a[j] * prodhelp(a, j+1, l)
        else:
            return 1

    return prodhelp(s, 0, len(s)-1)


print(product(x))

# ------------------------------




