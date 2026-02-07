aPriori.plot_utilities.plot_multifield
======================================

.. py:function:: aPriori.plot_utilities.plot_multifield(X, Y, fields, titles=None, n_cols=None, figsize=None, cmap='viridis', vmin=None, vmax=None, side_text=None)

   Plot multiple 2D fields as subplots with shared colorbar and scaling.

   Parameters:
   -----------
   X : array-like
       2D mesh for X coordinates
   Y : array-like
       2D mesh for Y coordinates
   fields : array-like
       3D array of shape (n_fields, ny, nx) or list of 2D arrays
       Each field represents the same variable at different conditions
   titles : list of str, optional
       Titles for each subplot. If None, uses "Field 1", "Field 2", etc.
   n_cols : int, optional
       Number of columns in the subplot grid. If None, automatically determined
   figsize : tuple, optional
       Figure size (width, height). If None, automatically computed based on data aspect ratio
   cmap : str, optional
       Colormap name (default: 'viridis')
   vmin : float, optional
       Minimum value for colorbar. If None, uses global minimum of fields
   vmax : float, optional
       Maximum value for colorbar. If None, uses global maximum of fields
   side_text : str, optional
       Text to display on the right side of the figure

   Returns:
   --------
   :
   fig : matplotlib.figure.Figure
       The figure object
   axes : numpy.ndarray
       Array of subplot axes

