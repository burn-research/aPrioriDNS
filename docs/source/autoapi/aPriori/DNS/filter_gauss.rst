aPriori.DNS.filter_gauss
========================

.. py:function:: aPriori.DNS.filter_gauss(field, delta, mode='mirror')

   Apply a Gaussian filter to a 3D numpy array.

   The function checks the input types and dimensions, then applies a
   Gaussian filter to the input array using scipy's gaussian_filter function.
   The standard deviation of the Gaussian filter is calculated as
   sqrt(1/12*delta^2), which corresponds to a Gaussian distribution with a
   variance equal to the square of the filter size divided by 12.

   Parameters:
   -----------

       field : numpy.ndarray
           The input 3D array.

       delta : int
           The size of the Gaussian filter.

       mode : str, optional
           Determines how the input array is extended when the filter overlaps a border. Default is 'mirror'.
           Possible values are 'reflect', 'constant', 'nearest', 'mirror', 'wrap'.

   Raises:
   -------

       TypeError:
           If delta is not an integer or field is not a numpy array.

       ValueError:
           If field is not a 3-dimensional array.

   Returns:
   --------
   :

       field_filt : numpy.ndarray
           The filtered array.

