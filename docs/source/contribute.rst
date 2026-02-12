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
   cd aPriori

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

   Please avoid committing directly to ``main``.

4. Install the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, install aPriori in editable mode:

.. code-block:: bash

   pip install -e .

Then install the development dependencies:

.. code-block:: bash

   pip install -r dev-requirements.txt

This installs development dependencies (testing, formatting, documentation tools)
and allows changes to be picked up immediately.

The following steps are recommended for who wants to contribute to the project, 
but they are not necessary if you're planning to edit the library for personal usage only.

5. Run tests
^^^^^^^^^^^^

Before moving on, please try to run the tests to check that everything works. The 
tests can take a long time even 5 to 10 minutes; please run them with
the following command:

.. code-block:: bash

   pytest -m slow --html=pytest_report.html --self-contained-html

If some of the tests fail, please open an issue attaching the test results.

If this command fails or you don't have installed pytest-html, also try this one:

.. code-block:: bash

   pytests

6. Make your changes
^^^^^^^^^^^^^^^^^^^^

- Keep changes focused and reasonably scoped
- Follow the existing code structure and naming conventions
- Prefer readable, explicit code over clever constructs
- Add docstrings to new public functions and classes
- Update documentation if behavior changes

If your contribution affects numerical results or algorithms, please document
the rationale clearly.

7. Run tests
^^^^^^^^^^^^

Before committing, run again the test suite locally:

.. code-block:: bash

   pytest -m slow --html=pytest_report.html --self-contained-html

If you add new functionality, please include corresponding tests whenever possible.

8. Commit your changes
^^^^^^^^^^^^^^^^^^^^^^

Write clear, descriptive commit messages:

.. code-block:: bash

   git add .
   git commit -m "Add high-order gradient option for stretched grids"

Avoid large commits that mix unrelated changes.

9. Push to your fork
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git push origin my-feature-name

10. Open a Pull Request
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

1. Remove the previously built folder content

.. code-block:: bash

   rm -rf docs/build/html

2. Remove the previously generated autodoc 

.. code-block:: bash

   rm -rf docs/source/autoapi

3. Build html

.. code-block:: bash

   python -m sphinx -b html docs/source docs/build/html

Documentation contributions are **highly appreciated**, especially tutorials and examples.

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

Thank you 🫶
---------

Thank you for contributing to the project.  
We sincerely appreciate the time and effort you have invested in improving the
library.

Community contributions are essential to the development of ``aPriori``, helping it
remain reliable, extensible, and useful for DNS post-processing and *a priori*
analysis. Whether through code, documentation, testing, or feedback, each
contribution plays an important role.

Your involvement is highly valued, and we are grateful for your support!