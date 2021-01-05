##parameters=b_start=0
##
from ZTUtils import Batch
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _
from Products.CMFDefault.utils import thousands_commas

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
ctool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ICatalogTool')
epoch = DateTime('1970/01/01 00:00:01 GMT')


options = {}

target = atool.getActionInfo('global/search')['url']
kw = context.REQUEST.form.copy()
for k, v in kw.items():
    if k in ('review_state', 'Title', 'Subject', 'Description', 'portal_type',
             'listCreators'):
        if same_type(v, []):
            v = filter(None, v)
        if not v:
            del kw[k]
    elif k in ('created',):
        if v['query'] == epoch and v['range'] == 'min':
            del kw[k]
        else:
            # work around problems with DateTime in records
            kw[k] = v.copy()
    elif k in ('go', 'go.x', 'go.y', 'b_start'):
            del kw[k]
items = ctool.searchResults(kw)
batch_obj = Batch(items, 25, b_start, orphan=1)

items = [ {'description': item.Description,
           'icon': item.getIconURL,
           'title': item.Title,
           'type': item.Type,
           'date': item.Date,
           'url': item.getURL()+'/view'}
          for item in batch_obj ]

length = batch_obj.sequence_length
summary = { 'length': length and thousands_commas(length) or '',
            'type': (length == 1) and _(u'item') or _(u'items'),
            'match': kw.get('SearchableText') }
navigation = context.getBatchNavigation(batch_obj, target, **kw)
options['batch'] = { 'summary': summary,
                     'listItemInfos': tuple(items),
                     'navigation': navigation }

return context.search_results_template(**decode(options, script))
