aPriori.DNS.check_mesh_files
============================

.. py:function:: aPriori.DNS.check_mesh_files(X_m_path, Y_m_path, Z_m_path, shape)

   Checks whether mesh coordinate files match either:
   - a full 3D mesh of size prod(shape)
   - a 1D mesh of sizes shape[0], shape[1], shape[2]

   :returns: * **check_3d** (*bool*) -- True if all coordinates match full 3D size.
             * **check_1d** (*bool*) -- True if all coordinates match corresponding 1D axis size.

