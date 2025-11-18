Quickstart
==========

The following example shows the typical workflow after installation: download a
formatted DNS dataset, initialize a 3D field object, and make a simple plot. :contentReference[oaicite:10]{index=10}

.. code-block:: python

   import aPrioriDNS as ap

   # 1. Download a sample dataset (if not already present)
   ap.download()

   # 2. Initialize a 3D DNS field
   field_DNS = ap.Field3D("Lifted_H2_subdomain")

   # 3. Visualise temperature on a mid-plane
   field_DNS.plot_z_midplane(
       "T",                 # temperature field
       levels=[1400, 2000], # isocontours
       vmin=1400,           # minimum value for the color scale
       title="T [K]",       # figure title
       linewidth=2,         # contour line thickness
       transpose=True,      # swap x/y axes in the plot
       x_name="y [mm]",     # x-axis label
       y_name="x [mm]",     # y-axis label
   )

Running this script should:

1. Download or reuse a hydrogen flame DNS dataset.
2. Initialize a ``Field3D`` object pointing to the dataset.
3. Produce a 2D slice plot of the temperature field.

Next steps
----------

- If you are comfortable with this quickstart, you can move on to more
  advanced examples and tutorials (which we’ll hook up through Jupyter
  notebooks via ``myst-nb``).
- If the code above feels too compact, the **Fundamentals & Usage** section
  (to be added) will walk through the same operations more slowly, explaining
  each building block of the library.