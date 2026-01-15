Installation
============

This page explains how to install **aPrioriDNS** in the two most common
scenarios:

1. **Regular users** who simply want to install the package and run analyses.
2. **Contributors / developers** who want to modify the source code, add new
   features, or participate in the project.

.. note::

   aPrioriDNS supports **Python 3.9+** and works on Linux, macOS and Windows.
   For best reproducibility, it is recommended to install it inside a virtual
   environment (``venv`` or ``conda``).

Quick Installation (PyPI) |pypi-logo|
-------------------------

.. |pypi-logo| image:: https://img.shields.io/pypi/v/aprioridns.svg?logo=pypi&logoColor=white
   :target: https://pypi.org/project/aprioridns/

The latest stable version of aPrioriDNS is available on the Python Package Index (**PyPI**):

.. code-block:: bash
   :caption: PyPI installation

   pip install aPrioriDNS

Installing via ``pip`` will automatically install the required dependencies:

   - ``numpy>=1.18.0``
   - ``scipy>=1.12.0``
   - ``matplotlib>=3.2.0``
   - ``cantera>=3.0.0``
   - ``tabulate>=0.9.0``
   - ``requests>=2.32.0``
   - ``PyCSP-lib>=1.4.0``

   Additional optional dependencies may be added over time.

After installation, verify it worked:

.. code-block:: python

   import aprioridns
   print(aprioridns.__version__)

Optional: creating a virtual environment
----------------------------------------

Although not required, it is **strongly recommended** to install aPrioriDNS inside
a clean environment:

.. tab-set::

   .. tab-item:: venv (Python built-in)

      .. code-block:: bash

         python3 -m venv .venv
         source .venv/bin/activate   # on macOS / Linux
         .venv\Scripts\activate      # on Windows

         pip install aprioridns

   .. tab-item:: Conda

      .. code-block:: bash

         conda create -n apriori python=3.11
         conda activate apriori
         pip install aprioridns


Installing the Development Version (for Contributors)
-----------------------------------------------------

If you plan to:

* add new features (both for yourself or to contribute)
* fix bugs,
* improve documentation,
* contribute DNS datasets or utilities,

then you should install the **development** version from GitHub.
It is strongly recommended to clone the 'dev' branch, as it is 
the one where new features are added before a new release.

.. container:: center

   .. card:: 🛠️ Repository
      :link: https://github.com/LorenzoPiu/aPrioriDNS
      :text-align: center
      :shadow: md
      :padding: 2

      Clone or fork the development repository on GitHub.

Developer installation steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Clone the repository**

   .. code-block:: bash

      git clone https://github.com/LorenzoPiu/aPrioriDNS.git
      cd aPrioriDNS
      git checkout dev

2. **Create a development environment**

   .. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate

3. **Install in editable mode**

   This installs the package so that changes in the source code are
   immediately reflected when you import it:

   .. code-block:: bash

      pip install -e .

Upgrading to the latest version
-------------------------------

To upgrade the PyPI version:

.. code-block:: bash

   pip install --upgrade aprioridns

To update the development version:

.. code-block:: bash

   git pull
   pip install -e .


You're ready to go!
-------------------

Once installed, head over to:

* :doc:`../quickstart` – skip directly here for a first, all-in-one example
* :doc:`../tutorials/index` – practical, step by step examples which help developing a deeper understanding of the different features
* :doc:`API Guide <../autoapi/aPrioriDNS/index>` – complete API reference genrated automatically using Sphinx’s `autodoc extension <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.

Happy exploring!