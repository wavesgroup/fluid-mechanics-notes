import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.rcParams["font.size"] = 16

k1 = 1
k2 = 1.1

a = 0.1
h = 100
g = 9.8

omega1 = np.sqrt(g * k1 * np.tanh(k1 * h))
omega2 = np.sqrt(g * k2 * np.tanh(k2 * h))

x = np.linspace(0, 2e2, 1000)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, a * np.cos(k1 * x) + a * np.cos(k2 * x))
ax.set_xlim(0, 2e2)
ax.set_xlabel("x (m)")
ax.set_ylabel("Surface elevation (m)")
ax.set_title("Superposition of two waves with wavenumbers 1 and 1.1 rad/m")
ax.grid()
plt.tight_layout()
plt.savefig("../assets/fig_wave_group.png", dpi=150)
plt.close()
