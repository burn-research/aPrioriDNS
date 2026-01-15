aPrioriDNS.DNS.generate_mask
============================

.. py:function:: aPrioriDNS.DNS.generate_mask(start, shape, delta)

   Computes the downsampled mask of a 3D field.

   :param start: Is the a list with the indexes where to start doing the mask.
   :type start: list of int
   :param shape: Is the shape of the input field
   :type shape: list of int
   :param delta: Is the filter size
   :type delta: int

   :returns: **mask** -- A 3D vector of boolean values.
   :rtype: numpy array of bool

