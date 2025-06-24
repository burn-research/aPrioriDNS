#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:31:52 2025

@author: lorenzo piu
"""

import aPrioriDNS as ap
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

s0 = [40, 30, 15]
f = 1.1
n = 39
shapes = [s0]
data_folder = 'data'

for _ in range(n):
    next_size = (np.array(shapes[-1]) * f).astype(int).tolist()
    shapes.append(next_size)

elements = [np.prod(shape) for shape in shapes]
    
# Make directory to save scalars
if not os.path.exists(data_folder):
    os.mkdir(data_folder)
    
filenames = [os.path.join(data_folder, 'f_{}_{}_{}.dat'.format(*shape)) for shape in shapes]

scalars = [np.float32(np.random.rand(*shape)) for shape in shapes]
for scalar, filename in zip(scalars,filenames):
    ap.save_file(scalar, file_name=filename)
    
ram_size = [scalar.nbytes/1024**2 for scalar in scalars] # size in MB
  
light_scalars = [ap.Scalar3D(shape=shape, path=filename) for shape,filename in zip(shapes,filenames)]
disk_sizes = [os.path.getsize(filename)/1024**2 for filename in filenames]
ram_size_light = [sys.getsizeof(light_scalar) for light_scalar in light_scalars]

t_load = []
for s in light_scalars:
    t0 = time.time()
    array = s.value #loading the array
    t1 = time.time()
    t_load.append(t1-t0)

# %% Plot
import matplotlib.pyplot as plt
import numpy as np

# Create figure and primary axis
fig, ax1 = plt.subplots(figsize=(6.3, 4.4), dpi=500)

# Plot on log-log scale
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.plot(ram_size, t_load, marker='o', linestyle='-', linewidth=2, markersize=6, color='C0')
ax1.set_xlabel('Memory usage (MB)', fontsize=16)
ax1.set_ylabel('Load time (s)', fontsize=16)
ax1.tick_params(axis='both', labelsize=14)
# ax1.grid(True, which='both', linestyle='--', alpha=0.2)
ax1.grid(False)

# Mapping functions for secondary x-axis
def ram_to_size(x):
    return np.interp(x, ram_size, elements)

def size_to_ram(x):
    return np.interp(x, elements, ram_size)

# Add log-scale secondary x-axis
ax2 = ax1.secondary_xaxis('top', functions=(ram_to_size, size_to_ram))
ax2.set_xscale('log')
ax2.set_xlabel('DNS grid points', fontsize=16, labelpad=10)
ax2.tick_params(axis='x', labelsize=14)

# Get max values
max_time = np.max(t_load)
max_ram = ram_size[np.array(t_load).argmax()]  # RAM at max load time
max_elems = elements[-1]

# Create annotation text
annotation_text = (
    f"Peak load time: {max_time:.2f} s\n"
    f"Peak memory usage: {max_ram / 1024:.2f} GB\n"
    f"Array size: {max_elems / 1e6:.1f} M elements"
)

# Add to plot (adjust x and y coordinates as needed)
plt.text(0.06, 1.2, annotation_text,
        fontsize=15, verticalalignment='top',
        #bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="gray", alpha=0.9)
        )

# Final layout
fig.tight_layout()

plt.savefig('Memory_load.png')
plt.show()
