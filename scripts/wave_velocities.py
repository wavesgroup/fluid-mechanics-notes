import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.rcParams["font.size"] = 16


# Elevation
def η(a, ψ):
    return a * np.cos(ψ)


# Velocity potential
def ϕ(a, ω, k, z, ψ, g):
    return a * g / ω * np.cosh(k * (z + h)) / (k * np.cosh(k * h)) * np.sin(ψ)


# Horizontal velocity
def u(a, ω, k, z, ψ):
    return a * ω * np.cosh(k * (z + h)) / np.cosh(k * h) * np.cos(ψ)


# Vertical velocity
def w(a, ω, k, z, ψ):
    return a * ω * np.cosh(k * (z + h)) / np.cosh(k * h) * np.sin(ψ)


# Horizontal displacement
def ζ(a, k, z, ψ):
    return -a * np.cosh(k * (z + h)) / np.cosh(k * h) * np.sin(ψ)


# Vertical displacement
def ξ(a, k, z, ψ):
    return a * np.cosh(k * (z + h)) / np.cosh(k * h) * np.cos(ψ)


# Angular frequency
def ω(g, k, h):
    return np.sqrt(g * k * np.tanh(k * h))


ψ = np.linspace(0, 2 * np.pi, 100, endpoint=False)
z = np.arange(-1, 0.21, 0.01)

g = 9.8
a = 0.1
k = 1
h = 100

ψ_, z_ = np.meshgrid(ψ, z)
η_ = η(a, ψ_)
ζ_ = z_ + η_

# Evaluate potential and velocities at z + η
ϕ_ = ϕ(a, ω(g, k, h), k, ζ_, ψ_, g)
u_ = u(a, ω(g, k, h), k, ζ_, ψ_)
w_ = w(a, ω(g, k, h), k, ζ_, ψ_)


fig, ax = plt.subplots(figsize=(16, 4))
im = ax.contourf(ψ_, ζ_ - z.max(), ϕ_, np.arange(-0.5, 0.55, 0.05), cmap=cm.bwr)
plt.colorbar(im, ax=ax)
ax.plot(ψ, η(a, ψ), "k-")
ax.plot(ψ, 0 * ψ, "k--")
ax.set_ylim(-1, 0.2)
ax.set_yticks(np.arange(-1, 0.4, 0.2))
ax.set_xticks(np.linspace(0, 2 * np.pi, 5))
ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
ax.set_xlabel("ψ")
ax.set_ylabel("z (m)")
ax.set_title("Velocity potential (m²/s), $a = 0.1$ m, $k = 1$ rad m$^{-1}$")
ax.set_aspect("equal")
plt.tight_layout()
plt.savefig("../assets/fig_wave_potential.png", dpi=150)
plt.close()


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8))

im1 = ax1.contourf(ψ_, ζ_ - z.max(), u_, np.arange(-0.5, 0.55, 0.05), cmap=cm.bwr)
plt.colorbar(im1, ax=ax1)
ax1.plot(ψ, η(a, ψ), "k-")
for xx in np.arange(np.pi / 4, 2 * np.pi, np.pi / 4) / k:
    for zz in np.arange(-0.8, -0, 0.2):
        ax1.plot(xx + ζ(a, k, zz, ψ), zz + ξ(a, k, zz, ψ), "k-", alpha=0.6)
ax1.plot(ψ, 0 * ψ, "k--")
ax1.set_title("Horizontal velocity (m/s), $a = 0.1$ m, $k = 1$ rad m$^{-1}$")

im2 = ax2.contourf(ψ_, ζ_ - z.max(), w_, np.arange(-0.5, 0.55, 0.05), cmap=cm.bwr)
plt.colorbar(im2, ax=ax2)
ax2.plot(ψ, η(a, ψ), "k-")
for xx in np.arange(np.pi / 4, 2 * np.pi, np.pi / 4) / k:
    for zz in np.arange(-0.8, -0, 0.2):
        ax2.plot(xx + ζ(a, k, zz, ψ), zz + ξ(a, k, zz, ψ), "k-", alpha=0.6)
ax2.plot(ψ, 0 * ψ, "k--")
ax2.set_title("Vertical velocity (m/s), $a = 0.1$ m, $k = 1$ rad m$^{-1}$")

for ax in [ax1, ax2]:
    ax.set_ylim(-1, 0.2)
    ax.set_yticks(np.arange(-1, 0.4, 0.2))
    ax.set_xlabel("ψ")
    ax.set_ylabel("z (m)")
    ax.set_xticks(np.linspace(0, 2 * np.pi, 5))
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax.set_aspect("equal")

plt.tight_layout()
plt.savefig("../assets/fig_wave_velocities.png", dpi=150)
plt.close()
