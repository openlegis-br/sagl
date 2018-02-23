CREATE TABLE `periodo_comp_bancada` (
  `cod_periodo_comp` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

ALTER TABLE `periodo_comp_bancada`
  ADD PRIMARY KEY (`cod_periodo_comp`),
  ADD KEY `ind_percompbancada_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  ADD KEY `idx_legislatura` (`num_legislatura`);

ALTER TABLE `periodo_comp_bancada`
  MODIFY `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `composicao_bancada` ADD `cod_periodo_comp` INT(11) NULL AFTER `cod_bancada`;

ALTER TABLE `composicao_bancada` ADD INDEX(`cod_periodo_comp`);

-- Status de tramitação adminatrativo - permissão por unidade

ALTER TABLE `unidade_tramitacao` ADD `status_adm_permitidos` VARCHAR(200) NULL AFTER `status_permitidos`;
