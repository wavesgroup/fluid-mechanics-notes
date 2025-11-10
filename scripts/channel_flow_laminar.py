import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams.update({"font.size": 14})


def channel_laminar_velocity(z, δ, τ_w, ρ, ν):
    return τ_w * z / (ρ * ν) * (1 - z / (2 * δ))


def channel_laminar_centerline_velocity(δ, τ_w, ρ, ν):
    return τ_w * δ / (2 * ρ * ν)


fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
δ = 0.05
τ_w = 0.01
ρ = 1e3
ν = 1e-6

z = np.linspace(0, 2 * δ, 1000)
u_bulk = channel_laminar_velocity(z, δ, τ_w, ρ, ν)

ax.plot(u_bulk, z / (2 * δ), label="Bulk Velocity Profile", color="tab:blue", lw=3)
ax.plot([0, 0.25], [0.5, 0.5], "k:")

ax.set_xlabel(r"$\overline{u}$ (m/s)")
ax.set_ylabel(r"$z/(2\delta)$")
ax.set_xlim(0, 0.25)
ax.set_ylim(0, 1)
ax.set_title(r"δ = 0.05 m, τ$_w$ = 0.01 N/m², ρ = 10$^3$ kg/m³, ν = 10$^{-6}$ m²/s")
plt.tight_layout()
plt.savefig("fig_channel_flow_laminar_u.pdf")
plt.close()
