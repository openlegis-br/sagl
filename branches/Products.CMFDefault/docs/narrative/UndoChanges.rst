Use Case:  Undo Changes to Content
==================================

Actor
-----

Content Creator

Assumptions
-----------

* Content Creator has logged into the CMF (see :doc:`LoginAsMember`).

* Content Creator has made changes to content which she wishes to undo (see
  :doc:`ChangeContent`).

* The changes are "undoable" [#]_.

Procedure
---------

1. Select 'Undo' from the actions box. The system will present a list of the
   transactions which you have permission to undo.

2. Select the checkbox next to the transaction which you wish to undo and
   click the undo button. The system will undo that transaction and redisplay
   the list of transactions.

.. :rubric::Notes

.. [#]
   Transactions which involve changing content remain undoable until one or
   more objects modified by the transaction are modified by a subsequent
   transaction. Normally, this means that only the latest transaction to an
   object is undoable, unless the later transactions are also undone.

   It is also possible to have transactions above the transaction in the list
   which do not effect the ability to undo a change a user wishes to undo.
