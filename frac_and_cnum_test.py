import frac, cnum

f1 = frac.frac(1, 2)
f2 = frac.frac(2, 3)
f3 = frac.frac(1, 3)
f4 = frac.frac(3, 4)
c1 = cnum.cnum(f1, f2)
c2 = cnum.cnum(f3, f4)

print("Comp Nums with Frac Parts")
print(c1, c2)
print()

print("Add")
print(c1 + c2)
print()

print("Subtract")
print(c1 - c2)
print()

print("Multiply")
print(c1 * c2)
print()

print("Division")
print(c1 / c2)
print()

print("Negation")
print(-c1)
print()

print("Exponentiation")
print(c1 ** 3)
print()

print("Magnitude")
print(abs(c1))
print()

print("Comparison")
f1 = frac.frac(3, 12)
f2 = frac.frac(2, 8)
f3 = frac.frac(2, 12)
f4 = frac.frac(3, 18)
f5 = frac.frac(1, 5)
c1 = cnum.cnum(f1, f3)
c2 = cnum.cnum(f2, f4)
c3 = cnum.cnum(f1, f5)
print(c1 == c2, c1 == c3, c1 != c2, c1 != c3)
