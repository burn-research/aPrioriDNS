aPriori.DNS.filter_box
======================

.. py:function:: aPriori.DNS.filter_box(field, delta, mode='mirror')

       Apply a box filter to a 3D numpy array using scipy's convolve function.

       The function creates a box kernel with the given size, normalizes it so that the sum of its elements is 1,
       and applies it to the input array using scipy's convolve function.

       Note:
       -----
       When the kernel size is even, the center of the kernel is not a single element but lies between elements.
       In such cases, scipy's convolve function does not shift the kernel to align its center with an element of the input array.
       Instead, it uses the original alignment where the center of the kernel is between elements.
       This means that the output array will be shifted compared to what you might expect if the kernel was centered on an element of the input array.
       If you want to ensure that the kernel is always centered on an element of the input array, you should use an odd-sized kernel.
       If you need to use an even-sized kernel and want to center it on an element, you would need to manually shift the output array to align it as desired.

       Parameters:
       -----------
       field : numpy.ndarray
           The input 3D array.

       delta : int
           The size of the box filter.

       mode : str, optional
           The mode parameter determines how the input array is extended when the filter overlaps a border.
           Default is 'mirror'.

       Returns:
       --------
       field_filt : numpy.ndarray
           The filtered array.

       Example:
       --------
       >>> import numpy as np
       >>> from scipy.ndimage import convolve

       >>> # Create a sample 3D array
       >>> field = np.random.rand(5, 5, 5)

       >>> # Apply a box filter with size 3
       >>> delta = 3
       >>> filtered_field = filter_box(field, delta)

       >>> print("Original field:
   ", field)
       >>> print("Filtered field:
   ", filtered_field)


