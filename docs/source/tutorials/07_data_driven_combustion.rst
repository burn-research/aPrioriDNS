Tutorial 7: Data-driven turbulent combustion modeling
=====================================================

.. note::

   The complete code associated with this tutorial is available
   `here <https://github.com/LorenzoPiu/aPriori/blob/main/tutorials/ML_closure_reaction_rates.py>`_.

Learner profile
---------------

This tutorial is aimed at a user who has a solid understanding of 
Computational Fluid Dynamics (CFD) for Combustion. A basic understanding of 
machine learning is not required. 

The tutorial could also be beneficial for those who do not have strong competencies 
in CFD but know Data Science; in fact, apart from some computations to extract interesting 
quantities in reacting flows, the basic operations that we are going to perform on the data 
are based on filtering of 3D fields. In case the overall code is too overwhelming at once,
make sure to try the previous tutorials in this documentation.

Dataset description
-------------------

The dataset used in this example is a sub-domain of the DNS dataset presented in 
:cite:p:`Jung2021, yoo2009three`. The configuration corresponds to a turbulent lifted
hydrogen jet flame issuing into a heated air coflow at atmospheric pressure. The DNS is designed
to investigate flame stabilization mechanisms close to the autoignition limit.

A diluted fuel mixture composed of 65\% H\ :sub:`2` and 35\% N\ :sub:`2` (by volume) is injected
from a central slot at an inlet temperature of 400 K. The jet is surrounded on both sides by
coflowing air streams at 850 K. The jet width at the inlet is 2 mm and the corresponding jet
Reynolds number is 8000. Turbulent inflow conditions are imposed by superimposing velocity
fluctuations with an intensity of 10\% of the bulk jet velocity, generated from an auxiliary
homogeneous isotropic turbulence field and prescribed at the inlet using Taylor’s hypothesis.

The full DNS domain comprises
:math:`2000 \times 1600 \times 400` grid points
(:math:`15H \times 20H \times 3H`) with uniform spacing in the streamwise and spanwise directions
and a stretched transverse grid. The simulation is performed using the Sandia DNS solver **S3D**
with a detailed hydrogen–air mechanism consisting of nine species and twenty-one
elementary reactions developed by Li *et al.* :cite:p:`Li2004`.

In this tutorial, only a spatial sub-domain of the original dataset is employed to reduce memory
requirements and improve reproducibility, while retaining the key physical and chemical features
of the lifted flame configuration.

.. figure:: /_static/figures/getting_started/Lifted_h2_subdomain.png
   :align: center
   :width: 95%

   Figure 1: Graphical representation of the DNS subset used in the present example

A priori validation methodology
-------------------------------

Filtered species transport equation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the context of Large Eddy Simulation (LES), the transport equation for the
Favre-filtered mass fraction of species :math:`k` reads

.. math::

   \frac{\partial (\bar{\rho}\,\tilde{Y}_k)}{\partial t}
   + \frac{\partial (\bar{\rho}\,\tilde{Y}_k\,\tilde{u}_i)}{\partial x_i}
   =
   - \frac{\partial j^{\mathrm{sgs}}_{k,i}}{\partial x_i}
   + \overline{\dot{\omega}}_k ,

where:

- :math:`\tilde{Y}_k` is the Favre-filtered mass fraction of species :math:`k`,
- :math:`j^{\mathrm{sgs}}_{k,i}` is the subgrid-scale diffusive flux of species :math:`k`,
- :math:`\overline{\dot{\omega}}_k` is the filtered chemical source term.

In this tutorial, we focus on the **closure of the chemical source term**
:math:`\overline{\dot{\omega}}_k`, which represents one of the main challenges
in turbulent combustion modeling.

A priori evaluation of chemical source terms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From Direct Numerical Simulation (DNS) data, chemical source terms can be
computed directly using detailed chemistry (e.g. through Cantera).
Since DNS resolves both transport and chemical processes down to the finest
relevant scales, the resulting reaction rates naturally account for the full
interaction between turbulence and chemistry.

In a priori analysis, these DNS-based reaction rates are considered as
reference values.

In contrast, LES does not have access to this level of detail. Only
filtered quantities—such as temperature, velocity, pressure, and species
mass fractions—are available. To mimic the information accessible in LES,
the DNS fields are therefore **filtered explicitly**.

Starting from these filtered fields, chemical source terms can be recomputed
using the same detailed chemistry models. However, because the filtering
operation removes small-scale fluctuations, the resulting reaction rates
are generally less accurate than those obtained from the original DNS data.
In particular, transport processes are no longer resolved down to the
Kolmogorov scale, and the interaction between turbulence and chemistry is
only partially captured.

The comparison between:
- reaction rates computed from the original DNS fields, and
- reaction rates recomputed from the filtered fields,

forms the basis of the a priori validation framework used to assess
turbulence–chemistry interaction closures.