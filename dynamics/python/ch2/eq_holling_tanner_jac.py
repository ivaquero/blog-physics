from sympy import symbols, solve, Matrix

x, y, N = symbols('x, y, N')
ϕ, ω = 0.2, 6 / 7
dx = x * (1 - x / 7) - ω * x * y / (1 + x)
dy = ϕ * y * (1 - N * y / x)
dy = dy.subs(N, .5)
sol = solve([dx, dy], [x, y])
print(sol)
dy = dy.subs(N, 1)
sol = solve([dx, dy], [x, y])
print(sol)

jac = Matrix([dx, dy]).jacobian([x, y])
print(jac)
jac_solution = jac.subs(x, sol[1][0]).subs(y, sol[1][1])
print(jac_solution)
print('eigenvalues:')
print(list(jac_solution.eigenvals()))
print('With the corresponding own vectors:')
print([list(tup[2][0]) for tup in jac_solution.eigenvects()])
