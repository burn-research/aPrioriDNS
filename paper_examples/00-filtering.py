#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:31:52 2025

@author: lorenzo piu
"""

import aPrioriDNS as ap
import numpy as np
import matplotlib.pyplot as plt

shape = [20, 26, 15]
delta = 3  # filter amplitude in terms of # of cells
n_cut = delta//2 # number of cells to cut to avoid boundary effects

# Random array initialization
np.random.seed(42)
array = np.random.rand(*shape)

scalar = ap.Scalar3D(shape=shape, value=array)
z_mid_1 = scalar.z_midplane
filtered_scalar = ap.Scalar3D(shape=shape, value=ap.filter_3D(array, filter_size=delta, filter_type='Gauss'))
z_mid_2 = filtered_scalar.z_midplane
filtered_scalar.cut(n_cut=n_cut, mode='equal')
z_mid_3 = filtered_scalar.z_midplane
print(f'Scalar\'s shape after cutting with \'equal\' mode:\n{scalar.shape}')
z_mid_3_padded = np.pad(z_mid_3, 
                        ((n_cut, n_cut), (n_cut, n_cut)), 
                        mode='constant', constant_values=np.nan)
# filtered_scalar_box = ap.Scalar3D(shape=shape, value=scalar.filter_box(delta))
# z_mid_4 = filtered_scalar_box.z_midplane
# filtered_scalar_box.cut(n_cut=n_cut, mode='equal')
# z_mid_5 = filtered_scalar_box.z_midplane

# plt.figure()
# plt.pcolormesh(z_mid_1)
# plt.figure()
# plt.pcolormesh(z_mid_2)
# plt.figure()
# plt.pcolormesh(z_mid_3_padded)

# Plot
# Plot all midplanes in one figure
fig, axes = plt.subplots(1, 3, figsize=(15, 4), dpi=500)
titles = ['Original z-midplane', 'Filtered z-midplane', 'Cut (padded)']
images = [z_mid_1, z_mid_2, z_mid_3_padded]
colorbars = []
i = 0
for ax, img, title in zip(axes, images, titles):
    mesh = ax.pcolormesh(img, vmax=1, vmin=0)
    # ax.set_title(title)
    cbar = fig.colorbar(mesh, ax=ax)
    ax.set_aspect('equal')
    colorbars.append(cbar)
    ax.set_xticks([0,13,26])
    if i>0:
        ax.set_yticks([])
    else:
        ax.set_yticks([10, 20])
    i+=1

# # Remove colorbars from all but the last axis
# for cbar in colorbars[:-1]:
#     cbar.remove()
    
plt.show()
