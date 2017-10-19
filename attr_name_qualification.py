# ------------------------------
# Author: Ian Torres
#
# Adapted from: Learning Python
# by Mark Lutz 5th ed.
#
# ------------------------------


import changer

print(changer)  # Simple module variable

# ------------------------------
# changer.message = X.Y
#
# Qualification: find X in current scope,
# then search for attribute Y
#
# ------------------------------

print(changer.message)

# ------------------------------

# ------------------------------
# changer.RandomClassExample.x = X.Y.Z
#
# Qualification Paths: Look up name Y
# in object X, then look up Z in object
# X.Y
#
# ------------------------------

print(changer.RandomClassExample.x + " " + changer.RandomClassExample.y)

# ------------------------------
