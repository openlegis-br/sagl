##parameters=b_start=0
##
from ZTUtils import Batch
from ZTUtils import LazyFilter
from Products.CMFDefault.utils import decode

options = {}

options['has_local'] = 'local_pt' in context.objectIds()

key, reverse = context.getDefaultSorting()
items = context.contentValues()
items = sequence.sort( items, ((key, 'cmp', reverse and 'desc' or 'asc'),) )
items = LazyFilter(items, skip='View')
batch_obj = Batch(items, 25, b_start, orphan=0)
listItemInfos = context.getBatchItemInfos(batch_obj)
target = context.getActionInfo('object/view')['url']
navigation = context.getBatchNavigation(batch_obj, target)
options['batch'] = { 'listItemInfos': listItemInfos,
                     'navigation': navigation }

return context.index_html_template(**decode(options, script))
