import numpy as np
import matplotlib.pyplot as plt
import os

ts = np.arange(0, 4, 0.01)


def FHN_coupled(Z, I_ext, R=45, a=0.1, γ=0.5, ϵ=0.008):
    V_1, w_1, V_2, w_2 = Z
    I_c21 = (V_2 - V_1) / R
    I_c12 = (V_1 - V_2) / R

    V_1_ = (1 / ϵ) * (-w_1 + V_1 * (1 - V_1) * (V_1 - a) + I_c21 + I_ext)
    w_1_ = V_1 - γ * w_1
    V_2_ = (1 / ϵ) * (-w_2 + V_2 * (1 - V_2) * (V_2 - a) + I_c12)
    w_2_ = V_2 - γ * w_2

    return [V_1_, w_1_, V_2_, w_2_]


def euler(cond, step_size=0.01, period=len(ts)):
    start_puls, stop_puls, recover_puls = cond
    v_1, w_1, v_2, w_2 = [], [], [], []
    i_ext = []
    V_1, W_1, V_2, W_2 = 0, 0, 0, 0
    for t in ts:
        v_1.append(V_1)
        w_1.append(W_1)
        v_2.append(V_2)
        w_2.append(W_2)
        last_derivatives = [v_1[-1], w_1[-1], v_2[-1], w_2[-1]]
        if start_puls <= t <= stop_puls:
            V_1 += step_size * FHN_coupled(last_derivatives, recover_puls)[0]
            W_1 += step_size * FHN_coupled(last_derivatives, recover_puls)[1]
            V_2 += step_size * FHN_coupled(last_derivatives, recover_puls)[2]
            W_2 += step_size * FHN_coupled(last_derivatives, recover_puls)[3]
            i_ext.append(recover_puls)
        else:
            V_1 += step_size * FHN_coupled(last_derivatives, 0)[0]
            W_1 += step_size * FHN_coupled(last_derivatives, 0)[1]
            V_2 += step_size * FHN_coupled(last_derivatives, 0)[2]
            W_2 += step_size * FHN_coupled(last_derivatives, 0)[3]
            i_ext.append(0)
    return v_1, w_1, v_2, w_2, i_ext


v_1, w_1, v_2, w_2, i_ext = euler([1, 1.20, 0.025])

_, ax = plt.subplots()

ax.set(xlim=(0, 4), ylim=(-0.35, 1))
ax.plot(ts, v_1, label='neuron 1')
ax.plot(ts, v_2, label='neuron 2')
ax.plot(ts, i_ext, label='power surge', title='2 connected neurons')
ax.legend()
plt.show()
