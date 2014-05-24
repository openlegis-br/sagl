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
nome="bkpbancosapl"

# Faz o backup e exporta o produto como 'sapl.zexp', no diretório 'var' do Zope
context.sapl.manage_exportObject()

#coloca o sapl.zexp no /tmp do zope
if hasattr(context.sapl.tmp,"sapl.zexp"):
    context.sapl.tmp.manage_delObjects(ids="sapl.zexp")
context.sapl.tmp.manage_addProduct['ExternalFile'].manage_add(id="sapl.zexp", title=" ", description=" ",
               target_filepath="./../var&dtml-portal_url;.zexp", basedir='')

context.backup_banco_pysc()
nomearq = context.empacota(nome=nome)


return response.redirect('backup_sapl?sistema=%s' % nomearq)
