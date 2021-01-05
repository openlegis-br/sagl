Use Case: Create a CMF Site
===========================

Actor
-----

Site Manager

Overview
--------

The top-level concept in the CMF is the idea of a "CMF Site". A CMF site is a
content-oriented Web site with specific business goals, workflows,
collaborations and audiences (content consumers).

The "CMF Site" object is used in Zope to represent and manage a CMF Web site.
The CMF Site object acts as a container for site components and content, and
provides interfaces for configuring the functionality of the site.

Assumptions
-----------

Site Manager is logged into the Zope Management Interface (ZMI) with a user
ID having the "Add CMF Sites" permission at the desired location.

Procedure
---------

1. From the ZMI, select "CMF Site" from the add list and click
   the "Add" button. This will bring up the "Add CMF Site" Web
   form. The elements on the add form are:

  **Id** --
     the id to be used for the new CMF Site object. This id will appear in
     URLs to the site and its subobjects. The id field is a required field.

   **Title** --
     the title to be used for the new CMF Site object. The title provides a
     more human-friendly label for the site object. Providing a title is
     optional, but recommended.

   **Membership Source** --
     the source of member information to be used by the new CMF Site. The
     default for this field is "Create a new user folder in the CMF Site".
     This option will create a new User Folder in the CMF Site to be used as
     the source of member data.

     You may also select "I have an existing user folder and want to use it
     instead". In this case, the CMF Site will draw its member information
     from a User Folder that already exists in the Zope object heirarchy
     above the new CMF Site.

   **Description** --
     a short description of the site. This description may be made available
     with syndicated content and may be used by some of the default user
     interface elements of the site. Providing a description is optional, but
     recommended.

   After completing the Web form, click the "Add" button to create the new
   CMF Site object.

2. After submitting the form, the right frame of the ZMI should contain an
   administrative "welcome" page of the new CMF site. The welcome page provides
   links to:

   **The site configuration form** --
     This form allows you manage sitewide policies and configuration options.
     This should be your first stop after creating a CMF Site object.

   **The management interface** --
     The Zope management interface (ZMI) for CMF Site objects provides
     management-level access to the individual components of the site and
     provides for more advanced configuration options.

   **The site home page** --
     The default homepage of the new CMF site. This is what visitors and
     members of the site will initially see when they access the site through
     the Web.

3. Now that the basic CMF Site object has been created, you should visit the
   site configuration form to continue setting up the new site.
