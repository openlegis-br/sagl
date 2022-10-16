CREATE TABLE IF NOT EXISTS `usuario_tipo_documento` (
  `cod_usuario` int NOT NULL,
  `tip_documento` int NOT NULL,
  `ind_excluido` tinyint NOT NULL DEFAULT '0',
  UNIQUE KEY `PRIMARY_KEY` (`cod_usuario`,`tip_documento`),
  KEY `idx_usuario` (`cod_usuario`),
  KEY `idx_tip_documento` (`tip_documento`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `usuario_tipo_documento`
  ADD CONSTRAINT `usuario_tipo_documento_ibfk_1` FOREIGN KEY (`cod_usuario`) REFERENCES `usuario` (`cod_usuario`) ON DELETE RESTRICT,
  ADD CONSTRAINT `usuario_tipo_documento_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE tipo_peticionamento CHANGE `cod_unid_tram_dest` `cod_unid_tram_dest` INT NULL;

ALTER TABLE tipo_peticionamento DROP FOREIGN KEY tipo_peticionamento_ibfk_1`;

ALTER TABLE peticao ADD `cod_unid_tram_dest` INT NULL AFTER `txt_observacao`;


