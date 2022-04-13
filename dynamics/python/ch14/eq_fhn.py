import numpy as np
import matplotlib.pyplot as plt
import os

_, axes = plt.subplots(1, 2, constrained_layout=True)
ts = np.arange(0, 4, 0.01)


def FHN(V, w, I, a=0.1, γ=1, ϵ=0.01):
    V_ = (1 / ϵ) * (-w + V * (1 - V) * (V - a) + I)
    w_ = V - γ * w
    return [V_, w_]


def euler(cond, step_size=0.01, period=len(ts)):
    start_puls, stop_puls, recover_puls = cond
    v, w = [], []
    i_ext = []
    V, W = 0, 0
    for t in ts:
        v.append(V)
        w.append(W)
        if start_puls <= t <= stop_puls:
            V += step_size * FHN(v[-1], w[-1], recover_puls)[0]
            W += step_size * FHN(v[-1], w[-1], recover_puls)[1]
            i_ext.append(recover_puls)
        else:
            V += step_size * FHN(v[-1], w[-1], 0)[0]
            W += step_size * FHN(v[-1], w[-1], 0)[1]
            i_ext.append(0)
    return v, w, i_ext


v, w, i_ext = euler([1, 1.20, 0.01])

axes[0].set(xlim=(0, 4),
            ylim=(-0.35, 1),
            title='$I_{ext} = 0.01$ from 1 to 1.20s')
axes[0].plot(ts, v, label='neuron')
axes[0].plot(ts, i_ext, label='power surge', color='r')
axes[0].legend()

v_, w_, i_ext_ = euler([1, 1.20, 0.03])

axes[1].plot(ts, v_, label='neuron')
axes[1].plot(ts, i_ext_, label='power surge', color='r')
axes[1].set(xlim=(0, 4),
            ylim=(-0.35, 1),
            title='$I_{ext} = 0.03$ from 1 to 1.20s')

axes[1].legend()

plt.show()
