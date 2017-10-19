# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th
#
# ------------------------------

# ------------------------------
# Common Iterable objects:
# - zip(...)
# - range(...)
# - map(...)
# - filter(...)
# ------------------------------

# ------------------------------
# zip(...)
# ------------------------------

z = zip((1, 2), (3, 4))
zl = zip(range(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('Zip contents z:')
print(next(z))
print(next(z))

print('Zip contents zl:')
for li in zl:
    print(li)

# ------------------------------


# ------------------------------
# range(...)
# ------------------------------

print('\nRange contents:')
r = range(10)
print(r)  # Right now it is a range object

i = iter(r)  # You can convert it to an iterable
print(i)

print(next(i))
print(next(i))

# ------------------------------

# ------------------------------
# map(...)
# ------------------------------

print('\nMap contents:')


def iseven(x):
    if x % 2 == 0:
        return x
    return 0


m = map(iseven, [1, 2, 4])
print(next(m))
print(next(m))
print(next(m))

# ------------------------------


# ------------------------------
# filter(...)
# ------------------------------

print('\nFilter contents:')


def iseven(x):
    if x % 2 == 0:
        return True
    return False


f = list(filter(iseven, [1, 2, 4]))
print(f)

# ------------------------------


# ------------------------------
# map(filter(...))
# ------------------------------

print('\nMap of Filtered contents:')


def iseven(x):
    if x % 2 == 0:
        return True
    return False


def something(x):
    return x


mf = map(something, filter(iseven, [1, 2, 4]))
print(mf)
for element in mf:
    print(element)

# ------------------------------


