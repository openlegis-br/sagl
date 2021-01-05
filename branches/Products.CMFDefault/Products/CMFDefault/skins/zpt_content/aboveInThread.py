##parameters=
##title=Discussion parent breadcrumbs
##
from Products.CMFDefault.utils import decode

breadcrumbs = ''
parents = context.parentsInThread()

if parents:
    breadcrumbs = 'Above in thread: '
    for parent in parents:
        p_str = '<a href="%s">%s</a>' % (parent.absolute_url(), parent.Title())
        breadcrumbs = breadcrumbs + p_str + ':'

    breadcrumbs = breadcrumbs[:-1] + '<p>'

return decode(breadcrumbs, script)
