import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.solvers import solve
from matplotlib import colors


def budworm(X, k, r):
    return r * X * (1 - X / k) - (X**2) / (1 + X**2)


def stablity(X_init, k, r):
    perturbation = 0.01
    time_interval = 0.01
    x = []
    X = X_init + perturbation
    for i in range(100):
        X += time_interval * budworm(X, k, r)
    return abs(X - X_init) <= perturbation


def track_in_3D(rs, ks):
    X = symbols('X', real=True)
    stable_points = [[], [], []]
    unstable_points = [[], [], []]
    for r in rs:
        for k in ks:
            equilibria = np.zeros(2)
            X_value = solve(r * (1 - X / k) - X / (1 + X**2), X)
            if X_value != []:
                equilibria[1] = X_value[0]
            for x in equilibria:
                if stablity(x, k, r):
                    stable_points[0].append(k)
                    stable_points[1].append(r)
                    stable_points[2].append(x)
                else:
                    unstable_points[0].append(k)
                    unstable_points[1].append(r)
                    unstable_points[2].append(x)

    return stable_points, unstable_points


n_points = 20
r_range = [0, 0.6]
k_range = [0, 40]
rs = np.linspace(r_range[0], r_range[1], n_points)
ks = np.linspace(k_range[0], k_range[1], n_points)
stable_points, unstable_points = track_in_3D(rs, ks)

fig, ax = plt.subplots()

ax = fig.axes(projection="3d")

ax.scatter(stable_points[0], stable_points[1], stable_points[2], color='g')
ax.scatter(unstable_points[0],
           unstable_points[1],
           unstable_points[2],
           color='r')

plt.show()
