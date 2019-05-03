import frac

print('A Few Fractions')
f1 = frac.frac(12, 15)  # Reduce to 4/5
f2 = frac.frac(27, 8)  # Irreducible
f3 = frac.frac(5, -2)  # Neg fraction is always neg numer over pos denom
f4 = frac.frac(-5, -2)  # Represent as 5/2
f5 = frac.frac(42)  # Represent as 42/1
f6 = frac.frac(0) # Represent as 0/1
print(f1, f2, f3, f4, f5, f6)
print(type(f1), type(f5))  # Should be type frac.
print()

print("Negation and Absolute Value")
print(-f1, --f1)
print(abs(f1), abs(f3))
print()

print('Two-Frac Operations')
f1 = frac.frac(1, 2)
f2 = frac.frac(-2, 3)
print(f1, '+', f2, '=', f1 + f2)
print(f1, '-', f2, '=', f1 - f2)
print(f1, '*', f2, '=', f1 * f2)
print(f1, '/', f2, '=', f1 / f2)
print(f1, '** 3 =', f1 ** 3)
print(f1, '** -3 = ', f1 ** -3)
print()

print('Chained Operations')
f3 = frac.frac(5, 4)
print(f1, '+', f2, '*', f3, '=', f1 + f2 * f3)
print(f3, '/', f1, '-', f3, '=', f3 / f1 - f3)
print()

print('Operations with Ints and Floats')
# Handle a non-frac on the left and on the right
print('3 + ', f2, '=', 3 + f2)
print('3.0 + ', f2, '=', 3.0 + f2)
print(f2, '+ 3 =', f2 + 3)
print(f2, '+ 3.0 =', f2 + 3.0)
print('3 - ', f2, '=', 3 - f2)
print('3.0 - ', f2, '=', 3.0 - f2)
print(f2, '- 3 =', f2 - 3)
print(f2, '- 3.0 =', f2 - 3.0)
print('3 *', f2, '=', 3 * f2)
print('3.0 *', f2, '=', 3.0 * f2)
print(f2, '* 3 =', f2 * 3)
print(f2, '* 3.0 =', f2 * 3.0)
print('3 /', f2, '=', 3 / f2)
print('3.0 /', f2, '=', 3.0 / f2)
print(f2, '/ 3 =', f2 / 3)
print(f2, '/ 3.0 =', f2 / 3.0)
print()

print('Comparison')
f1 = frac.frac(2, 3)
f2 = frac.frac(3, 4)
print(f1 == f1, f1 != f1, f1 != f2)
print(f1 == 1, 1 == f1, f1 != 1, 1 != f1, f2 == 0.75, 0.75 == f2, f2 != 0.75, 0.75 != f2)
print(f1 < f2, f2 < f1, f1 < 1, f1 < 1.0, f1 <= f1, f2 <= f1, f2 <= 0.75, f2 <= 0.7)
print()

print("Type Conversion")
f1 = frac.frac(2, 3)
f2 = frac.frac(15, 4)
print(float(f1), float(f2))
print(int(f1), int(f2))
print()

print("Nasty fracs")
f1 = frac.frac(127, 2985)
f2 = frac.frac(3981, 371)
print(f1 ** 2 + f2)
f3 = frac.frac(1, 2)
f4 = frac.frac(2, 3)
f5 = frac.frac(3, 4)
print((f3 ** 2 + f4 ** 3) / (f5 - 5))
f6 = frac.frac(510510, 44100)
f7 = frac.frac(6636630, 573302)
print(f6 == f7, f6 < f7, f6 > f7, f6 - f7, float(f6 - f7))