SET FOREIGN_KEY_CHECKS=0;

ALTER TABLE `acomp_materia`
  ADD CONSTRAINT `acomp_materia_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE RESTRICT;

ALTER TABLE `afastamento`
  ADD CONSTRAINT `afastamento_ibfk_1` FOREIGN KEY (`cod_mandato`) REFERENCES `mandato` (`cod_mandato`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `afastamento_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE,
  ADD CONSTRAINT `afastamento_ibfk_4` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `afastamento_ibfk_5` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `anexada`
  ADD CONSTRAINT `anexada_ibfk_1` FOREIGN KEY (`cod_materia_anexada`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `anexada_ibfk_2` FOREIGN KEY (`cod_materia_principal`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE;

ALTER TABLE `anexo_norma`
  ADD CONSTRAINT `anexo_norma_ibfk_1` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON DELETE CASCADE;

ALTER TABLE `assessor_parlamentar`
  ADD CONSTRAINT `assessor_parlamentar_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE,
  ADD CONSTRAINT `assessor_parlamentar_ibfk_2` FOREIGN KEY (`col_username`) REFERENCES `usuario` (`col_username`) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE `assinatura_documento`
  ADD CONSTRAINT `assinatura_documento_ibfk_1` FOREIGN KEY (`cod_usuario`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT;

ALTER TABLE `autor`
  ADD CONSTRAINT `autor_ibfk_1` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autor_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autor_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autor_ibfk_4` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autor_ibfk_5` FOREIGN KEY (`tip_autor`) REFERENCES `tipo_autor` (`tip_autor`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autor_ibfk_6` FOREIGN KEY (`col_username`) REFERENCES `usuario` (`col_username`) ON DELETE RESTRICT;

ALTER TABLE `autoria`
  ADD CONSTRAINT `autoria_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `autoria_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `autoria_emenda`
  ADD CONSTRAINT `autoria_emenda_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autoria_emenda_ibfk_2` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON DELETE CASCADE;

ALTER TABLE `autoria_substitutivo`
  ADD CONSTRAINT `autoria_substitutivo_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE RESTRICT,
  ADD CONSTRAINT `autoria_substitutivo_ibfk_2` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON DELETE CASCADE;

ALTER TABLE `bancada`
  ADD CONSTRAINT `bancada_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT,
  ADD CONSTRAINT `bancada_ibfk_2` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `casa_legislativa`
  ADD CONSTRAINT `casa_legislativa_ibfk_1` FOREIGN KEY (`cod_localidade`) REFERENCES `localidade` (`cod_localidade`) ON DELETE RESTRICT;

ALTER TABLE `categoria_instituicao`
  ADD CONSTRAINT `idx_tip_instituicao` FOREIGN KEY (`tip_instituicao`) REFERENCES `tipo_instituicao` (`tip_instituicao`) ON DELETE CASCADE;

ALTER TABLE `coligacao`
  ADD CONSTRAINT `coligacao_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `comissao`
  ADD CONSTRAINT `comissao_ibfk_1` FOREIGN KEY (`tip_comissao`) REFERENCES `tipo_comissao` (`tip_comissao`) ON DELETE RESTRICT;

ALTER TABLE `composicao_bancada`
  ADD CONSTRAINT `composicao_bancada_ibfk_1` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_bancada_ibfk_2` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_bancada` (`cod_cargo`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_bancada_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_bancada` (`cod_periodo_comp`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_bancada_ibfk_4` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `composicao_coligacao`
  ADD CONSTRAINT `composicao_coligacao_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT;

ALTER TABLE `composicao_comissao`
  ADD CONSTRAINT `composicao_comissao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`),
  ADD CONSTRAINT `composicao_comissao_ibfk_2` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_comissao` (`cod_cargo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `composicao_comissao_ibfk_3` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `composicao_comissao_ibfk_4` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_comissao` (`cod_periodo_comp`) ON DELETE RESTRICT;

ALTER TABLE `composicao_executivo`
  ADD CONSTRAINT `composicao_executivo_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_executivo_ibfk_2` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `composicao_mesa`
  ADD CONSTRAINT `composicao_mesa_ibfk_1` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_mesa` (`cod_cargo`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_mesa_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_mesa_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_mesa` (`cod_periodo_comp`) ON DELETE RESTRICT,
  ADD CONSTRAINT `composicao_mesa_ibfk_4` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON DELETE RESTRICT;

ALTER TABLE `dependente`
  ADD CONSTRAINT `dependente_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `dependente_ibfk_2` FOREIGN KEY (`tip_dependente`) REFERENCES `tipo_dependente` (`tip_dependente`) ON DELETE RESTRICT;

ALTER TABLE `despacho_inicial`
  ADD CONSTRAINT `despacho_inicial_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `despacho_inicial_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE;

ALTER TABLE `documento_acessorio`
  ADD CONSTRAINT `documento_acessorio_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `documento_acessorio_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento` (`tip_documento`) ON DELETE RESTRICT;

ALTER TABLE `documento_acessorio_administrativo`
  ADD CONSTRAINT `documento_acessorio_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE CASCADE,
  ADD CONSTRAINT `documento_acessorio_administrativo_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON DELETE RESTRICT;

ALTER TABLE `documento_administrativo`
  ADD CONSTRAINT `documento_administrativo_ibfk_1` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON DELETE RESTRICT;

ALTER TABLE `documento_administrativo_materia`
  ADD CONSTRAINT `documento_administrativo_materia_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE CASCADE,
  ADD CONSTRAINT `documento_administrativo_materia_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE;

ALTER TABLE `documento_administrativo_vinculado`
  ADD CONSTRAINT `documento_administrativo_vinculado_ibfk_1` FOREIGN KEY (`cod_documento_vinculado`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE CASCADE,
  ADD CONSTRAINT `documento_administrativo_vinculado_ibfk_2` FOREIGN KEY (`cod_documento_vinculante`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE CASCADE;

ALTER TABLE `documento_comissao`
  ADD CONSTRAINT `documento_comissao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT;

ALTER TABLE `emenda`
  ADD CONSTRAINT `emenda_ibfk_1` FOREIGN KEY (`tip_emenda`) REFERENCES `tipo_emenda` (`tip_emenda`) ON DELETE RESTRICT,
  ADD CONSTRAINT `emenda_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE;

ALTER TABLE `encerramento_presenca`
  ADD CONSTRAINT `encerramento_presenca_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `encerramento_presenca_ibfk_2` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE;

ALTER TABLE `expediente_discussao`
  ADD CONSTRAINT `expediente_discussao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `fk_cod_ordem` FOREIGN KEY (`cod_ordem`) REFERENCES `expediente_materia` (`cod_ordem`) ON DELETE CASCADE;

ALTER TABLE `expediente_materia`
  ADD CONSTRAINT `expediente_materia_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE RESTRICT,
  ADD CONSTRAINT `expediente_materia_ibfk_2` FOREIGN KEY (`cod_parecer`) REFERENCES `parecer` (`cod_relatoria`) ON DELETE RESTRICT,
  ADD CONSTRAINT `expediente_materia_ibfk_3` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE,
  ADD CONSTRAINT `expediente_materia_ibfk_4` FOREIGN KEY (`tip_quorum`) REFERENCES `quorum_votacao` (`cod_quorum`) ON DELETE RESTRICT,
  ADD CONSTRAINT `expediente_materia_ibfk_5` FOREIGN KEY (`tip_votacao`) REFERENCES `tipo_votacao` (`tip_votacao`) ON DELETE RESTRICT;

ALTER TABLE `expediente_presenca`
  ADD CONSTRAINT `expediente_presenca_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `expediente_presenca_ibfk_2` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE;

ALTER TABLE `expediente_sessao_plenaria`
  ADD CONSTRAINT `expediente_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE;

ALTER TABLE `filiacao`
  ADD CONSTRAINT `filiacao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `filiacao_ibfk_2` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT;

ALTER TABLE `funcionario`
  ADD CONSTRAINT `funcionario_ibfk_1` FOREIGN KEY (`cod_usuario`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT;

ALTER TABLE `gabinete_atendimento`
  ADD CONSTRAINT `gabinete_atendimento_ibfk_1` FOREIGN KEY (`cod_eleitor`) REFERENCES `gabinete_eleitor` (`cod_eleitor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `gabinete_atendimento_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `gabinete_eleitor`
  ADD CONSTRAINT `gabinete_eleitor_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `instituicao`
  ADD CONSTRAINT `instituicao_ibfk_1` FOREIGN KEY (`cod_categoria`) REFERENCES `categoria_instituicao` (`cod_categoria`) ON DELETE RESTRICT,
  ADD CONSTRAINT `instituicao_ibfk_2` FOREIGN KEY (`tip_instituicao`) REFERENCES `tipo_instituicao` (`tip_instituicao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `instituicao_ibfk_3` FOREIGN KEY (`cod_localidade`) REFERENCES `localidade` (`cod_localidade`) ON DELETE RESTRICT;

ALTER TABLE `legislacao_citada`
  ADD CONSTRAINT `legislacao_citada_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `legislacao_citada_ibfk_2` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON DELETE CASCADE;

ALTER TABLE `liderancas_partidarias`
  ADD CONSTRAINT `liderancas_partidarias_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `liderancas_partidarias_ibfk_2` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON DELETE RESTRICT,
  ADD CONSTRAINT `liderancas_partidarias_ibfk_3` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE RESTRICT;

ALTER TABLE `logradouro`
  ADD CONSTRAINT `logradouro_ibfk_1` FOREIGN KEY (`cod_localidade`) REFERENCES `localidade` (`cod_localidade`) ON DELETE RESTRICT,
  ADD CONSTRAINT `logradouro_ibfk_2` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON DELETE CASCADE;

ALTER TABLE `mandato`
  ADD CONSTRAINT `mandato_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE,
  ADD CONSTRAINT `mandato_ibfk_2` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT,
  ADD CONSTRAINT `mandato_ibfk_3` FOREIGN KEY (`cod_coligacao`) REFERENCES `coligacao` (`cod_coligacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `mandato_ibfk_4` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON DELETE RESTRICT;

ALTER TABLE `materia_apresentada_sessao`
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_2` FOREIGN KEY (`cod_doc_acessorio`) REFERENCES `documento_acessorio` (`cod_documento`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_3` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_4` FOREIGN KEY (`cod_parecer`) REFERENCES `parecer` (`cod_relatoria`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_5` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_6` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_7` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON DELETE RESTRICT;

ALTER TABLE `materia_legislativa`
  ADD CONSTRAINT `materia_legislativa_ibfk_2` FOREIGN KEY (`cod_local_origem_externa`) REFERENCES `origem` (`cod_origem`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_legislativa_ibfk_3` FOREIGN KEY (`tip_quorum`) REFERENCES `quorum_votacao` (`cod_quorum`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_legislativa_ibfk_4` FOREIGN KEY (`cod_regime_tramitacao`) REFERENCES `regime_tramitacao` (`cod_regime_tramitacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `materia_legislativa_ibfk_5` FOREIGN KEY (`tip_id_basica`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON DELETE RESTRICT;

ALTER TABLE `mesa_sessao_plenaria`
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_mesa` (`cod_cargo`) ON DELETE RESTRICT,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_3` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_4` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE RESTRICT;

ALTER TABLE `norma_juridica`
  ADD CONSTRAINT `norma_juridica_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE SET NULL,
  ADD CONSTRAINT `norma_juridica_ibfk_2` FOREIGN KEY (`cod_situacao`) REFERENCES `tipo_situacao_norma` (`tip_situacao_norma`) ON DELETE SET NULL ON UPDATE RESTRICT,
  ADD CONSTRAINT `norma_juridica_ibfk_3` FOREIGN KEY (`tip_norma`) REFERENCES `tipo_norma_juridica` (`tip_norma`) ON DELETE RESTRICT;

ALTER TABLE `numeracao`
  ADD CONSTRAINT `numeracao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `numeracao_ibfk_2` FOREIGN KEY (`tip_materia`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON DELETE CASCADE;

ALTER TABLE `oradores`
  ADD CONSTRAINT `oradores_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE,
  ADD CONSTRAINT `oradores_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `oradores_expediente`
  ADD CONSTRAINT `oradores_expediente_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE,
  ADD CONSTRAINT `oradores_expediente_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `ordem_dia`
  ADD CONSTRAINT `ordem_dia_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE RESTRICT,
  ADD CONSTRAINT `ordem_dia_ibfk_2` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE,
  ADD CONSTRAINT `ordem_dia_ibfk_3` FOREIGN KEY (`tip_quorum`) REFERENCES `quorum_votacao` (`cod_quorum`) ON DELETE RESTRICT,
  ADD CONSTRAINT `ordem_dia_ibfk_4` FOREIGN KEY (`tip_votacao`) REFERENCES `tipo_votacao` (`tip_votacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `ordem_dia_ibfk_5` FOREIGN KEY (`tip_turno`) REFERENCES `turno_discussao` (`cod_turno`) ON DELETE RESTRICT;

ALTER TABLE `ordem_dia_discussao`
  ADD CONSTRAINT `ordem_dia_discussao_ibfk_1` FOREIGN KEY (`cod_ordem`) REFERENCES `ordem_dia` (`cod_ordem`) ON DELETE CASCADE,
  ADD CONSTRAINT `ordem_dia_discussao_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `ordem_dia_presenca`
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE,
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `parecer`
  ADD CONSTRAINT `parecer_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `parecer_ibfk_2` FOREIGN KEY (`cod_relatoria`) REFERENCES `relatoria` (`cod_relatoria`) ON DELETE CASCADE;

ALTER TABLE `parlamentar`
  ADD CONSTRAINT `parlamentar_ibfk_1` FOREIGN KEY (`cod_localidade_resid`) REFERENCES `localidade` (`cod_localidade`) ON DELETE RESTRICT,
  ADD CONSTRAINT `parlamentar_ibfk_2` FOREIGN KEY (`cod_nivel_instrucao`) REFERENCES `nivel_instrucao` (`cod_nivel_instrucao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `parlamentar_ibfk_3` FOREIGN KEY (`tip_situacao_militar`) REFERENCES `tipo_situacao_militar` (`tip_situacao_militar`) ON DELETE RESTRICT;

ALTER TABLE `periodo_comp_bancada`
  ADD CONSTRAINT `periodo_comp_bancada_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `proposicao`
  ADD CONSTRAINT `proposicao_ibfk_1` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON DELETE SET NULL,
  ADD CONSTRAINT `proposicao_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE RESTRICT,
  ADD CONSTRAINT `proposicao_ibfk_3` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE SET NULL,
  ADD CONSTRAINT `proposicao_ibfk_4` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON DELETE SET NULL,
  ADD CONSTRAINT `proposicao_ibfk_5` FOREIGN KEY (`tip_proposicao`) REFERENCES `tipo_proposicao` (`tip_proposicao`) ON DELETE RESTRICT;

ALTER TABLE `protocolo`
  ADD CONSTRAINT `protocolo_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE RESTRICT,
  ADD CONSTRAINT `protocolo_ibfk_2` FOREIGN KEY (`cod_materia_principal`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE SET NULL;

ALTER TABLE `registro_votacao`
  ADD CONSTRAINT `registro_votacao_ibfk_1` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON DELETE RESTRICT,
  ADD CONSTRAINT `registro_votacao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE RESTRICT,
  ADD CONSTRAINT `registro_votacao_ibfk_3` FOREIGN KEY (`cod_parecer`) REFERENCES `parecer` (`cod_relatoria`) ON DELETE RESTRICT,
  ADD CONSTRAINT `registro_votacao_ibfk_4` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON DELETE RESTRICT,
  ADD CONSTRAINT `registro_votacao_ibfk_5` FOREIGN KEY (`tip_resultado_votacao`) REFERENCES `tipo_resultado_votacao` (`tip_resultado_votacao`) ON DELETE RESTRICT;

ALTER TABLE `registro_votacao_parlamentar`
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_2` FOREIGN KEY (`cod_votacao`) REFERENCES `registro_votacao` (`cod_votacao`) ON DELETE CASCADE;

ALTER TABLE `relatoria`
  ADD CONSTRAINT `relatoria_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `relatoria_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `relatoria_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `relatoria_ibfk_4` FOREIGN KEY (`tip_fim_relatoria`) REFERENCES `tipo_fim_relatoria` (`tip_fim_relatoria`) ON DELETE RESTRICT;

ALTER TABLE `reuniao_comissao`
  ADD CONSTRAINT `reuniao_comissao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT;

ALTER TABLE `sessao_legislativa`
  ADD CONSTRAINT `sessao_legislativa_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `sessao_plenaria`
  ADD CONSTRAINT `sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON DELETE RESTRICT,
  ADD CONSTRAINT `sessao_plenaria_ibfk_2` FOREIGN KEY (`tip_sessao`) REFERENCES `tipo_sessao_plenaria` (`tip_sessao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `sessao_plenaria_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON DELETE RESTRICT;

ALTER TABLE `sessao_plenaria_presenca`
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT,
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_2` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON DELETE CASCADE;

ALTER TABLE `substitutivo`
  ADD CONSTRAINT `substitutivo_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE;

ALTER TABLE `tramitacao`
  ADD CONSTRAINT `tramitacao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE,
  ADD CONSTRAINT `tramitacao_ibfk_2` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao` (`cod_status`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_ibfk_3` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_ibfk_4` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_ibfk_5` FOREIGN KEY (`cod_usuario_local`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_ibfk_6` FOREIGN KEY (`cod_usuario_dest`) REFERENCES `usuario` (`cod_usuario`) ON DELETE SET NULL;

ALTER TABLE `tramitacao_administrativo`
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE CASCADE,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_2` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao_administrativo` (`cod_status`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_3` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_4` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_5` FOREIGN KEY (`cod_usuario_local`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_6` FOREIGN KEY (`cod_usuario_dest`) REFERENCES `usuario` (`cod_usuario`) ON DELETE SET NULL;

ALTER TABLE `unidade_tramitacao`
  ADD CONSTRAINT `unidade_tramitacao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_2` FOREIGN KEY (`cod_orgao`) REFERENCES `orgao` (`cod_orgao`) ON DELETE RESTRICT,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE RESTRICT;

ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`cod_localidade_resid`) REFERENCES `localidade` (`cod_localidade`) ON DELETE RESTRICT;

ALTER TABLE `usuario_unid_tram`
  ADD CONSTRAINT `usuario_unid_tram_ibfk_1` FOREIGN KEY (`cod_unid_tramitacao`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE CASCADE,
  ADD CONSTRAINT `usuario_unid_tram_ibfk_2` FOREIGN KEY (`cod_usuario`) REFERENCES `usuario` (`cod_usuario`) ON DELETE CASCADE;

ALTER TABLE `vinculo_norma_juridica`
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_1` FOREIGN KEY (`cod_norma_referente`) REFERENCES `norma_juridica` (`cod_norma`) ON DELETE CASCADE,
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_2` FOREIGN KEY (`cod_norma_referida`) REFERENCES `norma_juridica` (`cod_norma`) ON DELETE CASCADE;

ALTER TABLE `visita`
  ADD CONSTRAINT `visita_ibfk_1` FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_funcionario`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `visita_ibfk_2` FOREIGN KEY (`cod_pessoa`) REFERENCES `pessoa` (`cod_pessoa`) ON DELETE CASCADE;
  
SET FOREIGN_KEY_CHECKS=1;
