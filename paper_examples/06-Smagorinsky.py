#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aPrioriDNS as ap
import os

data_folder = 'DNS_turbulent_transport'
filter_size = 8
Cs = 0.16

# Initialize the field, with the option 'reactive' set to false
DNS_field = ap.Field3D(os.path.join(data_folder, 'DNS_data_cut'), reactive=False)

# DNS_field.compute_velocity_module()
# DNS_field.plot_z_midplane('U_DNS')

DNS_field.compute_strain_rate(save_derivatives=False, save_tensor=True)

f1 = DNS_field.plot_z_midplane('S_DNS', 
                          log=True, 
                          vmax=2.6, 
                          vmin=.5, 
                          colormap='Blues',
                          scale='m',
                          title=r'$\mathcal{S}=2S_{ij}S_{ij}$',
                          remove_cbar=True,
                          transparent=False,
                          )


# Filtering field. 
# The function will return the relative path of the filtered field folder
f_name = DNS_field.filter(filter_size=filter_size, filter_type='Gauss')

filtered_field = ap.Field3D(f_name, reactive=False)

filtered_field.compute_strain_rate(save_derivatives=False, save_tensor=True)

filtered_field.plot_z_midplane('S_DNS', 
                               log=True, 
                               vmax=2.6, 
                               vmin=.5, 
                               colormap='Blues',
                               scale='m',
                               title=r'$\overline{\mathcal{S} }=\overline{2S_{ij}{S}_{ij}}$',
                               remove_y=True,
                               remove_cbar=True,
                               transparent=False,
                               )
filtered_field.plot_z_midplane('S_LES', 
                               log=True, 
                               vmax=2.6, 
                               vmin=.5, 
                               colormap='Blues',
                               scale='m',
                               title=r'$\bar{\mathcal{S}}=2\overline{S}_{ij}\overline{S}_{ij}$',
                               remove_y=True,
                               transparent=False,
                               )

filtered_field.DNS_folder_path = DNS_field.folder_path
filtered_field.compute_residual_dissipation_rate(mode='DNS')
filtered_field.Cs=Cs
filtered_field.compute_residual_dissipation_rate(mode='Smag')

filtered_field.plot_z_midplane('Epsilon_r_DNS',  vmin=-150, vmax=150, transparent=False)
filtered_field.plot_z_midplane('Epsilon_r_Smag', vmin=-150, vmax=150, transparent=False)

filtered_field.compute_tau_r(mode='DNS')
filtered_field.compute_tau_r(mode='Smag')

absolute_error = np.abs(filtered_field.TAU_r_DNS.value - filtered_field.TAU_r_Smag.value)
error_file_name = 'S_AE_id000.dat'
error_file_path = os.path.join(filtered_field.data_path, error_file_name)
ap.save_file(absolute_error, error_file_path)
ap.add_variable('S_AE', 'S_AE_{}.dat')
filtered_field.update(verbose=True)

filtered_field.plot_z_midplane('S_AE', 
                               scale='m',
                               colormap='Reds',
                               remove_title=True,
                               )

ap.parity_plot(filtered_field.TAU_r_DNS.value, 
               filtered_field.TAU_r_Smag.value, 
               density=True,
               cmin=1e-8,
               # limits=[-500, 500],
               # ticks=[-400, 400],
               rel_error=None,
               )


