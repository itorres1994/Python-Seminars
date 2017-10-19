# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th
#
# ------------------------------

# ------------------------------
# Name Resolution: The LEGB Rule
#
# Four possible scopes:
# L: local,
# E: enclosing functions (if any),
# G: global,
# B: built-in
#
# ------------------------------
import builtins
# ------------------------------
# L (i.e. inside functions)
# E (i.e. functions inside functions)
# G (i.e. variables in a module)
# B (i.e. an function that pre-exists)
# ------------------------------

a = 'World'
b = 'You'

# ------------------------------
# L (ex.)
# ------------------------------
def myfunc(a):
    print(a)

    # ------------------------------
    # E (ex.)
    # ------------------------------
    def mynestfunct(a):
        a = 'Hello'
        print(a)
        # ------------------------------
        # G (ex.)
        # ------------------------------
        print(b)

        # ------------------------------
        # B (ex.)
        # ------------------------------
        print(dir(builtins))

    mynestfunct(a)


myfunc(a)
