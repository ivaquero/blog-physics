from sympy import expand, lcm, LM, LT, symbols


def s_polynomial(f, g):
    return expand(lcm(LM(f), LM(g)) * (1 / LT(f) * f - 1 / LT(g) * g))


x, y, z = symbols('x y z')

f, g = [x - 13 * y**2 - 12 * z**3, x**2 - x * y + 92 * z]

s = s_polynomial(f, g)

s  # −13xy2+ xy−12xz3−92z
