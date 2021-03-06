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

-- Indice tramitacao materia
ALTER TABLE materia_legislativa ADD KEY idx_tramitacao (ind_tramitacao) USING BTREE;

-- Separa unidades de tramitação adm x leg

ALTER TABLE `unidade_tramitacao` ADD `ind_leg` TINYINT(4) NULL DEFAULT '0' AFTER `cod_parlamentar`;

ALTER TABLE `unidade_tramitacao` ADD INDEX(`ind_leg`);

UPDATE unidade_tramitacao set ind_leg = 1;

ALTER TABLE `unidade_tramitacao` ADD `ind_adm` TINYINT(4) NULL DEFAULT '0' AFTER `status_permitidos`;

ALTER TABLE `unidade_tramitacao` ADD INDEX(`ind_adm`);

-- Link para album de fotos da sessão

ALTER TABLE `sessao_plenaria` ADD `url_fotos` VARCHAR(150) NULL AFTER `dat_fim_sessao`;

-- Endereço de email de órgão

ALTER TABLE `orgao` ADD `end_email` VARCHAR(100) NULL AFTER `num_tel_orgao`;

--Código de acesso externo a protocolo administrativo

ALTER TABLE `protocolo` ADD `codigo_acesso` VARCHAR(18) NULL AFTER `timestamp_anulacao`;

ALTER TABLE `protocolo` ADD INDEX(`codigo_acesso`);

ALTER TABLE `documento_administrativo` ADD INDEX(`num_protocolo`);

-- Possibilidade de Adicionar Documentos para Leitura na Sessão

ALTER TABLE `materia_apresentada_sessao` ADD `cod_documento` INT(11) NULL AFTER `cod_materia`, 
ADD INDEX `idx_cod_documento` (`cod_documento`);

ALTER TABLE `materia_apresentada_sessao` CHANGE `cod_materia` `cod_materia` INT(11) NULL;

ALTER TABLE `materia_apresentada_sessao` ADD INDEX(`cod_materia`);


