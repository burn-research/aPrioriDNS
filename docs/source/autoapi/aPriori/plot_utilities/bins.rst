aPriori.plot_utilities.bins
===========================

.. py:function:: aPriori.plot_utilities.bins(x, y, n=40, log=False)

   Bins the data in x and y into n bins and computes the average, max, and min of y for each bin.

   Args:
   -----
       x (array-like):
           Independent variable.
       y (array-like):
           Dependent variable.
       n (int, optional):
           Number of bins. Default is 40.
       log (bool, optional):
           If True, use logarithmic bins. Default is False.

   Returns:
   --------
   :
       tuple
           - x_b (np.ndarray): Midpoints of the bins in x.
           - y_b (np.ndarray): Average values of y in each bin.
           - y_max (np.ndarray): Maximum values of y in each bin.
           - y_min (np.ndarray): Minimum values of y in each bin.

