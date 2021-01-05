Use Case:  Move / copy content between folders
==============================================

Actor
-----

Content Creator

Assumptions
-----------

Content Creator has logged into the CMF (see :doc:`LoginAsMember`).

Procedure
---------

1. Navigate to the folder containing the piece of content which you would
   like to move (or copy) to another folder.

   To retrieve a list of the content you have authored, see :doc:`ViewMyContent`

2. In the "Folder contents" view of the folder, check the box next to the
   content object(s) which you would like to move or copy.

3. Click the "Cut" button (or the "Copy" button, if you wish to create
   a copy in the new location rather than moving the content).

4. The system will set a cookie on your browser (you must have cookies
   enabled) representing the items you cut or copied.

5. Navigate to the folder into which you wish to move or copy the content
   (which might be the same folder).

6. Click the "Paste" button. The system will move or copy the content into
   the folder; new content whose IDs would conflict with exising content in that
   folder will receive an auto-generated name, typically `copy_of_` plus the
   original ID.

7. To undo this action, see :doc:`UndoChanges`.
