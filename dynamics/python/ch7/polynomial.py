from sympy import symbols, reduced

x, y, z = symbols('x y z')
f = x**4 + y**4 + z**4
p = reduced(f, [x**2 + y, z**2 * y - 1, y - z**2])

print(p)
# ([x**2-y, y**2+2, y**3+2*y], z**4+2)

q = reduced(f, [y - z**2, z**2 * y - 1, x**2 + y])
print(q)
# ([-x**2+ y**3+ y**2*z**2+ y*z**4+z**6+z**2, 0, x**2-z**2], z**8+2*z**4)
