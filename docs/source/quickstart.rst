Quickstart
==========

The following tutorial is intended for users who want a quick introduction 
to basic operations with the library. For a more thorough understanding and 
detailed explanations, please refer to the comprehensive tutorials available 
in the Fundamentals and usage section.

This section assumes you have already installed the library. If you haven't 
installed it yet, please refer to the :doc:`installation` page for instructions.

Optional: run tutorial with a different dataset
-----------------------------------------------

To follow this hands-on quickstart, you have two options:

1. **Use a dataset from BlastNet_**

   You can select any case that provides data for a *single timestep*
   (the current version of the library assumes one time index per dataset).
   Download the case locally and point :mod:`aPrioriDNS` to the top-level
   folder of the dataset.

2. **Use the reduced example dataset on GitHub**

   A small example dataset, extracted from a slot-burner hydrogen flame
   simulation, is available in the project repository. This dataset is
   formatted to be immediately compatible with :mod:`aPrioriDNS` and is
   convenient if you just want to test the library without browsing external
   databases.

   You can either download it manually from the GitHub repo or use the
   convenience helper provided by the package (see the tutorials for a
   complete example).

First step: download hydrogen diffusion flame DNS
-------------------------------------------------

As a first step we are going to download the dataset. 
Figure 1 shows a representation of the subdomain used in this tutorial.

.. figure:: /_static/figures/getting_started/Lifted_h2_subdomain.png

   Figure 1: Graphical representation of the DNS subset used in this tutorial

Run the following command to download the dataset:

.. code-block:: python

   import aPrioriDNS as ap

   ap.download()

This command should have downloaded from Github a folder with the following structure:

.. code-block:: text

   Lifted_H2_subdomain/
   ├── chem_thermo_tran/
   │   ├── li_h2.cti
   │   └── li_h2.yaml
   ├── data/
   │   ├── P_Pa_id000.dat
   │   ├── RHO_kgm-3_id000.dat
   │   ├── T_K_id000.dat
   │   ├── UX_ms-1_id000.dat
   │   ├── UY_ms-1_id000.dat
   │   ├── UZ_ms-1_id000.dat
   │   ├── YH2_id000.dat
   │   ├── YH2O_id000.dat
   │   ├── YH_id000.dat
   │   ├── YN2_id000.dat
   │   ├── YNO_id000.dat
   │   ├── YO2_id000.dat
   │   ├── YOH_id000.dat
   │   └── Z_id000.dat
   ├── grid/
   │   ├── X_m.dat
   │   ├── Y_m.dat
   │   └── Z_m.dat
   └── info.json

Visualization
-------------

After downloading the dataset, the following lines of code initialize a Field3D object. 
Once instantiated the object, we can display the field leveraging the plotting utilities:

.. code-block:: python

   # Initialize 3D DNS field
   field_DNS = ap.Field3D('Lifted_H2_subdomain')

   #----------------------------Visualize the dataset-----------------------------#
  
   # Plot Temperature on the xy midplane (transposed as yx plane)
   field_DNS.plot_z_midplane('T',                 # plots the Temperature
                             levels=[1400, 2000], # isocontours at 1400 and 2000
                             vmin=1400,           # minimum temperature to plot
                             title='T [K]',       # figure title
                             linewidth=2,         # isocontour lines thickness
                             transpose=True,      # inverts x and y axes
                             x_name='y [mm]',     # x axis label
                             y_name='x [mm]')     # y axis label
   # Plot Temperature on the xz midplane (transposed as zx plane)
   field_DNS.plot_y_midplane('T', 
                             levels=[1400, 2000], 
                             vmin=1400, 
                             title='T [K]', 
                             linewidth=2,
                             transpose=True, 
                             x_name='z [mm]', 
                             y_name='x [mm]')
   # Plot Temperature on the yz midplane
   field_DNS.plot_x_midplane('T', levels=[1400, 2000], vmin=1400, 
                             title='T [K]', linewidth=2)
   # Plot OH mass fraction on the transposed xy midplane
   field_DNS.plot_z_midplane('YOH', title=r'$Y_{OH}$', colormap='inferno',
                             transpose=True, x_name='z [mm]', y_name='x [mm]')

