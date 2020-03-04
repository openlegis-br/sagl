ALTER TABLE `relatoria` ADD `num_protocolo` INT(11) NULL AFTER `num_parecer`;
ALTER TABLE `relatoria` ADD INDEX(`num_protocolo`);

ALTER TABLE `materia_apresentada_sessao` ADD `cod_parecer` INT(11) NULL AFTER `cod_substitutivo`;
ALTER TABLE `materia_apresentada_sessao` ADD INDEX(`cod_parecer`);

ALTER TABLE `expediente_materia` ADD `cod_parecer` INT(11) NULL AFTER `cod_materia`;
ALTER TABLE `expediente_materia` ADD INDEX(`cod_parecer`);

