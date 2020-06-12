# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from five import grok

from zope.interface import Interface

import simplejson as json


class DadosPMView(grok.View):
    """ sample view class """

    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('opendata-json')

    def render(self):
        portal_url = self.context.portal_url.portal_url()
        portal = self.context.portal_url.getPortalObject()
        imagens = portal.sapl_documentos.parlamentar.fotos.objectIds()
        dados = {}
        legislatures = []
        parliamentarians = []


        legislaturas = self.context.zsql.legislatura_obter_zsql()
        for legislatura in legislaturas:
            leg = {}

            sessions = []
            parlamentares = self.context.zsql.parlamentar_obter_zsql(
                num_legislatura=legislatura.num_legislatura,
                ind_titular=1
            )
            leg['description'] = ""
            leg['end_date'] = legislatura.dat_fim.strftime('%Y-%m-%d')
            leg['id'] = str(legislatura.num_legislatura)
            leg['members'] = [parlamentar.cod_parlamentar for parlamentar in parlamentares]
            periodos = self.context.zsql.periodo_comp_mesa_obter_zsql(
                num_legislatura=legislatura.num_legislatura,
                ind_excluido=0
            )
            for periodo in periodos:
                legislative_board = []
                ses = {}
                ses['description'] = ""
                ses['end_date'] = self.context.pysc.data_converter_dados_pm_pysc(periodo.dat_fim_periodo)
                ses['id'] = str(periodo.cod_periodo_comp)
                composicao = self.context.zsql.composicao_mesa_obter_zsql(
                    cod_periodo_comp=periodo.cod_periodo_comp,
                    ind_excluido=0
                )

                for item in composicao:
                    board = {}
                    parlamentar = self.context.zsql.parlamentar_obter_zsql(
                        cod_parlamentar=item.cod_parlamentar,
                        ind_excluido=0
                    )
                    if parlamentar:
                        parlamentar = parlamentar[0].cod_parlamentar
                    else:
                        parlamentar = ''
                    cargo = self.context.zsql.cargo_mesa_obter_zsql(
                        cod_cargo=item.cod_cargo,
                        ind_excluido=0
                    )[0].des_cargo
                    board['member'] = parlamentar
                    board['position'] = cargo
                    legislative_board.append(board)
                ses['legislative_board'] = legislative_board
                ses['start_date'] = self.context.pysc.data_converter_dados_pm_pysc(periodo.dat_inicio_periodo)
                ses['title'] = '%s a %s' % (periodo.dat_inicio_periodo, periodo.dat_fim_periodo)
                sessions.append(ses)
            leg['sessions'] = sessions
            legislatures.append(leg)
        parlamentares = self.context.zsql.parlamentar_obter_zsql(ind_excluido = 0)
        for parlamentar in parlamentares:
            par = {}
            par['address'] = ""
            par['birthday'] = self.context.pysc.data_converter_dados_pm_pysc(parlamentar.dat_nascimento)
            par['description'] = parlamentar.txt_biografia
            par['full_name'] = parlamentar.nom_completo
            par['id'] = str(parlamentar.cod_parlamentar)
            imagem_parlamentar = '%s_foto_parlamentar' % parlamentar.cod_parlamentar
            if '%s_foto_parlamentar' % parlamentar.cod_parlamentar in imagens:
                par['image'] = '%s/sapl_documentos/parlamentar/fotos/%s' % (portal_url, imagem_parlamentar)
            else:
                par['image'] = ""
            filiacao = self.context.zsql.filiacao_obter_zsql(ind_excluido=0, cod_parlamentar=parlamentar.cod_parlamentar)
            party_affiliation = []
            for item in filiacao:
                partido = self.context.zsql.partido_obter_zsql(ind_excluido=0, cod_partido=item.cod_partido)[0]
                fil = {}
                fil['date_affiliation'] = self.context.pysc.data_converter_dados_pm_pysc(item.dat_filiacao)
                fil['date_disaffiliation'] = self.context.pysc.data_converter_dados_pm_pysc(item.dat_desfiliacao)
                fil['party'] = partido.sgl_partido
                party_affiliation.append(fil)
            par['party_affiliation'] = party_affiliation
            par['postal_code'] = ""
            par['telephone'] = parlamentar.num_tel_parlamentar
            par['title'] = parlamentar.nom_parlamentar
            parliamentarians.append(par)

        dados['legislatures'] = legislatures
        dados['parliamentarians'] = parliamentarians
        pretty = json.dumps(dados, sort_keys=True, indent='    ')
        self.request.response.setHeader("Content-type", "application/json; charset=utf-8")
        return pretty

