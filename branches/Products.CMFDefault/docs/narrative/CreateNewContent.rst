Use Case:  Create Content Object
================================

Actor
-----

Content Creator

Assumptions
-----------

Content Creator has logged into the CMF (see :doc:`LoginAsMember`).

Procedure
---------

1. Navigate to a location within CMF where you have rights to add content.
   For example, select 'My Stuff' from your navigation bar to create the content
   in your member folder.

2. If needed, select the 'Folder contents' link from the action box.

3. Click the "New" button. The system will display the "Add Content" page.
   From the list of available content types[1], select the radio button
   corresponding to the type of content which you wish to create. Enter an
   appropriate ID [#]_ for the new piece of content, and click the "Add" button.

4. The system will create a new, empty content object of the type you
   selected, and display the "Standard Resource Metadata" edit form. This form,
   common across all of the default content types which come stock with the CMF,
   allows you to enter specific metadata about your new content:

   **Title** --
     A string used to identify your content.

   **Description** --
     A short summary of the content.

   **Subject** --
     A set of keywords, used for cataloging your content.

   The form provides three submit buttons, each of which saves your content:

   **Change** --
     commits your changes and return to the metadata form.

   **Change and Edit** --
     commits your changes and redirects to the edit form, which will allow
     you to enter the "body" of your content.

   **Change and View** --
     commit your changes and proceed to viewing your new piece of content.

5. Select "Change and Edit", and supply the initial content for
   your object as follows:

   **Document** --
     Enter the text for your object, as either Structured Text [#]_ or HTML [#]_.
     You may either type or paste the text into the textarea, or upload it
     from your computer.

   **News Item** --
     Fill out the "Lead-in" and "Body" text areas.

   **File / Image** --
     Upload the content from your computer.

   **Link / Favorite / Event** --
     Fill out the form with appropriate values.

   Fill out the form and select the "Change" button to save your content.

6. You may wish to continue with one of the workflow use cases:

   - "Submit Content for Review":doc:`SubmitContentForReview`

   - "Publish Content":doc:`PublishContent`

.. :rubric::Notes


.. [#]
   see "Default CMF Content Types", :doc:`DefaultContentTypes`.

.. [#]
   Don't confuse the content's ID with the its Title. ID's cannot contain
   special characters (e.g., comma, asterisk, brackets, parentheses, etc.) A
   good practise is not to use spaces in an ID either. The ID is used in the
   URL to reach the folder's content, so any character which is not allowed
   in a URI is not allowed in the id (see "URI RFC",
   http://www.ietf.org/rfc/rfc2396.txt).

.. [#]
   See :doc.`StructuredTextIntro

.. [#]
   The HTML you enter will have everything outside the BODY tag stripped off;
   the TITLE and META tags will be used, if present, to update the content's
   metadata.
