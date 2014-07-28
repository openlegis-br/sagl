CREATE TABLE IF NOT EXISTS `assessor_parlamentar` (
  `cod_assessor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_assessor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_celular` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nomeacao` date NOT NULL,
  `dat_exoneracao` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `col_username` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_assessor`),
  UNIQUE KEY `assessor_parlamentar` (`cod_assessor`,`cod_parlamentar`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

INSERT INTO `tipo_emenda` (`tip_emenda`, `des_tipo_emenda`, `ind_excluido`) VALUES
(1, 'Aditiva', 0),
(2, 'Modificativa', 0),
(3, 'Substitutiva', 0),
(4, 'Supressiva', 0),
(5, 'Mensagem Aditiva', 0);

UPDATE emenda SET tip_emenda = 1 WHERE tip_emenda="Aditiva";

UPDATE emenda SET tip_emenda = 2 WHERE tip_emenda="Modificativa";

UPDATE emenda SET tip_emenda = 3 WHERE tip_emenda="Substitutiva";

UPDATE emenda SET tip_emenda = 4 WHERE tip_emenda="Supressiva";

UPDATE emenda SET tip_emenda = 5 WHERE tip_emenda="Mens. Aditiva";

ALTER TABLE `emenda`
   CHANGE  `tip_emenda`  `tip_emenda` INT( 11 ) NOT NULL, 
   DROP INDEX `idx_numemen_materia`, 
   ADD UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
   ADD KEY `idx_tip_emenda` (`tip_emenda`);

ALTER TABLE `subemenda` 
   CHANGE  `tip_subemenda`  `tip_subemenda` INT( 11 ) NOT NULL,
   DROP INDEX `idx_numsub_emenda`, 
   ADD UNIQUE KEY `idx_numsub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
   ADD KEY `idx_tip_subemenda` (`tip_subemenda`);


