CREATE TABLE IF NOT EXISTS `bancada` (
  `cod_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `nom_bancada` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_bancada`),
  KEY `idt_nom_bancada` (`nom_bancada`),
  KEY `idx_cod_bancada` (`ind_excluido`),
  FULLTEXT KEY `nom_bancada` (`nom_bancada`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `composicao_bancada` (
  `cod_comp_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_bancada` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comp_bancada`),
  KEY `fk_{F8A64E72-257D-4ABB-B921-85593A247FA9}` (`cod_cargo`),
  KEY `fk_{CC19A3D1-42B2-4156-A6F6-D51A7FED9BCA}` (`cod_bancada`),
  KEY `fk_{C52EA9E4-0190-4559-909D-336460F6F448}` (`cod_parlamentar`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

ALTER TABLE `autor` ADD `cod_bancada` INT( 11 ) NULL DEFAULT NULL AFTER `cod_comissao`;

ALTER TABLE `mandato` ADD `ind_titular` TINYINT( 4 ) NOT NULL AFTER `txt_observacao`;

ALTER TABLE `mandato` CHANGE `ind_titular` `ind_titular` TINYINT( 4 ) NOT NULL DEFAULT  '1';

ALTER TABLE `mandato` ADD `dat_inicio_mandato` DATE NULL DEFAULT NULL AFTER  `cod_coligacao`;

ALTER TABLE  `bancada` ADD  `dat_criacao` DATE NULL DEFAULT NULL AFTER  `descricao`;

ALTER TABLE  `bancada` ADD  `dat_extincao` DATE NULL DEFAULT NULL AFTER  `dat_criacao`;

ALTER TABLE  `parlamentar` ADD  `txt_observacao` TEXT NULL AFTER  `txt_biografia`;

CREATE TABLE IF NOT EXISTS `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `instituicao` (
  `cod_instituicao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_instituicao` tinyint(4) NOT NULL,
  `nom_instituicao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_instituicao` tinytext COLLATE utf8_unicode_ci,
  `nom_bairro` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_web` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_forma_tratamento` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` tinytext COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  `dat_insercao` datetime DEFAULT NULL,
  `txt_user_insercao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_insercao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp_alteracao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `txt_user_alteracao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_alteracao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_instituicao`),
  FULLTEXT KEY `idx_nom_instituicao` (`nom_instituicao`),
  FULLTEXT KEY `idx_nom_responsavel` (`nom_responsavel`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

ALTER TABLE  `norma_juridica` ADD  `cod_situacao` TINYINT( 4 ) NULL DEFAULT NULL AFTER  `cod_assunto`;

CREATE TABLE IF NOT EXISTS `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=20 ;

INSERT INTO `tipo_situacao_norma` (`tip_situacao_norma`, `des_tipo_situacao`, `ind_excluido`) VALUES
(1, 'Em vigor', 0),
(2, 'Revogada', 0),
(3, 'Revogada parcialmente', 0),
(4, 'Revogada tacitamente', 0),
(5, 'Execução suspensa', 0),
(6, 'Prejudicada', 0),
(7, 'Sub Judice', 0),
(8, 'Execução suspensa de dispositivos', 0),
(9, 'Nula', 0),
(10, 'Insubsistente', 0),
(11, 'Sub Judice (sem liminar)', 0),
(12, 'Em vigor, com revogação parcial', 0),
(13, 'Em vigor (sub judice parcial)', 0),
(14, 'Em vigor (execução suspensa parcial)', 0),
(15, 'Revogação sub judice', 0),
(16, 'Declarada inconstitucional pelo TJ', 0),
(17, 'Em vigor, parte declarada inconstitucional', 0),
(18, 'Em vigor 45 dias após a publicação', 0),
(19, 'Sem efeito', 0);

ALTER TABLE  `materia_legislativa` ADD  `cod_situacao` TINYINT( 4 ) NULL DEFAULT NULL AFTER  `txt_observacao`;

CREATE TABLE  `tipo_situacao_materia` (
`tip_situacao_materia` INT( 11 ) NOT NULL AUTO_INCREMENT ,
 `des_tipo_situacao` VARCHAR( 100 ) DEFAULT NULL ,
 `ind_excluido` TINYINT( 4 ) NOT NULL DEFAULT  '0',
PRIMARY KEY (  `tip_situacao_materia` )
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `tipo_situacao_materia` (`tip_situacao_materia`, `des_tipo_situacao`, `ind_excluido`) VALUES
(2, 'VETADO', 0),
(4, 'APROVADO', 0),
(5, 'APROVADO EM URGÊNCIA', 0),
(7, 'PREJUDICADO', 0),
(8, 'RETIRADO', 0),
(9, 'REJEITADO', 0),
(10, 'ADIADO', 0),
(11, 'APROVADO EM 1º TURNO', 0),
(12, 'APROVADO EM 2º TURNO', 0),
(15, 'ARQUIVADO', 0),
(16, 'DECLARADA INCONSTITUCIONAL', 0),
(18, 'APTO P/ APRECIAÇÃO', 0),
(21, 'DEFERIDO', 0),
(22, 'CANCELADO', 0),
(23, 'DESPACHADO', 0),
(24, 'APRESENTADO', 0),
(26, 'RECUSADO', 0),
(27, 'SANÇÃO TÁCITA', 0),
(28, 'SUSTADO', 0),
(31, 'PARECER CONTRÁRIO CJR (APTO)', 0),
(32, 'APTO (VETO)', 0),
(33, 'PARECER REJEITADO', 0),
(34, 'PARECER CONTRÁRIO CJR APROVADO', 0),
(35, 'APROVADO EM PREFERÊNCIA', 0),
(36, 'TRAMITANDO', 0),
(37, 'AUTÓGRAFO', 0),
(38, 'VETO TOTAL REJEITADO', 0),
(39, 'VETO TOTAL MANTIDO', 0),
(42, 'DISCUSSÃO INTERROMPIDA', 0),
(43, 'PARECER CONTRÁRIO DA CJR (TRAMITANDO)', 0),
(44, 'VETO PARCIAL MANTIDO', 0),
(45, 'VETO PARCIAL REJEITADO', 0),
(47, 'NORMA', 0),
(48, 'VETO EM TRÂMITE', 0),
(49, 'ENVIANDO OFÍCIOS', 0),
(50, 'CONSULTORIA JURÍDICA', 0),
(51, 'AGUARDANDO INFORMAÇÕES', 0),
(52, 'EM PAUTA', 0),
(53, 'DIRETORIA JURÍDICA', 0),
(54, 'VETO PARCIAL MANTIDO PARCIALMENTE', 0),
(55, 'AGUARDANDO AUDIÊNCIA PÚBLICA', 0),
(57, 'AGUARDANDO INF/AUD. PÚBLICA', 0),
(58, 'INDEFERIDO', 0),
(59, 'AUDIÊNCIA PÚBLICA', 0),
(60, 'SUBSTITUTIVO TRAMITANDO', 0),
(61, 'MANTIDO', 0),
(62, 'SEM EFEITO', 0),
(63, 'ADIADO/DISCUSSÃO INTERROMPIDA', 0),
(64, 'CONVERTIDO EM PDL', 0),
(65, 'CONVERTIDO EM PL', 0),
(66, 'CONVERTIDO EM PLC', 0),
(67, 'SEM RESULTADO', 0),
(69, 'REJEITADA NA COMISSÃO MISTA', 0),
(70, 'PUBLICAR NA IMPRENSA OFICIAL', 0),
(71, 'APROVADO COM ALTERAÇÕES', 0),
(72, 'APROVADO SEM ALTERAÇÕES', 0),
(73, 'CONVERTIDO EM PR', 0),
(74, 'VETO PARCIAL EM TRÂMITE', 0),
(75, 'VETADO PARCIALMENTE', 0),
(76, 'REVOGADO', 0),
(77, 'NORMA (VETO PARCIAL MANTIDO)', 0),
(78, 'NORMA (VETO TOTAL REJEITADO)', 0),
(79, 'NORMA (SANÇÃO TÁCITA)', 0),
(80, 'ADIADO (PAR. CONTRÁRIO CJR)', 0),
(81, 'NORMA (VETO PARCIAL REJEITADO)', 0),
(93, 'APTO P/ APRECIAÇÃO (2º. TURNO)', 0),
(94, 'VETO ADIADO', 0),
(95, 'DEVOLVIDO À PREFEITURA', 0),
(97, 'CONVERTIDO EM INDICAÇÃO', 0),
(98, 'ANEXADO A PROJETO DE LEI', 0),
(99, 'ANEXADO A PROJETO DE RESOLUÇÃO', 0),
(100, 'CONVERTIDO EM REQUERIMENTO', 0),
(101, 'CONVERTIDO EM MOÇÃO', 0),
(102, 'CONVERTIDO EM JUSTIFICATIVA DE PL', 0),
(103, 'ADIADO - AGUARDA AUD. PÚBLICA', 0),
(104, 'APTO ILEGAL', 0),
(105, 'APTO ILEGAL/INCOSNTITUCIONAL', 0),
(106, 'APTO INCONSTITUCIONAL', 0),
(107, 'ADIADO ILEGAL', 0),
(108, 'ADIADO ILEGAL/INCONSTITUCIONAL', 0),
(109, 'ADIADO INCONSTITUCIONAL', 0),
(110, 'PAUTADO PARA EXTRAORDINÁRIA', 0);

CREATE TABLE IF NOT EXISTS `reuniao_comissao` (
  `cod_reuniao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) NOT NULL,
  `num_reuniao` int(11) NOT NULL,
  `dat_inicio_reuniao` date NOT NULL,
  `hr_inicio_reuniao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_reuniao`),
  KEY `fk_cod_comissao` (`cod_comissao`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;


ALTER TABLE  `relatoria` ADD  `txt_parecer` TEXT NULL DEFAULT NULL AFTER  `dat_destit_relator`;

CREATE TABLE IF NOT EXISTS `materia_apresentada_sessao` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) unsigned NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `fk_cod_materia` (`cod_materia`),
  KEY `idx_apresent_datord` (`dat_ordem`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `encerramento_presenca` (
  `cod_presenca_encerramento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_encerramento`),
  UNIQUE KEY `idx_encpres_sessao_plenaria` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_cod_parlamentar` (`cod_parlamentar`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `expediente_presenca` (
  `cod_presenca_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_expediente`),
  UNIQUE KEY `idx_exppres_sessao_plenaria` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_cod_parlamentar` (`cod_parlamentar`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `emenda` (
  `cod_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_emenda` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `num_emenda` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_emenda`),
  UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_materia` (`cod_materia`),
  KEY `idx_cod_autor` (`cod_autor`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `subemenda` (
  `cod_subemenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_subemenda` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `num_subemenda` int(11) NOT NULL,
  `cod_emenda` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_subemenda`),
  UNIQUE KEY `idx_numsub_emenda` (`num_subemenda`,`cod_emenda`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_emenda` (`cod_emenda`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `substitutivo` (
  `cod_substitutivo` int(11) NOT NULL AUTO_INCREMENT,
  `num_substitutivo` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_substitutivo`),
  UNIQUE KEY `idx_numsub_materia` (`num_substitutivo`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_materia` (`cod_materia`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

ALTER TABLE  `documento_acessorio` ADD  `txt_observacao` TEXT NULL DEFAULT NULL AFTER  `txt_ementa`;

RENAME TABLE partido TO partido_old;

CREATE TABLE `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

INSERT INTO `partido` (`cod_partido`, `sgl_partido`, `nom_partido`, `dat_criacao`, `dat_extincao`, `ind_excluido`) VALUES
(1,'PMDB','Partido do Movimento Democrático Brasileiro','1981-06-30',NULL,0),(2,'PTB','Partido Trabalhista Brasileiro','1981-11-03',NULL,0),(3,'PDT','Partido Democrático Trabalhista','1981-11-10',NULL,0),(4,'PT','Partido dos Trabalhadores','1982-02-10',NULL,0),(5,'DEM','Democratas','2007-03-28',NULL,0),(6,'PCdoB','Partido Comunista do Brasil','1988-06-23',NULL,0),(7,'PSB','Partido Socialista Brasileiro','1988-07-01',NULL,0),(8,'PSDB','Partido da Social Democracia Brasileira','1989-08-24',NULL,0),(9,'PTC','Partido Trabalhista Cristão','1990-02-22',NULL,0),(10,'PSC','Partido Social Cristão','1990-03-29',NULL,0),(11,'PMN','Partido da Mobilização Nacional','1990-10-25',NULL,0),(12,'PRP','Partido Republicano Progressista','2005-08-25',NULL,0),(13,'PPS','Partido Popular Socialista','1992-03-19',NULL,0),(14,'PV','Partido Verde','1993-09-30',NULL,0),(15,'PTdoB','Partido Trabalhista do Brasil','1994-10-11',NULL,0),(16,'PP','Partido Progressista','1995-11-16',NULL,0),(17,'PSTU','Partido Socialista dos Trabalhadores Unificado','1995-12-19',NULL,0),(18,'PCB','Partido Comunista Brasileiro','1996-05-09',NULL,0),(19,'PRTB','Partido Renovador Trabalhista Brasileiro','1997-02-18',NULL,0),(20,'PHS','Partido Humanista da Solidariedade','1997-03-20',NULL,0),(21,'PSDC','Partido Social Democrata Cristão','1997-08-05',NULL,0),(22,'PCO','Partido da Causa Operária','1997-09-30',NULL,0),(23,'PTN','Partido Trabalhista Nacional','1997-10-02',NULL,0),(24,'PSL','Partido Social Liberal','1998-06-02',NULL,0),(25,'PRB','Partido Republicano Brasileiro','2005-08-25',NULL,0),(26,'PSOL','Partido Socialismo e Liberdade','2005-09-15',NULL,0),(27,'PR','Partido da República','2006-12-19',NULL,0),(28,'PPB','Partido Progressista Brasileiro','1993-01-31','2003-04-04',0),(29,'ARENA','Aliança Renovadora Nacional','1966-04-04','1979-12-20',0),(30,'MDB','Movimento Democrático Brasileiro','1966-03-24','1979-11-27',0),(31,'PDS','Partido Democrático Social','1980-01-30','1993-04-04',0),(32,'PL','Partido Liberal','1985-02-03','2006-12-21',0),(33,'PFL','Partido da Frente Liberal','1985-01-24','2007-03-28',0),(34,'PSD','Partido Social Democrático','2011-09-27',NULL,0),(35,'PSP','Partido Social Progressista','1945-11-08','1946-11-19',0),(36,'PDC','Partido Democrata Cristão','1945-07-09','1965-10-27',0),(37,'UDN','União Democrática Nacional','1945-04-07','1965-10-27',0),(38,'PRT','Partido Revolucionário dos Trabalhadores','1969-01-13','1971-02-05',0),(39,'PPR','Partido Progressista Renovador','1993-04-04','1995-04-15',0),(40,'PPL','Partido Pátria Livre','2011-10-04',NULL,0),(41,'PEN','Partido Ecológico Nacional','2012-06-19',NULL,0),(42,'PROS','Partido Republicano da Ordem Social','2013-09-24',NULL,0),(43,'SDD','Solidariedade','2013-09-24',NULL,0);

ALTER TABLE `proposicao` ADD `txt_observacao` TEXT NULL DEFAULT NULL AFTER `txt_justif_devolucao`;

ALTER TABLE `proposicao` CHANGE `txt_descricao` `txt_descricao` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;

ALTER TABLE `documento_acessorio` CHANGE `nom_documento` `nom_documento` VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

ALTER TABLE `ordem_dia` ADD `tip_quorum` INT(11) NULL DEFAULT NULL;

ALTER TABLE `relatoria` ADD `tip_apresentacao` CHAR(1) NULL DEFAULT NULL AFTER `dat_destit_relator`;

ALTER TABLE `relatoria` ADD `tip_conclusao` CHAR(1) NULL DEFAULT NULL AFTER `txt_parecer`;

ALTER TABLE `parlamentar` ADD FULLTEXT `nom_parlamentar` (`nom_parlamentar`);

UPDATE `tipo_autor` SET `des_tipo_autor`='Comissao' WHERE `tip_autor`=2;

DROP TABLE materia_assunto;

DROP TABLE assunto_materia;

ALTER TABLE  `emenda` CHANGE  `txt_ementa`  `txt_ementa` VARCHAR( 400 ) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

ALTER TABLE  `subemenda` CHANGE  `txt_ementa`  `txt_ementa` VARCHAR( 400 ) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

ALTER TABLE  `registro_votacao` ADD  `cod_emenda` INT( 11 ) NULL DEFAULT NULL AFTER  `cod_ordem`;

ALTER TABLE  `registro_votacao` ADD  `cod_subemenda` INT( 11 ) NULL DEFAULT NULL AFTER  `cod_emenda`;

ALTER TABLE  `registro_votacao` ADD  `cod_substitutivo` INT( 11 ) NULL DEFAULT NULL AFTER  `cod_subemenda`;

CREATE TABLE  `periodo_comp_mesa` (
`cod_periodo_comp` INT( 11 ) NOT NULL AUTO_INCREMENT ,
`num_legislatura` INT( 11 ) NOT NULL,
`dat_inicio_periodo` date NOT NULL ,
`dat_fim_periodo` date NOT NULL ,
`ind_excluido` TINYINT( 4 ) NOT NULL ,
PRIMARY KEY (  `cod_periodo_comp` ) ,
KEY  `ind_percompmesa_datas` (  `dat_inicio_periodo` ,  `dat_fim_periodo` ,  `ind_excluido` )
) ENGINE = MYISAM DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci PACK_KEYS =0;

INSERT INTO periodo_comp_mesa (cod_periodo_comp,num_legislatura,dat_inicio_periodo,dat_fim_periodo,ind_excluido) SELECT cod_sessao_leg,num_legislatura, dat_inicio,dat_fim,ind_excluido FROM sessao_legislativa ORDER BY cod_sessao_leg;

ALTER TABLE  `composicao_mesa` ADD  `cod_periodo_comp` INT( 11 ) NOT NULL AFTER  `cod_sessao_leg`;

UPDATE composicao_mesa SET cod_periodo_comp = cod_sessao_leg;

ALTER TABLE `composicao_mesa` DROP PRIMARY KEY,
ADD PRIMARY KEY (`cod_parlamentar`, `cod_periodo_comp`, `cod_cargo`);

ALTER TABLE  `composicao_mesa` CHANGE  `cod_sessao_leg`  `cod_sessao_leg` INT( 11 ) NULL DEFAULT NULL;

ALTER TABLE  `composicao_mesa` ADD INDEX  `idx_cod_periodo_comp` (  `cod_periodo_comp` );

CREATE TABLE `afastamento` (
  `cod_afastamento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_mandato` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `tip_afastamento` int(11) NOT NULL,
  `dat_inicio_afastamento` date NOT NULL,
  `dat_fim_afastamento` date DEFAULT NULL,
  `cod_parlamentar_suplente` int(11) NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_afastamento`),
  KEY `idx_parlamentar_mandato` (`cod_parlamentar`,`num_legislatura`),
  KEY `idx_afastamento_datas` (`cod_parlamentar`,`dat_inicio_afastamento`,`dat_fim_afastamento`),
  KEY `idx_tip_afastamento` (`tip_afastamento`),
  KEY `idx__parlamentar_suplente` (`cod_parlamentar_suplente`,`num_legislatura`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

UPDATE
  mandato m 
  LEFT JOIN legislatura l ON m.num_legislatura = l.num_legislatura
SET
   m.dat_inicio_mandato = l.dat_inicio,
   m.dat_fim_mandato = l.dat_fim
WHERE
   m.ind_titular = 1;

UPDATE norma_juridica set cod_situacao = 1;


