ALTER TABLE acomp_materia ENGINE=INNODB;
ALTER TABLE afastamento ENGINE=INNODB;
ALTER TABLE andamento_sessao ENGINE=INNODB;
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
ALTER TABLE partido_old ENGINE=INNODB;
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

CREATE TABLE `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_suporte`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_tit_documental`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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

ALTER TABLE `emenda` ADD `exc_pauta` tinyint(4) DEFAULT NULL AFTER `cod_autor`;

ALTER TABLE `emenda`
   CHANGE `tip_emenda` `tip_emenda` INT(11) NOT NULL, 
   DROP INDEX `idx_numemen_materia`, 
   ADD UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
   ADD KEY `idx_tip_emenda` (`tip_emenda`);

ALTER TABLE `subemenda` 
   CHANGE `tip_subemenda` `tip_subemenda` INT(11) NOT NULL,
   DROP INDEX `idx_numsub_emenda`, 
   ADD UNIQUE KEY `idx_numsub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
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
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tip_vinculo`),
  UNIQUE KEY `tip_vinculo` (`tip_vinculo`),
  UNIQUE KEY `idx_vinculo` (`tip_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `tipo_vinculo_norma` (`tip_vinculo`, `des_vinculo`, `des_vinculo_passivo`, `ind_excluido`) VALUES 
('A', 'Altera', 'Alteração', '0'),
('C', 'Norma correlata', 'Norma correlata', '0'),
('G', 'Regulamenta', 'Regulamentação', '0'),
('I', 'Suspende a execução', 'Suspensão de execução', '0'),
('P', 'Revoga parcialmente', 'Revogação parcial', '0'),
('R', 'Revoga', 'Revogação', '0'),
('T', 'Revoga por consolidação', 'Revogação por consolidação', '0');

ALTER TABLE `vinculo_norma_juridica` ADD INDEX (`tip_vinculo`);

ALTER TABLE `materia_legislativa` DROP `txt_resultado`;"

ALTER TABLE `protocolo` DROP `cod_documento`;"

ALTER TABLE `protocolo` DROP `cod_materia`;"

DELETE FROM `tramitacao` WHERE ind_excluido=1;
