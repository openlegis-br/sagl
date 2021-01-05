Use Case Configuring a CMF site
===============================

Actor
-----

Site Manager

Overview
--------

The "site configuration form" of a CMF Site object provides a simple
way to set and change the sitewide configuration options and policies
for a CMF site. Theses options include some of the information that was
provided when the CMF Site was created (such as site title and
description), as well as other options that were given defaults when
the CMF site was created.

Assumptions
-----------

Site Manager has logged into the CMF site using a user ID with the "Change
configuration" permission (see :doc:`LoginAsMember`).

Procedure
---------

1. Site Managers see a "Reconfigure site" link in the actions box.

Click the "Reconfigure site" link to bring up the site configuration form.

The configuration options available from the site configuration form are:

**Site 'From' Name** --
  The name to be used as the (apparent) sender when the site generates email.
  The site may generate email to provide information to new members, or to
  notify members of various events. The default value for this name is 'Site
  Administrator'. A value for this field is required in order to send mail
  from the site.

**Site 'From' Address** --
  The email address used as the (apparent) return address when the site
  generates email. The default value for the from address is
  'postmaster@localhost'. A value for this field is required in order to
  send mail from the site.

**SMTP Server** --
  The address of the SMTP (outgoing mail) server to be used when the site
  generates email. The default value for the SMTP server address is
  'localhost', which presumes that you have an SMTP server running on the
  same machine as the Zope software. A valid SMTP server address is required
  in order to send mail from the site.

**Site Title** --
  The title of the site that appears at the top of all site pages (when using
  the default site skins). Providing a title is optional, but recommended.

**Site Description** --
  A short description of the site. This description may be made available
  with syndicated content and may be used by some of the default user
  interface elements of the site. Providing a description is optional, but
  recommended.

**Password Policy** --
  The password policy configuration option allows you to choose the way that
  the site handles passwords when members register with the site.

  If you select "Generate an email member's initial password" the site will
  randomly generate an initial password that members must use to log into the
  site and email that password to the address provided by the member. This
  option may be preferred if you want to verify a prospective member's email
  address before granting membership to the site.

  If you select "Allow members to select their initial password" (the
  default), the site will allow new members to enter their own password at
  registration time.

After making changes to the site configuration options,
click the "Change" button to save the changes.
