import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from sympy import symbols


def opinion(X, a):
    return (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X)


def function(X, a):
    return lambda X: (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X)


def stability(X_init, a):
    perturbation = 0.01
    time_interval = 0.01
    x = []
    X = X_init + perturbation
    for _ in range(50):
        X += time_interval * opinion(X, a)
    return abs(X - X_init) <= perturbation


def pitchwork(a_vals, x_vals):
    final_xs, final_ys = [], []
    final_x, final_y = [], []

    for a in a_vals:
        values = opinion(x_vals, a)
        x_list = []
        for i in range(len(values) - 1):
            if (values[i] <= 0
                    and values[i + 1] >= 0) or (values[i] >= 0
                                                and values[i + 1] <= 0):
                x_list.append(x_vals[i + 1])
        # find null_points:
        null_points = np.zeros(len(x_list))
        for x in x_list:
            null_points[i] = brentq(function(X, a), x - 0.02, x + 0.02)
            # 0.01 is the spacing between 2 points with different sign -> 0.02 certainly
        for null_point in null_points:
            if stability(null_point, a):
                final_xs.append(a)
                final_ys.append(null_point)
            else:
                final_x.append(a)
                final_y.append(null_point)
    return final_xs, final_ys, final_x, final_y


a = 1.3
x = np.arange(-1, 1, 0.01)

a_vals = np.arange(-1, 2, 0.01)
x_vals = np.arange(-1, 1, 0.01)

X = symbols('X')
final_xs, final_ys, final_x, final_y = pitchwork(a_vals, x_vals)

_, ax = plt.subplots()

ax.scatter(final_xs, final_ys, color='g')
ax.scatter(final_x, final_y, color='r')
plt.show()
