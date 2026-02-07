Tutorial 3: Read a DNS dataset
===============================

.. note::

   The complete code associated with this tutorial, including the original
   Jupyter notebook, is available
   `here <https://github.com/LorenzoPiu/aPriori/blob/main/tutorials/03-initialize_DNS_field.py>`_.

This exercise introduces the :class:`Field3D` class, which highlights the main
purpose of **aPrioriDNS**: providing a clean, memory-efficient interface for
working with formatted DNS datasets.

From this point onward, the tutorials assume you are working with properly
formatted DNS data (e.g., BlastNet).  
If you want to run the tutorial locally, download the dataset from the
aPrioriDNS GitHub repository using the function ``ap.download()``.  
If you already downloaded the data, simply comment out that line.

Import modules and define data path
-----------------------------------

.. code-block:: python
   :caption: Script header

   import os
   import aPrioriDNS as ap
   import json

   # Download data (comment this if already downloaded)
   ap.download()

   # Adjust this path depending on where the DNS dataset is stored
   directory = os.path.join('.', 'Lifted_H2_subdomain')

   # BlastNet stores the global shape in info.json.
   # Field3D will automatically parse everything, so we don't need to load it manually.
   # The following lines check that the dataset is present in your system
   with open(os.path.join(directory, 'info.json'), 'r') as file:
       info = json.load(file)
   DNS_shape = info['global']['Nxyz']

Initialize the Field3D object
-----------------------------

If your dataset follows the **BlastNet format**, you only need to provide the
correct folder path. ``Field3D`` will automatically:

- read the mesh,
- load the chemistry mechanism,
- detect all scalar/vector fields available,
- create memory-light pointers to the data files.

.. code-block:: python

   DNS_field = ap.Field3D(directory)

Example console output
----------------------

.. code-block:: text

   ---------------------------------------------------------------
   Initializing 3D Field

   Checking files inside folder ../data/Lifted_H2_subdomain...

   Folder structure OK

   ---------------------------------------------------------------
   Building mesh attribute...
   Mesh fields read correctly

   ---------------------------------------------------------------
   Reading kinetic mechanism...
   Kinetic mechanism file found: ../data/Lifted_H2_subdomain/chem_thermo_tran/li_h2.yaml
   Species:
   ['H2', 'O2', 'H2O', 'H', 'O', 'OH', 'HO2', 'H2O2', 'N2']

   ---------------------------------------------------------------
   Building scalar attributes...
   Field attributes:
   +-----------+------------------------------------------------------+
   | Attribute |                         Path                         |
   +-----------+------------------------------------------------------+
   |     P     |   ../data/Lifted_H2_subdomain/data/P_Pa_id000.dat    |
   |    RHO    | ../data/Lifted_H2_subdomain/data/RHO_kgm-3_id000.dat |
   |     T     |    ../data/Lifted_H2_subdomain/data/T_K_id000.dat    |
   |    U_X    |  ../data/Lifted_H2_subdomain/data/UX_ms-1_id000.dat  |
   |    U_Y    |  ../data/Lifted_H2_subdomain/data/UY_ms-1_id000.dat  |
   |    U_Z    |  ../data/Lifted_H2_subdomain/data/UZ_ms-1_id000.dat  |
   |    YH2    |    ../data/Lifted_H2_subdomain/data/YH2_id000.dat    |
   |    YO2    |    ../data/Lifted_H2_subdomain/data/YO2_id000.dat    |
   |   YH2O    |   ../data/Lifted_H2_subdomain/data/YH2O_id000.dat    |
   |    YH     |    ../data/Lifted_H2_subdomain/data/YH_id000.dat     |
   |    YO     |    ../data/Lifted_H2_subdomain/data/YO_id000.dat     |
   |    YOH    |    ../data/Lifted_H2_subdomain/data/YOH_id000.dat    |
   |   YHO2    |   ../data/Lifted_H2_subdomain/data/YHO2_id000.dat    |
   |   YH2O2   |   ../data/Lifted_H2_subdomain/data/YH2O2_id000.dat   |
   |    YN2    |    ../data/Lifted_H2_subdomain/data/YN2_id000.dat    |
   +-----------+------------------------------------------------------+

Using the Field3D object
------------------------

Once initialized, the ``Field3D`` object exposes all field variables as
``Scalar3D`` objects.

Access a scalar field:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   DNS_field.T

Example output:

.. code-block:: text

   <aPrioriDNS.DNS.Scalar3D at 0x14c36ab50>

Access the raw 3D data:
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   DNS_field.U_Y._3D

This returns the full NumPy array of the *Y* velocity component.

Filtering a field
~~~~~~~~~~~~~~~~~

You may apply any filtering operation (e.g., Gaussian, box, or Favre filtering):

.. code-block:: python

   filt_YO2 = DNS.filter_3D(DNS_field.YO2._3D, 8)

Plotting a midplane slice
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   DNS_field.plot_z_midplane('YH2O2')

3D visualisation and further examples will be covered in the next tutorials.