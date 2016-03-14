import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import seaborn as sns

def dvdt(v, t, alpha, rho, beta): 
    x, y, z = v
    return alpha * (y - x), x * (rho - z) - y, x * y - beta * z

alpha = 10
rho = 28
beta = 8/3

t = np.linspace(0, 4, 1000)
v0 = [1, 1, 1]

v = odeint(dvdt, v0, t, (alpha, rho, beta))

fig, ax = plt.subplots(4, 1, sharex=False, sharey=False, figsize=(10, 20))
ax[0].plot(t, v[:, 0])
ax[0].plot(t, v[:, 1])
ax[0].plot(t, v[:, 2])
ax[0].set(xlabel='Time', ylabel='Displacement')
ax[1].plot(v[:,0], v[:,1])
ax[1].set(xlabel='Displacement in x', ylabel='Displacement in y')
ax[2].plot(v[:,1], v[:,2])
ax[2].set(xlabel='Displacement in y', ylabel='Displacement in z')
ax[3].plot(v[:,0], v[:,2])
ax[3].set(xlabel='Displacement in x', ylabel='Displacement in z')
sns.despine()