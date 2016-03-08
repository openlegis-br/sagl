## Script (Python) "breadcrumbs"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
root = ('',)
breadcrumbs = []
request = context.REQUEST
vRoot = request.has_key('VirtualRootPhysicalPath')

PARENTS = context.REQUEST.PARENTS[:-2]

foldertypes = ('Folder','CMF-Folder')

PARENTS.reverse()
if vRoot:
  root = request.VirtualRootPhysicalPath #inside if block
  PARENTS = PARENTS[len(root)-1:] #inside if block

for crumb in PARENTS:
  breadcrumbs.append(crumb)

return breadcrumbs
