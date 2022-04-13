import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')


def HPG(t, init):
    P, H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    p = H - 0.2 * P
    g = P - 0.2 * G
    return [p, h, g]


def euler3(xyz_init, step_size, period):
    P, H, G = xyz_init
    x, y, z = [], [], []
    # For the arrow:
    dx, dy, dz = np.zeros(period), np.zeros(period), np.zeros(period)

    for i in range(0, period):
        x.append(P)
        y.append(H)
        z.append(G)
        dP, dH, dG = HPG(t=0, init=[x[-1], y[-1], z[-1]])
        P += step_size * dP
        H += step_size * dH
        G += step_size * dG
        dx[i], dy[i], dz[i] = dP, dH, dG

    return x, y, z, dx, dy, dz


xyz_init = [1, 0.2, 2]
step_size, period = 0.1, 1000
x, y, z, dx, dy, dz = euler3(xyz_init, step_size, period)

for i in range(100, 1000, 400):
    ax.quiver(x[i], y[i], z[i], dx[i], dy[i], dz[i], color='red')

ax.plot(x, y, z, label='Limit Cycle of HPG', color='r')
ax.legend()


def HPG2(t, init):
    H, G = init
    h = 1 / (1 + G**9) - 0.2 * H
    g = H - 0.2 * G
    return [h, g]


ax2 = fig.add_subplot(122)

t_span = [0, 100]
t = np.linspace(t_span[0], t_span[1], 1000)

# Number of starting points:
θs = np.linspace(0, 2 * np.pi, 5)
coordinates = []

for θ in θs:
    coordinates.append([1.5 * np.cos(θ), 1.5 * np.sin(θ)])
    coordinates.append([0.05 * np.cos(θ), 0.05 * np.sin(θ)])
for coordinate in coordinates:
    x_i = coordinate[0]
    y_i = coordinate[1]
    sol = solve_ivp(HPG2, t_span, [x_i, y_i], dense_output=True)
    X = sol.sol(t).T
    x, y = X[:, 0], X[:, 1]
    ax2.plot(x, y)

# ax2.set(xlim=(-2, 2)
# ax2.set(ylim=(-2, 4)
plt.show()
