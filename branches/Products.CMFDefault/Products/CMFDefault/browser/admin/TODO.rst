Converting skins to views:
==========================

[x] ISiteRoot @@configure.html:
-------------------------------
- [x] reconfig_form.py -> PortalConfig
- [x] portal_config_control.py -> PortalConfig
- [x] reconfig_template.pt -> config.pt

[/, broken] ISiteRoot @@syndication.html:
-----------------------------------------
- [/, broken] SyndicationTool properties form -> syndication.Site

[/, broken] IFolderish @@syndicate.html:
----------------------------------------
- [/] synPropertiesForm.py -> syndication.Folder
- [/, broken] editSynProperties.py -> syndication.Folder
- [/] disableSyndication.py -> syndication.Folder
- [/] enableSyndication.py -> syndication.Folder
- [/, not used] synPropertiesForm_template.pt -> syndication.pt
