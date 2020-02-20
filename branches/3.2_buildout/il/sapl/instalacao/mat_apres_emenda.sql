ALTER TABLE `materia_apresentada_sessao` DROP INDEX `cod_materia_2`;

ALTER TABLE `materia_apresentada_sessao` DROP INDEX `cod_materia`;

ALTER TABLE `materia_apresentada_sessao` ADD `cod_emenda` INT(11) NULL AFTER `cod_materia`;

ALTER TABLE `materia_apresentada_sessao` ADD INDEX(`cod_emenda`);

ALTER TABLE `materia_apresentada_sessao` ADD `cod_substitutivo` INT(11) NULL AFTER `cod_emenda`;

ALTER TABLE `materia_apresentada_sessao` ADD INDEX(`cod_substitutivo`);

ALTER TABLE `materia_apresentada_sessao` ADD `cod_doc_acessorio` INT(11) NULL AFTER `cod_substitutivo`;

ALTER TABLE `materia_apresentada_sessao` ADD INDEX(`cod_doc_acessorio`);
