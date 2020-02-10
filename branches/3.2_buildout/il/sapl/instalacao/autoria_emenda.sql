CREATE TABLE IF NOT EXISTS `autoria_emenda` (
  `cod_autor` int(11) NOT NULL,
  `cod_emenda` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`,`cod_emenda`),
  KEY `idx_autor` (`cod_autor`),
  KEY `idx_emenda` (`cod_emenda`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO autoria_emenda (cod_autor, cod_emenda, ind_excluido)
  SELECT cod_autor, cod_emenda, ind_excluido FROM emenda WHERE ind_excluido = 0;

ALTER TABLE `emenda` DROP `cod_autor`;

CREATE TABLE IF NOT EXISTS `autoria_substitutivo` (
  `cod_autor` int(11) NOT NULL,
  `cod_substitutivo` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`,`cod_substitutivo`),
  KEY `idx_autor` (`cod_autor`),
  KEY `idx_substitutivo` (`cod_substitutivo`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO autoria_substitutivo (cod_autor, cod_substitutivo, ind_excluido)
  SELECT cod_autor, cod_substitutivo, ind_excluido FROM substitutivo WHERE ind_excluido = 0;

ALTER TABLE `substitutivo` DROP `cod_autor`;
