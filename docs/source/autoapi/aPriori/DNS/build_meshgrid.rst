aPriori.DNS.build_meshgrid
==========================

.. py:function:: aPriori.DNS.build_meshgrid(X_m_path: str, Y_m_path: str, Z_m_path: str)

   Converts 1D mesh coordinate files (X, Y, Z) into 3D meshgrid
   coordinate fields and overwrites the original files.

   The input files must contain 1D coordinate vectors.
   The output files will contain the corresponding 3D meshgrid
   coordinates stored in flattened binary format via `save_file()`.

   :param X_m_path: Path to the X coordinate file (1D vector).
   :type X_m_path: str
   :param Y_m_path: Path to the Y coordinate file (1D vector).
   :type Y_m_path: str
   :param Z_m_path: Path to the Z coordinate file (1D vector).
   :type Z_m_path: str

   :returns: The generated mesh shape as (Nx, Ny, Nz).
   :rtype: tuple[int, int, int]

   :raises ValueError: If any of the input arrays is not 1D or is empty.

