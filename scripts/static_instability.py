import numpy as np
import matplotlib.pyplot as plt


def parcel_displacement(z0: float, N2: float, t: float) -> float:
    """Given initial parcel displacement z0, buoyancy frequency squared N2,
    return the parcel displacement at time t."""
    N = np.sqrt(complex(N2))
    if N2 > 0:  # stable
        return z0 * np.cos(N * t)
    else:  # unstable
        return z0 * np.cosh(np.abs(N) * t)


if __name__ == "__main__":
    # Stable case
    z0 = 0.1
    duration = 6 * 3600  # seconds
    t = np.linspace(0, duration, 1000)

    fig, axs = plt.subplots(2, 1, figsize=(8, 4), sharex=True)

    # Stable case (top panel)
    ax = axs[0]
    for N2 in [1e-4, 1e-6, 1e-8]:
        z_t = parcel_displacement(z0, N2, t)
        ax.plot(t, z_t, label=f"N={np.sqrt(N2)}")
    ax.axhline(0, color="black", lw=0.5, ls="--")
    ax.set_xlim(0, duration)
    ax.set_xticks(np.arange(0, duration + 1, 3600))
    ax.set_xticklabels(np.arange(0, duration / 3600 + 1, 1))
    ax.set_ylabel(r"$\delta z$ (m)")
    ax.set_title("Stable stratification")
    ax.legend(loc="upper right", title="Buoyancy frequency")
    ax.grid()

    # Unstable case (bottom panel)
    N2 = -1e-8
    ax = axs[1]
    for z0_val in [-0.1, 0.1]:
        z_t = parcel_displacement(z0_val, N2, t)
        ax.plot(t, z_t, label=r"$\delta z_{t=0}$=" + f"{z0_val} m")
    ax.axhline(0, color="black", lw=0.5, ls="--")
    ax.set_xlim(0, duration)
    ax.set_xticks(np.arange(0, duration + 1, 3600))
    ax.set_xticklabels(np.arange(0, duration / 3600 + 1, 1))
    ax.set_xlabel("Time (h)")
    ax.set_ylabel(r"$\delta z$ (m)")
    ax.set_title(r"Unstable stratification ($|N| = 10^{-4} s^{-1}$)")
    ax.legend()
    ax.grid()

    plt.tight_layout()
    plt.savefig("fig_static_instability_numerical.pdf")
    plt.close()
