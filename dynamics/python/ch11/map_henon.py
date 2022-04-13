import numpy as np
import matplotlib.pyplot as plt

a = 1.2  # Set a= 1 to get Figure 14.23(a)
b = 0.4
num_iterations = 10000


def henon(X):
    x, y = X
    xn = 1 - a * x * x + y
    yn = b * x
    return xn, yn


X0 = [(1 - b) / 2, (1 - b) / 2]

X, Y = [], []

for i in range(100):
    xn, yn = henon(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

X, Y = [], []
for i in range(num_iterations):
    xn, yn = henon(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

_, ax = plt.subplots(dpi=100)

ax.plot(X, Y, 'b.', ms=1)
ax.set(xlabel='x', ylabel='y')
plt.show()
