ALTER TABLE `proposicao` ADD `cod_parecer` INT NULL AFTER `cod_substitutivo`;

ALTER TABLE `proposicao` ADD INDEX(`cod_parecer`);
