#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import aPrioriDNS as ap
import os

data_folder = os.path.join('DNS_turbulent_transport', 'Filtering_example')

# Initialize the field, with the option 'reactive' set to false
DNS_field = ap.Field3D(os.path.join(data_folder, 'DNS_data_cut'), reactive=False)

DNS_field.compute_velocity_module()
f, ax = DNS_field.plot_z_midplane('U_DNS', 
                            scale='m', 
                            colormap='Blues',
                            vmin=0,
                            vmax=11,
                            cbar_title=r'U [m/s]',
                            y_ticks=[2, 4, 6],
                            remove_title=True
                            )


filter_sizes = [8, 16, 32]
filtered_fields = dict()

for delta in filter_sizes:
    f_name = DNS_field.filter(delta)
    f = ap.Field3D(f_name, reactive=False)
    filtered_fields[f'{delta}'] = f
    del f

figures_dir = os.path.join(data_folder,'Figures')
os.mkdir(figures_dir)
for i, delta in enumerate(filter_sizes):
    # apply different figure properties depending on the position
    if i == 0:
        remove_y = False
    else:
        remove_y = True
    if i == len(filter_sizes)-1:
        remove_cbar = False
        cbar_title = r'U [m/s]'
    else:
        remove_cbar = True
        cbar_title = None
        
    # Plot and save figure and axis objects
    f, ax = filtered_fields[f'{delta}'].plot_z_midplane('U_DNS', 
                                                scale='m', 
                                                colormap='Blues',
                                                title=r'$\Delta$'+f' = {delta}',
                                                vmin=0,
                                                vmax=11,
                                                cbar_title=cbar_title,
                                                y_ticks=[2, 4, 6],
                                                remove_x=True,
                                                remove_y=remove_y,
                                                remove_cbar=remove_cbar
                                                )
    # Save figure
    f.savefig(os.path.join(figures_dir,f'delta{delta}.png'), 
              transparent=True, 
              bbox_inches='tight'
              )
    
    

downsampled_fields = dict() # initialize an empty dictionary
for delta in filter_sizes:
    # Downsample the filtered field and initialize a new one using the new directory
    ds = ap.Field3D(filtered_fields[f'{delta}'].downsample(ds_size=delta), reactive=False) 
    downsampled_fields[f"{delta}"] = ds
    del ds


for i, delta in enumerate(filter_sizes):
    if i == 0:
        remove_y = False
    else:
        remove_y = True
    if i == len(filter_sizes)-1:
        remove_cbar = False
        cbar_title = r'U [m/s]'
    else:
        remove_cbar = True
        cbar_title = None
        
    f, ax = downsampled_fields[f"{delta}"].plot_z_midplane('U_DNS', 
                                                scale='m', 
                                                colormap='Blues',
                                                title=r'$\Delta$'+f' = {delta}',
                                                vmin=0,
                                                vmax=11,
                                                cbar_title=cbar_title,
                                                remove_title=True,
                                                y_ticks=[2, 4, 6],
                                                remove_x=False,
                                                remove_y=remove_y,
                                                remove_cbar=remove_cbar
                                                )
    
    f.savefig(os.path.join(figures_dir,f'delta{delta}DS.png'), 
              transparent=True, 
              bbox_inches='tight'
              )
