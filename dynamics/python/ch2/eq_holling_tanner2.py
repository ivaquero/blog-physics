import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, Matrix, im

w_list = np.arange(0, 10, 0.1)

x, y, N, ω = symbols('x, y, N, ω')
ϕ = 0.2
dx = x * (1 - x / 7) - ω * x * y / (1 + x)
dy = ϕ * y * (1 - N * y / x)


def stability_2d(eigen_values):
    eig1, eig2 = tuple(eigen_values)
    stability = np.zeros(5)
    if im(eig1) < 10**-10 and im(eig2) < 10**-10:
        if eig1 < 0 and eig2 < 0:
            stab_type = "Stable node"
            stability[0] = 1
        elif eig1 > 0 and eig2 > 0:
            stab_type = "Unstable node"
            stability[1] = 1
        else:
            stab_type = "Saddle point"
            stability[2] = 1
    elif re(eig1) < 0:
        stab_type = "Stable spiral"
        stability[3] = 1
    else:
        stab_type = "Unstable spiral or limit cycle"
        stability[4] = 1
    return stab_type, stability


_, ax = plt.subplots(dpi=100)

for w in w_list:
    dx_chosen = dx.subs(ω, w)
    solutions = solve([dx_chosen, dy], [x, y])
    for sol in solutions:
        if sol[0] == sol[1]:
            solution = sol
            jac = Matrix([dx_chosen, dy]).jacobian([x, y])
            jac_solution = jac.subs(x, solution[0]).subs(y, solution[1])
            eigen_values = jac_solution.eigenvals()
            stab_type, stability = stability_2d(eigen_values)
            if stability[0] == 1 or stability[3] == 1:
                ax.scatter(w, solution[0], color='g')
            else:
                ax.scatter(w, solution[0], color='r')

plt.show()
