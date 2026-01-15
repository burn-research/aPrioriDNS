aPrioriDNS.NN.VectorScaler
==========================

.. py:class:: aPrioriDNS.NN.VectorScaler(mode='minmax', modulus=False, log=False, vmin=None, vmax=None, copy=True)

   Description:
   ------------
   A class for scaling and transforming vector data. This class supports various scaling
   modes, such as min-max scaling, standard scaling, and mean scaling, with additional options
   for modulus transformation, logarithmic scaling, and value clipping.

   The operations are performed in the following order:
       1. Modulus transformation
       2. Clipping
       3. Logarithmic transformation (with an automatic clipping at 1e-20 to avoid negative or zero values)
       4. Scaling based on the specified mode

   Attributes:
   -----------
       - mode (str):
           The scaling mode. Options are 'minmax', 'standard', 'mean', or None.

       - modulus (bool):
           Whether to apply the modulus (absolute value) operation.

       - log (bool):
           Whether to apply logarithmic transformation.

       - vmin (float, optional):
           Minimum value for clipping.

       - vmax (float, optional):
           Maximum value for clipping.

       - copy (bool):
           Whether to create a copy of the input array.

       - max, min, mean, std, ptp (float):
           calculated scaling parameters, depending on mode.

   Methods:
   --------
       - __init__(mode='minmax', modulus=False, log=False, vmin=None, vmax=None, copy=True):
           Initialize the VectorScaler with scaling mode, transformation options, and optional clipping bounds.

       - _preprocess_input(x):
           Preprocess the input array by applying modulus, clipping, and logarithmic transformations.

       - _reset():
           Reset the scaler attributes (max, min, mean, std, ptp) to None. Used before recalculating parameters.

       - fit(x):
           Fit the VectorScaler to the data by calculating the necessary statistics based on the specified mode.

       - transform(x):
           Transform the input data based on the fitted scaling parameters and mode.

       - load(state_dict):
           Load saved state values into the VectorScaler.

       - state_dict:
           Return the current state of the VectorScaler, including mode and calculated parameters.


   .. py:attribute:: mode
      :value: 'minmax'



   .. py:attribute:: modulus
      :value: False



   .. py:attribute:: log
      :value: False



   .. py:attribute:: vmin
      :value: None



   .. py:attribute:: vmax
      :value: None



   .. py:attribute:: copy
      :value: True



   .. py:attribute:: max
      :value: None



   .. py:attribute:: min
      :value: None



   .. py:attribute:: mean
      :value: None



   .. py:attribute:: std
      :value: None



   .. py:attribute:: ptp
      :value: None



   .. py:method:: fit(x)

      Fit the VectorScaler to the data by calculating the necessary statistics based on the specified mode.

      Parameters:
      -----------
          - x (array-like):
              The data to fit the scaler to.

      Raises:
      -------
          - ValueError:
              If the mode is unrecognized.



   .. py:method:: transform(x)

      Transform the input data based on the fitted scaling parameters and mode.

      Parameters:
      -----------
          - x (array-like):
              The data to transform.

      Returns:
      --------
      :
          - np.ndarray:
              The scaled and transformed data.

      Raises:
      -------
          - ValueError:
              If the mode is unrecognized.



   .. py:method:: load(state_dict)

      Load saved state values into the VectorScaler.

      Parameters:
      -----------
          - state_dict (dict):
              Dictionary containing scaler attributes to load.



   .. py:property:: state_dict

      Return the current state of the VectorScaler, including mode and calculated parameters.

      Returns:
      --------
          - dict:
              A dictionary representation of the scaler's current state.

