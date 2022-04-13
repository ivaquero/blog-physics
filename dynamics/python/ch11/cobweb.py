import numpy as np
import matplotlib.pyplot as plt


def logistic_map(X, r):
    return r * X * (1 - X)


fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

r = 4
X_init = 0.01
step = 50


def cobweb(step, X_init, r):
    X, Y = [], []

    X.append(X_init)
    Y.append(0)
    for stap in range(step):
        Y.append(logistic_map(X[-1], r))
        X.append(X[-1])
        ax1.plot(X[-2:], Y[-2:], color='b')
        X.append(Y[-1])
        Y.append(Y[-1])
        ax1.plot(X[-2:], Y[-2:], color='b')


ax1.set(xlim=(0, 1), ylim=(0, 1.1))
cobweb(step, X_init, r)

T = np.arange(0, 1, 0.001)
X = logistic_map(T, 4)

ax1.plot(T, X, color='black')
ax1.plot(T, T, color='grey')

ax2.set(xlim=(0, step), ylim=(0, 1.1))
T = np.arange(0, step, 1)
X = np.zeros(step)


def stepwise(initX, r, period=len(T)):
    X[0] = initX
    for i in range(1, period):
        X[i] = logistic_map(X[i - 1], r)
    return X


X = stepwise(X_init, r)
ax2.plot(T, X, color='b')
ax2.scatter(T, X, color='black')
plt.show()
