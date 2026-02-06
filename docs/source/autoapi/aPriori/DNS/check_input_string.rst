aPriori.DNS.check_input_string
==============================

.. py:function:: aPriori.DNS.check_input_string(input_string, valid_strings, input_name)

   Checks if the value of input_string is contained in the list valid_strings.
   If the result is positive, returns None, if the result is negative
   raises an error

   :param input_string: Is the string that must be checked
   :type input_string: string
   :param valid_strings: Is the list of valid strings
   :type valid_strings: list of strings
   :param input_name: Is the name of the parameter that we are checking
   :type input_name: string

   :returns: * *None*
             * *NOTES*
             * *-------*
             * *Example of output if the function finds an error*
             * **ValueError** (*Invalid parameter mode 'mode1'. Valid options are:*) --

               - mode_1
               - mode_2
               - mode_3

