CREATE TABLE `liderancas_partidarias` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_partido` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;


ALTER TABLE `liderancas_partidarias`
  ADD PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  ADD UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_partido` (`cod_partido`);
