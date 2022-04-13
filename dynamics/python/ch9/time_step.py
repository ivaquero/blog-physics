import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, lambdify

ξ, t, i = symbols('xi t i')


def ϕ(i, t):
    if i == 0:
        return 1  # Initial history x(t) = 1 on [-1, 0]
    else:
        return ϕ(i - 1, i - 1) - integrate(ϕ(i - 1, ξ - 1), (ξ, i - 1, t))


tmax = 10
x = [ϕ(j, t) for j in range(tmax + 1)]

expressions = [lambdify(t, x[i]) for i in range(tmax + 1)]

t = np.linspace(-1, 10, 1000)

conditions = [
    t <= 0, t > 0, t > 1, t > 2, t > 3, t > 4, t > 5, t > 6, t > 7, t > 8,
    t > 9
]

_, ax = plt.subplots(dpi=100)

ax.plot(t, np.piecewise(t, conditions, expressions))

ax.set(xlabel='t', ylabel='x(t)')
plt.show()
