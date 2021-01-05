##parameters=batch_obj
##
items = []
for item in batch_obj:
    item_description = item.Description()
    item_title = item.Title()
    item_type = item.getPortalTypeName()
    if item_type == 'Favorite':
        try:
            item = item.getObject()
            item_description = item_description or item.Description()
            item_title = item_title or item.Title()
            item_type = item.getPortalTypeName()
        except KeyError:
            pass
    is_file = item_type in ('File', 'Image')
    is_link = item_type == 'Link'
    items.append({'description': item_description,
                  'format': is_file and item.Format() or '',
                  'icon': item.getIconURL(),
                  'size': is_file and ('%0.1f kB' %
                                     (item.get_size() / 1024.0)) or '',
                  'title': item_title,
                  'type': item.Type(),
                  'url': is_link and item.getRemoteUrl() or
                         item.absolute_url()})
return tuple(items)
