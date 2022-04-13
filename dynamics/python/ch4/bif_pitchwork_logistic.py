import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.solvers import solve
from scipy.optimize import brentq


def logistic(X, h, a):
    return (X * (1 - X) - h * X / (a + X))


def function(X, h, a):
    return lambda X: X * (1 - X) - h * X / (a + X)


def stablity(X_init, h, a):
    perturbation = 0.01
    time_interval = 0.01
    x = []
    X = X_init + perturbation
    for i in range(50):
        X += time_interval * logistic(X, h, a)
    return abs(X - X_init) <= perturbation


def bifurication(a_values=np.arange(0, 1, 0.1),
                 h_values=np.arange(0, 1, 0.01),
                 x_values=np.arange(0.01, 1, 0.01)):
    final_xs, final_ys = [], []
    final_x, final_y = [], []
    for a in a_values:
        x_s, y_s = [], []
        x_i, y_i = [], []
        for h in h_values:
            values = logistic(x_values, h, a)
            x_list = []
            for i in range(len(values) - 1):
                if (values[i] <= 0 and values[i + 1] >= 0) or (
                        values[i] >= 0 and
                        values[i + 1] <= 0):  # Find low precision null_point
                    x_list.append(x_values[i + 1])
            # Find null_points:
            null_points = np.zeros(len(x_list))
            for ind, x in enumerate(x_list):
                if np.sign(logistic((x - 0.02), h, a)) != np.sign(
                        logistic((x + 0.02), h, a)
                ):  # Avoid cases such as -x^2 with same sign along both sides
                    null_points[ind] = brentq(
                        function(X, h, a), x - 0.02,
                        x + 0.02)  # Find high precision null_point
                else:
                    null_points[ind] = x
                # 0.01 is the spacing between 2 points with different sign -> 0.02 certainly
            for null_point in null_points:
                if stablity(null_point, h, a):
                    x_s.append(h)
                    y_s.append(null_point)
                else:
                    x_i.append(h)
                    y_i.append(null_point)
        final_xs.append(x_s)
        final_ys.append(y_s)
        final_x.append(x_i)
        final_y.append(y_i)
    return final_xs, final_ys, final_x, final_y


X = symbols('X', nonzero=True)
final_xs, final_ys, final_x, final_y = bifurication()

_, ax = plt.subplots()

ax.scatter(final_xs, final_ys, color='g')
ax.scatter(final_x, final_y, color='r')
plt.show()
