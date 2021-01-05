SyndicationTool - Overview: CMF Syndication Overview
====================================================

Description
-----------

The SyndicationTool allows for sitewide syndication of content in folders (or
folder-like objects which support the synContentValues interface). Currently
on the SyndicationTool the following features are present:

1.  Enable/disable sitewide syndication.

2.  Override my Syndicaiton Element defaults on the Properties
    management form.

Once sitewide syndication has been enabled, the Syndication action on folders
is enabled, allowing syndication for a specific folder to be enabled. This is
to protect calling the RSS dtml method on folder contents one wishes to
remain non-syndicated. A 'syndication_information' object is set on the
folder which acts as the 'propertysheet' for over- riding sitewide defaults
for each particular syndication instance.

In the next revision of the SyndicationTool, the following features are
being planned:

1. Reimplementation of the manner properties are called on the
   SyndicationTool class and instance, as well as on the 'syndication-
   information' object.  A getElementProperty method will handle generic
   grabing of properties.

2. Adding the ability to addElementProperties, to allow for easily
   enabling additional XML namespaces to be incorporated on an instance
   without requiring reimplementation of the SyndicationTool.

3. Default sitewide properties for the dublin core module support.

4. Sitewide enabling/disabling override switches for the supported
   XML namespace module default values.

5. Sitewide/Folder level content filtering of content returned back
   in the itemRSS DTML method to allow for selective content returned
   for the syndication.

6. Sort Order setting.  Allow the setting of how the content is sorted
   in the syndication.

7. Add switch to disallow acquisition to disable sub-folder syndication
   within an existing syndicated folder.

8. Other features are possible as users give feedback on the
   Syndication implementation.
