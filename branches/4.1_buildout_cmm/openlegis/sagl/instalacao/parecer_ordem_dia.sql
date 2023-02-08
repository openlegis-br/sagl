ALTER TABLE `ordem_dia` ADD `cod_parecer` INT NULL AFTER `cod_materia`, ADD INDEX `idx_cod_parecer` (`cod_parecer`);

ALTER TABLE `ordem_dia` CHANGE `cod_materia` `cod_materia` INT NULL;

ALTER TABLE `expediente_materia` DROP FOREIGN KEY `expediente_materia_ibfk_2`; ALTER TABLE `expediente_materia` ADD CONSTRAINT `expediente_materia_ibfk_2` FOREIGN KEY (`cod_parecer`) REFERENCES `relatoria`(`cod_relatoria`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `ordem_dia` ADD FOREIGN KEY (`cod_parecer`) REFERENCES `relatoria`(`cod_relatoria`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `registro_votacao` DROP FOREIGN KEY `registro_votacao_ibfk_3`; ALTER TABLE `registro_votacao` ADD CONSTRAINT `registro_votacao_ibfk_3` FOREIGN KEY (`cod_parecer`) REFERENCES `relatoria`(`cod_relatoria`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `registro_votacao` DROP FOREIGN KEY `registro_votacao_ibfk_5`; 
