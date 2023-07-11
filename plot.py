import matplotlib.pyplot as plt
import pandas as pd

params = {
    "font.size": 14,
    # "figure.constrained_layout.use": True,
    "lines.markersize": 4,
    "savefig.dpi": 200.0,
}
plt.rcParams.update(params)

df = pd.read_csv("measurements.csv", index_col="Datetime_UTC", parse_dates=True)

fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(14, 8))
df["temp"].plot(ax=axs[0], ylabel="$T \ (\degree C)$", grid=True, style=".")
df["RH"].plot(ax=axs[1], ylabel="$RH \ (\%)$", grid=True, style=".")
df["PW"].plot(ax=axs[2], ylabel="$PW \ (cm)$", grid=True, style=".")
plt.xlabel("Datetime (UTC)")
plt.savefig("deepsky_temp_rh_pw.png")
plt.show()
