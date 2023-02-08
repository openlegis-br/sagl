ALTER TABLE `documento_administrativo` ADD `cod_assunto` INT NULL AFTER `cod_situacao`;

ALTER TABLE `documento_acessorio` CHANGE `nom_documento` `nom_documento` VARCHAR(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL;

UPDATE assinatura_storage SET pdf_location = 'sapl_documentos/peticao/', storage_path='sapl_documentos.peticao' WHERE tip_documento = 'peticao';

ALTER TABLE `usuario` ADD `ind_ativo` INT NOT NULL DEFAULT '1' AFTER `txt_observacao`, ADD INDEX `ind_ativo` (`ind_ativo`);


CREATE TABLE `tipo_peticionamento` (
  `tip_peticionamento` int NOT NULL,
  `des_tipo_peticionamento` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `ind_norma` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ind_doc_adm` char(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ind_doc_materia` char(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tip_derivado` int NOT NULL,
  `cod_unid_tram_dest` int NOT NULL,
  `ind_excluido` tinyint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `tipo_peticionamento`
  ADD PRIMARY KEY (`tip_peticionamento`),
  ADD KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`);

ALTER TABLE `tipo_peticionamento`
  MODIFY `tip_peticionamento` int NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_peticionamento`
  ADD CONSTRAINT `tipo_peticionamento_ibfk_1` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON DELETE RESTRICT;

CREATE TABLE `peticao` (
  `cod_peticao` int NOT NULL,
  `tip_peticionamento` int NOT NULL,
  `txt_descricao` varchar(400) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cod_usuario` int NOT NULL,
  `cod_materia` int DEFAULT NULL,
  `cod_doc_acessorio` int DEFAULT NULL,
  `cod_documento` int DEFAULT NULL,
  `cod_documento_vinculado` int DEFAULT NULL,
  `cod_norma` int DEFAULT NULL,
  `num_norma` int DEFAULT NULL,
  `ano_norma` int DEFAULT NULL,
  `dat_norma` date DEFAULT NULL,
  `dat_envio` datetime DEFAULT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `num_protocolo` int DEFAULT NULL,
  `txt_observacao` mediumtext COLLATE utf8mb4_unicode_ci,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ind_excluido` tinyint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `peticao`
  ADD PRIMARY KEY (`cod_peticao`),
  ADD KEY `cod_usuario` (`cod_usuario`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `cod_documento` (`cod_documento`),
  ADD KEY `cod_doc_acessorio` (`cod_doc_acessorio`),
  ADD KEY `cod_norma` (`cod_norma`),
  ADD KEY `num_protocolo` (`num_protocolo`),
  ADD KEY `dat_envio` (`dat_envio`),
  ADD KEY `dat_recebimento` (`dat_recebimento`),
  ADD KEY `ind_excluido` (`ind_excluido`),
  ADD KEY `num_norma` (`num_norma`),
  ADD KEY `dat_norma` (`dat_norma`),
  ADD KEY `tip_peticionamento` (`tip_peticionamento`) USING BTREE,
  ADD KEY `cod_documento_vinculado` (`cod_documento_vinculado`);

ALTER TABLE `peticao`
  MODIFY `cod_peticao` int NOT NULL AUTO_INCREMENT;

ALTER TABLE `peticao`
  ADD CONSTRAINT `peticao_ibfk_1` FOREIGN KEY (`tip_peticionamento`) REFERENCES `tipo_peticionamento` (`tip_peticionamento`) ON DELETE RESTRICT,
  ADD CONSTRAINT `peticao_ibfk_2` FOREIGN KEY (`cod_usuario`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT,
  ADD CONSTRAINT `peticao_ibfk_3` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE RESTRICT,
  ADD CONSTRAINT `peticao_ibfk_4` FOREIGN KEY (`cod_doc_acessorio`) REFERENCES `documento_acessorio` (`cod_documento`) ON DELETE RESTRICT,
  ADD CONSTRAINT `peticao_ibfk_5` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE RESTRICT,
  ADD CONSTRAINT `peticao_ibfk_7` FOREIGN KEY (`cod_documento_vinculado`) REFERENCES `documento_administrativo` (`cod_documento`) ON DELETE RESTRICT ON UPDATE RESTRICT;

