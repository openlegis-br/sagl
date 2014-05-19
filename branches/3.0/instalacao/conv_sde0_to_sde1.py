#Este script deve ser executado com "zopectl run"


de_para = {}
de_para['StructuredDocument']='SDE-Document'
de_para['StrDocElement']='SDE-Document-Element'
de_para['StructuredDocumentDefinition']='SDE-Template'
de_para['StrDocAttrDef']='SDE-Template-Attribute'
de_para['StrDocElementDefinition']='SDE-Template-Element'
de_para['StrDocElemDefLink']='SDE-Template-Link'



def conv_rec(obj):
    if obj.meta_type in ['StructuredDocument','SDE-Document','StrDocElement','SDE-Document-Element','StructuredDocumentDefinition','SDE-Template','StrDocAttrDef','SDE-Template-Attribute','StrDocElementDefinition','SDE-Template-Element','StrDocElemDefLink','SDE-Template-Link']:
        tupla=obj._objects
        for x in tupla:        
            if de_para.has_key(x['meta_type']):
                x['meta_type']=de_para[x['meta_type']]
        obj._objects=tupla
        for x in obj.objectValues():
            conv_rec(x)



def converte():
    tran = get_transaction()
    print "###"
    print "###"
    print "### SAPL - INICIANDO Conversão de MODELOS de Documentos"
    print "###"
    print "###"
    mods = app.sapl_documentos.modelo
    tupla = mods._objects
    for x in tupla:        
            if de_para.has_key(x['meta_type']):
                x['meta_type']=de_para[x['meta_type']]
    mods._objects=tupla
    for x in mods.objectValues():
        print "###   - Convertendo: %s (%s) " % (x.id, x.meta_type)
        conv_rec(x)
        print "###   - Ok"
        print "###"    
    print "###"
    print "###"
    print "### SAPL - Conversão de MODELOS CONCLUÍDA"
    print "###"
    print "###"
    print "###"
    print "###"
    print "### SAPL - INICIANDO Conversão de DOCUMENTOS"
    print "###"
    print "###"
    props = app.sapl_documentos.proposicao
    tupla = props._objects
    for x in tupla:        
            if de_para.has_key(x['meta_type']):
                x['meta_type']=de_para[x['meta_type']]
    props._objects=tupla
    for x in props.objectValues():
        if x.meta_type in ['StructuredDocument','SDE-Document']:
            print "###   - Convertendo: %s (%s) " % (x.id, x.meta_type)
            conv_rec(x)
            print "###   - Ok"
            print "###"    
    print "###"
    print "###"
    print "### SAPL - Conversão de DOCUMENTOS CONCLUÍDA"
    print "###"
    print "###"
    tran.commit()    
converte()

