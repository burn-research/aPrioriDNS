#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Make a two-panel figure:
  · Top  : DNS grid-size evolution vs. year
  · Bottom: Estimated CO₂ emission vs. year
"""

import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fontsize = 12
figsize = (7, 6)
dpi = 800

# ─────────────────────────────────────────────────────────────────────────────
# 1. DNS-size data (scatter + log-trend)
# ─────────────────────────────────────────────────────────────────────────────
CSV_PATH = "material/DNS_size_table.csv"          # adjust if needed
df = pd.read_csv(CSV_PATH)                        # must have Year, Max Grid Points

# literature points for consistent markers
studies_grid = [
    (2004, 3072*385*2304, "o", "del Álamo et al. (2004)"),
    (2006, 6144*633*4608, ">", "Hoyas & Jiménez (2006)"),
    (2013, 10240*1536*7680, "^", "Lee et al. (2013)"),
    (2014, 8192*1024*4096, "p", "Bernardini et al. (2014)"),
    (2014, 2048*1081*2048, "s", "Lozano & Jiménez (2014)"),
    (2018, 8640*4096*6144, "D", "Yamamoto & Tsuji (2018)"),
]

# ─────────────────────────────────────────────────────────────────────────────
# 2. CO₂-footprint model (Eq. 13)
# ─────────────────────────────────────────────────────────────────────────────
BASELINE_RE, BASELINE_YEAR, BASELINE_CO2 = 5200, 2013, 1e6
def carbon_footprint(re_tau, year):
    """kg CO₂ for a DNS at Re_tau executed in *year* (Eq. 13)."""
    return (BASELINE_CO2 *
            (re_tau / BASELINE_RE)**4 *
            2**((BASELINE_YEAR - year) / 1.5))

re_lines  = [1000, 2000, 4000, 5200, 8000]
colors    = ["maroon", "royalblue", "darkorange", "goldenrod", "purple"]
labels_co2 = [fr"$Re_\tau = {Re}$" for Re in re_lines]

studies_CO2 = {
    "del Álamo 04":  dict(year=2004, Re=1000, marker="o"),
    "Hoyas 06":      dict(year=2006, Re=2003, marker=">"),
    "Lee 13":        dict(year=2013, Re=5200, marker="^"),
    "Bernardini 14": dict(year=2014, Re=4000, marker="p"),
    "Lozano 14":     dict(year=2014, Re=2048, marker="s"),
    "Yamamoto 18":   dict(year=2018, Re=8000, marker="D"),
}

# ─────────────────────────────────────────────────────────────────────────────
# 3. Figure with two stacked sub-plots
# ─────────────────────────────────────────────────────────────────────────────
fig, (ax_size, ax_co2) = plt.subplots(
    2, 1, figsize=figsize, dpi=300, sharex=True,
    gridspec_kw={"height_ratios": [1.0, 1.0], "hspace": 0.45})

# 3a ── DNS grid-size panel ──────────────────────────────────────────────────
ax_size.scatter(df["Year"], df["Max Grid Points"],
                color="C0", s=30, zorder=2)
ax_size.set_yscale("log")
ax_size.set_ylabel("DNS Grid Points", fontsize=fontsize*1.2)

# log-trend (dashed black)
m, c = np.polyfit(df["Year"], np.log10(df["Max Grid Points"]), 1)
years_line = np.linspace(2004, df["Year"].max(), 200)
ax_size.plot(years_line, 10**(m*years_line + c), "k--", lw=1)

# literature markers
for x, y, mk, lab in studies_grid:
    ax_size.plot(x, y, color="none", marker=mk, ms=8, mfc="none",
                 mec="k", mew=1.5, label=lab)
ax_size.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
               frameon=False, fontsize=fontsize)
ax_size.tick_params(axis="both", labelsize=fontsize)

# 3b ── CO₂ panel ─────────────────────────────────────────────────────────────
years_full = np.linspace(2002, 2026, 200)
for Re, col, lab in zip(re_lines, colors, labels_co2):
    ax_co2.plot(years_full, carbon_footprint(Re, years_full),
                color=col, lw=1.1, label=lab)

# horizontal references
for y_ref, txt in [(1e2, "1 kg beef"),
                   (1e4, "Per-capita CO₂ (US)"),
                   (1e6, "Boeing 777 NYC ↔ Beijing")]:
    # ax_co2.text(2004, y_ref*1.22, txt, va="bottom", fontsize=fontsize)
    ax_co2.text(2003.6, y_ref*1.22, txt, va="bottom", 
                fontsize=fontsize, bbox=dict(facecolor='white', 
                edgecolor='none', pad=1.2))
    ax_co2.hlines(y_ref, 2000, 2040, color="k", lw=1.1)

for lab, d in studies_CO2.items():
    ax_co2.plot(d["year"], carbon_footprint(d["Re"], d["year"]),
                   color="none", marker=d['marker'], ms=8, mfc="w",
                                mec="k", mew=1.5)

ax_co2.set_yscale("log")
ax_co2.set_ylim(1e1, 1e7)
ax_co2.set_xlabel("Year", fontsize=fontsize*1.2)
ax_co2.set_ylabel("CO$_2$ emission (kg)", fontsize=fontsize*1.2)
ax_co2.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
              frameon=False, fontsize=fontsize)
ax_co2.set_xlim(2003, 2025)
ax_co2.set_xticks(range(2004, 2025, 4))
ax_co2.tick_params(axis="both", labelsize=fontsize)

# super-title & layout
# fig.suptitle("DNS Size and Carbon-Footprint Trends", fontsize=16, y=0.98)
# fig.tight_layout(rect=[0, 0, 0.88, 0.96])

# Add annotations to identify figures
ax_size.text(
    0.0, 1.15,              # x,y in axes fraction
    'a', fontsize=fontsize*1.7, fontweight='bold', fontname='arial',
    ha='left', va='center',
    rotation=0,
    transform=ax_size.transAxes
)
ax_co2.text(
    0.0, 1.15,              # x,y in axes fraction
    'b', fontsize=fontsize*1.7, fontweight='bold', fontname='arial',
    ha='left', va='center',
    rotation=0,
    transform=ax_co2.transAxes
)

# ensure output directory exists, then save
pathlib.Path("figures").mkdir(exist_ok=True)
fig.savefig("figures/DNS_size_and_CO2.png",
            transparent=False, bbox_inches="tight", dpi=dpi)

plt.show()
print("Figure saved to figures/DNS_size_and_CO2.png")

