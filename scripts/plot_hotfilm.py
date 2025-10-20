import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("asist-hotfilm-sample-1kHz.csv")

time = np.arange(0, 10, 0.001)
mean_u = df["u"].mean()
fluctuation = df["u"] - mean_u

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.plot(time, df["u"], label=r"$u(t)$", lw=0.5)
ax.plot(time, fluctuation, label=r"$u'(t)$", lw=0.5)
ax.plot(time, [mean_u] * len(time), "k--", label=r"$\overline{u}$", lw=2)
ax.legend(fontsize=16)
ax.set_xlabel("Time [s]", fontsize=16)
ax.set_ylabel("Velocity [m/s]", fontsize=16)
ax.set_xlim(0, 10)
ax.grid()

plt.savefig("fig_reynolds_decomposition.pdf")
plt.close()
