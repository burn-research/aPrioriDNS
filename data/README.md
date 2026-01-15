# Tutorial datasets

## Lifted H2 subdomain

This folder contains a dataset used as a reference to test the library. The dataset was extracted from a DNS simulation of a [lifted non-premixed hydrogen jet flame](https://blastnet.github.io/jung2021.html) [1]. 

The original snapshot of this flame is available on [Blastnet](https://blastnet.github.io) [2, 3] The domain was reduced to a size of 200x200x100 grid points, without changing the formatting.

<p align="center">
  <img src="img/Lifted_H2_subset%20asymmetric_2.png" width="80%">
</p>

## Forced HIT Re_lambda = 184

This dataset originates from a Direct Numerical Simulation (DNS) of forced Homogeneous Isotropic Turbulence (HIT) at a turbulent Reynolds number Re_lambda equal to 184. The simulation was conducted as part of a study on the structure and kinematics of iso-scalar fields by Michael Gauding et al. [[4](10.1017/jfm.2022.367)].

It is provided here as a reference case for demonstrating non-reactive applications of the library. The dataset is a subset of the original case available on [BLASTNet](https://blastnet.github.io/gauding2022), selected to comply with GitHub’s storage constraints and to enable faster execution during tutorials.

<p align="center">
  <img src="img/Forced_HIT.png" width="100%">
</p>

## License

All datasets provided on BLASTNet are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/))

## Bibliography

[1] Ki Sung Jung, Seung Ook Kim, Tianfeng Lu, Jacqueline H. Chen, Chun Sang Yoo,
On the flame stabilization of turbulent lifted hydrogen jet flames in heated coflows near the autoignition limit: A comparative DNS study,
Combustion and Flame,
Volume 233,
2021,
111584,
ISSN 0010-2180,
https://doi.org/10.1016/j.combustflame.2021.111584.
(https://www.sciencedirect.com/science/article/pii/S0010218021003278)

[2] W. T. Chung, B. Akoush, P. Sharma, A. Tamkin, K. S. Jung, J. H. Chen, J. Guo, D. Brouzet, M. Talei, B. Savard, A.Y. Poludnenko & M. Ihme. Turbulence in Focus: Benchmarking Scaling Behavior of 3D Volumetric Super-Resolution with BLASTNet 2.0 Data. Advances in Neural Information Processing Systems (2023) 36.

[3] W. T. Chung, M. Ihme, K. S. Jung, J. H. Chen, J. Guo,  D. Brouzet, M. Talei, B. Jiang, B. Savard, A. Y. Poludnenko, B. Akoush, P. Sharma & A. Tamkin. BLASTNet Simulation Dataset (Version 2.0), 2023. https://blastnet.github.io/. 

[4] Gauding M, Thiesset F, Varea E, Danaila L. Structure of iso-scalar sets. Journal of Fluid Mechanics. 2022;942:A14. doi:10.1017/jfm.2022.367
