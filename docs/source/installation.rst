Installation
============

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