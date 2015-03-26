# -*- coding: utf-8 -*-

import os
import datetime
import sqlalchemy as rdb
from sqlalchemy.orm import aliased

from five import grok
from zope.interface import Interface
from zope.component import getMultiAdapter, getUtility
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

from il.spdo.config import MessageFactory as _
from il.spdo import db
from il.spdo.config import Session, PATH_ANEXOS, SEARCH_LIMIT, NOTIFICACAO_ASSUNTO, NOTIFICACAO_MSG
from il.spdo.saconfig import ScopeID
from il.spdo.nav import url
from il.spdo.log import log, logger
from il.spdo.interfaces import (ISPDOAPI, ISecurityChecker,
                                getTipoProtocolo, getTipoDocumento, getAssunto, getSituacao,
                                getOrigem, getDestino, getArea, getTempoInativo)

class SAPLAPI(grok.GlobalUtility):
    """API SPDO.
    """
    grok.provides(ISPDOAPI)


    @log
    def addApensamento(self, id_protocolo, id_protocolo_apensado, **kwargs):
        """Apensa protocolo.
        """
        session = Session()
        protocolo = db.Protocolo(
            tipoprotocolo=tipoprotocolo,
            tipodocumento_id=tipodocumento_id,
            numero_documento=numero_documento,
            data_emissao=data_emissao,
            assunto=assunto,
            situacao_id=situacao_id,
            usuario=self.getAuthId(),
        )
        session.add(protocolo)
        session.flush()
        protocolo_id = protocolo.id
        for pessoa_id in origem:
            pessoa_origem = db.PessoaOrigem(
                protocolo_id=protocolo_id,
                pessoa_id=pessoa_id,
            )
            session.add(pessoa_origem)
        for pessoa_id in destino:
            pessoa_destino = db.PessoaDestino(
                protocolo_id=protocolo_id,
                pessoa_id=pessoa_id,
            )
            session.add(pessoa_destino)
        session.flush()
        return protocolo_id
