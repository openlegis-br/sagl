##parameters=tree_root
##title=Standard Tree
##
from ZTUtils import SimpleTreeMaker
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.utils import decode

mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')

tm = SimpleTreeMaker('tb_tree')
def getKids(object):
    return object.talkback.getReplies()
tm.setChildAccess(function=getKids)

tree, rows = tm.cookieTree(tree_root)
rows.pop(0)

is_delete_allowed = mtool.checkPermission(ManagePortal, context)

items = []
for row in rows:
    branch = row.branch()
    item = row.object
    item_url = item.absolute_url()
    items.append({'tree_colspan': tree.height - row.depth,
                  'tree_icon': branch and branch['img'] or '',
                  'tree_id': row.id,
                  'tree_indent': row.depth - 1,
                  'tree_url': branch and branch['link'] or '',
                  'creators': item.listCreators(),
                  'date': item.CreationDate(),
                  'delete_url': is_delete_allowed and \
                                ('%s/discitem_delete' % item_url) or '',
                  'icon': item.getIconURL(),
                  'title': item.Title(),
                  'url': item_url})

return decode(tuple(items), context)
