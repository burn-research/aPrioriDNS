#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import aPrioriDNS as ap
import os

#============ Input variables ============#
data_folder = 'DNS_turbulent_transport'
filter_size = 8
Cs = 0.16
figures_folder = 'figures_subgrid_turbulence'
#=========================================#

# Create the folder for the output figures
if not os.path.exists(figures_folder):
    os.mkdir(figures_folder)

# Initialize the field, with the option 'reactive' set to false
DNS_field = ap.Field3D(os.path.join(data_folder, 'DNS_data_cut'), reactive=False)

# DNS Strain rate computation
DNS_field.compute_strain_rate(save_derivatives=False, save_tensor=True)

# Strain rate plot
f1,ax1 = DNS_field.plot_z_midplane(
    'S_DNS', 
    log=True, 
    vmax=2.6, 
    vmin=.5, 
    colormap='Blues',
    scale='m',
    title=r'$\mathcal{S}=2S_{ij}S_{ij}$',
    remove_cbar=True,
    transparent=False,
    )
f1.savefig(
    os.path.join(figures_folder, 'f1'), 
    transparent=True,
    bbox_inches='tight')

# Filtering field.
# The function will return the relative path of the filtered field folder
f_name = DNS_field.filter(filter_size=filter_size, filter_type='Gauss')
# The filtered field can now be initialized
filtered_field = ap.Field3D(f_name, reactive=False)

# DNS filtered dissipation rate plot
f2, ax2 = filtered_field.plot_z_midplane(
    'S_DNS', 
    log=True, 
    vmax=2.6, 
    vmin=.5, 
    colormap='Blues',
    scale='m',
    title=r'$\overline{\mathcal{S}}_{DNS} \equiv \overline{2S_{ij}{S}_{ij}}$',
    remove_y=True,
    remove_cbar=True,
    transparent=False,
    )
f2.savefig(
    os.path.join(figures_folder, 'f2'), 
    transparent=True,
    bbox_inches='tight')

# LES Strain rate plot
filtered_field.compute_strain_rate(save_derivatives=False, save_tensor=True)
f3, ax3 = filtered_field.plot_z_midplane(
    'S_LES', 
    log=True, 
    vmax=2.6, 
    vmin=.5, 
    colormap='Blues',
    scale='m',
    title=r'$\overline{\mathcal{S}}_{LES} \equiv 2\overline{S}_{ij}\overline{S}_{ij}$',
    remove_y=True,
    transparent=False,
    )
f3.savefig(os.path.join(figures_folder, 'f3'), 
           transparent=True,
           bbox_inches='tight')

f4, ax4 = ap.parity_plot(
    filtered_field.S_DNS.value, 
    filtered_field.S_LES.value, 
    density=True,
    cmin=1e-9,
    ticks=[100, 200, 300, 400],
    rel_error=None,
    x_name=r'$\overline{\mathcal{S}}_{DNS}$',
    y_name=r'$\bar{\mathcal{S}}_{LES}$',
    )
f4.savefig(
    os.path.join(figures_folder, 'f4'), 
    transparent=True,
    bbox_inches='tight')

# Compute residual dissipation rate
filtered_field.DNS_folder_path = DNS_field.folder_path
filtered_field.compute_residual_dissipation_rate(mode='DNS')
filtered_field.Cs=Cs # set the Smagorinsky constant
filtered_field.compute_residual_dissipation_rate(mode='Smag')

# Compute absolute error, save it to file, and add it as a variable
absolute_error = np.abs(filtered_field.Epsilon_r_DNS.value - filtered_field.Epsilon_r_Smag.value)
error_file_name = 'Epsilon_r_AE_id000.dat'
error_file_path = os.path.join(filtered_field.data_path, error_file_name)
ap.save_file(absolute_error, error_file_path)
ap.add_variable('Epsilon_r_AE', 'Epsilon_r_AE_{}.dat')
filtered_field.update(verbose=True)

# Residual dissipation rate plot
f5, ax5 = filtered_field.plot_z_midplane(
    'Epsilon_r_DNS',  
    vmin=-150, 
    vmax=150, 
    transparent=False,
    title=r'$\epsilon_r^{DNS}$',
    scale='m',
    remove_cbar=True,
    colormap='Blues'
    )
f5.savefig(
    os.path.join(figures_folder, 'f5'), 
    transparent=True,
    bbox_inches='tight')

# Smagorinsky modeled residual dissipation rate
f6, ax6 = filtered_field.plot_z_midplane(
    'Epsilon_r_Smag', 
    vmin=-150, 
    vmax=150, 
    title=r'$\epsilon_r^{LES}$',
    transparent=False,
    scale='m',
    remove_y=True,
    remove_cbar=True,
    colormap='Blues'
    )
f6.savefig(
    os.path.join(figures_folder, 'f6'), 
    transparent=True,
    bbox_inches='tight')

f7,ax7 = filtered_field.plot_z_midplane(
    'Epsilon_r_AE', 
    scale='m',
    colormap='Blues',
    title=r'$|\epsilon_r^{DNS} - \epsilon_r^{LES}|$',
    vmin=-150,
    vmax=150,
    transparent=False,
    remove_y=True
    )
f7.savefig(
    os.path.join(figures_folder, 'f7'), 
    transparent=True,
    bbox_inches='tight')

# Residual dissipation rate parity plot
f8, ax8 = ap.parity_plot(
    filtered_field.Epsilon_r_DNS.value, 
    filtered_field.Epsilon_r_Smag.value, 
    density=True,
    cmin=1e-9,
    limits=[-800, 800],
    ticks=[-500, 0, 500],
    rel_error=None,
    x_name=r'$\epsilon_r^{DNS}$',
    y_name=r'$\epsilon_r^{LES}$',
    )
f8.savefig(
    os.path.join(figures_folder, 'f8'), 
    transparent=True,
    bbox_inches='tight')

# Residual stress computation
filtered_field.compute_tau_r(mode='DNS')
filtered_field.compute_tau_r(mode='Smag')

# Compute absolute error, save it to file, and add it as a variable
absolute_error = np.abs(filtered_field.TAU_r_DNS.value - filtered_field.TAU_r_Smag.value)
error_file_name = 'TAU_r_AE_id000.dat'
error_file_path = os.path.join(filtered_field.data_path, error_file_name)
ap.save_file(absolute_error, error_file_path)
ap.add_variable('TAU_r_AE', 'TAU_r_AE_{}.dat')
filtered_field.update(verbose=True)

# Residual sub-filter stress plot
f9, ax9 = filtered_field.plot_z_midplane(
    'TAU_r_DNS', 
    vmin=0, 
    vmax=10,
    title=r'$\tau_r^{DNS}$',
    transparent=False,
    scale='m',
    remove_cbar=True,
    colormap='Blues',
    )
f9.savefig(
    os.path.join(figures_folder, 'f9'), 
    transparent=True,
    bbox_inches='tight')

# Residual stress Smagorinsky plot
f10, ax10 = filtered_field.plot_z_midplane(
    'TAU_r_Smag', 
    vmin=-0, 
    vmax=10, 
    title=r'$\tau_r^{LES}$',
    transparent=False,
    scale='m',
    remove_y=True,
    remove_cbar=True,
    colormap='Blues'
    )
f10.savefig(
    os.path.join(figures_folder, 'f10'), 
    transparent=True,
    bbox_inches='tight')

# Absolute error plot
f11, ax11 = filtered_field.plot_z_midplane(
    'TAU_r_AE', 
    scale='m',
    colormap='Blues',
    title=r'$|\tau_r^{DNS} - \tau_r^{LES}|$',
    vmin=0,
    vmax=10,
    remove_y=True
    )
f11.savefig(
    os.path.join(figures_folder, 'f11'), 
    transparent=True,
    bbox_inches='tight')
# Parity plot
f12, ax12 = ap.parity_plot(
    filtered_field.TAU_r_DNS.value, 
    filtered_field.TAU_r_Smag.value, 
    density=True,
    cmin=1e-8,
    # limits=[-500, 500],
    # ticks=[-400, 400],
    rel_error=None,
    x_name=r'$\tau_r^{DNS}$',
    y_name=r'$\tau_r^{LES}$',
    limits=[0, 30],
    ticks=[0, 10, 20, 30]
    )
f12.savefig(
    os.path.join(figures_folder, 'f12'), 
    transparent=True,
    bbox_inches='tight')

