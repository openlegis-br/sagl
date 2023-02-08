ALTER TABLE `assinatura_documento` ADD `dat_recusa` DATETIME NULL AFTER `dat_assinatura`;
ALTER TABLE `assinatura_documento` ADD `ind_recusado` TINYINT NOT NULL DEFAULT '0' AFTER `ind_assinado`;
ALTER TABLE `assinatura_documento` ADD `txt_motivo_recusa` TEXT NULL AFTER `ind_recusado`;
ALTER TABLE `assinatura_documento` ADD INDEX(`ind_assinado`);
ALTER TABLE `assinatura_documento` ADD INDEX(`ind_recusado`);

