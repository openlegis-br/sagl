-- INSERT INTO `assinatura_storage` (`tip_documento`, `pdf_location`, `storage_path`, `pdf_file`, `pdf_signed`) VALUES ('pauta_comissao', 'sapl_documentos/reuniao_comissao/', 'sapl_documentos.reuniao_comissao', '_pauta.pdf', '_pauta_signed.pdf');

-- INSERT INTO `assinatura_storage` (`tip_documento`, `pdf_location`, `storage_path`, `pdf_file`, `pdf_signed`) VALUES ('ata_comissao', 'sapl_documentos/reuniao_comissao/', 'sapl_documentos.reuniao_comissao', '_ata.pdf', '_ata_signed.pdf');

-- INSERT INTO `assinatura_storage` (`tip_documento`, `pdf_location`, `storage_path`, `pdf_file`, `pdf_signed`) VALUES ('documento_comissao', 'sapl_documentos/documento_comissao/', 'sapl_documentos.documento_comissao', '_documento.pdf', '_documento_signed.pdf');

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Estrutura de reunião

ALTER TABLE `reuniao_comissao` ADD `txt_tema` TEXT NULL AFTER `num_reuniao`;

ALTER TABLE `reuniao_comissao` ADD `hr_fim_reuniao` VARCHAR(5) NULL DEFAULT NULL AFTER `hr_inicio_reuniao`;

ALTER TABLE `reuniao_comissao` ADD `url_video` VARCHAR(150) NULL DEFAULT NULL AFTER `txt_observacao`;

ALTER TABLE `reuniao_comissao` ADD `des_tipo_reuniao` VARCHAR(15) NOT NULL DEFAULT 'Ordinária' AFTER `num_reuniao`;

-- tabela reuniao_comissao_presenca

CREATE TABLE IF NOT EXISTS `reuniao_comissao_presenca` (
  `cod_reuniao` int NOT NULL,
  `cod_parlamentar` int NOT NULL,
  UNIQUE KEY `idx_reuniao_parlamentar` (`cod_reuniao`,`cod_parlamentar`) USING BTREE,
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_reuniao` (`cod_reuniao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


ALTER TABLE `reuniao_comissao_presenca`
  ADD CONSTRAINT `reuniao_comissao_presenca_ibfk_1` FOREIGN KEY (`cod_reuniao`) REFERENCES `reuniao_comissao` (`cod_reuniao`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE ON UPDATE RESTRICT;


-- tabela reuniao_comissao_pauta

CREATE TABLE IF NOT EXISTS `reuniao_comissao_pauta` (
  `cod_item` int NOT NULL AUTO_INCREMENT,
  `cod_reuniao` int NOT NULL,
  `num_ordem` int NOT NULL,
  `cod_materia` int DEFAULT NULL,
  `cod_emenda` int DEFAULT NULL,
  `cod_substitutivo` int DEFAULT NULL,
  `cod_parecer` int DEFAULT NULL,
  `cod_relator` int DEFAULT NULL,
  `tip_resultado_votacao` int UNSIGNED DEFAULT NULL,
  `txt_observacao` text COLLATE utf8mb4_unicode_ci,
  `ind_excluido` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_item`),
  KEY `cod_reuniao` (`cod_reuniao`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_emenda` (`cod_emenda`),
  KEY `cod_substitutivo` (`cod_substitutivo`),
  KEY `cod_parecer` (`cod_parecer`),
  KEY `cod_relator` (`cod_relator`),
  KEY `tip_resultado_votacao` (`tip_resultado_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `reuniao_comissao_pauta`
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_1` FOREIGN KEY (`cod_reuniao`) REFERENCES `reuniao_comissao` (`cod_reuniao`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_3` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_4` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_5` FOREIGN KEY (`cod_parecer`) REFERENCES `relatoria` (`cod_relatoria`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_6` FOREIGN KEY (`cod_relator`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `reuniao_comissao_pauta_ibfk_7` FOREIGN KEY (`tip_resultado_votacao`) REFERENCES `tipo_resultado_votacao` (`tip_resultado_votacao`) ON DELETE CASCADE ON UPDATE RESTRICT;
SET FOREIGN_KEY_CHECKS=1;
COMMIT;
