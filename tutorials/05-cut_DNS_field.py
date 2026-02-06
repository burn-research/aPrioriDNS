#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:50:44 2024

@author: lorenzo piu
"""

import os
import aPriori as ap
from aPriori.DNS import Field3D
from aPriori import DNS
import json

directory = os.path.join('Lifted_H2_subdomain') # change this with your path to the data folder
T_path = os.path.join(directory,'data', 'T_K_id000.dat')
print(f"\nChecking the path \'{T_path}\' is correct...")
if not os.path.exists(T_path):
    print(f"The path '{T_path}' does not exist in your system. Downloading the dataset from Github...")
    ap.download(dataset='h2_lifted')
    

DNS_field = Field3D(directory)

cut_field_name = DNS_field.cut([40,50,10])

DNS_field_cut = Field3D(cut_field_name)

DNS_field.plot_z_midplane('U_X',
                          vmin=100,
                          vmax=280, 
                          transparent=False,
                          cbar_title=r'$U_x [m/s]$',
                          title='Uncut field',
                          dpi=500
                          )


DNS_field_cut.plot_z_midplane('U_X',
                              vmin=100,
                              vmax=280, 
                              transparent=False,
                              cbar_title=r'$U_x [m/s]$',
                              title='Cut field',
                              dpi=500
                              )
