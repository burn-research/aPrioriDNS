aPriori.DNS.filter_3D
=====================

.. py:function:: aPriori.DNS.filter_3D(field, filter_size, RHO=None, favre=False, filter_type='Gauss')

       Apply a 3D filter (Gaussian or box) to a numpy array, with optional Favre filtering.

       This function filters a 3D field using either a Gaussian or box filter. When Favre filtering is enabled, the field
       is first multiplied by the density field (RHO) before filtering, and the result is normalized by the filtered density field.

       Parameters:
       -----------
       field : numpy.ndarray
           The input 3D array to be filtered.

       filter_size : float
           The size of the filter.

       RHO : numpy.ndarray, optional
           The density field used for Favre filtering. Required if favre is True.

       favre : bool, optional
           If True, apply Favre filtering using the density field (RHO). Default is False.

       filter_type : str, optional
           The type of filter to apply. Valid options are 'Gauss' and 'Box'. Default is 'Gauss'.

       Returns:
       --------
       field_filt : numpy.ndarray
           The filtered 3D array.

       Raises:
       -------
       ValueError
           - If favre is True and RHO is not provided.
           - If field or RHO are not 3-dimensional arrays.
           - If field and RHO do not have the same shape.
           - If an invalid filter_type is provided.

       TypeError
           If RHO is not a numpy array.

       Example:
       --------
       >>> import numpy as np

       >>> # Create a sample 3D array
       >>> field = np.random.rand(5, 5, 5)
       >>> RHO = np.random.rand(5, 5, 5)
       >>> filter_size = 2.0

       >>> # Apply Gaussian filter
       >>> filtered_field = filter_3D(field, filter_size, filter_type='Gauss')
       >>> print("Filtered field (Gaussian):
   ", filtered_field)

       >>> # Apply box filter
       >>> filtered_field = filter_3D(field, filter_size, filter_type='Box')
       >>> print("Filtered field (Box):
   ", filtered_field)

       >>> # Apply Favre filtering with Gaussian filter
       >>> filtered_field_favre = filter_3D(field, filter_size, RHO=RHO, favre=True, filter_type='Gauss')
       >>> print("Favre filtered field (Gaussian):
   ", filtered_field_favre)

       >>> # Apply Favre filtering with box filter
       >>> filtered_field_favre = filter_3D(field, filter_size, RHO=RHO, favre=True, filter_type='Box')
       >>> print("Favre filtered field (Box):
   ", filtered_field_favre)


