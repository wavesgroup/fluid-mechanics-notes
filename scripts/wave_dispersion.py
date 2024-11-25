import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.rcParams["font.size"] = 16

# Angular frequency
def ω(g, k, h):
    return np.sqrt(g * k * np.tanh(k * h))

g = 9.8
k = np.linspace(1e-2, 1e2, 1000)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(ω(g, k, 1000) / (2 * np.pi), k, "k-")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Wavenumber (rad/m)")
ax.set_title("Wave dispersion")
ax.set_xlim(0, 5)
ax.set_ylim(0, 100)
ax.grid()
plt.tight_layout()
plt.savefig("../assets/fig_wave_dispersion.png", dpi=150)
plt.close()