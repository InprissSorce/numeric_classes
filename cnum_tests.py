# Experiment

import cnum

# Create and print a complex number
c1 = cnum.cnum(1, 1)
print("Here's a complex number:", c1)
print("Here's its type:", type(c1))
print()

# Add two complex numbers
c2 = cnum.cnum(2, 3)
c3 = c1 + c2
print("Add: ", end = "")
print(c1, "+", c2, "=", c3)
print()

# Multiply two complex numbers
c4 = c1 * c2
print("Multiply: ", end = "")
print(c1, "*", c2, "=", c4)
print()

# Negate a complex number
c5 = -c1
print("The negation of", c1, "is", c5)
print()

# Subtraction is addition of the negative
c6 = c1 - c2
print("Subtract: ", end = "")
print(c1, "-", c2, "=", c6)
print()

# Conjugate
print("The conjugate of", c2, "is", c2.conj())
print()

# Divide two complex numbers
c7 = c1 / c2
print("Division: ", end = "")
print(c1, "/", c2, "=", c7)
print()

# Integer Powers
print(c1, "raised to powers 1, 2, 3 and 4:", c1, c1 ** 2, c1 ** 3, c1 ** 4)
print(c1, "raised to powers -1 and -2:", c1 ** -1, c1 ** -2)
print("(3 + 4i) ** 5 = ", cnum.cnum(3, 4) ** 5)
print()

# Magnitude
print("The magnitude of", c1, "is", abs(c1))
print()

# Operations with Reals
print("Operations with Reals")
print("2 +", c1, "=", 2 + c1)
print(c1, "+ 2 =", c1 + 2)
print("2 -", c1, "=", 2 - c1)
print(c1, "- 2 =", c1 - 2)
print("2 /", c1, "=", 2 / c1)
print(c1, "/ 2 =", c1 / 2)
print()

# Equality Tests
print("Equality Tests")
print(c1 == c1, c1 != c1)
print(1 == c1, c1 == 1)
print(1 != c1, c1 != 1)
print()

# Chained Operations
print("Chained Operations")
c10 = cnum.cnum(5, 12)
c11 = cnum.cnum(12, 15)
c12 = cnum.cnum(3, 18)
c13 = cnum.cnum(15, 1)
print((c12 + c13) ** (-2) / (c10 + c11) ** (-3))