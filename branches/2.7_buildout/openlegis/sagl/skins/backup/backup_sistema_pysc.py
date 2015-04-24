## Script (Python) "backup_sistema_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
nome="bkpbancosagl"

# Faz o backup e exporta o produto como 'sagl.zexp', no diretório 'var' do Zope
context.sagl.manage_exportObject()

#coloca o sagl.zexp no /tmp do zope
if hasattr(context.sagl.tmp,"sagl.zexp"):
    context.sagl.tmp.manage_delObjects(ids="sagl.zexp")
context.sagl.tmp.manage_addProduct['ExternalFile'].manage_add(id="sagl.zexp", title=" ", description=" ",
               target_filepath="./../var&dtml-portal_url;.zexp", basedir='')

context.backup_banco_pysc()
nomearq = context.empacota(nome=nome)


return response.redirect('backup_sagl?sistema=%s' % nomearq)
