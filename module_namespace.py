# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th ed.
#
# ------------------------------

import changer

# ------------------------------
# Every module or python file
# has an internal dictionary
# object <__dict__> which have
# .keys() and .values()
# ------------------------------

print(changer.__dict__.keys())

print(list(name for name in changer.__dict__.keys() if not name.startswith('__')))

# ------------------------------

