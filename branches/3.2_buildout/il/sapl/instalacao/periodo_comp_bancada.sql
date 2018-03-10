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

-- Ajusta indices

ALTER TABLE emenda DROP INDEX idx_numemen_materia; 

ALTER TABLE emenda ADD KEY `idx_emenda` (cod_emenda,tip_emenda,cod_materia) USING BTREE;

ALTER TABLE substitutivo DROP INDEX idx_numsub_materia; 

ALTER TABLE substitutivo ADD KEY `idx_substitutivo` (cod_substitutivo,cod_materia) USING BTREE;

ALTER TABLE substitutivo CHANGE `txt_ementa` `txt_ementa` TEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

ALTER TABLE substitutivo CHANGE `txt_observacao` `txt_observacao` TEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;

