Use Case: Add content folders
=============================

Actor
-----

Content Creator

Overview
--------

As with directories on a filesystem, foldersin a CMF Site allow Content
Creators to partition their content into manageable groups.

Assumptions
-----------

Content Creator has logged into the CMF (see :doc:`LoginAsMember`).

Procedure
---------

1. Navigate to the folder in which you would like to create sub-folders.

2. In the "Folder contents" view of the folder, select the "New" button.

3. From the list of addable portal types, select "Folder" by clicking the
   adjacent radio button. Supply an ID [#]_ for the new folder in the input
   field at the bottom of the page, and click the "Add" button.

4. The system will create the new folder using the ID you supplied, and
   present you with a form for editing the folder's properties.

5. Supply appropriate values as follows:

   **Title** --  a "human-readable" title for the folder.

   **Description** -- a brief paragraph summarizing the use to which the
   folder is put.

6. Click the "Change" button. The system will update the folder's metadata
   using the values you supply.

.. rubric:: Notes

.. [#]
   Don't confuse the folder's ID with the its Title. ID's cannot contain
   special characters (e.g., comma, asterisk, brackets, parentheses, etc.) A
   good practise is not to use spaces in an ID either. The ID is used in the url
   to reach the folder's content, so any character which is not allowed in a URI
   is not allowed in the id (see: "URI RFC",
   http://www.ietf.org/rfc/rfc2396.txt).
