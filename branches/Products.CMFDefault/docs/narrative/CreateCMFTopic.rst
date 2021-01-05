Use Case: Create CMF Topic
==========================

Actor
-----

Site Manager [#]_

Overview
--------

One of the ways you manage the structure of a CMF site is through the use of
CMF Topics. Often a site is comprised of a large amount of content through
which visitors are able to navigate. A Topic allows you to create a dynamic
view onto the available content enabling visitors to drill down into that
content.

Within each Topic can be configured a set of Criteria which constrain the
list of content that appear when viewing the Topic. Topic Criteria can be
based upon any of the data or meta-data that comprise your content.

Note that one useful meta-datam on which to base a Topic Criteria is
"Subject," which is generally configured to allow a set of categories to be
chosen when creating new content. These categories can then be used in a
Topic Criteria to enable visitors to view categorized content. A standard
pattern is to create a number of Topics which each correspond to a category.

Another example of a useful Topic is one which constrains your content by
creation or modification date in order to display all recently changed
content.

Assumptions
-----------

Site Manager has logged into the CMF (see :doc:`LoginAsMember`)

Procedure
---------

1. Select "Folder Contents" from the actions box and navigate to the folder
   which will contain the Topic.

2. Click the "New..." button, which brings up the "Add Content" form allowing
   you to choose among the various content types that you are allowed to create.
   Select "Topic," type in an ID which will be used to identify the Topic in the
   future, and click "Add."

3. The system will create the topic and present you with its "Edit Topic"
   form, which allows you to supply metadata about the topic.

   **Title** --
     the name which will be displayed to visitors.

   **Description** --
     a brief paragraph describing the intended purpose of the Topic. The
     description will be used to annotate the topic object when it is
     included in another display (e.g., the view of its parent folder).

   **Acquire criteria from parent** --
     when creating topic hierarchies [#]_, allows sub-topics to
     refine the search criteria they acquire from their
     parents.

   Click "Change" to save the changes you've made. The system will then show
   the default view of your new Topic, including the list of content which
   match the Topic's criteria and the list of the Topic's Criteria.

   Note that since you have not yet set up any criteria, the Topic will match
   all content objects in the catalog.

4. To constrain the Topic's matches, select "Criteria" in the actions box.
   Create a new Criterion by filling out the "Add Criteria" form, which has the
   following fields:

   **Field id** --
     a drop-down list containing the names of all indexed attributes. Select
     the value corresponding to the field to be searched by the criterion.

   **Criteria type** --
     the kind of search to apply.  The standard types include:

     *String Criterion* --
       matches all content objects for which the specified field in the
       content contains the supplied value

     *Integer Criterion* --
       matches ranges or exact values for fields which are represented as
       whole numbers

     *List Criterion* --
       matches content objects for which the specified field contains one of
       a set of string values.

     *Friendly Date Criterion* --
       applies a range search to a date field, relative to the current time.

   Click "Add" to create the criterion and add it to the Topic.

5. Fill in the value of the "Criterion value" and click "Save changes." You
   may continue to add criteria which each further constrain the content matched
   by the Topic.

6. To view the content matching the current set of criteria, select "View"
   from the actions box.

.. :rubric::Notes

.. [#]
   Like "Create Folder", this is not solely the prerogative of Site Managers;
   Content Creators build topics.

.. [#]
   See "Add a Subtopic":AddSubtopic for an explanation of topic hierarchies.
