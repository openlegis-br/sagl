Browser Views
=============

This sub-package provides browser views for all CMF content, generic and
control scripts and templates. Unlike PythonScripts browser views have no
restrictions on the Python modules used. As views are not checked each time
they run, they can be faster the PythonScripts. The "ursa globals" are good a
example of this.

These views are not used by the default profile.

Documentation is still missing but the most views have unit and functional
tests and should work just as well as the corresponding skin methods. The
URLs are mapped using the ActionsTool.

See TODO.txt in each folder for a detailed list of converted skin methods.

Using the Browser Views
-----------------------

In an un-customized CMFDefault site you will notice almost no difference
because the browser views are just different in implementation, not in look
and feel. But the browser view machinery lagrely bypasses the CMF skin
machinery, so you will notice that TTW customizations no longer have any
effect. A site's "main_template" can still be customized.
