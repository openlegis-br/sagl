ALTER TABLE `protocolo` ADD `cod_materia_principal` INT(11) NULL AFTER `tip_materia`;

ALTER TABLE `protocolo` ADD INDEX(`cod_materia_principal`);

ALTER TABLE `protocolo` ADD `tip_natureza_materia` SMALLINT(1) NULL AFTER `tip_materia`;

ALTER TABLE `documento_acessorio` ADD `num_protocolo` INT(11) NULL AFTER `dat_documento`;

UPDATE protocolo SET tip_natureza_materia = 1 WHERE tip_processo = 1;
