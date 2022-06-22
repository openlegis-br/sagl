ALTER TABLE `parlamentar` ADD `dat_falecimento` DATE NULL AFTER `dat_nascimento`;
ALTER TABLE `parlamentar` ADD `des_curso` VARCHAR(50) NULL AFTER `cod_nivel_instrucao`;
ALTER TABLE `parlamentar` ADD `num_celular` VARCHAR(50) NULL AFTER `num_tel_resid`;

