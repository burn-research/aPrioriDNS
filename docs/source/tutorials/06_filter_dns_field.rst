Tutorial 6: Favre filtering for variable density flows
======================================================

.. note::

   The complete code associated with this tutorial is available
   `here <https://github.com/LorenzoPiu/aPriori/blob/main/tutorials/06-filter_DNS_field.py>`_.

This tutorial introduces the Favre filtering utilities available in the library.
Favre filtering is commonly used in large-eddy simulation (LES) and combustion
applications to separate resolved and sub-filter contributions of thermochemical
quantities. The example below shows how to apply Favre filtering to a DNS dataset
and how to generate new filtered fields using different filter kernels.

Import modules and define data path
-----------------------------------

.. code-block:: python
   :caption: Imports and paths definition

   import os
   from aPrioriDNS.DNS import Field3D
   from aPrioriDNS import DNS
   import json

   # Change this with your path to the data folder if necessary
   directory = os.path.join('..','data','Lifted_H2_subdomain')

   # Check the folder with the data exists in your system
   T_path = os.path.join(directory,'data', 'T_K_id000.dat')
   print(f"\nChecking the path \'{T_path}\' is correct...")
   if not os.path.exists(T_path):
       raise ValueError(
           "The path '{T_path}' does not exist in your system. "
           "Check to have the correct path to your data folder in the code"
       )
   else:
       print("Folder path OK\n")

Apply Favre filtering
---------------------

.. container:: demo

   .. code-block:: python
      :caption: Favre filtering with Gaussian and box kernels

      # Load the DNS field
      DNS_field = Field3D(directory)

      # Define the filter size (in grid points)
      filter_size = 12

      # Apply Favre filtering using a Gaussian kernel
      field_filt_name = DNS_field.filter_favre(
          filter_size,
          filter_type='Gauss'
      )
      DNS_field_filt_gauss = Field3D(field_filt_name)

      # Apply Favre filtering using a box kernel
      DNS_field_filt_box = Field3D(
          DNS_field.filter_favre(filter_size, filter_type='Box')
      )

   .. container:: demo-result

      .. figure:: /_static/figures/fundamentals_and_usage/tutorial_X_fig1.png
         :width: 80%
         :align: center

         Figure 1 - Example of a Favre-filtered field using a Gaussian kernel.

      .. figure:: /_static/figures/fundamentals_and_usage/tutorial_X_fig2.png
         :width: 80%
         :align: center

         Figure 2 - Example of a Favre-filtered field using a box kernel.