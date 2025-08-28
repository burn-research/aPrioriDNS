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

# Initialize the field, with the option 'reactive' set to false
DNS_field = ap.Field3D(os.path.join(data_folder, 'DNS_data_cut'), reactive=False)

# DNS_field.cut([0, 0, 0, 0, 472, 472])

DNS_field.compute_velocity_module()
DNS_field.plot_z_midplane('U_DNS')

DNS_field.compute_strain_rate(save_derivatives=False, save_tensor=True)

DNS_field.plot_z_midplane('S_DNS', log=True)

# Filtering field. 
# The function will return the relative path of the filtered field folder
f_name = DNS_field.filter(filter_size=8, filter_type='Gauss')

filtered_field = ap.Field3D(f_name, reactive=False)

filtered_field.compute_strain_rate(save_derivatives=False, save_tensor=True)

filtered_field.plot_z_midplane('S_DNS', 
                               log=True, 
                               vmax=2.6, 
                               vmin=.5, 
                               colormap='Blues',
                               remove_title=True,
                               cbar_title=r'$\mathcal{S}$',
                               scale='m'
                               )
filtered_field.plot_z_midplane('S_LES', 
                               log=True, 
                               vmax=2.6, 
                               vmin=.5, 
                               colormap='Blues',
                               remove_title=True,
                               # cbar_title=r'$\mathcal{\overline{S }}$',
                               remove_y=True,
                               scale='m'
                               )

filtered_field.DNS_folder_path = DNS_field.folder_path
filtered_field.compute_residual_dissipation_rate(mode='DNS')
filtered_field.Cs=0.14
filtered_field.compute_residual_dissipation_rate(mode='Smag')

filtered_field.plot_z_midplane('Epsilon_r_DNS',  vmin=-150, vmax=150, transparent=False)
filtered_field.plot_z_midplane('Epsilon_r_Smag', vmin=-150, vmax=150, transparent=False)

absolute_error = filtered_field.S_DNS.value - filtered_field.S_LES.value
error_file_name = 'S_AE_id000.dat'
error_file_path = os.path.join(filtered_field.data_path, error_file_name)
ap.save_file(absolute_error, error_file_path)
ap.add_variable('S_AE', 'S_AE_{}.dat')
# filtered_field.add_variable('S_AE', 'S_AE_id000.dat')
filtered_field.update(verbose=True)

ap.parity_plot(filtered_field.Epsilon_r_DNS.value, filtered_field.Epsilon_r_Smag.value, density=True)


