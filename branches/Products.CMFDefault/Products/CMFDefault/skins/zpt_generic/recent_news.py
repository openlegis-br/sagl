##parameters=b_start=0
##
from Products.PythonScripts.standard import structured_text
from ZTUtils import Batch
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode

ctool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ICatalogTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()


options = {}

target = '%s/recent_news' % portal_url
items = ctool.searchResults(portal_type='News Item', sort_on='Date',
                            sort_order='reverse', review_state='published')
batch_obj = Batch(items, 10, b_start, orphan=1)

items = [ {'creators': item.listCreators,
           'date': item.Date,
           'description': structured_text(item.Description),
           'title': item.Title,
           'url': item.getURL()}
          for item in batch_obj ]

navigation = context.getBatchNavigation(batch_obj, target)
options['batch'] = {'listItemInfos': items,
                    'navigation': navigation}

return context.recent_news_template(**decode(options, script))
