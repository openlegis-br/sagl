-- -----------------------------------------------------
-- Table `props_painel`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `props_painel` (
  `cod_props_painel` INT(11) NOT NULL ,
  `txt_jornal` TEXT NULL ,
  `txt_jornal_cor` VARCHAR(45) NULL ,
  `txt_jornal_fonte` VARCHAR(5) NULL ,
  `txt_mensagem` TEXT NULL ,
  `txt_mensagem_fonte` VARCHAR(5) NULL ,
  `txt_fonte` VARCHAR(45) NOT NULL ,
  `txt_painel_cor_fonte` VARCHAR(45) NOT NULL ,
  `txt_painel_cor_fundo` VARCHAR(45) NOT NULL ,
  `txt_apartante_cor` VARCHAR(45) NULL ,
  `txt_apartante_tempo` VARCHAR(45) NULL ,
  `txt_apartante_fonte` VARCHAR(5) NULL,
  `txt_questao_ordem_cor` VARCHAR(45) NULL ,
  `txt_questao_ordem_tempo` VARCHAR(45) NULL ,
  `txt_questao_ordem_fonte` VARCHAR(5) NULL,
  `txt_orador_cor` VARCHAR(45) NULL ,
  `txt_orador_tempo` VARCHAR(45) NULL ,
  `txt_orador_fonte` VARCHAR(5) NULL ,
  `txt_mesa_cor` VARCHAR(45) NULL ,
  `txt_mesa_fonte` VARCHAR(5) NULL ,
  `txt_presenca_cor` VARCHAR(45) NULL ,
  `txt_presenca_fonte` VARCHAR(5) NULL ,
  `txt_ausencia_cor` VARCHAR(45) NULL ,
  `txt_ausencia_fonte` VARCHAR(5) NULL ,
  `txt_presenca_total_cor` VARCHAR(45) NULL ,
  `txt_presenca_total_fonte` VARCHAR(5) NULL ,
  `txt_ausencia_total_cor` VARCHAR(45) NULL ,
  `txt_ausencia_total_fonte` VARCHAR(5) NULL ,
  `txt_total_sim_cor` VARCHAR(45) NULL ,
  `txt_total_sim_fonte` VARCHAR(5) NULL ,
  `txt_total_nao_cor` VARCHAR(45) NULL ,
  `txt_total_nao_fonte` VARCHAR(5) NULL ,
  `txt_total_abstencao_cor` VARCHAR(45) NULL ,
  `txt_total_abstencao_fonte` VARCHAR(5) NULL ,
  `txt_total_nao_votou_cor` VARCHAR(45) NULL ,
  `txt_total_nao_votou_fonte` VARCHAR(5) NULL ,
  `txt_total_votos_cor` VARCHAR(45) NULL ,
  `txt_total_votos_fonte` VARCHAR(5) NULL ,
  `txt_total_presentes_cor` VARCHAR(45) NULL ,
  `txt_total_presentes_fonte` VARCHAR(5) NULL ,
  `txt_total_ausentes_cor` VARCHAR(45) NULL ,
  `txt_total_ausentes_fonte` VARCHAR(5) NULL ,
  PRIMARY KEY (`cod_props_painel`)
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE `ordem_dia` ADD COLUMN `ind_votacao_iniciada` INT(4) NOT NULL DEFAULT 0  AFTER `tip_votacao` ;

ALTER TABLE `ordem_dia` ADD COLUMN `dat_ultima_votacao` DATETIME NULL ;

DELIMITER $$

  CREATE TRIGGER before_ordem_dia_update BEFORE UPDATE ON ordem_dia
    FOR EACH ROW BEGIN
      IF OLD.ind_votacao_iniciada = 1 AND NEW.ind_votacao_iniciada = 0 THEN
        SET NEW.dat_ultima_votacao = NOW();
      END IF;
    END;$$

DELIMITER ;

INSERT INTO `props_painel` (`txt_fonte`, `txt_painel_cor_fonte`, `txt_painel_cor_fundo`) VALUES ('Arial', '#FFFFFF', '#000000') ;

ALTER TABLE `sessao_plenaria` ADD COLUMN `ind_iniciada` TINYINT(4) NULL  DEFAULT 0 AFTER `url_video` ;

ALTER TABLE `parlamentar` ADD COLUMN `txt_login` VARCHAR(45) NOT NULL  AFTER `ind_unid_deliberativa` ;

CREATE  TABLE `presenca_endereco` (
  `cod_presenca_endereco` INT NOT NULL AUTO_INCREMENT,
  `txt_mac_address` VARCHAR(45) NOT NULL ,
  `txt_ip_address` VARCHAR(45) NOT NULL ,
  `ind_excluido` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`cod_presenca_endereco`)
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE `sessao_plenaria_presenca`
  ADD COLUMN `dat_presenca` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  ON UPDATE CURRENT_TIMESTAMP AFTER `dat_sessao` ,
  ADD COLUMN `cod_ip` VARCHAR(50) NOT NULL  AFTER `dat_presenca` ,
  ADD COLUMN `cod_mac` VARCHAR(50) NOT NULL  AFTER `cod_ip` ,
  ADD COLUMN `cod_perfil` VARCHAR(20) NOT NULL DEFAULT 'parlamentar'  AFTER `cod_mac` ,
  ADD COLUMN `ind_recontagem` TINYINT(4) NOT NULL DEFAULT 0  AFTER `cod_perfil` ;

ALTER TABLE `ordem_dia_presenca`
  ADD COLUMN `dat_presenca` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  AFTER `dat_ordem`,
  ADD COLUMN `cod_ip` VARCHAR(50) NOT NULL  AFTER `dat_presenca` ,
  ADD COLUMN `cod_mac` VARCHAR(50) NOT NULL  AFTER `cod_ip` ,
  ADD COLUMN `cod_perfil` VARCHAR(45) NOT NULL DEFAULT 'parlamentar'  AFTER `cod_mac` ,
  ADD COLUMN `num_id_quorum` TINYINT(4) NOT NULL  AFTER `cod_perfil` ,
  ADD COLUMN `ind_recontagem` TINYINT(4) NOT NULL DEFAULT 0  AFTER `cod_perfil`;

CREATE  TABLE `registro_presenca_sessao` (
  `cod_registro_pre` INT(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` INT(11) NOT NULL ,
  `num_id_quorum` TINYINT(4) NOT NULL ,
  `ind_status_pre` TINYINT(1) NOT NULL DEFAULT 1 ,
  `dat_abre_pre` DATETIME NOT NULL ,
  `dat_fecha_pre` DATETIME NOT NULL ,
  `ind_excluido` TINYINT(4) NOT NULL DEFAULT 0 ,
  PRIMARY KEY (`cod_registro_pre`)
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE  TABLE `registro_presenca_ordem` (
  `cod_registro_pre` INT(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` INT(11) NOT NULL ,
  `num_id_quorum` TINYINT(4) NOT NULL ,
  `ind_status_pre` TINYINT(1) NOT NULL DEFAULT 1 ,
  `dat_abre_pre` DATETIME NOT NULL ,
  `dat_fecha_pre` DATETIME NOT NULL ,
  `ind_excluido` TINYINT(4) NOT NULL DEFAULT 0 ,
  PRIMARY KEY (`cod_registro_pre`)
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE  TABLE `cronometro_aparte` (
  `int_reset` TINYINT(4) NOT NULL ,
  `int_start` TINYINT(4) NOT NULL ,
  `int_stop` TINYINT(4) NOT NULL
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO `cronometro_aparte` VALUES(0,0,0);

CREATE  TABLE `cronometro_ordem` (
  `int_reset` TINYINT(4) NOT NULL ,
  `int_start` TINYINT(4) NOT NULL ,
  `int_stop` TINYINT(4) NOT NULL
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO `cronometro_ordem` VALUES(0,0,0);

CREATE  TABLE `cronometro_discurso` (
  `int_reset` TINYINT(4) NOT NULL ,
  `int_start` TINYINT(4) NOT NULL ,
  `int_stop` TINYINT(4) NOT NULL
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO `cronometro_discurso` VALUES(0,0,0);

CREATE  TABLE `sessao_plenaria_log` (
  `cod_sessao_plen_log` INT(11) NOT NULL AUTO_INCREMENT ,
  `cod_sessao_plen` INT(11) DEFAULT NULL ,
  `txt_login` VARCHAR(45) NOT NULL ,
  `txt_ip` VARCHAR(45) NOT NULL ,
  `txt_mac` VARCHAR(45) NOT NULL ,
  `txt_acao` VARCHAR(45) NOT NULL ,
  `txt_mensagem` VARCHAR(500) NOT NULL ,
  `dat_log` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
  `ind_excluido` TINYINT(4) NOT NULL DEFAULT 0 ,
  PRIMARY KEY (`cod_sessao_plen_log`)
  )ENGINE = MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `bancada` (
  `cod_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `nom_bancada` varchar(60) NOT NULL,
  `descricao` mediumtext,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_bancada`),
  KEY `idt_nom_bancada` (`nom_bancada`),
  KEY `idx_cod_bancada` (`ind_excluido`),
  FULLTEXT KEY `nom_bancada` (`nom_bancada`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `composicao_bancada` (
  `cod_comp_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_bancada` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) DEFAULT NULL,
  `obs_composicao` varchar(150) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comp_bancada`),
  KEY `fk_{F8A64E72-257D-4ABB-B921-85593A247FA9}` (`cod_cargo`),
  KEY `fk_{CC19A3D1-42B2-4156-A6F6-D51A7FED9BCA}` (`cod_bancada`),
  KEY `fk_{C52EA9E4-0190-4559-909D-336460F6F448}` (`cod_parlamentar`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

ALTER TABLE `autor` ADD `cod_bancada` INT( 11 ) NULL DEFAULT NULL AFTER `cod_comissao`;

ALTER TABLE `mandato` ADD `ind_titular` TINYINT( 4 ) NOT NULL AFTER `txt_observacao`;

ALTER TABLE `mandato` CHANGE `ind_titular` `ind_titular` TINYINT( 4 ) NOT NULL DEFAULT  '1';

ALTER TABLE `mandato` ADD `dat_inicio_mandato` DATE NULL DEFAULT NULL AFTER  `cod_coligacao`;

ALTER TABLE  `bancada` ADD  `dat_criacao` DATE NULL DEFAULT NULL AFTER  `descricao`;

ALTER TABLE  `bancada` ADD  `dat_extincao` DATE NULL DEFAULT NULL AFTER  `dat_criacao`;

ALTER TABLE  `parlamentar` ADD  `txt_observacao` TEXT NULL AFTER  `txt_biografia`;

CREATE TABLE IF NOT EXISTS `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `instituicao` (
  `cod_instituicao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_instituicao` tinyint(4) NOT NULL,
  `nom_instituicao` varchar(200) DEFAULT NULL,
  `end_instituicao` tinytext,
  `nom_bairro` varchar(80) DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `num_cep` varchar(9) DEFAULT NULL,
  `num_telefone` varchar(50) DEFAULT NULL,
  `num_fax` varchar(50) DEFAULT NULL,
  `end_email` varchar(100) DEFAULT NULL,
  `end_web` varchar(100) DEFAULT NULL,
  `nom_responsavel` varchar(50) DEFAULT NULL,
  `des_cargo` varchar(80) DEFAULT NULL,
  `txt_forma_tratamento` varchar(30) DEFAULT NULL,
  `txt_observacao` tinytext,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  `dat_insercao` datetime DEFAULT NULL,
  `txt_user_insercao` varchar(20) DEFAULT NULL,
  `txt_ip_insercao` varchar(15) DEFAULT NULL,
  `timestamp_alteracao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `txt_user_alteracao` varchar(20) DEFAULT NULL,
  `txt_ip_alteracao` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`cod_instituicao`),
  FULLTEXT KEY `idx_nom_instituicao` (`nom_instituicao`),
  FULLTEXT KEY `idx_nom_responsavel` (`nom_responsavel`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci AUTO_INCREMENT=1 ;

ALTER TABLE  `norma_juridica` ADD  `cod_situacao` TINYINT( 4 ) NULL DEFAULT NULL AFTER  `cod_assunto`;

INSERT INTO `assunto_norma` (`cod_assunto`, `des_assunto`, `des_estendida`, `ind_excluido`) VALUES
(10, 'Acessibilidade / Mobilidade Urbana', '  \r\n           \r\n           ', 0),
(11, 'Assistência Social', ' \r\n           ', 0),
(12, 'Autarquias', ' \r\n           ', 0),
(13, 'Calendário de Eventos / Feriados', ' \r\n           ', 0),
(14, 'Comércio / Publicidade', ' \r\n           ', 0),
(15, 'Compras / Licitações', ' \r\n           ', 0),
(16, 'Conselhos / Comissões / Fundos', ' \r\n           ', 0),
(17, 'Contratos / Convênios / Consórcios', ' \r\n           ', 0),
(18, 'Créditos Adicionais', ' \r\n           ', 0),
(19, 'Criança / Adolescente', ' \r\n           ', 0),
(20, 'Cultura / Turismo', ' \r\n           ', 0),
(21, 'Defesa Civil', ' \r\n           ', 0),
(22, 'Orçamento / PPA / LDO / LOA', ' \r\n           ', 0),
(23, 'Educação', ' \r\n           ', 0),
(24, 'Saneamento', ' \r\n           ', 0),
(25, 'Saúde', ' \r\n           ', 0),
(26, 'Utilidade Pública', ' \r\n           ', 0),
(27, 'Zoneamento Urbano', ' \r\n           ', 0),
(28, 'Segurança Pública', ' \r\n           ', 0),
(29, 'Câmara Municipal', ' \r\n           ', 0),
(30, 'Servidor Público', ' \r\n           ', 0),
(31, 'Remuneração / Vencimentos / Salários / Subsídios', ' \r\n           ', 0);

CREATE TABLE IF NOT EXISTS `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci AUTO_INCREMENT=20 ;

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
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

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
  `hr_inicio_reuniao` varchar(5) DEFAULT NULL,
  `txt_observacao` text,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_reuniao`),
  KEY `fk_cod_comissao` (`cod_comissao`)
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci AUTO_INCREMENT=1;


ALTER TABLE  `relatoria` ADD  `txt_parecer` TEXT NULL DEFAULT NULL AFTER  `dat_destit_relator`;

ALTER TABLE  `documento_acessorio` ADD  `txt_observacao` TEXT NULL DEFAULT NULL AFTER  `txt_ementa`;

RENAME TABLE partido TO partido_old;

CREATE TABLE `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) DEFAULT NULL,
  `nom_partido` varchar(50) DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

INSERT INTO `partido` (`cod_partido`, `sgl_partido`, `nom_partido`, `dat_criacao`, `dat_extincao`, `ind_excluido`) VALUES
(1,'PMDB','Partido do Movimento Democrático Brasileiro','1981-06-30',NULL,0),(2,'PTB','Partido Trabalhista Brasileiro','1981-11-03',NULL,0),(3,'PDT','Partido Democrático Trabalhista','1981-11-10',NULL,0),(4,'PT','Partido dos Trabalhadores','1982-02-10',NULL,0),(5,'DEM','Democratas','2007-03-28',NULL,0),(6,'PCdoB','Partido Comunista do Brasil','1988-06-23',NULL,0),(7,'PSB','Partido Socialista Brasileiro','1988-07-01',NULL,0),(8,'PSDB','Partido da Social Democracia Brasileira','1989-08-24',NULL,0),(9,'PTC','Partido Trabalhista Cristão','1990-02-22',NULL,0),(10,'PSC','Partido Social Cristão','1990-03-29',NULL,0),(11,'PMN','Partido da Mobilização Nacional','1990-10-25',NULL,0),(12,'PRP','Partido Republicano Progressista','2005-08-25',NULL,0),(13,'PPS','Partido Popular Socialista','1992-03-19',NULL,0),(14,'PV','Partido Verde','1993-09-30',NULL,0),(15,'PTdoB','Partido Trabalhista do Brasil','1994-10-11',NULL,0),(16,'PP','Partido Progressista','1995-11-16',NULL,0),(17,'PSTU','Partido Socialista dos Trabalhadores Unificado','1995-12-19',NULL,0),(18,'PCB','Partido Comunista Brasileiro','1996-05-09',NULL,0),(19,'PRTB','Partido Renovador Trabalhista Brasileiro','1997-02-18',NULL,0),(20,'PHS','Partido Humanista da Solidariedade','1997-03-20',NULL,0),(21,'PSDC','Partido Social Democrata Cristão','1997-08-05',NULL,0),(22,'PCO','Partido da Causa Operária','1997-09-30',NULL,0),(23,'PTN','Partido Trabalhista Nacional','1997-10-02',NULL,0),(24,'PSL','Partido Social Liberal','1998-06-02',NULL,0),(25,'PRB','Partido Republicano Brasileiro','2005-08-25',NULL,0),(26,'PSOL','Partido Socialismo e Liberdade','2005-09-15',NULL,0),(27,'PR','Partido da República','2006-12-19',NULL,0),(28,'PPB','Partido Progressista Brasileiro','1993-01-31','2003-04-04',0),(29,'ARENA','Aliança Renovadora Nacional','1966-04-04','1979-12-20',0),(30,'MDB','Movimento Democrático Brasileiro','1966-03-24','1979-11-27',0),(31,'PDS','Partido Democrático Social','1980-01-30','1993-04-04',0),(32,'PL','Partido Liberal','1985-02-03','2006-12-21',0),(33,'PFL','Partido da Frente Liberal','1985-01-24','2007-03-28',0),(34,'PSD','Partido Social Democrático','2011-09-27',NULL,0),(35,'PSP','Partido Social Progressista','1945-11-08','1946-11-19',0),(36,'PDC','Partido Democrata Cristão','1945-07-09','1965-10-27',0),(37,'UDN','União Democrática Nacional','1945-04-07','1965-10-27',0),(38,'PRT','Partido Revolucionário dos Trabalhadores','1969-01-13','1971-02-05',0),(39,'PPR','Partido Progressista Renovador','1993-04-04','1995-04-15',0),(40,'PPL','Partido Pátria Livre','2011-10-04',NULL,0),(41,'PEN','Partido Ecológico Nacional','2012-06-19',NULL,0),(42,'PROS','Partido Republicano da Ordem Social','2013-09-24',NULL,0),(43,'SDD','Solidariedade','2013-09-24',NULL,0);

ALTER TABLE `proposicao` ADD `txt_observacao` TEXT NULL DEFAULT NULL AFTER `txt_justif_devolucao`;

ALTER TABLE `proposicao` CHANGE COLUMN `txt_descricao` `txt_descricao` VARCHAR(400) CHARACTER SET 'latin1' NOT NULL  ;

ALTER TABLE `documento_acessorio` CHANGE `nom_documento` `nom_documento` VARCHAR(50) CHARACTER SET 'latin1' NULL DEFAULT NULL;

ALTER TABLE `ordem_dia` ADD `tip_quorum` INT(11) NULL DEFAULT NULL;

ALTER TABLE `relatoria` ADD `tip_apresentacao` CHAR(1) NULL DEFAULT NULL AFTER `dat_destit_relator`;

ALTER TABLE `relatoria` ADD `tip_conclusao` CHAR(1) NULL DEFAULT NULL AFTER `txt_parecer`;

ALTER TABLE `parlamentar` ADD FULLTEXT `nom_parlamentar` (`nom_parlamentar`);

CREATE TABLE  `periodo_comp_mesa` (
`cod_periodo_comp` INT( 11 ) NOT NULL AUTO_INCREMENT ,
`num_legislatura` INT( 11 ) NOT NULL,
`dat_inicio_periodo` date NOT NULL ,
`dat_fim_periodo` date NOT NULL ,
`ind_excluido` TINYINT( 4 ) NOT NULL ,
PRIMARY KEY (  `cod_periodo_comp` ) ,
KEY  `ind_percompmesa_datas` (  `dat_inicio_periodo` ,  `dat_fim_periodo` ,  `ind_excluido` )
) ENGINE=MyISAM  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

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
  `txt_observacao` text,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_afastamento`),
  KEY `idx_parlamentar_mandato` (`cod_parlamentar`,`num_legislatura`),
  KEY `idx_afastamento_datas` (`cod_parlamentar`,`dat_inicio_afastamento`,`dat_fim_afastamento`),
  KEY `idx_tip_afastamento` (`tip_afastamento`),
  KEY `idx__parlamentar_suplente` (`cod_parlamentar_suplente`,`num_legislatura`)
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

UPDATE mandato SET ind_titular = 1;

UPDATE
  mandato m
  LEFT JOIN legislatura l ON m.num_legislatura = l.num_legislatura
SET
   m.dat_inicio_mandato = l.dat_inicio,
   m.dat_fim_mandato = l.dat_fim
WHERE
   m.ind_titular = 1;

UPDATE norma_juridica set cod_situacao = 1;

ALTER TABLE `expediente_materia` ADD COLUMN `ind_votacao_iniciada` TINYINT(4) NOT NULL  AFTER `tip_votacao` ;
ALTER TABLE `expediente_materia` ADD COLUMN `dat_ultima_votacao` DATETIME NULL  AFTER `ind_votacao_iniciada` ;

DELIMITER $$

  CREATE TRIGGER before_materias_expediente_update BEFORE UPDATE ON expediente_materia
    FOR EACH ROW BEGIN
      IF OLD.ind_votacao_iniciada = 1 AND NEW.ind_votacao_iniciada = 0 THEN
        SET NEW.dat_ultima_votacao = NOW();
      END IF;
    END;$$

DELIMITER ;

ALTER TABLE `registro_votacao_parlamentar` ADD COLUMN `txt_login` VARCHAR(15) NOT NULL  AFTER `vot_parlamentar` ;

ALTER TABLE `registro_votacao` ADD COLUMN `num_nao_votou` TINYINT(4) NULL  AFTER `ind_excluido` ;

ALTER TABLE `materia_legislativa` ADD COLUMN `txt_cep` VARCHAR(15) NULL AFTER `txt_resultado`;
