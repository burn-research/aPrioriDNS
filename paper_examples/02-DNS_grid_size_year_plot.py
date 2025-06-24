#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:31:52 2025

@author: lorenzo piu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fontsize = 12

# Load the CSV file
df = pd.read_csv("material/DNS_size_table.csv")  # replace with the full path if needed

# Plotting
plt.figure(figsize=(10, 3), dpi=800)
plt.scatter(df["Year"], df["Max Grid Points"], color='C0', s=30)
plt.yscale("log")
plt.xlabel("Year", fontsize=fontsize*1.2)
plt.ylabel("DNS Grid Points", fontsize=fontsize*1.2)

# Fit and plot the log trend line
x = df["Year"]
y = np.log10(df["Max Grid Points"])
m, c = np.polyfit(x, y, 1)
x_line = np.linspace(2004, 2024, 200)
plt.plot(x_line, 10**(m * x_line + c), 'k--', linewidth=1)

# Manual legend for reference markers
legend_elems = [
    plt.plot([2004], [3072*385*2304], marker="o",   color=(1, 1, 1, 0),   markeredgecolor="k", markersize=8, markeredgewidth=1.6, label="del Álamo et al. 2004"),
    plt.plot([2006], [6144*633*4608], marker=">",   color=(1, 1, 1, 0),   markeredgecolor="k", markersize=8, markeredgewidth=1.6, label="Hoyas & Jiménez 2006"),
    plt.plot([2013], [10240*1536*7680], marker="^", color=(1, 1, 1, 0), markeredgecolor="k", markersize=8, markeredgewidth=1.6, label="Lee et al. 2013"),
    plt.plot([2014], [8192*1024*4096], marker="p",  color=(1, 1, 1, 0),  markeredgecolor="k", markersize=10, markeredgewidth=1.6, label="Bernardini et al. 2014"),
    plt.plot([2014], [2048*1081*2048], marker="s",  color=(1, 1, 1, 0),  markeredgecolor="k", markersize=8, markeredgewidth=1.6, label="Lozano & Jiménez 2014"),
    plt.plot([2018], [8640*4096*6144], marker="D",  color=(1, 1, 1, 0),  markeredgecolor="k", markersize=7, markeredgewidth=1.6, label="Yamamoto & Tsuji 2018"),
]

# plt.legend( loc="lower right", frameon=False)
plt.legend(
    loc="center left",          # anchor relative to left-center of the box
    bbox_to_anchor=(1.01, 0.5), # 1% to the right of the axes, vertically centered
    frameon=False,
    fontsize=fontsize
)

plt.xticks([2004, 2008, 2012, 2016, 2020, 2024], fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.tight_layout()
plt.savefig('figures/DNS_size_year.png', transparent=True, bbox_inches='tight')


plt.show()
