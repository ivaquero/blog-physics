import numpy as np
import matplotlib.pyplot as plt


def logistic_map(X, r):
    return r * X * (1 - X)


T = np.arange(0, 500, 1)
X = np.zeros(500)
X_ = np.arange(0, 1, 0.001)
f = 4 * X_ * (1 - X_)


def ppen(initX, r, period=len(T)):
    X[0] = initX
    for i in range(1, period):
        X[i] = logistic_map(X[i - 1], r)
    return X


X = ppen(0.4, 4)

_, ax = plt.subplots()

ax.scatter(X[:-1], X[1:])
ax.plot(X_, f)
plt.show()
