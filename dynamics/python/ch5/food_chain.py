import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a1, a2 = 5, 0.1
b1, b2 = 3, 2
d1, d2 = 0.4, 0.01


def food_chain(t, init0):
    X, Y, Z = init0
    dX = X * (1 - X) - a1 * X / (1 + b1 * X) * Y
    dY = a1 * X / (1 + b1 * X) * Y - d1 * Y - a2 * Y / (1 + b2 * Y) * Z
    dZ = a2 * Y / (1 + b2 * Y) * Z - d2 * Z
    return [dX, dY, dZ]


t_span = [0, 400]
t = np.linspace(t_span[0], t_span[1], 1000)
z0 = [1, 0.5, 8]

fig = plt.figure()
ax = fig.add_subplot(121)

sol = solve_ivp(food_chain, t_span, z0, dense_output=True)
X = sol.sol(t).T
x, y, z = X[:, 0], X[:, 1], X[:, 2]
ax.plot(t, x, label='Plant')
ax.plot(t, y, label='Herbivoor')
ax.plot(t, z, label='Carnivoor')
ax.set(xlabel='Time', ylabel='Population')
ax.legend(loc='right')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(x, y, z)

plt.show()
