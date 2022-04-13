import numpy as np
import matplotlib.pyplot as plt

n_points = 16000
result = []
λs = []
maps = []
xmin, xmax = 3, 4
mult = (xmax - xmin) * n_points

μs = np.arange(xmin, xmax, 20 / n_points)

for r in μs:
    x = 0.1
    result = []
    for t in range(100):
        x = r * x * (1 - x)
        result.append(np.log(abs(r - 2 * r * x)))
    λs.append(np.mean(result))
    # Ignore first 100 iterates.
    for t in range(20):
        x = r * x * (1 - x)
        maps.append(x)

_, ax = plt.subplots()

xticks = np.linspace(xmin, xmax, mult)
zero = [0] * mult
ax.plot(xticks, zero, 'k-')
ax.plot(xticks, maps, 'r.', ms=3, label='Logistic map')
ax.plot(μs, λs, 'b-', lw=1, label='Lyapunov exponent')
ax.grid('on')

ax.set(xlabel='$μ$',
       ylim=(-1, 1),
       title='Logistic map versus Lyapunov exponent')
ax.legend(loc='best')
plt.show()
