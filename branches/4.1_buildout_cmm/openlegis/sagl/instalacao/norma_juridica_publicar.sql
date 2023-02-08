ALTER TABLE `norma_juridica` ADD `ind_publico` INT NOT NULL DEFAULT '0' AFTER `timestamp`;
UPDATE norma_juridica SET ind_publico = 1;
ALTER TABLE `norma_juridica` ADD INDEX(`ind_publico`);

