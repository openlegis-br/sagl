SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
CREATE TABLE `listaAutores` (
`cod_autor` varchar(11)
,`nom_autor_join` varchar(100)
);
CREATE TABLE `listaComissoes` (
`cod_comissao` int(11)
,`sgl_comissao` varchar(10)
,`nom_comissao` varchar(100)
,`dat_criacao` date
,`dat_extincao` date
,`tipo_comissao` varchar(50)
);
CREATE TABLE `listaMembrosComissoes` (
`cod_comissao` int(11)
,`nom_comissao` varchar(100)
,`cod_parlamentar` int(11)
,`nom_completo` varchar(50)
,`nom_parlamentar` varchar(50)
,`des_cargo` varchar(50)
,`ind_titular` tinyint(4)
,`dat_designacao` varchar(10)
,`dat_desligamento` varchar(10)
,`des_motivo_desligamento` varchar(150)
,`obs_composicao` varchar(150)
);
CREATE TABLE `mesaAtual` (
`cod_parlamentar` int(11)
,`des_cargo` varchar(50)
,`nom_parlamentar` varchar(50)
,`nom_completo` varchar(50)
,`sgl_partido` varchar(9)
,`foto_parlamentar` varchar(108)
,`end_email` varchar(100)
);
CREATE TABLE `vereadoresAtuais` (
`cod_parlamentar` int(11)
,`nom_parlamentar` varchar(50)
,`nom_completo` varchar(50)
,`sgl_partido` varchar(9)
,`foto_parlamentar` varchar(108)
,`end_email` varchar(100)
,`num_legislatura` int(11)
,`dat_inicio_mandato` date
,`dat_fim_mandato` date
,`ind_titular` tinyint(4)
);
DROP TABLE IF EXISTS `listaAutores`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `listaAutores`  AS  select distinct replace(`autor`.`cod_autor`,'L','') AS `cod_autor`,if((`tipo_autor`.`des_tipo_autor` = 'Parlamentar'),`parlamentar`.`nom_parlamentar`,if((`tipo_autor`.`des_tipo_autor` = 'Bancada'),concat(`bancada`.`nom_bancada`,' (',convert(date_format(`legislatura`.`dat_inicio`,'%Y') using utf8),'-',convert(date_format(`legislatura`.`dat_fim`,'%Y') using utf8),')'),if((`tipo_autor`.`des_tipo_autor` = 'Comissao'),`comissao`.`nom_comissao`,`autor`.`nom_autor`))) AS `nom_autor_join` from (`tipo_autor` join ((((`autor` left join `parlamentar` on(((`autor`.`cod_parlamentar` = `parlamentar`.`cod_parlamentar`) and (`parlamentar`.`ind_excluido` = 0)))) left join `comissao` on(((`autor`.`cod_comissao` = `comissao`.`cod_comissao`) and (`comissao`.`ind_excluido` = 0)))) left join `bancada` on(((`autor`.`cod_bancada` = `bancada`.`cod_bancada`) and (`bancada`.`ind_excluido` = 0)))) left join `legislatura` on((`bancada`.`num_legislatura` = `legislatura`.`num_legislatura`)))) where ((((`parlamentar`.`cod_parlamentar` is not null) and (`tipo_autor`.`des_tipo_autor` = 'Parlamentar')) or ((`bancada`.`cod_bancada` is not null) and (`tipo_autor`.`des_tipo_autor` = 'Bancada')) or ((`comissao`.`cod_comissao` is not null) and (`tipo_autor`.`des_tipo_autor` = 'Comissao')) or ((`tipo_autor`.`des_tipo_autor` <> 'Parlamentar') and (`tipo_autor`.`des_tipo_autor` <> 'Bancada') and (`tipo_autor`.`des_tipo_autor` <> 'Comissao'))) and (`autor`.`ind_excluido` = 0) and (`autor`.`tip_autor` = `tipo_autor`.`tip_autor`)) order by `nom_autor_join` ;
DROP TABLE IF EXISTS `listaComissoes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `listaComissoes`  AS  select `c`.`cod_comissao` AS `cod_comissao`,`c`.`sgl_comissao` AS `sgl_comissao`,`c`.`nom_comissao` AS `nom_comissao`,`c`.`dat_criacao` AS `dat_criacao`,`c`.`dat_extincao` AS `dat_extincao`,`tc`.`nom_tipo_comissao` AS `tipo_comissao` from (`comissao` `c` left join `tipo_comissao` `tc` on((`c`.`tip_comissao` = `tc`.`tip_comissao`))) where ((`c`.`ind_excluido` = 0) and (`tc`.`ind_excluido` = 0)) order by `c`.`nom_comissao` ;
DROP TABLE IF EXISTS `listaMembrosComissoes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `listaMembrosComissoes`  AS  select `cp`.`cod_comissao` AS `cod_comissao`,`c`.`nom_comissao` AS `nom_comissao`,`cp`.`cod_parlamentar` AS `cod_parlamentar`,`p`.`nom_completo` AS `nom_completo`,`p`.`nom_parlamentar` AS `nom_parlamentar`,`cc`.`des_cargo` AS `des_cargo`,`cp`.`ind_titular` AS `ind_titular`,date_format(`cp`.`dat_designacao`,'%d/%m/%Y') AS `dat_designacao`,date_format(`cp`.`dat_desligamento`,'%d/%m/%Y') AS `dat_desligamento`,`cp`.`des_motivo_desligamento` AS `des_motivo_desligamento`,`cp`.`obs_composicao` AS `obs_composicao` from ((((`periodo_comp_comissao` `pc` left join `composicao_comissao` `cp` on((`cp`.`cod_periodo_comp` = `pc`.`cod_periodo_comp`))) left join `cargo_comissao` `cc` on((`cp`.`cod_cargo` = `cc`.`cod_cargo`))) left join `parlamentar` `p` on((`cp`.`cod_parlamentar` = `p`.`cod_parlamentar`))) left join `comissao` `c` on((`cp`.`cod_comissao` = `c`.`cod_comissao`))) where ((cast(now() as date) >= `pc`.`dat_inicio_periodo`) and (cast(now() as date) <= `pc`.`dat_fim_periodo`) and (`pc`.`ind_excluido` = 0) and (`cp`.`ind_excluido` = 0)) order by `c`.`nom_comissao`,`cc`.`cod_cargo` ;
DROP TABLE IF EXISTS `mesaAtual`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `mesaAtual`  AS  select `cm`.`cod_parlamentar` AS `cod_parlamentar`,`cme`.`des_cargo` AS `des_cargo`,`p`.`nom_parlamentar` AS `nom_parlamentar`,`p`.`nom_completo` AS `nom_completo`,`pr`.`sgl_partido` AS `sgl_partido`,concat('https://publico.camararibeiraopreto.sp.gov.br/sapl_documentos/parlamentar/fotos/',`p`.`cod_parlamentar`,'_foto_parlamentar') AS `foto_parlamentar`,`p`.`end_email` AS `end_email` from (((((`composicao_mesa` `cm` left join `periodo_comp_mesa` `pm` on((`cm`.`cod_periodo_comp` = `pm`.`cod_periodo_comp`))) left join `cargo_mesa` `cme` on((`cm`.`cod_cargo` = `cme`.`cod_cargo`))) left join `parlamentar` `p` on((`cm`.`cod_parlamentar` = `p`.`cod_parlamentar`))) left join `filiacao` `f` on((`f`.`cod_parlamentar` = `p`.`cod_parlamentar`))) left join `partido` `pr` on((`f`.`cod_partido` = `pr`.`cod_partido`))) where ((cast(now() as date) >= `pm`.`dat_inicio_periodo`) and (cast(now() as date) <= `pm`.`dat_fim_periodo`) and (cast(now() as date) >= `f`.`dat_filiacao`) and isnull(`f`.`dat_desfiliacao`)) order by `cm`.`cod_cargo` ;
DROP TABLE IF EXISTS `vereadoresAtuais`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vereadoresAtuais`  AS  select `p`.`cod_parlamentar` AS `cod_parlamentar`,`p`.`nom_parlamentar` AS `nom_parlamentar`,`p`.`nom_completo` AS `nom_completo`,`pr`.`sgl_partido` AS `sgl_partido`,concat('https://publico.camararibeiraopreto.sp.gov.br/sapl_documentos/parlamentar/fotos/',`p`.`cod_parlamentar`,'_foto_parlamentar') AS `foto_parlamentar`,`p`.`end_email` AS `end_email`,`l`.`num_legislatura` AS `num_legislatura`,`m`.`dat_inicio_mandato` AS `dat_inicio_mandato`,`m`.`dat_fim_mandato` AS `dat_fim_mandato`,`m`.`ind_titular` AS `ind_titular` from ((((`mandato` `m` left join `legislatura` `l` on((`m`.`num_legislatura` = `l`.`num_legislatura`))) left join `parlamentar` `p` on((`m`.`cod_parlamentar` = `p`.`cod_parlamentar`))) left join `filiacao` `f` on((`f`.`cod_parlamentar` = `p`.`cod_parlamentar`))) left join `partido` `pr` on((`f`.`cod_partido` = `pr`.`cod_partido`))) where ((cast(now() as date) >= `l`.`dat_inicio`) and (cast(now() as date) <= `l`.`dat_fim`) and (cast(now() as date) >= `f`.`dat_filiacao`) and isnull(`f`.`dat_desfiliacao`)) group by `p`.`cod_parlamentar` order by `p`.`nom_completo` ;
COMMIT;

