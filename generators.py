# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th
#
# ------------------------------


# ------------------------------
# Generator Expressions
# ------------------------------

print('Created using Generator Expression:')
G = (x * 4 for x in 'SPAM')
print(list(G))

# ------------------------------


# ------------------------------
# Generator Functions
# ------------------------------

print('\nCreated using Generator Function:')
some_string = 'SPAM'


def genfunc(x):
    for y in x:
        yield y * 4


G = genfunc(some_string)

print(list(G))
# ------------------------------


# ------------------------------
# Automatic Generator Expressions
# ------------------------------

print('\nCreated using Automatic Generator Expression:')
some_output = ''.join(x.upper() for x in 'aa bbb c'.split() if len(x) > 1)
print(some_output)

# ------------------------------
