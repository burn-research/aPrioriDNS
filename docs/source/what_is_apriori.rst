What is aPriori
===============

Scope of the project
~~~~~~~~~~~~~~~~~~~~

**aPriori** is a Python package for working with **Direct Numerical Simulation
(DNS)** data. Its goal is to make large, high-fidelity datasets easier to use,
both for people with a background in combustion / fluid dynamics and for those
coming from other domains such as data science or machine learning. :contentReference[oaicite:5]{index=5}

What are Direct numerical simulations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the rise of Data Science, large datasets have become increasingly valuable for researchers. The vast amount of information they contain offers various opportunities in many fields of science and engineering. 
In the field of Fluid Dynamics, Direct Numerical Simulation (DNS) is a computational method that resolves all the scales of the turbulence spectrum :cite:`baritaud1996direct`. This makes the resulting datasets extremely valuable for:

- carrying out detailed physical analyses of flow and chemical structures. :contentReference[oaicite:6]{index=6}
- training data-driven models (e.g. neural networks),
- developing and evaluating turbulence or combustion models,

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