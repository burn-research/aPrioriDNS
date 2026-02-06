aPriori.process_file
====================

.. py:function:: aPriori.process_file(file_path)

   Read a binary file and convert its contents into a numpy array.

   The function uses numpy's fromfile function to read a binary file and
   convert its contents into a numpy array.
   The data type of the elements in the output array is set to '<f4', which
   represents a little-endian single-precision float.

   Parameters:
   -----------
   file_path : str
       The path to the file to be processed.

   Returns:
   --------
   :

   numpy.ndarray:
       The numpy array obtained from the file contents.

