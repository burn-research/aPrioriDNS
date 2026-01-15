What is aPriori
===============

Scope of the project
~~~~~~~~~~~~~~~~~~~~

**aPriori** is a Python package designed to simplify the analysis of
**Direct Numerical Simulation (DNS)** datasets in fluid dynamics research.
Its goal is to make large, high-fidelity datasets easier to explore,
post-process, and use in physics-based or data-driven workflows. The package
offers a consistent interface to heterogeneous DNS formats, efficient memory
management, and a growing collection of tools for data extraction,
visualisation, filtering, and modelling support.

Scientific motivation
~~~~~~~~~~~~~~~~~~~~~

Direct Numerical Simulation (DNS) has become a central tool in fluid
mechanics, turbulence, and reacting-flow research. By resolving the full
Navier–Stokes equations and all relevant spatio-temporal scales
:cite:p:`moin1998direct`, DNS provides highly detailed information on:

- the interaction between turbulence and chemical reactions
  :cite:p:`PoinsotVeynante_2005`;
- small-scale mixing, dissipation, and scalar transport;
- statistical and structural properties of turbulent flows
  :cite:p:`Pope2012-jn`.

This level of detail comes at a cost: modern DNS runs are computationally
expensive and increasingly energy-intensive. A recent analysis of DNS studies
published in the *Journal of Fluid Mechanics* (2004–2024) showed that the
largest simulations can emit **up to 1000 metric tons of CO₂**
— comparable to a transcontinental flight — depending on domain size, chemistry
complexity and resolution :cite:p:`Yang2024`. Community efforts to **share DNS
data** (e.g. JHTDB) were estimated to have avoided *millions of tons* of CO₂
emissions by preventing redundant computations.

These results underline two key needs:

1. **public availability of DNS datasets**, and  
2. **tools that make these datasets easy to access and reuse**.

The role of shared DNS datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A notable recent effort in this direction is the **BlastNet** database
:cite:p:`chung_wai_tong_2023_8034232, chung2022the, CHUNG2022100087`, an
open repository containing **744 DNS samples across 34 cases** and totalling
more than **2.2 TB**. BlastNet aggregates data contributed by multiple
institutions and includes:

- isotropic turbulence cases :cite:p:`Chung2022, Donzis2010`,
- channel flows :cite:p:`Samuel2024`,
- flame configurations of varying complexity
  :cite:p:`Brouzet_Talei_Brear_Cuenot_2021, Coulon2023, Jung2021`.

This diversity is especially valuable for turbulence modelling and
data-driven approaches. Modern machine-learning studies—such as model discovery,
subfilter-scale closure learning, or physics-informed regression
:cite:p:`swaminathan_parente_2023, Ihme2022-ac, Bode2019-ue, Bode2021-ur,
Nista2023-re, deFrahan2019, Piu2025`—benefit greatly from access to clean,
well-structured DNS data.

However, unlike common ML benchmark datasets (e.g. MNIST, CIFAR, ImageNet),
DNS data often require **significant post-processing** before becoming usable:
computing subfilter quantities, evaluating gradients, extracting slices,
computing chemistry-related quantities, or reformatting variables for neural
network pipelines. These steps can be computationally demanding and error-prone
when performed manually. Moreover, the code for doing these operations is
typically re-written specifically for every case, as a unified, open-access 
tool to systematically perform this kind of processing is currently missing.

Why use aPriori?
~~~~~~~~~~~~~~~~

The **aPriori** package is designed to streamline this entire workflow. Its
main features include:

- **High-level abstractions** (3D fields, meshes, scalar/vector variables)
  that hide low-level storage details.
- **Pointer-based data access**: data are read from disk *only
  when needed*, enabling work on large datasets even on modest machines.
- **Built-in operations** frequently required in turbulence and combustion:
  filtering, gradients, dissipation rates, scalar statistics, and more.
- **Interoperability** with scientific Python tools (NumPy, PyVista,
  PyTorch/TensorFlow, Cantera, PyCSP).
- **Visualisation utilities** to quickly inspect fields and slices.
- **Extensive documentation and tutorials**, guiding both newcomers and
  experienced users through typical analysis patterns.

The package aims to provide a uniform, intuitive, and efficient interface to
heterogeneous DNS datasets—reducing friction, avoiding unnecessary memory
usage, and accelerating research workflows in turbulence, combustion, and
machine learning. As an example, the following figure displays the typical 
set of operations that using aPriori can be performed with a few lines of code:

.. figure:: /_static/figures/getting_started/Functionalities_light.png
   :figclass: light-only
   :alt: Light mode version
   :align: center

.. figure:: /_static/figures/getting_started/Functionalities_dark.png
   :figclass: dark-only
   :alt: Dark mode version
   :align: center