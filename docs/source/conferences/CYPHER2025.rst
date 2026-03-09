CYPHER Meeting, Naples 2025
===========================

**Title:**  
*aPriori: a Python package to process direct numerical simulations*

**Event:** `CYPHER WG1 & WG2 Meeting – Integrating Renewable Fuels and Advanced Simulations <https://cypher.ulb.be/event/cypher-wg1-wg2-meeting-workshop-integrating-renewable-fuels-and-advanced-simulations/>`_.

**Location:** Naples, Italy  

**Dates:** 10th - 12th September 2025

**Authors:**  
Lorenzo Piu, Heinz Pitsch, Alessandro Parente

**Slides:**  
:download:`Download presentation (PDF) </_static/pdf/Cypher_workshop_apriori.pdf>`

.. raw:: html

   <div style="display:flex; justify-content:center; margin-top:1em;">
       <iframe 
           src="../_static/pdf/Cypher_workshop_apriori.pdf" 
           width="100%" 
           height="500px"
           style="border:1px solid #ddd; border-radius:8px;">
       </iframe>
   </div>

Overview
--------

This presentation introduced **aPriori**, an open-source Python framework
designed to simplify the post-processing and analysis of **Direct Numerical
Simulation (DNS)** datasets for reacting and non-reacting flows.

The talk addressed three main aspects:

1. **Growing importance of DNS datasets** -  
   DNS provide highly detailed physical insights into turbulent flows and
   combustion processes, including flame instabilities, pollutant formation,
   and turbulence–chemistry interactions. However, the increasing size and
   complexity of these datasets also raises challenges in terms of
   accessibility, storage, and post-processing workflows.

2. **Need for standardized DNS post-processing tools** -  
   Public DNS repositories such as BLASTNet provide valuable datasets for
   turbulence and combustion research, but extracting physically meaningful
   quantities often requires extensive custom scripts and significant
   computational effort. A dedicated software framework can streamline
   operations such as filtering, sub-domain extraction, and the computation
   of derived quantities.

3. **Open-source software for reproducible analysis** -  
   Inspired by the need for reproducible workflows in data-driven combustion
   modeling, **aPriori** provides a modular Python library that facilitates
   DNS data handling, filtering operations, and model assessment tasks
   required in turbulence and combustion research.

Software Description
--------------------

The **aPriori framework** provides a set of tools for handling and
post-processing large DNS datasets used in turbulence and combustion studies.

The library enables several key operations:

- Reading DNS datasets from structured file repositories,
- Handling large multidimensional scalar and vector fields,
- Performing spatial filtering and downsampling operations,
- Extracting sub-domains for localized analysis,
- Computing derived quantities such as gradients and strain rates,
- Evaluating turbulence and combustion models using DNS data.

The software architecture is designed around a **modular and
object-oriented structure**, where core classes manage different aspects of
the workflow, including scalar fields, mesh information, and three-dimensional
datasets.

DNS Data Processing Workflow
----------------------------

The framework enables efficient workflows for processing large DNS datasets
that may reach tens or hundreds of gigabytes.

Typical analysis steps include:

1. Loading DNS data fields from disk,
2. Computing derived quantities such as velocity gradients or strain rates,
3. Applying spatial filters to obtain LES-like fields,
4. Computing sub-filter quantities required for turbulence model assessment.

For example, the software can be used to perform an **a-priori evaluation of
the Smagorinsky model**, where filtered DNS fields are used to compute the
quantities required for Large Eddy Simulation closures.

These operations can be performed using concise Python scripts while
maintaining computational efficiency when handling large arrays.

Key Features
------------

The main capabilities of **aPriori** include:

- Efficient handling of large DNS datasets,
- Modular architecture facilitating extensibility,
- Built-in tools for spatial filtering and downsampling,
- Computation of sub-filter quantities for turbulence and combustion models,
- Integration with Python scientific computing libraries.

The framework is particularly well suited for **data-driven turbulence and
combustion modeling**, where large datasets must be processed to extract
training features for machine learning models.


Acknowledgments
---------------

Lorenzo Piu has received funding from the European Union’s Horizon
Europe research and innovation programme under the Marie Skłodowska-Curie
grant agreement No 101072779 (ENCODING).
The results of this publication/presentation reflect only the author(s)
view and do not necessarily reflect those of the European Union.
The European Union cannot be held responsible for them.

