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


