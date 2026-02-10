How to contribute
=================

Contributions to **aPriori** are very welcome.
The project is developed openly and collaboratively, and contributions can range from
bug fixes and new features to documentation improvements, examples, and tests.

This page describes the recommended workflow to contribute to the codebase.

Ways to contribute
------------------

You can contribute to aPriori in several ways:

- Reporting **bugs** or unexpected behavior
- Suggesting new **features** or improvements
- Improving **documentation** or **tutorials**
- Adding new utilities, post-processing **methods**, or examples
- Writing or extending **tests**
- Reviewing **pull requests**

If you are unsure whether a change fits the scope of the project, feel free to open an
issue and discuss it first.

Development workflow
--------------------

The recommended contribution workflow follows standard GitHub practices.

1. Fork the repository
^^^^^^^^^^^^^^^^^^^^^^

Go to the main repository:

https://github.com/LorenzoPiu/aPriori

Click **Fork** (top right) to create a copy of the repository under your own GitHub account.

2. Clone your fork locally
^^^^^^^^^^^^^^^^^^^^^^^^^^

Clone your fork to your local machine:

.. code-block:: bash

   git clone https://github.com/<your-username>/aPriori.git
   cd aPrioriDNS

Add the upstream repository (optional but recommended):

.. code-block:: bash

   git remote add upstream https://github.com/LorenzoPiu/aPriori.git

3. Create a dedicated branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new branch for your contribution:

.. code-block:: bash

   git checkout -b my-feature-name

Use short, descriptive branch names, for example:

- ``fix-gradient-boundary``
- ``add-favre-filtering``
- ``improve-docs-installation``

.. warning::

   Avoid committing directly to ``main``.

.. Avoid committing directly to ``main``.

4. Install the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to install aPriori in editable mode:

.. code-block:: bash

   pip install -e .[dev]

This installs development dependencies (testing, formatting, documentation tools)
and allows changes to be picked up immediately.

5. Make your changes
^^^^^^^^^^^^^^^^^^^^

- Keep changes focused and reasonably scoped
- Follow the existing code structure and naming conventions
- Prefer readable, explicit code over clever constructs
- Add docstrings to new public functions and classes
- Update documentation if behavior changes

If your contribution affects numerical results or algorithms, please document
the rationale clearly.

6. Run tests
^^^^^^^^^^^^

Before committing, run the test suite locally:

.. code-block:: bash

   pytest

If you add new functionality, please include corresponding tests whenever possible.

7. Commit your changes
^^^^^^^^^^^^^^^^^^^^^^

Write clear, descriptive commit messages:

.. code-block:: bash

   git add .
   git commit -m "Add high-order gradient option for stretched grids"

Avoid large commits that mix unrelated changes.

8. Push to your fork
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git push origin my-feature-name

9. Open a Pull Request
^^^^^^^^^^^^^^^^^^^^^^

Go to your fork on GitHub and open a **Pull Request** targeting the ``main`` branch
of the upstream repository.

In the Pull Request description, please:

- Explain what the change does
- Explain why it is needed
- Reference related issues if applicable
- Attach the pytests results (if applicable)
- Mention limitations or future improvements

Draft Pull Requests are welcome.

Code style and conventions
--------------------------

- Python version: see ``pyproject.toml``
- Follow PEP8 where reasonable
- Use NumPy-style docstrings for public APIs
- Prefer explicit imports and readable variable names
- Keep numerical assumptions clearly documented

Documentation contributions
----------------------------

Documentation is written using **Sphinx** and reStructuredText.

To build the documentation locally:

.. code-block:: bash

   cd docs
   make html

Documentation contributions are highly appreciated, especially tutorials and examples.

Reporting issues
----------------

If you encounter a bug or unexpected behavior, please open an issue and include:

- a minimal reproducible example
- the aPriori version
- Python version and OS
- relevant error messages or stack traces

Code of conduct
---------------

All contributors are expected to interact respectfully and professionally.
Constructive discussion and scientific rigor are valued.

Thank you
---------

Thank you for contributing to **aPriori**.
Community involvement is essential for the project to grow into a robust and
widely useful tool for DNS post-processing and a priori analysis.