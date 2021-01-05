##parameters=
##
from ZTUtils import Batch
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode

ctool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ICatalogTool')

options = {}

items = ctool.searchResults(portal_type='News Item', sort_on='Date',
                            sort_order='reverse', review_state='published')
batch_obj = Batch(items, 10, 0, orphan=1)
items = [ {'title': item.Title,
           'date': item.Date,
           'url': item.getURL()}
          for item in batch_obj ]
options['listItemInfos'] = items

return context.news_box_template(**decode(options, script))
