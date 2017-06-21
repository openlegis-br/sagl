-- Compatibiliza tabela 'legislatura' com MySQL 5.7

ALTER TABLE  `legislatura` 
 CHANGE `dat_inicio` `dat_inicio` DATE DEFAULT NULL,
 CHANGE `dat_fim` `dat_fim` DATE DEFAULT NULL,
 CHANGE `dat_eleicao` `dat_eleicao` DATE DEFAULT NULL;

UPDATE `legislatura` SET `dat_eleicao` = NULL WHERE `dat_eleicao`= 0000-00-00;


-- Compatibiliza tabela 'comissao' com MySQL 5.7

ALTER TABLE  `comissao`
 CHANGE `dat_criacao` `dat_criacao` DATE NOT NULL;


-- Compatibiliza tabela 'proposicao' com MySQL 5.7

ALTER TABLE  `proposicao`
 CHANGE `dat_envio` `dat_envio` varchar(20) DEFAULT NULL;

UPDATE `proposicao` SET `dat_envio` = NULL WHERE `dat_envio`= '0000-00-00 00:00:00';

ALTER TABLE  `proposicao`
 CHANGE `dat_envio` `dat_envio` DATETIME DEFAULT NULL;


-- Compatibiliza tabela 'sessao_legislativa' com MySQL 5.7

ALTER TABLE  `sessao_legislativa`
 CHANGE `dat_fim` `dat_fim` DATE NOT NULL;


-- Cria Tabela "cargo_executivo"

CREATE TABLE `cargo_executivo` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `cargo_executivo` (`cod_cargo`, `des_cargo`, `ind_excluido`) VALUES ('1', 'Prefeito ', '0');
INSERT INTO `cargo_executivo` (`cod_cargo`, `des_cargo`, `ind_excluido`) VALUES ('2', 'Vice-prefeito', '0');

-- Cria Tabela "composicao_executivo"

CREATE TABLE `composicao_executivo` (
  `cod_composicao` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` tinyint(4) NOT NULL,
  `nom_completo` varchar(50) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `dat_inicio_mandato` date DEFAULT NULL,
  `dat_fim_mandato` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
   PRIMARY KEY (`cod_composicao`),
   KEY `num_legislatura` (`num_legislatura`),
   KEY `cod_cargo` (`cod_cargo`),
   KEY `cod_partido` (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


-- Adiciona campo responsável pela unidade - tabela de vinculo de usuários com unidades
ALTER TABLE `usuario_unid_tram` ADD `ind_responsavel` TINYINT(4) NOT NULL DEFAULT '0' AFTER `cod_unid_tramitacao`;


-- Corrige num_ordem tabelas sessão

ALTER TABLE `expediente_materia` CHANGE `num_ordem` `num_ordem` INT(10) NULL DEFAULT NULL;

ALTER TABLE `materia_apresentada_sessao` CHANGE `num_ordem` `num_ordem` INT(10) NULL DEFAULT NULL;

ALTER TABLE `ordem_dia` CHANGE `num_ordem` `num_ordem` INT(10) NULL DEFAULT NULL;


-- 17/02/2017

-- Natureza de matérias 
ALTER TABLE `tipo_materia_legislativa` ADD `tip_natureza` CHAR(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL AFTER `des_tipo_materia`;

-- Corrige datas zeradas no cadastro das matérias
UPDATE materia_legislativa SET dat_apresentacao = NULL WHERE `dat_apresentacao` = 0000-00-00

-- Adiciona coluna para matéria prncipal no cadastro de matérias acessórias
ALTER TABLE `materia_legislativa` ADD `cod_materia_principal` INT(11) NULL DEFAULT NULL AFTER `cod_situacao`, ADD INDEX `idx_mat_principal` (`cod_materia_principal`);

-- Adiciona coluna para proposições permitidas por tipo de autor
ALTER TABLE `tipo_autor` ADD `tip_proposicao` VARCHAR(32) NULL DEFAULT NULL AFTER `des_tipo_autor`;

-- 20/02/2017 

-- Desfragmentar tabela 
ALTER TABLE `documento_administrativo` ENGINE = InnoDB;

-- Adiciona tabela documento_administrativo_materia

CREATE TABLE `documento_administrativo_materia` ( 
   `cod_vinculo` INT(11) NOT NULL AUTO_INCREMENT ,
   `cod_documento` INT(11) NOT NULL ,
   `cod_materia` INT(11) NOT NULL ,
   `ind_excluido` TINYINT(4) NOT NULL , 
   PRIMARY KEY (`cod_vinculo`), 
   INDEX `idx_cod_documento` (`cod_documento`), 
   INDEX `idx_cod_materia` (`cod_materia`)) ENGINE = InnoDB;

-- 21/06/2017 

-- Adiciona campos para workflow básico na tabela unidade_tramitacao

ALTER TABLE `unidade_tramitacao` ADD `unid_dest_permitidas` VARCHAR(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL AFTER `cod_parlamentar`;

ALTER TABLE `unidade_tramitacao` ADD `status_permitidos` VARCHAR(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL AFTER `unid_dest_permitidas`;
