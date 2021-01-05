Converting skins to views:
==========================

[/] IFolderish @@view:
----------------------
- [/] index_html.py -> FolderView
- [/, depends on local_pt and news_box] index_html_template.pt -> folder.pt

- [?] folder_view.pt
- [-] index_html_categorized.pt
- [?] index_html_utils.html (macros)
- [?] TitleOrId.py

- [?] news_box.py (structure)
- [?] news_box_template.pt

[x] IFolderish folder_factories -> replaced by add views:
---------------------------------------------------------
- [-] folder_factories.py
- [-] folder_factories_template.pt
- [-] folder_add_control.py
- [-] validateId.py
- [-] validateType.py
- [x] cmf.link -> LinkAddView
- [x] cmf.favorite -> FavoriteAddView
- [x] cmf.file -> FileAddView
- [x] cmf.image -> FileAddView

[x] IFolderish @@edit:
----------------------
- [x] folder_contents.py -> ContentsView
- [x] folder_contents_template.pt -> folder_contents.pt
- [x] validateItemIds.py -> ContentsView.validate_items
- [x] validateClipboardData.py -> obsolete (show_paste checks cb_dataValid)
- [x] folder_cut_control.py -> ContentsView.handle_cut_success
- [x] folder_copy_control.py -> ContentsView.handle_copy_success
- [x] folder_paste_control.py -> ContentsView.handle_paste_success
- [x] folder_delete_control.py -> ContentsView.handle_delete_success
- [x] folder_sort_control.py -> ContentsView.handle_sort_order_success
- [x] folder_up_control.py -> ContentsView.handle_up_success
- [x] folder_down_control.py -> ContentsView.handle_down_success
- [x] folder_top_control.py -> ContentsView.handle_top_success
- [x] folder_bottom_control.py -> ContentsView.handle_bottom_success
- [-] folder_filter_form.pt (structure)
- [-] filterCookie.py
- [-] clearCookie.py

- [x] folder_rename_form.py -> ContentsView
- [x] folder_rename_control.py -> ContentsView.handle_rename_success
- [x] folder_rename_template.pt -> folder_rename.pt

[x] IFolderish @@share:
-----------------------
- [x] folder_localrole_edit.py -> FolderShareView
- [x] folder_localrole_form.pt -> folder_share.pt

[x] IMutableMinimalDublinCore @@properties:
-------------------------------------------
- [x] folder_edit_form.py -> MinimalMetadataEditView
- [x] folder_edit_template.pt -> formlib based
- [x] folder_edit_control.py -> formlib based

[x] IMutableDublinCore @@properties:
------------------------------------
- [x] metadata_edit_form.py -> MetadataEditView
- [x] metadata_edit_template.pt -> formlib based
- [x] metadata_edit_control.py -> formlib based

[x] IDocument @@view:
---------------------
- [x] document_view.py, newsitem_view.py -> DocumentView
- [x] document_view_template.pt -> document.pt

[x] IDocument @@gethtml:
------------------------
- [x] source_html.py -> SourceView
- [x] source_html_template.pt -> source.pt

[x] IMutableDocument @@edit:
----------------------------
- [x] document_edit_form.py -> DocumentEditView
- [x] document_edit_template.pt -> formlib based
- [x] validateHTML.py -> formlib based
- [x] validateTextFile.py -> formlib based
- [x] document_edit_control.py -> formlib based

[x] IMutableNewsItem @@edit:
----------------------------
- [x] newsitem_edit_form.py -> NewsItemEditView
- [x] newsitem_edit_template.pt -> formlib based
- [x] validateHTML.py -> formlib based
- [x] newsitem_edit_control.py -> formlib based

[x] ILink @@view:
-----------------
- [x] link_view.py, favorite_view.py -> LinkView
- [x] link_view_template.pt -> link.pt

[x] IMutableLink @@edit:
------------------------
- [x] link_edit_form.py -> LinkEditView
- [x] link_edit_template.pt -> formlib based
- [x] link_edit_control.py -> formlib based

[x] IMutableFavorite @@edit:
----------------------------
- [x] link_edit_form.py -> FavoriteEditView
- [x] link_edit_template.pt -> formlib based
- [x] link_edit_control.py -> formlib based

[x] IFile @@view:
-----------------
- [x] file_view.py -> FileView
- [x] file_view_template.pt -> file.pt

[x] IMutableFile @@edit:
------------------------
- [x] file_edit_form.py, image_edit_form.py -> FileEditView
- [x] file_edit_template.pt, image_edit_template.pt -> formlib based
- [x] file_edit_control.py, image_edit_control.py -> formlib based

[x] IImage @@view:
------------------
- [x] image_view.py -> ImageView
- [x] image_view_template.pt -> image.pt

[/] ISyndicatable @@rss.xml (not hooked up):
--------------------------------------------
- [x] RSS.py -> rss.View
- [x] RSS_template.pt -> rss.pt
- [-] rssDisabled.pt

[ ] other:
----------
- [ ] addtoFavorites.py

- [ ] recent_news.py (target)
- [ ] recent_news_template.pt
