import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from sympy import symbols, solve, Matrix, im, re

w_list = np.arange(0, 10, 0.1)

x, y, N, ω = symbols('x, y, N, ω')
ϕ = 0.2
dx = x * (1 - x / 7) - ω * x * y / (1 + x)
dy = ϕ * y * (1 - N * y / x)

re1 = np.zeros(len(w_list))
re2 = np.zeros(len(w_list))
im1 = np.zeros(len(w_list))
im2 = np.zeros(len(w_list))

for i, w in enumerate(w_list):
    dx_chosen = dx.subs(ω, w)
    solutions = solve([dx_chosen, dy], [x, y])
    for sol in solutions:
        if sol[0] == sol[1]:
            solution = sol
    jac = Matrix([dx_chosen, dy]).jacobian([x, y])
    jac_solution = jac.subs(x, solution[0]).subs(y, solution[1])
    eigen_values = list(jac_solution.eigenvals())
    re_temp = []
    im_temp = []
    for eigen_value in eigen_values:
        if re(eigen_value):
            re_temp.append(re(eigen_value))
        else:
            re_temp.append(0)

        if im(eigen_value):
            im_temp.append(im(eigen_value))
        else:
            im_temp.append(0)
    re_temp.sort()  #smallest from
    im_temp.sort()
    re1[i] = re_temp[0]
    re2[i] = re_temp[1]
    im1[i] = im_temp[0]
    im2[i] = im_temp[1]

bifs = []
for i in range(1, len(w_list) - 2):
    if re1[i] < 0 < re1[i + 1] or re1[i] > 0 > re1[i + 1]:
        y1, y2 = re1[i], re1[i + 1]
        x1, x2 = w_list[i], w_list[i + 1]
        bifs.append(x1 - y1 * (x2 - x1) / (y2 - y1))

_, ax = plt.subplots(dpi=100)

ax.plot(w_list, re1, color='b', label='real')
ax.plot(w_list, re2, color='b')
ax.plot(w_list, im1, color='y', label='imaginary')
ax.plot(w_list, im2, color='y')
ax.plot(bifs, [0] * len(bifs), 'ro', label="bifurcations")
ax.set(xlim=(0, 10), ylim=(-1, 0.6), title='Eigenvalues of Function')
ax.legend()
plt.show()
