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

Favre Filtered species transport equation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Step 1: DNS data processing
---------------------------

In this first step, we extract from the DNS dataset all the quantities required
to perform an a priori analysis and to build a data-driven closure model.
The goal is to construct, from the DNS data, both reference quantities and
LES-like quantities obtained by explicit filtering.

Dataset loading and initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We begin by specifying the path to the DNS sub-domain and initializing a
:class:`Field3D` object. If the dataset is not found locally,
it is automatically downloaded.

.. code-block:: python

   import os
   import aPriori as ap
   from aPriori.DNS import Field3D

   directory = os.path.join('.', 'Lifted_H2_subdomain')

   T_path = os.path.join(directory, 'data', 'T_K_id000.dat')
   if not os.path.exists(T_path):
       ap.download(dataset='h2_lifted')

   DNS_field = Field3D(directory)

At this stage, the DNS field contains all primitive variables (velocity,
temperature, species mass fractions) resolved down to the smallest scales.

Compute reaction rates on the DNS grid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the detailed chemical mechanism associated with the dataset, we compute
the chemical source terms directly on the DNS grid. These reaction rates
naturally account for the full interaction between turbulence and chemistry
and are therefore used as reference values in the a priori analysis.

.. code-block:: python

   DNS_field.compute_reaction_rates()

The heat release rate (HRR) is computed automatically as part
of this operation.

Filtering the DNS field
^^^^^^^^^^^^^^^^^^^^^^

To mimic the information available in Large Eddy Simulation (LES), the DNS
field is explicitly Favre-filtered. In this example, a filter width of
:math:`\Delta = 16` grid points is used.

It is important to note that the filtering operation applies to **all**
variables present in the data folder. Since the DNS reaction rates have already
been computed, they are filtered as well, yielding the filtered reference
source terms :math:`\overline{\dot{\omega}}^{DNS}`.

.. code-block:: python

   filter_size = 16
   filtered_field = Field3D(DNS_field.filter_favre(filter_size))

Compute reaction rates on the filtered field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting from the LES-like filtered quantities (filtered temperature and
species mass fractions), reaction rates are recomputed using the same
detailed chemistry. These rates correspond to a **Laminar Finite Rate (LFR)**
approximation evaluated on filtered fields.

.. code-block:: python

   filtered_field.compute_reaction_rates()

The discrepancy between DNS-filtered and LFR reaction rates highlights the
impact of unresolved turbulence–chemistry interactions.

Compute additional variables of interest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To train a data-driven closure model, additional LES-scale quantities are
required. In this tutorial, we compute:

- the strain-rate magnitude,
- the residual dissipation rate (Smagorinsky model),
- the residual kinetic energy,
- chemical and mixing time scales.

These quantities characterize the local interaction between turbulence
and chemistry and are commonly used in subgrid-scale modeling.

.. code-block:: python

   filtered_field.compute_strain_rate(save_tensor=True)
   filtered_field.compute_residual_dissipation_rate(mode='Smag')
   filtered_field.compute_residual_kinetic_energy()

   filtered_field.compute_chemical_timescale(mode='SFR')
   filtered_field.fuel = 'H2'
   filtered_field.ox = 'O2'
   filtered_field.compute_chemical_timescale(mode='Ch')
   filtered_field.compute_mixing_timescale(mode='Kolmo')

At the end of this step, the filtered field contains both LES-resolved variables
and reference subgrid-scale quantities, enabling the construction of
data-driven closure models.

Step 2: Neural network training
-------------------------------

In this second step, a neural network is trained to model the correction factor
:math:`\gamma` that accounts for unresolved turbulence–chemistry interactions.
The approach follows the same conceptual framework used in models such as
EDC and PaSR, where the filtered chemical source term is written as

.. math::

   \overline{\dot{\omega}}_k = \gamma \, \dot{\omega}^{LFR}_k .

Here, :math:`\dot{\omega}^{LFR}_k` is the reaction rate computed from filtered
quantities, and :math:`\gamma` is a data-driven correction predicted by the
neural network.

Data preprocessing for PyTorch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We construct the input feature matrix using quantities available at LES scale:
temperature, strain-rate magnitude, and the slowest chemical time scale.
The target output is the DNS heat release rate.

.. code-block:: python

   shape  = filtered_field.shape
   length = shape[0] * shape[1] * shape[2]

   T     = filtered_field.T.value.reshape(length, 1)
   S     = filtered_field.S_LES.value.reshape(length, 1)
   Tau_c = filtered_field.Tau_c_SFR.value.reshape(length, 1)

   HRR_LFR = filtered_field.HRR_LFR.value.reshape(length, 1)
   HRR_DNS = filtered_field.HRR_DNS.value.reshape(length, 1)

The input variables are normalized and transformed before building the
training matrix.

.. code-block:: python

   T = (T - np.min(T)) / (np.max(T) - np.min(T))
   S = np.log10(S)
   S = (S - np.min(S)) / (np.max(S) - np.min(S))
   Tau_c = np.log10(Tau_c)
   Tau_c = (Tau_c - np.min(Tau_c)) / (np.max(Tau_c) - np.min(Tau_c))

   X = np.hstack([T, S, Tau_c])

The dataset is then split into training and testing subsets and converted
to PyTorch tensors.

Neural network architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The neural network is implemented as a fully connected feed-forward model
using PyTorch. The architecture consists of multiple hidden layers with
ReLU activation functions.

.. code-block:: python

   class NeuralNetwork(nn.Module):
       def __init__(self, input_size, hidden_size, output_size, num_layers):
           super().__init__()
           self.layers = nn.ModuleList()
           self.layers.append(nn.Linear(input_size, hidden_size))
           for _ in range(num_layers - 1):
               self.layers.append(nn.Linear(hidden_size, hidden_size))
           self.layers.append(nn.Linear(hidden_size, output_size))

       def forward(self, x):
           for layer in self.layers[:-1]:
               x = torch.relu(layer(x))
           return self.layers[-1](x)

Training loop
^^^^^^^^^^^^^

The model is trained by minimizing the mean squared error between the
DNS heat release rate and the corrected LFR prediction
:math:`\gamma \dot{Q}_{LFR}`.

.. code-block:: python

   loss = criterion(output * HRR_LFR_train, HRR_DNS_train)

Training and testing losses are monitored to assess convergence and
generalization.

Step 3: Results visualization
^^^^^^^^^^^^^^^^^^^^^

Once trained, the neural network is evaluated on the full dataset.
Parity plots are used to compare the DNS heat release rate with both
the LFR model and the machine-learning-corrected prediction.

.. code-block:: python

   gamma = model(torch.tensor(X, dtype=torch.float32).to(device)).cpu().numpy()

   ap.parity_plot(HRR_DNS, HRR_LFR, density=True,
                  x_name=r'$\dot{Q}_{DNS}$',
                  y_name=r'$\dot{Q}_{LFR}$')

   ap.parity_plot(HRR_DNS, gamma * HRR_LFR, density=True,
                  x_name=r'$\dot{Q}_{DNS}$',
                  y_name=r'$\dot{Q}_{ML}$')

Spatial distributions of the error and of the predicted correction factor
are finally visualized using mid-plane contour plots.