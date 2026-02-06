aPriori.DNS.save_file
=====================

.. py:function:: aPriori.DNS.save_file(X, file_name)

   Saves the given array to a file in binary format.

   This function converts the input array to a 32-bit float representation and saves it
   to a file using the specified file name. The file is saved in a binary format.

   Parameters:
   -----------
   X : np.ndarray
       The array to be saved. It will be converted to a 32-bit float array before saving.
   file_name : str
       The name of the file where the array will be saved.

   Returns:
   --------
   :
   None

   Example:
   --------
   >>> import numpy as np
   >>> X = np.array([1.5, 2.5, 3.5], dtype=np.float64)
   >>> save_file(X, "test.bin")
   >>> loaded_X = np.fromfile("test.bin", dtype=np.float32)
   >>> print(loaded_X)
   [1.5 2.5 3.5]

