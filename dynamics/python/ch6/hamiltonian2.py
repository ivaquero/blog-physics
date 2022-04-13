import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D


def hamiltonian_4d(t, X, w1, w2):
    p1, p2, q1, q2 = X
    dp1 = -w1 * q1
    dp2 = -w2 * q2
    dq1 = w1 * p1
    dq2 = w2 * p2
    return (dp1, dp2, dq1, dq2)


w1, w2 = np.sqrt(2), 1
t_span = [0, 100]
n_points = 2000
z = 0.5, 1.5, 0.5, 0

sol = solve_ivp(hamiltonian_4d, t_span, z, args=(w1, w2), dense_output=True)

t = np.linspace(t_span[0], t_span[1], 2000)
X = sol.sol(t)
p1, p2, q1, q2 = X

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

ax.plot(p1, q1, q2, 'b-', lw=0.5)
ax.set(xlabel=r'$p_1$',
       ylabel=r'$q_1$',
       zlabel=r'$q_2$',
       title='H=1.365416000')
plt.show()
