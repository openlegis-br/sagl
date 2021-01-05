Converting skins to views:
==========================

[x] * @@batch_widget (macros):
------------------------------
- [x] batch_widgets.pt -> batch_widgets.pt
- [x] getBatchItemInfos.py -> BatchViewBase.listBatchItems
- [x] getBatchNavigation.py -> BatchViewBase.navigation_previous
                               BatchViewBase.navigation_next

[x] deprecated: * @@form_widget (macros) / new: * @@formlib_macros (macros):
----------------------------------------------------------------------------
- [x] form_widgets.pt -> form_widgets.pt
- [x] new: formlib_macros.pt

[/] * @@content_macros (macros):
--------------------------------
- [x] getBaseTag.pt (structure) -> content_macros.pt
- [x] content_byline.pt (macros) -> content_macros.pt
- [x] viewThreadsAtBottom.pt (structure) -> content_macros.pt
