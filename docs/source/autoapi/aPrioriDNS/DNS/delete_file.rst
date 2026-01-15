aPrioriDNS.DNS.delete_file
==========================

.. py:function:: aPrioriDNS.DNS.delete_file(file_path)

   Deletes the specified file from the file system.

   This function checks if the file at the given path exists and deletes it if it does.
   If the file does not exist, it prints a message indicating that the file was not found.

   Parameters:
   -----------
   file_path : str
       The path to the file that needs to be deleted.

   Returns:
   --------
   :
   None

   Example:
   --------
   >>> delete_file("example.txt")
   No such file: 'example.txt'
   >>> with open("example.txt", "w") as f:
   ...     f.write("This is a test file.")
   >>> delete_file("example.txt")
   >>> os.path.exists("example.txt")
   False

