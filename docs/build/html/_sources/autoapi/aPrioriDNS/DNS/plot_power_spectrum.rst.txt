aPrioriDNS.DNS.plot_power_spectrum
==================================

.. py:function:: aPrioriDNS.DNS.plot_power_spectrum(field, C=5)

   Plots the power spectrum of a 3D field.

   This function performs a 3D Fourier Transform on the input field, computes the power spectrum,
   and plots both the power spectrum and its averaged version. It also includes a reference line
   proportional to k^(-5/3).

   Parameters:
   -----------
   field : np.ndarray
       The 3D field for which the power spectrum is to be plotted.
   C : float, optional
       The proportionality constant for the reference line. Default is 5.

   Returns:
   --------
   :
   None

   Example:
   --------
   >>> field = np.random.random((64, 64, 64))
   >>> plot_power_spectrum(field)

