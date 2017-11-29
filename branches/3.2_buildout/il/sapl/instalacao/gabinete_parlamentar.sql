CREATE TABLE `gabinete_eleitor` (
  `cod_eleitor` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `dat_cadastro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nom_eleitor` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_eleitor` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `des_estado_civil` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `doc_identidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cpf` varchar(50) CHARACTER SET utf32 COLLATE utf32_unicode_ci DEFAULT NULL,
  `txt_classe` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_escolaridade` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `num_tit_eleitor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_bairro` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_localidade` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_uf` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_celular` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_conjuge` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dependentes` tinytext COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `des_local_trabalho` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_atualizacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


ALTER TABLE `gabinete_eleitor`
  ADD PRIMARY KEY (`cod_eleitor`),
  ADD KEY `sex_eleitor` (`sex_eleitor`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_eleitor` (`nom_eleitor`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `des_profissao` (`des_profissao`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `end_residencial` (`end_residencial`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_localidade` (`nom_localidade`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `des_local_trabalho` (`des_local_trabalho`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_bairro` (`nom_bairro`);

ALTER TABLE `gabinete_eleitor`
  MODIFY `cod_eleitor` int(11) NOT NULL AUTO_INCREMENT;


CREATE TABLE `gabinete_atendimento` (
  `cod_atendimento` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_eleitor` int(11) NOT NULL,
  `dat_atendimento` date NOT NULL,
  `txt_assunto` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `dat_resultado` date DEFAULT NULL,
  `txt_resultado` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_atendente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_status` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `gabinete_atendimento`
  ADD PRIMARY KEY (`cod_atendimento`),
  ADD KEY `idx_resultado` (`txt_resultado`) USING BTREE,
  ADD KEY `idx_eleitor` (`cod_eleitor`) USING BTREE,
  ADD KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE;
ALTER TABLE `gabinete_atendimento` ADD FULLTEXT KEY `idx_assunto` (`txt_assunto`);

ALTER TABLE `gabinete_atendimento`
  MODIFY `cod_atendimento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `gabinete_atendimento`
  ADD CONSTRAINT `gabinete_atendimento_ibfk_1` FOREIGN KEY (`cod_eleitor`) REFERENCES `gabinete_eleitor` (`cod_eleitor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `gabinete_atendimento_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE ON UPDATE CASCADE;

