ALTER TABLE `documento_acessorio` ADD `ind_publico` TINYINT NOT NULL DEFAULT '1' AFTER `txt_indexacao`, ADD INDEX `ind_publico` (`ind_publico`);

