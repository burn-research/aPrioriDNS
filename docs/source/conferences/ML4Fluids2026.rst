Machine Learning for Fluids, Amsterdam 2026
===========================================

**Title:**  
*CYPHER data challenge: Benchmarking ML-enhanced turbulent combustion closures*

**Event:** `ERCOFTAC ML4Fluids Conference <https://ml4fluids2026.github.io>`_.

**Location:** Amsterdam, Netherlands  

**Dates:** 4th - 6th March 2026 

**Authors:**  
Lorenzo Piu, Pasquale Eduardo Lapenna, Tamara Osseily, Giuseppe Indelicato,  
Kisuke Shigematsu, Albina Tocilla, Joni Kazani, Antonio Attili, Alessandro Parente

**Related links**

- Cypher webpage: https://cypher.ulb.be
- Data challenge Github page: https://github.com/burn-research/Cypher-challenge-2025
- Data challenge page: https://cypher.ulb.be/data-challenge/
- Download the data for the 2nd part of the challenge: https://drive.google.com/drive/folders/1fyxajDioxhJVdp36sT5zSkMKTxjSQgIq?usp=share_link

**Slides:**  
:download:`Download presentation (PDF) </_static/pdf/ML4Fluids-Cypher.pdf>`

.. raw:: html

   <div style="display:flex; justify-content:center; margin-top:1em;">
       <iframe 
           src="../_static/pdf/ML4Fluids-Cypher.pdf" 
           width="100%" 
           height="500px"
           style="border:1px solid #ddd; border-radius:8px;">
       </iframe>
   </div>

Overview
--------

This presentation introduced the **CYPHER Data Challenge**, a community
initiative aimed at benchmarking machine-learning–enhanced closure models
for turbulent premixed hydrogen flames in Large Eddy Simulation (LES).

The talk addressed three main aspects:

1. **Energy transition context** - 
   Combustion will continue to play a key role in hard-to-abate sectors,
   with hydrogen and synthetic fuels becoming central energy carriers.
   Accurate and predictive simulations are therefore essential.

2. **Need for improved sub-filter closures** - 
   High-fidelity simulations (DNS) reveal the complexity of
   turbulence–chemistry interactions, particularly in hydrogen flames
   affected by thermo-diffusive instabilities.  
   Machine learning has shown strong potential to enhance classical
   physics-based models.

3. **Standardized ML benchmarking via shared datasets** - 
   Inspired by successful ML benchmarks (e.g., ImageNet), the CYPHER
   challenge leverages shared DNS datasets and the Codabench platform
   to enable reproducible and fair comparison of different architectures.

Data Challenge Description
--------------------------

The first data challenge focuses on modeling the **sub-filter scalar flux**
of the filtered progress variable :math:`\widetilde{C}` in lean premixed H₂ flames.

The closure target is:

.. math::

   \mathbf{q}_{\widetilde{C}} = \overline{\rho} \widetilde{\mathbf{u} C}
   - \overline{\rho} \, \widetilde{\mathbf{u}} \widetilde{C}

which is modeled under an eddy-diffusivity assumption:

.. math::

   \nabla \cdot \mathbf{q}_{\widetilde{C}}
   \approx \nabla \cdot \left( \overline{\rho} \, \alpha_t \nabla \widetilde{C} \right)

The dataset includes:

- Flames at different equivalence ratios,
- Multiple filter sizes :math:`\Delta`,
- Separate training and test configurations.

Evaluation metrics combine:

- Prediction accuracy and
- Inference time,

allowing a balanced assessment between model performance and
practical applicability in LES solvers.

Second part
------------

A second data challenge was introduced, focusing on
modeling filtered reaction rates in premixed lean hydrogen flames
under gas-turbine-relevant conditions.

Researchers interested in participating are encouraged to contact:

``pasquale.lapenna@uniroma1.it``

Relevance for aPriori
---------------------

The aPriori framework supports the entire workflow required
for such benchmarking activities:

- DNS data processing,
- Filtering and downsampling,
- Computation of sub-filter quantities,
- Extraction of tensors for model training,
- Integration with PyTorch-based ML models

The software therefore plays a key role in enabling
standardized, reproducible ML-assisted combustion modeling.

Acknowledgments
---------------

The CYPHER Data Challenge is organized within the
CYPHER COST Action, promoting collaboration between
European researchers and industrial stakeholders to
accelerate digitalization in sustainable fuels combustion systems.

Lorenzo Piu has received funding from the European Union’s Horizon 
Europe research and innovation programme under the Marie Skłodowska-Curie 
grant agreement No 101072779 (ENCODING). 
The results of this publication/presentation reflect only the author(s) 
view and do not necessarily reflect those of the European Union. 
The European Union cannot be held responsible for them.
