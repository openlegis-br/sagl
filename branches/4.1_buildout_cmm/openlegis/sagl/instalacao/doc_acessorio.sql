ALTER TABLE `relatoria` CHANGE `dat_desig_relator` `dat_desig_relator` DATETIME NOT NULL;

ALTER TABLE `documento_acessorio_administrativo` CHANGE `dat_documento` `dat_documento` DATETIME NULL DEFAULT NULL;

ALTER TABLE `documento_acessorio` CHANGE `dat_documento` `dat_documento` DATETIME NULL DEFAULT NULL;

ALTER TABLE `documento_acessorio_administrativo` ADD FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo`(`cod_documento`) ON DELETE RESTRICT ON UPDATE NO ACTION;

ALTER TABLE `documento_acessorio_administrativo` ADD FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo`(`tip_documento`) ON DELETE RESTRICT ON UPDATE NO ACTION;

ALTER TABLE `documento_acessorio` ADD FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa`(`cod_materia`) ON DELETE RESTRICT ON UPDATE NO ACTION;

ALTER TABLE `documento_acessorio` ADD FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento`(`tip_documento`) ON DELETE RESTRICT ON UPDATE NO ACTION;

ALTER TABLE `documento_administrativo` ADD FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo`(`tip_documento`) ON DELETE RESTRICT ON UPDATE NO ACTION;

ALTER TABLE `documento_acessorio` ADD `ind_publico` TINYINT NOT NULL DEFAULT '1' AFTER `txt_indexacao`, ADD INDEX `ind_publico` (`ind_publico`);

