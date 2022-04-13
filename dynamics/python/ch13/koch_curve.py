import numpy as np
import matplotlib.pyplot as plt

k = 6
n_lines = 4**k
h = 3**(-k)
x = [0] * (n_lines + 1)
y = [0] * (n_lines + 1)
x[0], y[0] = 0, 0

segment = [0] * n_lines

# The angles of the four segments.
angle = [0, np.pi / 3, -np.pi / 3, 0]
for i in range(n_lines):
    m = i
    ang = 0
    for j in range(k):
        segment[j] = np.mod(m, 4)
        m = np.floor(m / 4)
        ang = ang + angle[int(segment[j])]

    x[i + 1] = x[i] + h * np.cos(ang)
    y[i + 1] = y[i] + h * np.sin(ang)

_, ax = plt.subplots()

ax.axis('equal')
ax.plot(x, y)
plt.show()
