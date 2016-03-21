DROP TABLE IF EXISTS andamento_sessao;
DROP TABLE IF EXISTS partido_old;

ALTER TABLE acomp_materia ENGINE=INNODB;
ALTER TABLE afastamento ENGINE=INNODB;
ALTER TABLE anexada ENGINE=INNODB;
ALTER TABLE assunto_norma ENGINE=INNODB;
ALTER TABLE autor ENGINE=INNODB;
ALTER TABLE autoria ENGINE=INNODB;
ALTER TABLE bancada ENGINE=INNODB;
ALTER TABLE cargo_bancada ENGINE=INNODB;
ALTER TABLE cargo_comissao ENGINE=INNODB;
ALTER TABLE cargo_mesa ENGINE=INNODB;
ALTER TABLE coligacao ENGINE=INNODB;
ALTER TABLE comissao ENGINE=INNODB;
ALTER TABLE composicao_bancada ENGINE=INNODB;
ALTER TABLE composicao_coligacao ENGINE=INNODB;
ALTER TABLE composicao_comissao ENGINE=INNODB;
ALTER TABLE composicao_mesa ENGINE=INNODB;
ALTER TABLE dependente ENGINE=INNODB;
ALTER TABLE despacho_inicial ENGINE=INNODB;
ALTER TABLE documento_acessorio ENGINE=INNODB;
ALTER TABLE documento_acessorio_administrativo ENGINE=INNODB;
ALTER TABLE documento_administrativo ENGINE=INNODB;
ALTER TABLE emenda ENGINE=INNODB;
ALTER TABLE encerramento_presenca ENGINE=INNODB;
ALTER TABLE expediente_materia ENGINE=INNODB;
ALTER TABLE expediente_presenca ENGINE=INNODB;
ALTER TABLE expediente_sessao_plenaria ENGINE=INNODB;
ALTER TABLE filiacao ENGINE=INNODB;
ALTER TABLE instituicao ENGINE=INNODB;
ALTER TABLE legislacao_citada ENGINE=INNODB;
ALTER TABLE legislatura ENGINE=INNODB;
ALTER TABLE lexml_registro_provedor ENGINE=INNODB;
ALTER TABLE lexml_registro_publicador ENGINE=INNODB;
ALTER TABLE localidade ENGINE=INNODB;
ALTER TABLE mandato ENGINE=INNODB;
ALTER TABLE materia_apresentada_sessao ENGINE=INNODB;
ALTER TABLE materia_legislativa ENGINE=INNODB;
ALTER TABLE mesa_sessao_plenaria ENGINE=INNODB;
ALTER TABLE nivel_instrucao ENGINE=INNODB;
ALTER TABLE norma_juridica ENGINE=INNODB;
ALTER TABLE numeracao ENGINE=INNODB;
ALTER TABLE oradores ENGINE=INNODB;
ALTER TABLE oradores_expediente ENGINE=INNODB;
ALTER TABLE ordem_dia ENGINE=INNODB;
ALTER TABLE ordem_dia_presenca ENGINE=INNODB;
ALTER TABLE orgao ENGINE=INNODB;
ALTER TABLE origem ENGINE=INNODB;
ALTER TABLE parecer ENGINE=INNODB;
ALTER TABLE parlamentar ENGINE=INNODB;
ALTER TABLE partido ENGINE=INNODB;
ALTER TABLE periodo_comp_comissao ENGINE=INNODB;
ALTER TABLE periodo_comp_mesa ENGINE=INNODB;
ALTER TABLE proposicao ENGINE=INNODB;
ALTER TABLE protocolo ENGINE=INNODB;
ALTER TABLE regime_tramitacao ENGINE=INNODB;
ALTER TABLE registro_votacao ENGINE=INNODB;
ALTER TABLE registro_votacao_parlamentar ENGINE=INNODB;
ALTER TABLE relatoria ENGINE=INNODB;
ALTER TABLE reuniao_comissao ENGINE=INNODB;
ALTER TABLE sessao_legislativa ENGINE=INNODB;
ALTER TABLE sessao_plenaria ENGINE=INNODB;
ALTER TABLE sessao_plenaria_presenca ENGINE=INNODB;
ALTER TABLE status_tramitacao ENGINE=INNODB;
ALTER TABLE status_tramitacao_administrativo ENGINE=INNODB;
ALTER TABLE subemenda ENGINE=INNODB;
ALTER TABLE substitutivo ENGINE=INNODB;
ALTER TABLE tipo_afastamento ENGINE=INNODB;
ALTER TABLE tipo_autor ENGINE=INNODB;
ALTER TABLE tipo_comissao ENGINE=INNODB;
ALTER TABLE tipo_dependente ENGINE=INNODB;
ALTER TABLE tipo_documento ENGINE=INNODB;
ALTER TABLE tipo_documento_administrativo ENGINE=INNODB;
ALTER TABLE tipo_expediente ENGINE=INNODB;
ALTER TABLE tipo_fim_relatoria ENGINE=INNODB;
ALTER TABLE tipo_instituicao ENGINE=INNODB;
ALTER TABLE tipo_materia_legislativa ENGINE=INNODB;
ALTER TABLE tipo_norma_juridica ENGINE=INNODB;
ALTER TABLE tipo_proposicao ENGINE=INNODB;
ALTER TABLE tipo_resultado_votacao ENGINE=INNODB;
ALTER TABLE tipo_sessao_plenaria ENGINE=INNODB;
ALTER TABLE tipo_situacao_materia ENGINE=INNODB;
ALTER TABLE tipo_situacao_militar ENGINE=INNODB;
ALTER TABLE tipo_situacao_norma ENGINE=INNODB;
ALTER TABLE tramitacao ENGINE=INNODB;
ALTER TABLE tramitacao_administrativo ENGINE=INNODB;
ALTER TABLE unidade_tramitacao ENGINE=INNODB;
ALTER TABLE vinculo_norma_juridica ENGINE=INNODB;

CREATE TABLE `arquivo_armario` (
  `cod_armario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_armario` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_corredor` (
  `cod_corredor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_unidade` int(11) NOT NULL,
  `nom_corredor` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_item` (
  `cod_item` int(11) NOT NULL AUTO_INCREMENT,
  `cod_recipiente` int(11) NOT NULL,
  `tip_suporte` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_norma` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `cod_protocolo` int(7) unsigned zerofill DEFAULT NULL,
  `des_item` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_arquivamento` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_item`),
  KEY `cod_recipiente` (`cod_recipiente`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_norma` (`cod_norma`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_protocolo` (`cod_protocolo`),
  KEY `tip_suporte` (`tip_suporte`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_prateleira` (
  `cod_prateleira` int(11) NOT NULL AUTO_INCREMENT,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_prateleira` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_prateleira`),
  KEY `cod_armario` (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_recipiente` (
  `cod_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `tip_recipiente` int(11) NOT NULL,
  `num_recipiente` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `tip_tit_documental` int(11) NOT NULL,
  `ano_recipiente` smallint(6) NOT NULL,
  `dat_recipiente` date NOT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_prateleira` int(11) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_recipiente`),
  UNIQUE KEY `num_tipo_recipiente` (`num_recipiente`,`tip_recipiente`,`ano_recipiente`,`ind_excluido`),
  KEY `tip_recipiente` (`tip_recipiente`),
  KEY `tip_tit_documental` (`tip_tit_documental`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_tipo_recipiente` (
  `tip_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_recipiente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_recipiente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `arquivo_tipo_recipiente` (`tip_recipiente`, `des_tipo_recipiente`, `ind_excluido`) VALUES
(1, 'Caixa Arquivo', 0),
(2, 'Pasta Suspensa', 0),
(3, 'Pasta A-Z', 0);

CREATE TABLE `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_suporte`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `arquivo_tipo_suporte` (`tip_suporte`, `des_tipo_suporte`, `ind_excluido`) VALUES
(1, 'Papel', 0),
(2, 'Fita Magnética', 0),
(3, 'CD / DVD', 0);

CREATE TABLE `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_tit_documental`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `arquivo_tipo_tit_documental` (`tip_tit_documental`, `sgl_tip_tit_documental`, `des_tipo_tit_documental`, `ind_excluido`) VALUES
(1, 'PL', 'LEI', 0),
(2, 'DL', 'DECRETO LEGISLATIVO', 0),
(3, 'A', 'PROCESSOS ARQUIVADOS', 0),
(4, 'RES', 'RESOLUÇÃO', 0),
(5, 'DIV', 'DIVERSOS', 0),
(6, 'AM', 'ATO DA MESA', 0),
(7, 'EM', 'EMENDA LOM', 0),
(8, 'SEP', 'CEI', 0);

CREATE TABLE `arquivo_unidade` (
  `cod_unidade` int(11) NOT NULL AUTO_INCREMENT,
  `tip_extensao_atuacao` int(11) NOT NULL,
  `tip_estagio_evolucao` int(11) NOT NULL,
  `nom_unidade` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `txt_localizacao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS `assessor_parlamentar` (
  `cod_assessor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_assessor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_celular` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nomeacao` date NOT NULL,
  `dat_exoneracao` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `col_username` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_assessor`),
  UNIQUE KEY `assessor_parlamentar` (`cod_assessor`,`cod_parlamentar`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `destinatario_oficio` (
  `cod_destinatario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_instituicao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_destinatario`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_instituicao` (`cod_instituicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

INSERT INTO `tipo_emenda` (`tip_emenda`, `des_tipo_emenda`, `ind_excluido`) VALUES
(1, 'Aditiva', 0),
(2, 'Modificativa', 0),
(3, 'Substitutiva', 0),
(4, 'Supressiva', 0),
(5, 'Mensagem Aditiva', 0);

UPDATE emenda SET tip_emenda = 1 WHERE tip_emenda="Aditiva";

UPDATE emenda SET tip_emenda = 2 WHERE tip_emenda="Modificativa";

UPDATE emenda SET tip_emenda = 3 WHERE tip_emenda="Substitutiva";

UPDATE emenda SET tip_emenda = 4 WHERE tip_emenda="Supressiva";

UPDATE emenda SET tip_emenda = 5 WHERE tip_emenda="Mens. Aditiva";

UPDATE emenda SET tip_emenda = 6 WHERE tip_emenda="De Redação";

UPDATE emenda SET tip_emenda = 7 WHERE tip_emenda="Subemenda";

ALTER TABLE `emenda` ADD `exc_pauta` tinyint(4) DEFAULT NULL AFTER `cod_autor`;

ALTER TABLE `emenda`
   CHANGE `tip_emenda` `tip_emenda` INT(11) NOT NULL, 
   ADD UNIQUE KEY `idx_emen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
   ADD KEY `idx_tip_emenda` (`tip_emenda`);

ALTER TABLE `subemenda` 
   CHANGE `tip_subemenda` `tip_subemenda` INT(11) NOT NULL,
   ADD UNIQUE KEY `idx_sub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
   ADD KEY `idx_tip_subemenda` (`tip_subemenda`);

CREATE TABLE IF NOT EXISTS `quorum_votacao` (
  `cod_quorum` int(11) NOT NULL AUTO_INCREMENT,
  `des_quorum` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `txt_formula` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_quorum`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `quorum_votacao` (`cod_quorum`, `des_quorum`, `txt_formula`, `ind_excluido`) VALUES
(1, 'Maioria simples', '(NP/2)+1', 0),
(2, 'Maioria absoluta', '(NT/2)+1', 0),
(3, 'Maioria qualificada - 1/3', '(NT/3)+1', 0),
(4, 'Maioria qualificada - 2/3', '{(NT/3)x2}+1', 0),
(5, 'Maioria qualificada - 3/5', '{(NT/5)x3}+1', 0);

ALTER TABLE `materia_legislativa` ADD `tip_quorum` INT(11) NULL AFTER `txt_observacao`;

UPDATE ordem_dia SET tip_quorum =1 WHERE tip_quorum IS NULL;

ALTER TABLE `materia_legislativa` ADD INDEX (`tip_quorum`);

ALTER TABLE `ordem_dia` ADD INDEX (`tip_quorum`);

ALTER TABLE `expediente_materia` ADD `tip_quorum` INT(11) NULL AFTER `txt_resultado`;

ALTER TABLE `expediente_materia` ADD INDEX (`tip_quorum`);

CREATE TABLE IF NOT EXISTS `turno_discussao` (
  `cod_turno` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_turno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_turno`),
  UNIQUE KEY `idx_unique_key` (`cod_turno`,`sgl_turno`,`ind_excluido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `turno_discussao` (`cod_turno`, `sgl_turno`, `des_turno`, `ind_excluido`) VALUES
(1, 'P', '1ª Discussão', 0),
(2, 'S', '2ª Discussão', 0),
(3, 'U', 'Único', 0),
(4, 'R', 'Redação Final', 0);

ALTER TABLE `ordem_dia` ADD `tip_turno` INT(11) NULL AFTER `txt_resultado`;

UPDATE ordem_dia SET tip_turno=1 WHERE tip_turno IS NULL;

ALTER TABLE `ordem_dia` ADD INDEX (`tip_turno`);

CREATE TABLE IF NOT EXISTS `tipo_votacao` (
  `tip_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_votacao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_votacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `tipo_votacao` (`tip_votacao`, `des_tipo_votacao`, `ind_excluido`) VALUES
(1, 'Simbólica', 0),
(2, 'Nominal', 0),
(3, 'Secreta', 0);

UPDATE ordem_dia SET tip_votacao=2 WHERE tip_votacao IS NULL;

ALTER TABLE `ordem_dia` ADD INDEX (`tip_votacao`);

ALTER TABLE `expediente_materia` ADD INDEX (`tip_votacao`);

ALTER TABLE `ordem_dia_presenca` ADD `tip_frequencia` CHAR(1) NOT NULL DEFAULT 'P' AFTER `cod_parlamentar`,
ADD INDEX (`tip_frequencia`) ;

ALTER TABLE `ordem_dia_presenca` ADD `txt_justif_ausencia` VARCHAR(200) NULL AFTER `tip_frequencia` ;

ALTER TABLE `sessao_plenaria_presenca` ADD `tip_frequencia` CHAR(1) NOT NULL DEFAULT 'P' AFTER `cod_parlamentar`,
ADD INDEX (`tip_frequencia`) ;

ALTER TABLE `sessao_plenaria_presenca` ADD `txt_justif_ausencia` VARCHAR(200) NULL AFTER `tip_frequencia` ;

CREATE TABLE IF NOT EXISTS `tipo_vinculo_norma` (
  `cod_tip_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_vinculo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tip_situacao` int(11) NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tip_vinculo`),
  UNIQUE KEY `tipo_vinculo` (`tipo_vinculo`),
  UNIQUE KEY `idx_vinculo` (`tipo_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`),
  KEY `tip_situacao` (`tip_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `tipo_vinculo_norma` (`cod_tip_vinculo`, `tipo_vinculo`, `des_vinculo`, `des_vinculo_passivo`, `tip_situacao`, `ind_excluido`) VALUES
(1, 'A', 'Altera a', 'Alterada pela', NULL, 0),
(2, 'C', 'Norma correlata', 'Norma correlata', NULL, 0),
(3, 'G', 'Regulamenta', 'Regulamentação', NULL, 0),
(4, 'I', 'Suspende a execução', 'Suspensão de execução', NULL, 0),
(5, 'P', 'Revoga parcialmente', 'Revogação parcial', 3, 0),
(6, 'R', 'Revoga a', 'Revogada pela', 2, 0),
(7, 'T', 'Revoga por consolidação', 'Revogação por consolidação', NULL, 0);

ALTER TABLE `vinculo_norma_juridica` ADD INDEX (`tip_vinculo`);

DELETE FROM `tramitacao` WHERE ind_excluido=1;

ALTER TABLE  `relatoria` ADD  `num_ordem` TINYINT( 4 ) NOT NULL AFTER  `cod_comissao` ;

ALTER TABLE  `materia_legislativa` CHANGE  `cod_situacao`  `cod_situacao` INT( 11 ) NULL DEFAULT NULL ;

ALTER TABLE materia_legislativa DROP INDEX txt_ementa;

ALTER TABLE materia_legislativa DROP INDEX txt_indexacao;

ALTER TABLE `materia_legislativa` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`);

ALTER TABLE norma_juridica DROP INDEX txt_ementa;

ALTER TABLE norma_juridica DROP INDEX txt_indexacao;

ALTER TABLE `norma_juridica` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`);

alter table documento_administrativo drop index documento_administrativo_ind1;

alter table documento_administrativo drop index txt_assunto;

alter table documento_administrativo drop index txt_autoria;

ALTER TABLE `documento_administrativo`   ADD KEY `idx_num_ano` (`num_documento`,`ano_documento`),   ADD KEY `idx_dat_documento` (`dat_documento`),   ADD KEY `idx_cod_autor` (`cod_autor`),   ADD KEY `idx_tip_documento` (`tip_documento`),   ADD FULLTEXT KEY `idx_busca_documento` (`txt_assunto`,`txt_observacao`);

ALTER TABLE `documento_administrativo`   ADD FULLTEXT KEY `idx_txt_interessado` (`txt_interessado`);

--
-- Tipo vinculo (rodar somente nas versões 2.7)
--

--- ALTER TABLE  `tipo_vinculo_norma` CHANGE  `tip_vinculo`  `tipo_vinculo` CHAR( 1 ) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL ;

ALTER TABLE  `vinculo_norma_juridica` ADD  `txt_observacao_vinculo` VARCHAR( 250 ) NULL DEFAULT NULL AFTER  `tip_vinculo` ;

--- ALTER TABLE  `tipo_vinculo_norma` ADD  `tip_situacao` INT( 11 ) NULL DEFAULT NULL AFTER  `des_vinculo_passivo` ;

--- ALTER TABLE  `tipo_vinculo_norma` ADD INDEX (  `tip_situacao` ) ;

--
-- Fim Tipo vinculo
--

-- Anexo Norma (rodar somente nas versões 2.7)

CREATE TABLE IF NOT EXISTS `anexo_norma` (
  `cod_anexo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma` int(11) NOT NULL,
  `txt_descricao` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_anexo`),
  KEY `cod_norma` (`cod_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- Fim Anexo Norma

ALTER TABLE `oradores`  ADD  UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),

ALTER TABLE `oradores_expediente`  ADD  UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),

ALTER TABLE  `ordem_dia` ADD INDEX (  `cod_sessao_plen` ) ;

ALTER TABLE  `expediente_materia` ADD INDEX (  `cod_sessao_plen` ) ;

ALTER TABLE `materia_legislativa` DROP `txt_resultado`;

ALTER TABLE `protocolo` DROP `cod_documento`;

ALTER TABLE `protocolo` DROP `cod_materia`;

-- Versão 3.1

ALTER TABLE `autor` ADD `end_email` VARCHAR( 100 ) NULL AFTER `col_username` ;

ALTER TABLE `proposicao` ADD `cod_emenda` INT( 11 ) NULL AFTER `cod_mat_ou_doc` ,
ADD INDEX ( `cod_emenda` ) ;

ALTER TABLE `proposicao` ADD `cod_substitutivo` INT( 11 ) NULL AFTER `cod_emenda` ,
ADD INDEX ( `cod_substitutivo` ) ;

ALTER TABLE  `tipo_documento_administrativo` ADD  `ind_publico` TINYINT( 4 ) NOT NULL DEFAULT  '0' AFTER  `des_tipo_documento` ;

CREATE TABLE IF NOT EXISTS `coautoria_proposicao` (
  `cod_proposicao` int(11) NOT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_aderido` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_proposicao`,`cod_autor`),
  KEY `idx_proposicao` (`cod_proposicao`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `usuario` (
  `cod_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `col_username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci NOT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade_resid` int(11) DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_celular` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nom_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_comercial` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_ramal` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_usuario`),
  KEY `idx_col_username` (`col_username`),
  KEY `idx_cod_localidade` (`cod_localidade_resid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE `usuario_unid_tram` (
  `cod_usuario` int(11) NOT NULL,
  `cod_unid_tramitacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  UNIQUE KEY `PRIMARY_KEY` (`cod_usuario`,`cod_unid_tramitacao`),
  KEY `idx_usuario` (`cod_usuario`),
  KEY `idx_unid_tramitacao` (`cod_unid_tramitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


