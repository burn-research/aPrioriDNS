Getting Started
===============

This page introduces the **scope of the project**, how to install the package,
and a minimal script to verify that everything is working.

What is aPriori?
----------------

Scope of the project
~~~~~~~~~~~~~~~~~~~~

**aPriori** is a Python package for working with **Direct Numerical Simulation
(DNS)** data. Its goal is to make large, high-fidelity datasets easier to use,
both for people with a background in combustion / fluid dynamics and for those
coming from other domains such as data science or machine learning. :contentReference[oaicite:5]{index=5}

Why DNS data?
~~~~~~~~~~~~~

DNS datasets resolve the full turbulence spectrum and can capture detailed
turbulence–chemistry interactions. This makes them extremely valuable for:

- training data-driven models (e.g. neural networks),
- developing and evaluating turbulence or combustion models,
- carrying out detailed analysis of flow and chemical structures. :contentReference[oaicite:6]{index=6}

However, these datasets are typically:

- **huge** (easily many gigabytes),
- stored in formats that vary between research groups,
- produced on large HPC systems, while analysis is often done on more modest
  machines.

A frequent practical problem is simply **running out of memory** when trying to
load everything into RAM. :contentReference[oaicite:7]{index=7}

Why use aPriori?
~~~~~~~~~~~~~~~~

aPriori is designed to make this kind of data more manageable and intuitive:

- it provides **high-level objects** (such as 3D fields and meshes) so that you
  can focus on the analysis rather than the file layout;
- it operates mainly on **pointers / lazy access** to the data, only reading
  arrays from disk when needed, which helps avoid exhausting RAM;
- it includes utilities for **filtering**, **computing reaction rates**, and
  **preparing data** for turbulence / combustion modelling and machine learning
  workflows. :contentReference[oaicite:8]{index=8}

Installation
------------

You can install the package from PyPI:

.. code-block:: bash

   pip install aPrioriDNS

This will also install or update the main dependencies such as:

- ``numpy``
- ``scipy``
- ``matplotlib``
- ``cantera``
- ``tabulate``
- ``requests`` :contentReference[oaicite:9]{index=9}

Make sure you are in a clean virtual environment (for example, using
``venv`` or ``conda``) before installing, especially if you plan to develop or
contribute to the library.

After installation, you can quickly check that the package is available:

.. code-block:: python

   import aPrioriDNS as ap
   print(getattr(ap, "__version__", "unknown"))

Quickstart
----------

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
