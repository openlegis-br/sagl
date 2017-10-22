-- 15/08/2017
-- Estrutura de armazenamento para módulo de cadastro de visitantes

CREATE TABLE `logradouro` (
  `cod_logradouro` int(11) NOT NULL,
  `nom_logradouro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `logradouro`
  ADD PRIMARY KEY (`cod_logradouro`),
  ADD KEY `num_cep` (`num_cep`),
  ADD KEY `cod_localidade` (`cod_localidade`);
ALTER TABLE `logradouro` ADD FULLTEXT KEY `nom_logradouro` (`nom_logradouro`);

ALTER TABLE `logradouro`
  MODIFY `cod_logradouro` int(11) NOT NULL AUTO_INCREMENT;



CREATE TABLE `funcionario` (
  `cod_funcionario` int(11) NOT NULL,
  `nom_funcionario` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cod_usuario` int(11) DEFAULT NULL,
  `des_cargo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_cadastro` date NOT NULL,
  `ind_ativo` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`cod_funcionario`),
  ADD INDEX(`cod_usuario`);

ALTER TABLE `funcionario`
  MODIFY `cod_funcionario` int(11) NOT NULL AUTO_INCREMENT;



CREATE TABLE `pessoa` (
  `cod_pessoa` int(11) NOT NULL,
  `nom_pessoa` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `doc_identidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `sex_pessoa` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estado_civil` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_conjuge` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dependentes` tinytext COLLATE utf8_unicode_ci,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_logradouro` int(11) DEFAULT NULL,
  `end_residencial` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `num_imovel` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `num_cep` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nom_cidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_tempo_residencia` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_celular` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_local_trabalho` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `dat_atualizacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`cod_pessoa`),
  ADD KEY `num_cep` (`num_cep`),
  ADD KEY `cod_logradouro` (`cod_logradouro`),
  ADD KEY `nom_cidade` (`nom_cidade`),
  ADD KEY `dat_nascimento` (`dat_nascimento`),
  ADD KEY `des_profissao` (`des_profissao`),
  ADD KEY `des_estado_civil` (`des_estado_civil`),
  ADD KEY `sex_visitante` (`sex_pessoa`),
  ADD KEY `nom_bairro` (`nom_bairro`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_pessoa` (`nom_pessoa`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_conjuge` (`nom_conjuge`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `idx_busca` (`doc_identidade`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `end_residencial` (`end_residencial`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `doc_identidade` (`doc_identidade`);

ALTER TABLE `pessoa`
  MODIFY `cod_pessoa` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `pessoa` ADD `txt_complemento` VARCHAR(50) NULL DEFAULT NULL AFTER `num_imovel`;

ALTER TABLE `pessoa` ADD `sgl_uf` VARCHAR(2) NULL DEFAULT NULL AFTER `nom_cidade`;



CREATE TABLE `visita` (
  `cod_visita` int(11) NOT NULL,
  `cod_pessoa` int(11) NOT NULL,
  `dat_entrada` datetime NOT NULL,
  `cod_funcionario` int(11) NOT NULL,
  `num_cracha` int(11) DEFAULT NULL,
  `dat_saida` datetime DEFAULT NULL,
  `txt_atendimento` text COLLATE utf8_unicode_ci,
  `des_situacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_solucao` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `visita`
  ADD PRIMARY KEY (`cod_visita`),
  ADD KEY `cod_funcionario` (`cod_funcionario`),
  ADD KEY `cod_pessoa` (`cod_pessoa`) USING BTREE,
  ADD KEY `dat_entrada` (`dat_entrada`),
  ADD KEY `des_situacao` (`des_situacao`);

ALTER TABLE `visita`
  MODIFY `cod_visita` int(11) NOT NULL AUTO_INCREMENT;



CREATE TABLE `sessao_plenaria_painel` (
  `cod_item` int(11) NOT NULL,
  `tip_item` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `nom_fase` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_ordem` int(11) NOT NULL,
  `txt_exibicao` text COLLATE utf8_unicode_ci NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `txt_autoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_turno` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_extrapauta` tinyint(4) DEFAULT '0',
  `ind_exibicao` tinyint(4) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `sessao_plenaria_painel`
  ADD PRIMARY KEY (`cod_item`),
  ADD UNIQUE KEY `ind_cod_materia` (`cod_materia`);

ALTER TABLE `sessao_plenaria_painel`
  MODIFY `cod_item` int(11) NOT NULL AUTO_INCREMENT;
