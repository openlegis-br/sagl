CREATE TABLE `documento_comissao` (
  `cod_documento` int(11) NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `dat_documento` date NOT NULL,
  `txt_descricao` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


ALTER TABLE `documento_comissao`
  ADD PRIMARY KEY (`cod_documento`),
  ADD KEY `cod_comissao` (`cod_comissao`);
ALTER TABLE `documento_comissao` ADD FULLTEXT KEY `txt_descricao` (`txt_descricao`);


ALTER TABLE `documento_comissao`
  MODIFY `cod_documento` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `documento_comissao`
  ADD CONSTRAINT `documento_comissao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION;
