import numpy as np
import matplotlib.pyplot as plt

# --- carbon-footprint model (Eq. 13) ------------------------------------------
BASELINE_RE   = 5200       # reference friction Reynolds number
BASELINE_YEAR = 2013
BASELINE_CO2  = 1e6        # kg CO₂ emitted by the baseline run in 2013

def carbon_footprint(re_tau, year):
    """Return estimated kg CO₂ for a DNS at Reτ and calendar *year*."""
    return (BASELINE_CO2 *
            (re_tau / BASELINE_RE)**4 *
            2**((BASELINE_YEAR - year) / 1.5))   # Moore-law efficiency gain

# --- slanted lines for a few target Reτ values ---------------------------------
re_lines = [1000, 2000, 4000, 5200, 8000]
colors   = ["maroon", "royalblue", "darkorange", "goldenrod", "purple"]
labels   = [rf"$Re_\tau = {Re}$" for Re in re_lines]

years = np.linspace(2000, 2040, 200)

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)

for Re, c, lab in zip(re_lines, colors, labels):
    ax.plot(years, carbon_footprint(Re, years),
            color=c, lw=1.6, label=lab)

# --- horizontal reference lines ------------------------------------------------
references = [(1e2, "1 kg of beef"),
              (1e4, "per capita CO$_2$ emissions, US"),
              (1e6, "Boeing 777 NYC ↔ Beijing")]
for y, txt in references:
    ax.hlines(y, 2000, 2040, color="k", lw=2)
    ax.text(2001, y*1.2, txt, va="bottom", fontsize=11)

# --- individual DNS data points (approx. Reτ values) ---------------------------
studies = {
    "del Álamo et al. 04":  dict(year=2004, Re=1000, marker="o"),
    "Hoyas & Jiménez 06":   dict(year=2006, Re=2003, marker="x"),
    "Lee et al. 13":        dict(year=2013, Re=5200, marker="^"),
    "Bernardini et al. 14": dict(year=2014, Re=4000, marker="*"),
    "Lozano & Jiménez 14":  dict(year=2014, Re=2048, marker="s"),
    "Yamamoto & Tsuji 18":  dict(year=2018, Re=8000, marker="D"),
}
for lab, d in studies.items():
    ax.scatter(d["year"], carbon_footprint(d["Re"], d["year"]),
               marker=d["marker"], s=70,
               facecolors="none", edgecolors="k", lw=1.6, label=lab)

# --- axes, legend, & layout ----------------------------------------------------
ax.set_yscale("log")
ax.set_xlim(2000, 2040)
ax.set_ylim(1e2, 1e8)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("CO$_2$ emission (kg)", fontsize=14)

# one tidy legend that groups markers + coloured lines
handles, labs = ax.get_legend_handles_labels()
ax.legend(handles, labs, loc="center left",
          bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=11)

fig.tight_layout()
plt.show()
