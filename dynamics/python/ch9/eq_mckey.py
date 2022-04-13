import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

ts = np.arange(0, 10, 0.01)
τ = 0.2
n_list = np.arange(1, 10, 1)
L, Vmax = 6, 16


def mckey_glass(X, X_τ, n):
    return L - (Vmax * X_τ**n) / (1 + X_τ**n) * X


def euler(X_init, n, τ=0.2, period=len(ts), step_size=0.01):
    X = X_init
    x = []
    for i in range(0, period):
        x.append(X)
        if ts[i] <= τ:
            X_τ = 0.5
        else:
            X_τ = x[i - int(τ / step_size)]
        X += step_size * mckey_glass(x[-1], X_τ, n)
    return x


fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    ax.set(xlim=(0, 10), ylim=(0, 4), xlabel='time', title=f'n={n_list[i]}')
    X = euler(2, n_list[i])
    ax.plot(ts, X)


anim = FuncAnimation(fig, animate, frames=len(n_list), interval=200)
plt.show()
