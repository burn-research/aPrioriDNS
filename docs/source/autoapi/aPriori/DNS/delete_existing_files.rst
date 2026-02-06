aPriori.DNS.delete_existing_files
=================================

.. py:function:: aPriori.DNS.delete_existing_files(paths, delete=False, context='the API indexes')

   Checks if any of the given paths exist. If so, prompts the user once to confirm deletion.
   Deletes the files if confirmed.

   :param paths: List of file paths to check and possibly delete
   :param context: Optional string to clarify what the files represent (for user message)

