request=context.REQUEST

#mport pdb; pdb.set_trace()
if request.ACTUAL_URL == context.portal_url() or request.ACTUAL_URL == context.portal_url()+'/' or request.ACTUAL_URL == context.portal_url()+'/index_html':
    redirect_url=context.portal_url()+'/default_index_html'
else:
    #redirect_url=context.portal_url()+'/'+context.id+'/'+context.id+'_index_html'
    redirect_url=request['URL1']+'/'+context.id+'_index_html'
if request.has_key('QUERY_STRING') and request['QUERY_STRING'] != '':
    redirect_url+='?%s'%request['QUERY_STRING']
request.RESPONSE.redirect(redirect_url)
