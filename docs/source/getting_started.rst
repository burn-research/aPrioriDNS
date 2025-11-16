Getting started
===============

Installation
------------

.. code-block:: bash

   pip install aPrioriDNS

Quick example
-------------

.. code-block:: python

   import aPrioriDNS as ap

   # Download the dataset
   ap.download()

   field_DNS = ap.Field3D('Lifted_H2_subdomain')

   field_DNS.plot_z_midplane(
       'T',
       levels=[1400, 2000],
       vmin=1400,
       title='T [K]',
       linewidth=2,
       transpose=True,
       x_name='y [mm]',
       y_name='x [mm]',
   )
