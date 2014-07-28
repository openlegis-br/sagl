-- Tempo de Geração: 28/07/2014 às 11:23
-- Versão do servidor: 5.6.17-0ubuntu0.14.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de dados: `interlegis`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `acomp_materia`
--

CREATE TABLE IF NOT EXISTS `acomp_materia` (
  `cod_cadastro` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_hash` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cadastro`),
  UNIQUE KEY `fk_{CCECA63D-5992-437B-BCD3-D7C98DA3E926}` (`cod_materia`,`end_email`),
  KEY `cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `acomp_materia`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `afastamento`
--

CREATE TABLE IF NOT EXISTS `afastamento` (
  `cod_afastamento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_mandato` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `tip_afastamento` tinyint(4) NOT NULL,
  `dat_inicio_afastamento` date NOT NULL,
  `dat_fim_afastamento` date DEFAULT NULL,
  `cod_parlamentar_suplente` int(11) NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_afastamento`),
  KEY `idx_parlamentar_mandato` (`cod_parlamentar`,`num_legislatura`),
  KEY `idx_afastamento_datas` (`cod_parlamentar`,`dat_inicio_afastamento`,`dat_fim_afastamento`),
  KEY `idx_tip_afastamento` (`tip_afastamento`),
  KEY `idx__parlamentar_suplente` (`cod_parlamentar_suplente`,`num_legislatura`),
  KEY `cod_mandato` (`cod_mandato`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `num_legislatura` (`num_legislatura`),
  KEY `cod_parlamentar_suplente` (`cod_parlamentar_suplente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `afastamento`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_afastamento`
--       `tipo_afastamento` -> `tip_afastamento`
--   `cod_mandato`
--       `mandato` -> `cod_mandato`
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--   `cod_parlamentar_suplente`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `anexada`
--

CREATE TABLE IF NOT EXISTS `anexada` (
  `cod_materia_principal` int(11) NOT NULL,
  `cod_materia_anexada` int(11) NOT NULL,
  `dat_anexacao` date NOT NULL,
  `dat_desanexacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia_principal`,`cod_materia_anexada`),
  KEY `idx_materia_anexada` (`cod_materia_anexada`),
  KEY `idx_materia_principal` (`cod_materia_principal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `anexada`:
--   `cod_materia_anexada`
--       `materia_legislativa` -> `cod_materia`
--   `cod_materia_principal`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `assessor_parlamentar`
--

CREATE TABLE IF NOT EXISTS `assessor_parlamentar` (
  `cod_assessor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_assessor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_cargo` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
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

--
-- RELACIONAMENTOS PARA TABELAS `assessor_parlamentar`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `assunto_norma`
--

CREATE TABLE IF NOT EXISTS `assunto_norma` (
  `cod_assunto` int(4) NOT NULL AUTO_INCREMENT,
  `des_assunto` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estendida` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_assunto`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=32 ;

--
-- Fazendo dump de dados para tabela `assunto_norma`
--

INSERT INTO `assunto_norma` (`cod_assunto`, `des_assunto`, `des_estendida`, `ind_excluido`) VALUES
(1, 'Nao classificada', ' ', 1),
(10, 'Acessibilidade / Mobilidade Urbana', '  \r\n           \r\n           ', 0),
(11, 'Assistência Social', ' \r\n           ', 0),
(12, 'Autarquias', ' \r\n           ', 0),
(13, 'Calendário de Eventos / Feriados', ' \r\n           ', 0),
(14, 'Comércio / Publicidade', ' \r\n           ', 0),
(15, 'Compras / Licitações', ' \r\n           ', 0),
(16, 'Conselhos / Comissões / Fundos', ' \r\n           ', 0),
(17, 'Contratos / Convênios / Consórcios', ' \r\n           ', 0),
(18, 'Créditos Adicionais', ' \r\n           ', 0),
(19, 'Criança / Adolescente', ' \r\n           ', 0),
(20, 'Cultura / Turismo', ' \r\n           ', 0),
(21, 'Defesa Civil', ' \r\n           ', 0),
(22, 'Orçamento / PPA / LDO / LOA', ' \r\n           ', 0),
(23, 'Educação', ' \r\n           ', 0),
(24, 'Saneamento', ' \r\n           ', 0),
(25, 'Saúde', ' \r\n           ', 0),
(26, 'Utilidade Pública', ' \r\n           ', 0),
(27, 'Zoneamento Urbano', ' \r\n           ', 0),
(28, 'Segurança Pública', ' \r\n           ', 0),
(29, 'Câmara Municipal', ' \r\n           ', 0),
(30, 'Servidor Público', ' \r\n           ', 0),
(31, 'Remuneração / Vencimentos / Salários / Subsídios', ' \r\n           ', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `autor`
--

CREATE TABLE IF NOT EXISTS `autor` (
  `cod_autor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_partido` int(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_bancada` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `tip_autor` tinyint(4) NOT NULL,
  `nom_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `col_username` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`),
  KEY `idx_tip_autor` (`tip_autor`),
  KEY `idx_parlamentar` (`cod_parlamentar`),
  KEY `idx_comissao` (`cod_comissao`),
  KEY `idx_partido` (`cod_partido`),
  KEY `idx_bancada` (`cod_bancada`),
  FULLTEXT KEY `nom_autor` (`nom_autor`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=4 ;

--
-- RELACIONAMENTOS PARA TABELAS `autor`:
--   `tip_autor`
--       `tipo_autor` -> `tip_autor`
--   `cod_partido`
--       `partido` -> `cod_partido`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_bancada`
--       `bancada` -> `cod_bancada`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

--
-- Fazendo dump de dados para tabela `autor`
--

INSERT INTO `autor` (`cod_autor`, `cod_partido`, `cod_comissao`, `cod_bancada`, `cod_parlamentar`, `tip_autor`, `nom_autor`, `des_cargo`, `col_username`, `ind_excluido`) VALUES
(1, NULL, NULL, NULL, NULL, 4, 'Executivo Municipal', 'Prefeito', NULL, 0),
(2, NULL, NULL, NULL, NULL, 5, 'Mesa Diretora', 'Mesa', NULL, 0),
(3, NULL, NULL, NULL, NULL, 4, 'Iniciativa Popular', 'Cidadão', NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `autoria`
--

CREATE TABLE IF NOT EXISTS `autoria` (
  `cod_autor` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_primeiro_autor` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`,`cod_materia`),
  KEY `idx_materia` (`cod_materia`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA TABELAS `autoria`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `bancada`
--

CREATE TABLE IF NOT EXISTS `bancada` (
  `cod_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `nom_bancada` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_bancada`),
  KEY `idt_nom_bancada` (`nom_bancada`),
  KEY `idx_cod_bancada` (`ind_excluido`),
  FULLTEXT KEY `nom_bancada` (`nom_bancada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `cargo_bancada`
--

CREATE TABLE IF NOT EXISTS `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `cargo_bancada`
--

INSERT INTO `cargo_bancada` (`cod_cargo`, `des_cargo`, `ind_unico`, `ind_excluido`) VALUES
(1, 'Líder', 1, 0),
(2, 'Vice-Líder', 1, 0),
(3, 'Membro', 0, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cargo_comissao`
--

CREATE TABLE IF NOT EXISTS `cargo_comissao` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `cargo_comissao`
--

INSERT INTO `cargo_comissao` (`cod_cargo`, `des_cargo`, `ind_unico`, `ind_excluido`) VALUES
(1, 'Presidente', 1, 0),
(2, 'Membro', 0, 0),
(3, 'Suplente', 0, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cargo_mesa`
--

CREATE TABLE IF NOT EXISTS `cargo_mesa` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `cargo_mesa`
--

INSERT INTO `cargo_mesa` (`cod_cargo`, `des_cargo`, `ind_unico`, `ind_excluido`) VALUES
(1, 'Presidente', 1, 0),
(2, 'Vice-Presidente', 1, 0),
(3, '1º Secretário', 1, 0),
(4, '2º Secretário', 1, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `coligacao`
--

CREATE TABLE IF NOT EXISTS `coligacao` (
  `cod_coligacao` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `nom_coligacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_votos_coligacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_coligacao`),
  KEY `idx_legislatura` (`num_legislatura`),
  KEY `idx_coligacao_legislatura` (`num_legislatura`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `coligacao`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `comissao`
--

CREATE TABLE IF NOT EXISTS `comissao` (
  `cod_comissao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_comissao` tinyint(4) NOT NULL,
  `nom_comissao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date NOT NULL,
  `dat_extincao` date DEFAULT NULL,
  `nom_apelido_temp` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_instalacao_temp` date DEFAULT NULL,
  `dat_final_prevista_temp` date DEFAULT NULL,
  `dat_prorrogada_temp` date DEFAULT NULL,
  `dat_fim_comissao` date DEFAULT NULL,
  `nom_secretario` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_reuniao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_secretaria` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_secretaria` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax_secretaria` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_agenda_reuniao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `loc_reuniao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_finalidade` text COLLATE utf8_unicode_ci,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comissao`),
  KEY `idx_comissao_tipo` (`tip_comissao`),
  KEY `idx_comissao_nome` (`nom_comissao`),
  FULLTEXT KEY `nom_comissao` (`nom_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `comissao`:
--   `tip_comissao`
--       `tipo_comissao` -> `tip_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `composicao_bancada`
--

CREATE TABLE IF NOT EXISTS `composicao_bancada` (
  `cod_comp_bancada` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_bancada` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comp_bancada`),
  KEY `idx_cargo` (`cod_cargo`),
  KEY `idx_bancada` (`cod_bancada`),
  KEY `idx_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `composicao_bancada`:
--   `cod_cargo`
--       `cargo_bancada` -> `cod_cargo`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_bancada`
--       `bancada` -> `cod_bancada`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `composicao_coligacao`
--

CREATE TABLE IF NOT EXISTS `composicao_coligacao` (
  `cod_partido` int(11) NOT NULL,
  `cod_coligacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_partido`,`cod_coligacao`),
  KEY `idx_coligacao` (`cod_coligacao`),
  KEY `idx_partido` (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA TABELAS `composicao_coligacao`:
--   `cod_coligacao`
--       `coligacao` -> `cod_coligacao`
--   `cod_partido`
--       `partido` -> `cod_partido`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `composicao_comissao`
--

CREATE TABLE IF NOT EXISTS `composicao_comissao` (
  `cod_comp_comissao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `cod_periodo_comp` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comp_comissao`),
  KEY `idx_cargo` (`cod_cargo`),
  KEY `idx_periodo_comp` (`cod_periodo_comp`),
  KEY `idx_comissao` (`cod_comissao`),
  KEY `idx_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `composicao_comissao`:
--   `cod_cargo`
--       `cargo_comissao` -> `cod_cargo`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_periodo_comp`
--       `periodo_comp_comissao` -> `cod_periodo_comp`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `composicao_mesa`
--

CREATE TABLE IF NOT EXISTS `composicao_mesa` (
  `cod_parlamentar` int(11) NOT NULL,
  `cod_sessao_leg` int(11) DEFAULT NULL,
  `cod_periodo_comp` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_parlamentar`,`cod_periodo_comp`,`cod_cargo`),
  KEY `idx_cargo` (`cod_cargo`),
  KEY `idx_periodo_comp` (`cod_periodo_comp`),
  KEY `idx_parlamentar` (`cod_parlamentar`),
  KEY `cod_sessao_leg` (`cod_sessao_leg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `composicao_mesa`:
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_cargo`
--       `cargo_mesa` -> `cod_cargo`
--   `cod_periodo_comp`
--       `periodo_comp_mesa` -> `cod_periodo_comp`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `dependente`
--

CREATE TABLE IF NOT EXISTS `dependente` (
  `cod_dependente` int(11) NOT NULL AUTO_INCREMENT,
  `tip_dependente` tinyint(4) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_dependente` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_dependente`),
  KEY `idx_dep_parlam` (`tip_dependente`,`cod_parlamentar`,`ind_excluido`),
  KEY `idx_dependente` (`tip_dependente`),
  KEY `idx_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `dependente`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_dependente`
--       `tipo_dependente` -> `tip_dependente`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `despacho_inicial`
--

CREATE TABLE IF NOT EXISTS `despacho_inicial` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) unsigned NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`,`num_ordem`),
  KEY `idx_comissao` (`cod_comissao`),
  KEY `idx_despinic_comissao` (`cod_comissao`,`ind_excluido`),
  KEY `idx_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `despacho_inicial`:
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `documento_acessorio`
--

CREATE TABLE IF NOT EXISTS `documento_acessorio` (
  `cod_documento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `tip_documento` int(11) NOT NULL,
  `nom_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_documento` date DEFAULT NULL,
  `nom_autor_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_documento`),
  KEY `idx_tip_documento` (`tip_documento`),
  KEY `idx_materia` (`cod_materia`),
  FULLTEXT KEY `idx_ementa` (`txt_ementa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `documento_acessorio`:
--   `tip_documento`
--       `tipo_documento` -> `tip_documento`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `documento_acessorio_administrativo`
--

CREATE TABLE IF NOT EXISTS `documento_acessorio_administrativo` (
  `cod_documento_acessorio` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL DEFAULT '0',
  `tip_documento` int(11) NOT NULL DEFAULT '0',
  `nom_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_arquivo` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_documento` date DEFAULT NULL,
  `nom_autor_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_documento_acessorio`),
  KEY `idx_tip_documento` (`tip_documento`),
  KEY `idx_documento` (`cod_documento`),
  KEY `idx_autor_documento` (`nom_autor_documento`),
  KEY `idx_dat_documento` (`dat_documento`),
  FULLTEXT KEY `idx_assunto` (`txt_assunto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `documento_acessorio_administrativo`:
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `documento_administrativo`
--

CREATE TABLE IF NOT EXISTS `documento_administrativo` (
  `cod_documento` int(11) NOT NULL AUTO_INCREMENT,
  `tip_documento` int(11) NOT NULL,
  `num_documento` int(11) NOT NULL,
  `ano_documento` smallint(6) NOT NULL DEFAULT '0',
  `dat_documento` date NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `txt_interessado` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_documento`),
  KEY `idx_num_ano` (`num_documento`,`ano_documento`),
  KEY `idx_dat_documento` (`dat_documento`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_documento` (`tip_documento`),
  FULLTEXT KEY `idx_txt_assunto` (`txt_assunto`),
  FULLTEXT KEY `idx_txt_autoria` (`txt_interessado`),
  FULLTEXT KEY `txt_observacao` (`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `documento_administrativo`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_documento`
--       `tipo_documento_administrativo` -> `tip_documento`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `emenda`
--

CREATE TABLE IF NOT EXISTS `emenda` (
  `cod_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_emenda` int(11) NOT NULL,
  `num_emenda` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_emenda`),
  UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_materia` (`cod_materia`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_emenda` (`tip_emenda`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `emenda`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_emenda`
--       `tipo_emenda` -> `tip_emenda`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `encerramento_presenca`
--

CREATE TABLE IF NOT EXISTS `encerramento_presenca` (
  `cod_presenca_encerramento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_encerramento`),
  UNIQUE KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `dat_ordem` (`dat_ordem`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `encerramento_presenca`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `expediente_materia`
--

CREATE TABLE IF NOT EXISTS `expediente_materia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) unsigned NOT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_votacao` int(11) unsigned NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `idx_exped_datord` (`dat_ordem`,`ind_excluido`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_materia` (`cod_materia`),
  KEY `tip_votacao` (`tip_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `expediente_materia`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `expediente_presenca`
--

CREATE TABLE IF NOT EXISTS `expediente_presenca` (
  `cod_presenca_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_expediente`),
  UNIQUE KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `dat_ordem` (`dat_ordem`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `expediente_presenca`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `expediente_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `expediente_sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_expediente` int(11) NOT NULL,
  `txt_expediente` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_expediente`),
  KEY `cod_expediente` (`cod_expediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `expediente_sessao_plenaria`:
--   `cod_expediente`
--       `tipo_expediente` -> `cod_expediente`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `filiacao`
--

CREATE TABLE IF NOT EXISTS `filiacao` (
  `dat_filiacao` date NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_partido` int(11) NOT NULL,
  `dat_desfiliacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`dat_filiacao`,`cod_parlamentar`,`cod_partido`),
  KEY `idx_partido` (`cod_partido`),
  KEY `idx_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `filiacao`:
--   `cod_partido`
--       `partido` -> `cod_partido`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `instituicao`
--

CREATE TABLE IF NOT EXISTS `instituicao` (
  `cod_instituicao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_instituicao` tinyint(4) NOT NULL,
  `nom_instituicao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_instituicao` tinytext COLLATE utf8_unicode_ci,
  `nom_bairro` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_web` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_forma_tratamento` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` tinytext COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  `dat_insercao` datetime DEFAULT NULL,
  `txt_user_insercao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_insercao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp_alteracao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `txt_user_alteracao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_alteracao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_instituicao`),
  KEY `tip_instituicao` (`tip_instituicao`),
  KEY `cod_localidade` (`cod_localidade`),
  FULLTEXT KEY `idx_nom_instituicao` (`nom_instituicao`),
  FULLTEXT KEY `idx_nom_responsavel` (`nom_responsavel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `instituicao`:
--   `cod_localidade`
--       `localidade` -> `cod_localidade`
--   `tip_instituicao`
--       `tipo_instituicao` -> `tip_instituicao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `legislacao_citada`
--

CREATE TABLE IF NOT EXISTS `legislacao_citada` (
  `cod_materia` int(11) NOT NULL,
  `cod_norma` int(11) NOT NULL,
  `des_disposicoes` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_parte` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_livro` varchar(7) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_titulo` varchar(7) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_capitulo` varchar(7) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_secao` varchar(7) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_subsecao` varchar(7) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_artigo` varchar(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_paragrafo` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_inciso` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_alinea` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_item` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`,`cod_norma`),
  KEY `cod_norma` (`cod_norma`),
  KEY `cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `legislacao_citada`:
--   `cod_norma`
--       `norma_juridica` -> `cod_norma`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `legislatura`
--

CREATE TABLE IF NOT EXISTS `legislatura` (
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_eleicao` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`num_legislatura`),
  KEY `idx_legislatura_datas` (`dat_inicio`,`dat_fim`,`dat_eleicao`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura para tabela `lexml_registro_provedor`
--

CREATE TABLE IF NOT EXISTS `lexml_registro_provedor` (
  `cod_provedor` int(11) NOT NULL AUTO_INCREMENT,
  `id_provedor` int(11) NOT NULL,
  `nom_provedor` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_provedor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adm_email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_responsavel` int(11) DEFAULT NULL,
  `xml_provedor` longtext COLLATE utf8_unicode_ci,
  PRIMARY KEY (`cod_provedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `lexml_registro_publicador`
--

CREATE TABLE IF NOT EXISTS `lexml_registro_publicador` (
  `cod_publicador` int(11) NOT NULL AUTO_INCREMENT,
  `id_publicador` int(11) NOT NULL,
  `nom_publicador` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adm_email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sigla` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_responsavel` int(11) NOT NULL,
  PRIMARY KEY (`cod_publicador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `localidade`
--

CREATE TABLE IF NOT EXISTS `localidade` (
  `cod_localidade` int(11) NOT NULL DEFAULT '0',
  `nom_localidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_localidade_pesq` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_localidade` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_uf` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_regiao` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_localidade`),
  KEY `nom_localidade` (`nom_localidade`),
  KEY `sgl_uf` (`sgl_uf`),
  KEY `tip_localidade` (`tip_localidade`),
  FULLTEXT KEY `nom_localidade_pesq` (`nom_localidade_pesq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

--
-- Fazendo dump de dados para tabela `localidade`
--

INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(1100000, 'Rondônia', 'RONDONIA', 'U', 'RO', 'NO', 0),
(1100015, 'Alta Floresta D''oeste', 'ALTA FLORESTA D''OESTE', 'M', 'RO', 'NO', 0),
(1100023, 'Ariquemes', 'ARIQUEMES', 'M', 'RO', 'NO', 0),
(1100031, 'Cabixi', 'CABIXI', 'M', 'RO', 'NO', 0),
(1100049, 'Cacoal', 'CACOAL', 'M', 'RO', 'NO', 0),
(1100056, 'Cerejeiras', 'CEREJEIRAS', 'M', 'RO', 'NO', 0),
(1100064, 'Colorado do Oeste', 'COLORADO DO OESTE', 'M', 'RO', 'NO', 0),
(1100072, 'Corumbiara', 'CORUMBIARA', 'M', 'RO', 'NO', 0),
(1100080, 'Costa Marques', 'COSTA MARQUES', 'M', 'RO', 'NO', 0),
(1100098, 'Espigão D''oeste', 'ESPIGAO D''OESTE', 'M', 'RO', 'NO', 0),
(1100106, 'Guajará-Mirim', 'GUAJARA-MIRIM', 'M', 'RO', 'NO', 0),
(1100114, 'Jaru', 'JARU', 'M', 'RO', 'NO', 0),
(1100122, 'Ji-paraná', 'JI-PARANA', 'M', 'RO', 'NO', 0),
(1100130, 'Machadinho D''oeste', 'MACHADINHO D''OESTE', 'M', 'RO', 'NO', 0),
(1100148, 'Nova Brasilândia D''oeste', 'NOVA BRASILANDIA D''OESTE', 'M', 'RO', 'NO', 0),
(1100155, 'Ouro Preto do Oeste', 'OURO PRETO DO OESTE', 'M', 'RO', 'NO', 0),
(1100189, 'Pimenta Bueno', 'PIMENTA BUENO', 'M', 'RO', 'NO', 0),
(1100205, 'Porto Velho', 'PORTO VELHO', 'M', 'RO', 'NO', 0),
(1100254, 'Presidente Médici', 'PRESIDENTE MEDICI', 'M', 'RO', 'NO', 0),
(1100262, 'Rio Crespo', 'RIO CRESPO', 'M', 'RO', 'NO', 0),
(1100288, 'Rolim de Moura', 'ROLIM DE MOURA', 'M', 'RO', 'NO', 0),
(1100296, 'Santa Luzia D''oeste', 'SANTA LUZIA D''OESTE', 'M', 'RO', 'NO', 0),
(1100304, 'Vilhena', 'VILHENA', 'M', 'RO', 'NO', 0),
(1100320, 'São Miguel do Guaporé', 'SAO MIGUEL DO GUAPORE', 'M', 'RO', 'NO', 0),
(1100338, 'Nova Mamoré', 'NOVA MAMORE', 'M', 'RO', 'NO', 0),
(1100346, 'Alvorada D''oeste', 'ALVORADA D''OESTE', 'M', 'RO', 'NO', 0),
(1100379, 'Alto Alegre do Parecis', 'ALTO ALEGRE DO PARECIS', 'M', 'RO', 'NO', 0),
(1100403, 'Alto Paraíso', 'ALTO PARAISO', 'M', 'RO', 'NO', 0),
(1100452, 'Buritis', 'BURITIS', 'M', 'RO', 'NO', 0),
(1100502, 'Novo Horizonte do Oeste', 'NOVO HORIZONTE DO OESTE', 'M', 'RO', 'NO', 0),
(1100601, 'Cacaulândia', 'CACAULANDIA', 'M', 'RO', 'NO', 0),
(1100700, 'Campo Novo de Rondonia', 'CAMPO NOVO DE RONDONIA', 'M', 'RO', 'NO', 0),
(1100809, 'Candeias do Jamari', 'CANDEIAS DO JAMARI', 'M', 'RO', 'NO', 0),
(1100908, 'Castanheiras', 'CASTANHEIRAS', 'M', 'RO', 'NO', 0),
(1100924, 'Chupinguaia', 'CHUPINGUAIA', 'M', 'RO', 'NO', 0),
(1100940, 'Cujubim', 'CUJUBIM', 'M', 'RO', 'NO', 0),
(1101005, 'Governador Jorge Teixeira', 'GOVERNADOR JORGE TEIXEIRA', 'M', 'RO', 'NO', 0),
(1101104, 'Itapuã do Oeste', 'ITAPUA DO OESTE', 'M', 'RO', 'NO', 0),
(1101203, 'Ministro Andreazza', 'MINISTRO ANDREAZZA', 'M', 'RO', 'NO', 0),
(1101302, 'Mirante da Serra', 'MIRANTE DA SERRA', 'M', 'RO', 'NO', 0),
(1101401, 'Monte Negro', 'MONTE NEGRO', 'M', 'RO', 'NO', 0),
(1101435, 'Nova União', 'NOVA UNIAO', 'M', 'RO', 'NO', 0),
(1101450, 'Parecis', 'PARECIS', 'M', 'RO', 'NO', 0),
(1101468, 'Pimenteiras do Oeste', 'PIMENTEIRAS DO OESTE', 'M', 'RO', 'NO', 0),
(1101476, 'Primavera de Rondônia', 'PRIMAVERA DE RONDONIA', 'M', 'RO', 'NO', 0),
(1101484, 'São Felipe D''Oeste', 'SAO FELIPE D''OESTE', 'M', 'RO', 'NO', 0),
(1101492, 'São Francisco do Guaporé', 'SAO FRANCISCO DO GUAPORE', 'M', 'RO', 'NO', 0),
(1101500, 'Seringueiras', 'SERINGUEIRAS', 'M', 'RO', 'NO', 0),
(1101559, 'Teixeirópolis', 'TEIXEIROPOLIS', 'M', 'RO', 'NO', 0),
(1101609, 'Theobroma', 'THEOBROMA', 'M', 'RO', 'NO', 0),
(1101708, 'Urupá', 'URUPA', 'M', 'RO', 'NO', 0),
(1101757, 'Vale do Anari', 'VALE DO ANARI', 'M', 'RO', 'NO', 0),
(1101807, 'Vale do Paraíso', 'VALE DO PARAISO', 'M', 'RO', 'NO', 0),
(1200000, 'Acre', 'ACRE', 'U', 'AC', 'NO', 0),
(1200013, 'Acrelândia', 'ACRELANDIA', 'M', 'AC', 'NO', 0),
(1200054, 'Assis Brasil', 'ASSIS BRASIL', 'M', 'AC', 'NO', 0),
(1200104, 'Brasiléia', 'BRASILEIA', 'M', 'AC', 'NO', 0),
(1200138, 'Bujari', 'BUJARI', 'M', 'AC', 'NO', 0),
(1200179, 'Capixaba', 'CAPIXABA', 'M', 'AC', 'NO', 0),
(1200203, 'Cruzeiro do Sul', 'CRUZEIRO DO SUL', 'M', 'AC', 'NO', 0),
(1200252, 'Epitaciolândia', 'EPITACIOLANDIA', 'M', 'AC', 'NO', 0),
(1200302, 'Feijó', 'FEIJO', 'M', 'AC', 'NO', 0),
(1200328, 'Jordão', 'JORDAO', 'M', 'AC', 'NO', 0),
(1200336, 'Mâncio Lima', 'MANCIO LIMA', 'M', 'AC', 'NO', 0),
(1200344, 'Manoel Urbano', 'MANOEL URBANO', 'M', 'AC', 'NO', 0),
(1200351, 'Marechal Thaumaturgo', 'MARECHAL THAUMATURGO', 'M', 'AC', 'NO', 0),
(1200385, 'Plácido de Castro', 'PLACIDO DE CASTRO', 'M', 'AC', 'NO', 0),
(1200393, 'Porto Walter', 'PORTO WALTER', 'M', 'AC', 'NO', 0),
(1200401, 'Rio Branco', 'RIO BRANCO', 'M', 'AC', 'NO', 0),
(1200427, 'Rodrigues Alves', 'RODRIGUES ALVES', 'M', 'AC', 'NO', 0),
(1200435, 'Santa Rosa do Purus', 'SANTA ROSA DO PURUS', 'M', 'AC', 'NO', 0),
(1200450, 'Senador Guiomard', 'SENADOR GUIOMARD', 'M', 'AC', 'NO', 0),
(1200500, 'Sena Madureira', 'SENA MADUREIRA', 'M', 'AC', 'NO', 0),
(1200609, 'Tarauacá', 'TARAUACA', 'M', 'AC', 'NO', 0),
(1200708, 'Xapuri', 'XAPURI', 'M', 'AC', 'NO', 0),
(1200807, 'Porto Acre', 'PORTO ACRE', 'M', 'AC', 'NO', 0),
(1300000, 'Amazonas', 'AMAZONAS', 'U', 'AM', 'NO', 0),
(1300029, 'Alvarães', 'ALVARAES', 'M', 'AM', 'NO', 0),
(1300060, 'Amaturá', 'AMATURA', 'M', 'AM', 'NO', 0),
(1300086, 'Anamã', 'ANAMA', 'M', 'AM', 'NO', 0),
(1300102, 'Anori', 'ANORI', 'M', 'AM', 'NO', 0),
(1300144, 'Apuí', 'APUI', 'M', 'AM', 'NO', 0),
(1300201, 'Atalaia do Norte', 'ATALAIA DO NORTE', 'M', 'AM', 'NO', 0),
(1300300, 'Autazes', 'AUTAZES', 'M', 'AM', 'NO', 0),
(1300409, 'Barcelos', 'BARCELOS', 'M', 'AM', 'NO', 0),
(1300508, 'Barreirinha', 'BARREIRINHA', 'M', 'AM', 'NO', 0),
(1300607, 'Benjamin Constant', 'BENJAMIN CONSTANT', 'M', 'AM', 'NO', 0),
(1300631, 'Beruri', 'BERURI', 'M', 'AM', 'NO', 0),
(1300680, 'Boa Vista do Ramos', 'BOA VISTA DO RAMOS', 'M', 'AM', 'NO', 0),
(1300706, 'Boca do Acre', 'BOCA DO ACRE', 'M', 'AM', 'NO', 0),
(1300805, 'Borba', 'BORBA', 'M', 'AM', 'NO', 0),
(1300839, 'Caapiranga', 'CAAPIRANGA', 'M', 'AM', 'NO', 0),
(1300904, 'Canutama', 'CANUTAMA', 'M', 'AM', 'NO', 0),
(1301001, 'Carauari', 'CARAUARI', 'M', 'AM', 'NO', 0),
(1301100, 'Careiro', 'CAREIRO', 'M', 'AM', 'NO', 0),
(1301159, 'Careiro da Varzea', 'CAREIRO DA VARZEA', 'M', 'AM', 'NO', 0),
(1301209, 'Coari', 'COARI', 'M', 'AM', 'NO', 0),
(1301308, 'Codajás', 'CODAJAS', 'M', 'AM', 'NO', 0),
(1301407, 'Eirunepé', 'EIRUNEPE', 'M', 'AM', 'NO', 0),
(1301506, 'Envira', 'ENVIRA', 'M', 'AM', 'NO', 0),
(1301605, 'Fonte Boa', 'FONTE BOA', 'M', 'AM', 'NO', 0),
(1301654, 'Guajará', 'GUAJARA', 'M', 'AM', 'NO', 0),
(1301704, 'Humaitá', 'HUMAITA', 'M', 'AM', 'NO', 0),
(1301803, 'Ipixuna', 'IPIXUNA', 'M', 'AM', 'NO', 0),
(1301852, 'Iranduba', 'IRANDUBA', 'M', 'AM', 'NO', 0),
(1301902, 'Itacoatiara', 'ITACOATIARA', 'M', 'AM', 'NO', 0),
(1301951, 'Itamarati', 'ITAMARATI', 'M', 'AM', 'NO', 0),
(1302009, 'Itapiranga', 'ITAPIRANGA', 'M', 'AM', 'NO', 0),
(1302108, 'Japurá', 'JAPURA', 'M', 'AM', 'NO', 0),
(1302207, 'Juruá', 'JURUA', 'M', 'AM', 'NO', 0),
(1302306, 'Jutaí', 'JUTAI', 'M', 'AM', 'NO', 0),
(1302405, 'Lábrea', 'LABREA', 'M', 'AM', 'NO', 0),
(1302504, 'Manacapuru', 'MANACAPURU', 'M', 'AM', 'NO', 0),
(1302553, 'Manaquiri', 'MANAQUIRI', 'M', 'AM', 'NO', 0),
(1302603, 'Manaus', 'MANAUS', 'M', 'AM', 'NO', 0),
(1302702, 'Manicoré', 'MANICORE', 'M', 'AM', 'NO', 0),
(1302801, 'Maraã', 'MARAA', 'M', 'AM', 'NO', 0),
(1302900, 'Maués', 'MAUES', 'M', 'AM', 'NO', 0),
(1303007, 'Nhamundá', 'NHAMUNDA', 'M', 'AM', 'NO', 0),
(1303106, 'Nova Olinda do Norte', 'NOVA OLINDA DO NORTE', 'M', 'AM', 'NO', 0),
(1303205, 'Novo Airão', 'NOVO AIRAO', 'M', 'AM', 'NO', 0),
(1303304, 'Novo Aripuanã', 'NOVO ARIPUANA', 'M', 'AM', 'NO', 0),
(1303403, 'Parintins', 'PARINTINS', 'M', 'AM', 'NO', 0),
(1303502, 'Pauini', 'PAUINI', 'M', 'AM', 'NO', 0),
(1303536, 'Presidente Figueiredo', 'PRESIDENTE FIGUEIREDO', 'M', 'AM', 'NO', 0),
(1303569, 'Rio Preto da Eva', 'RIO PRETO DA EVA', 'M', 'AM', 'NO', 0),
(1303601, 'Santa Isabel do Rio Negro', 'SANTA ISABEL DO RIO NEGRO', 'M', 'AM', 'NO', 0),
(1303700, 'Santo Antônio do Içá', 'SANTO ANTONIO DO ICA', 'M', 'AM', 'NO', 0),
(1303809, 'São Gabriel da Cachoeira', 'SAO GABRIEL DA CACHOEIRA', 'M', 'AM', 'NO', 0),
(1303908, 'São Paulo de Olivença', 'SAO PAULO DE OLIVENCA', 'M', 'AM', 'NO', 0),
(1303957, 'São Sebastião do Uatumã', 'SAO SEBASTIAO DO UATUMA', 'M', 'AM', 'NO', 0),
(1304005, 'Silves', 'SILVES', 'M', 'AM', 'NO', 0),
(1304062, 'Tabatinga', 'TABATINGA', 'M', 'AM', 'NO', 0),
(1304104, 'Tapauá', 'TAPAUA', 'M', 'AM', 'NO', 0),
(1304203, 'Tefé', 'TEFE', 'M', 'AM', 'NO', 0),
(1304237, 'Tonantins', 'TONANTINS', 'M', 'AM', 'NO', 0),
(1304260, 'Uarini', 'UARINI', 'M', 'AM', 'NO', 0),
(1304302, 'Urucará', 'URUCARA', 'M', 'AM', 'NO', 0),
(1304401, 'Urucurituba', 'URUCURITUBA', 'M', 'AM', 'NO', 0),
(1400000, 'Roraima', 'RORAIMA', 'U', 'RR', 'NO', 0),
(1400027, 'Amajari', 'AMAJARI', 'M', 'RR', 'NO', 0),
(1400050, 'Alto Alegre', 'ALTO ALEGRE', 'M', 'RR', 'NO', 0),
(1400100, 'Boa Vista', 'BOA VISTA', 'M', 'RR', 'NO', 0),
(1400159, 'Bonfim', 'BONFIM', 'M', 'RR', 'NO', 0),
(1400175, 'Cantá', 'CANTA', 'M', 'RR', 'NO', 0),
(1400209, 'Caracaraí', 'CARACARAI', 'M', 'RR', 'NO', 0),
(1400233, 'Caroebe', 'CAROEBE', 'M', 'RR', 'NO', 0),
(1400282, 'Iracema', 'IRACEMA', 'M', 'RR', 'NO', 0),
(1400308, 'Mucajaí', 'MUCAJAI', 'M', 'RR', 'NO', 0),
(1400407, 'Normandia', 'NORMANDIA', 'M', 'RR', 'NO', 0),
(1400456, 'Pacaraima', 'PACARAIMA', 'M', 'RR', 'NO', 0),
(1400472, 'Rorainópolis', 'RORAINOPOLIS', 'M', 'RR', 'NO', 0),
(1400506, 'São João da Baliza', 'SAO JOAO DA BALIZA', 'M', 'RR', 'NO', 0),
(1400605, 'São Luiz', 'SAO LUIZ', 'M', 'RR', 'NO', 0),
(1400704, 'Uiramutã', 'UIRAMUTA', 'M', 'RR', 'NO', 0),
(1500000, 'Pará', 'PARA', 'U', 'PA', 'NO', 0),
(1500107, 'Abaetetuba', 'ABAETETUBA', 'M', 'PA', 'NO', 0),
(1500131, 'Abel Figueiredo', 'ABEL FIGUEIREDO', 'M', 'PA', 'NO', 0),
(1500206, 'Acará', 'ACARA', 'M', 'PA', 'NO', 0),
(1500305, 'Afuá', 'AFUA', 'M', 'PA', 'NO', 0),
(1500347, 'Água Azul do Norte', 'AGUA AZUL DO NORTE', 'M', 'PA', 'NO', 0),
(1500404, 'Alenquer', 'ALENQUER', 'M', 'PA', 'NO', 0),
(1500503, 'Almeirim', 'ALMEIRIM', 'M', 'PA', 'NO', 0),
(1500602, 'Altamira', 'ALTAMIRA', 'M', 'PA', 'NO', 0),
(1500701, 'Anajás', 'ANAJAS', 'M', 'PA', 'NO', 0),
(1500800, 'Ananindeua', 'ANANINDEUA', 'M', 'PA', 'NO', 0),
(1500859, 'Anapu', 'ANAPU', 'M', 'PA', 'NO', 0),
(1500909, 'Augusto Corrêa', 'AUGUSTO CORREA', 'M', 'PA', 'NO', 0),
(1500958, 'Aurora do Pará', 'AURORA DO PARA', 'M', 'PA', 'NO', 0),
(1501006, 'Aveiro', 'AVEIRO', 'M', 'PA', 'NO', 0),
(1501105, 'Bagre', 'BAGRE', 'M', 'PA', 'NO', 0),
(1501204, 'Baião', 'BAIAO', 'M', 'PA', 'NO', 0),
(1501253, 'Bannach', 'BANNACH', 'M', 'PA', 'NO', 0),
(1501303, 'Barcarena', 'BARCARENA', 'M', 'PA', 'NO', 0),
(1501402, 'Belém', 'BELEM', 'M', 'PA', 'NO', 0),
(1501451, 'Belterra', 'BELTERRA', 'M', 'PA', 'NO', 0),
(1501501, 'Benevides', 'BENEVIDES', 'M', 'PA', 'NO', 0),
(1501576, 'Bom Jesus do Tocantins', 'BOM JESUS DO TOCANTINS', 'M', 'PA', 'NO', 0),
(1501600, 'Bonito', 'BONITO', 'M', 'PA', 'NO', 0),
(1501709, 'Bragança', 'BRAGANCA', 'M', 'PA', 'NO', 0),
(1501725, 'Brasil Novo', 'BRASIL NOVO', 'M', 'PA', 'NO', 0),
(1501758, 'Brejo Grande do Araguaia', 'BREJO GRANDE DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1501782, 'Breu Branco', 'BREU BRANCO', 'M', 'PA', 'NO', 0),
(1501808, 'Breves', 'BREVES', 'M', 'PA', 'NO', 0),
(1501907, 'Bujaru', 'BUJARU', 'M', 'PA', 'NO', 0),
(1501956, 'Cachoeira do Piriá', 'CACHOEIRA DO PIRIA', 'M', 'PA', 'NO', 0),
(1502004, 'Cachoeira do Arari', 'CACHOEIRA DO ARARI', 'M', 'PA', 'NO', 0),
(1502103, 'Cametá', 'CAMETA', 'M', 'PA', 'NO', 0),
(1502152, 'Canaã dos Carajás', 'CANAA DOS CARAJAS', 'M', 'PA', 'NO', 0),
(1502202, 'Capanema', 'CAPANEMA', 'M', 'PA', 'NO', 0),
(1502301, 'Capitão Poço', 'CAPITAO POCO', 'M', 'PA', 'NO', 0),
(1502400, 'Castanhal', 'CASTANHAL', 'M', 'PA', 'NO', 0),
(1502509, 'Chaves', 'CHAVES', 'M', 'PA', 'NO', 0),
(1502608, 'Colares', 'COLARES', 'M', 'PA', 'NO', 0),
(1502707, 'Conceição do Araguaia', 'CONCEICAO DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1502756, 'Concórdia do Pará', 'CONCORDIA DO PARA', 'M', 'PA', 'NO', 0),
(1502764, 'Cumaru do Norte', 'CUMARU DO NORTE', 'M', 'PA', 'NO', 0),
(1502772, 'Curionópolis', 'CURIONOPOLIS', 'M', 'PA', 'NO', 0),
(1502806, 'Curralinho', 'CURRALINHO', 'M', 'PA', 'NO', 0),
(1502855, 'Curuá', 'CURUA', 'M', 'PA', 'NO', 0),
(1502905, 'Curuçá', 'CURUCA', 'M', 'PA', 'NO', 0),
(1502939, 'Dom Eliseu', 'DOM ELISEU', 'M', 'PA', 'NO', 0),
(1502954, 'Eldorado dos Carajás', 'ELDORADO DOS CARAJAS', 'M', 'PA', 'NO', 0),
(1503002, 'Faro', 'FARO', 'M', 'PA', 'NO', 0),
(1503044, 'Floresta do Araguaia', 'FLORESTA DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1503077, 'Garrafão do Norte', 'GARRAFAO DO NORTE', 'M', 'PA', 'NO', 0),
(1503093, 'Goianésia do Pará', 'GOIANESIA DO PARA', 'M', 'PA', 'NO', 0),
(1503101, 'Gurupá', 'GURUPA', 'M', 'PA', 'NO', 0),
(1503200, 'Igarapé-Açu', 'IGARAPE-ACU', 'M', 'PA', 'NO', 0),
(1503309, 'Igarapé-Miri', 'IGARAPE-MIRI', 'M', 'PA', 'NO', 0),
(1503408, 'Inhangapi', 'INHANGAPI', 'M', 'PA', 'NO', 0),
(1503457, 'Ipixuna do Pará', 'IPIXUNA DO PARA', 'M', 'PA', 'NO', 0),
(1503507, 'Irituia', 'IRITUIA', 'M', 'PA', 'NO', 0),
(1503606, 'Itaituba', 'ITAITUBA', 'M', 'PA', 'NO', 0),
(1503705, 'Itupiranga', 'ITUPIRANGA', 'M', 'PA', 'NO', 0),
(1503754, 'Jacareacanga', 'JACAREACANGA', 'M', 'PA', 'NO', 0),
(1503804, 'Jacundá', 'JACUNDA', 'M', 'PA', 'NO', 0),
(1503903, 'Juruti', 'JURUTI', 'M', 'PA', 'NO', 0),
(1504000, 'Limoeiro do Ajuru', 'LIMOEIRO DO AJURU', 'M', 'PA', 'NO', 0),
(1504059, 'Mãe do Rio', 'MAE DO RIO', 'M', 'PA', 'NO', 0),
(1504109, 'Magalhães Barata', 'MAGALHAES BARATA', 'M', 'PA', 'NO', 0),
(1504208, 'Marabá', 'MARABA', 'M', 'PA', 'NO', 0),
(1504307, 'Maracanã', 'MARACANA', 'M', 'PA', 'NO', 0),
(1504406, 'Marapanim', 'MARAPANIM', 'M', 'PA', 'NO', 0),
(1504422, 'Marituba', 'MARITUBA', 'M', 'PA', 'NO', 0),
(1504455, 'Medicilândia', 'MEDICILANDIA', 'M', 'PA', 'NO', 0),
(1504505, 'Melgaço', 'MELGACO', 'M', 'PA', 'NO', 0),
(1504604, 'Mocajuba', 'MOCAJUBA', 'M', 'PA', 'NO', 0),
(1504703, 'Moju', 'MOJU', 'M', 'PA', 'NO', 0),
(1504802, 'Monte Alegre', 'MONTE ALEGRE', 'M', 'PA', 'NO', 0),
(1504901, 'Muaná', 'MUANA', 'M', 'PA', 'NO', 0),
(1504950, 'Nova Esperança do Piriá', 'NOVA ESPERANCA DO PIRIA', 'M', 'PA', 'NO', 0),
(1504976, 'Nova Ipixuna', 'NOVA IPIXUNA', 'M', 'PA', 'NO', 0),
(1505007, 'Nova Timboteua', 'NOVA TIMBOTEUA', 'M', 'PA', 'NO', 0),
(1505031, 'Novo Progresso', 'NOVO PROGRESSO', 'M', 'PA', 'NO', 0),
(1505064, 'Novo Repartimento', 'NOVO REPARTIMENTO', 'M', 'PA', 'NO', 0),
(1505106, 'Óbidos', 'OBIDOS', 'M', 'PA', 'NO', 0),
(1505205, 'Oeiras do Pará', 'OEIRAS DO PARA', 'M', 'PA', 'NO', 0),
(1505304, 'Oriximiná', 'ORIXIMINA', 'M', 'PA', 'NO', 0),
(1505403, 'Ourém', 'OUREM', 'M', 'PA', 'NO', 0),
(1505437, 'Ourilândia do Norte', 'OURILANDIA DO NORTE', 'M', 'PA', 'NO', 0),
(1505486, 'Pacajá', 'PACAJA', 'M', 'PA', 'NO', 0),
(1505494, 'Palestina do Pará', 'PALESTINA DO PARA', 'M', 'PA', 'NO', 0),
(1505502, 'Paragominas', 'PARAGOMINAS', 'M', 'PA', 'NO', 0),
(1505536, 'Parauapebas', 'PARAUAPEBAS', 'M', 'PA', 'NO', 0),
(1505551, 'Pau D''Arco', 'PAU D''ARCO', 'M', 'PA', 'NO', 0),
(1505601, 'Peixe-Boi', 'PEIXE-BOI', 'M', 'PA', 'NO', 0),
(1505635, 'Piçarra', 'PICARRA', 'M', 'PA', 'NO', 0),
(1505650, 'Placas', 'PLACAS', 'M', 'PA', 'NO', 0),
(1505700, 'Ponta de Pedras', 'PONTA DE PEDRAS', 'M', 'PA', 'NO', 0),
(1505809, 'Portel', 'PORTEL', 'M', 'PA', 'NO', 0),
(1505908, 'Porto de Moz', 'PORTO DE MOZ', 'M', 'PA', 'NO', 0),
(1506005, 'Prainha', 'PRAINHA', 'M', 'PA', 'NO', 0),
(1506104, 'Primavera', 'PRIMAVERA', 'M', 'PA', 'NO', 0),
(1506112, 'Quatipuru', 'QUATIPURU', 'M', 'PA', 'NO', 0),
(1506138, 'Redenção', 'REDENCAO', 'M', 'PA', 'NO', 0),
(1506161, 'Rio Maria', 'RIO MARIA', 'M', 'PA', 'NO', 0),
(1506187, 'Rondon do Pará', 'RONDON DO PARA', 'M', 'PA', 'NO', 0),
(1506195, 'Rurópolis', 'RUROPOLIS', 'M', 'PA', 'NO', 0),
(1506203, 'Salinópolis', 'SALINOPOLIS', 'M', 'PA', 'NO', 0),
(1506302, 'Salvaterra', 'SALVATERRA', 'M', 'PA', 'NO', 0),
(1506351, 'Santa Bárbara do Pará', 'SANTA BARBARA DO PARA', 'M', 'PA', 'NO', 0),
(1506401, 'Santa Cruz do Arari', 'SANTA CRUZ DO ARARI', 'M', 'PA', 'NO', 0),
(1506500, 'Santa Isabel do Pará', 'SANTA ISABEL DO PARA', 'M', 'PA', 'NO', 0),
(1506559, 'Santa Luzia do Pará', 'SANTA LUZIA DO PARA', 'M', 'PA', 'NO', 0),
(1506583, 'Santa Maria das Barreiras', 'SANTA MARIA DAS BARREIRAS', 'M', 'PA', 'NO', 0),
(1506609, 'Santa Maria do Pará', 'SANTA MARIA DO PARA', 'M', 'PA', 'NO', 0),
(1506708, 'Santana do Araguaia', 'SANTANA DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1506807, 'Santarém', 'SANTAREM', 'M', 'PA', 'NO', 0),
(1506906, 'Santarém Novo', 'SANTAREM NOVO', 'M', 'PA', 'NO', 0),
(1507003, 'Santo Antônio do Tauá', 'SANTO ANTONIO DO TAUA', 'M', 'PA', 'NO', 0),
(1507102, 'São Caetano de Odivelas', 'SAO CAETANO DE ODIVELAS', 'M', 'PA', 'NO', 0),
(1507151, 'São Domingos do Araguaia', 'SAO DOMINGOS DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1507201, 'São Domingos do Capim', 'SAO DOMINGOS DO CAPIM', 'M', 'PA', 'NO', 0),
(1507300, 'São Félix do Xingu', 'SAO FELIX DO XINGU', 'M', 'PA', 'NO', 0),
(1507409, 'São Francisco do Pará', 'SAO FRANCISCO DO PARA', 'M', 'PA', 'NO', 0),
(1507458, 'São Geraldo do Araguaia', 'SAO GERALDO DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1507466, 'São João da Ponta', 'SAO JOAO DA PONTA', 'M', 'PA', 'NO', 0),
(1507474, 'São João de Pirabas', 'SAO JOAO DE PIRABAS', 'M', 'PA', 'NO', 0),
(1507508, 'São João do Araguaia', 'SAO JOAO DO ARAGUAIA', 'M', 'PA', 'NO', 0),
(1507607, 'São Miguel do Guamá', 'SAO MIGUEL DO GUAMA', 'M', 'PA', 'NO', 0),
(1507706, 'São Sebastião da Boa Vista', 'SAO SEBASTIAO DA BOA VISTA', 'M', 'PA', 'NO', 0),
(1507755, 'Sapucaia', 'SAPUCAIA', 'M', 'PA', 'NO', 0),
(1507805, 'Senador José Porfírio', 'SENADOR JOSE PORFIRIO', 'M', 'PA', 'NO', 0),
(1507904, 'Soure', 'SOURE', 'M', 'PA', 'NO', 0),
(1507953, 'Tailândia', 'TAILANDIA', 'M', 'PA', 'NO', 0),
(1507961, 'Terra Alta', 'TERRA ALTA', 'M', 'PA', 'NO', 0),
(1507979, 'Terra Santa', 'TERRA SANTA', 'M', 'PA', 'NO', 0),
(1508001, 'Tomé-Açu', 'TOME-ACU', 'M', 'PA', 'NO', 0),
(1508035, 'Tracuateua', 'TRACUATEUA', 'M', 'PA', 'NO', 0),
(1508050, 'Trairão', 'TRAIRAO', 'M', 'PA', 'NO', 0),
(1508084, 'Tucumã', 'TUCUMA', 'M', 'PA', 'NO', 0),
(1508100, 'Tucuruí', 'TUCURUI', 'M', 'PA', 'NO', 0),
(1508126, 'Ulianópolis', 'ULIANOPOLIS', 'M', 'PA', 'NO', 0),
(1508159, 'Uruará', 'URUARA', 'M', 'PA', 'NO', 0),
(1508209, 'Vigia', 'VIGIA', 'M', 'PA', 'NO', 0),
(1508308, 'Viseu', 'VISEU', 'M', 'PA', 'NO', 0),
(1508357, 'Vitória do Xingu', 'VITORIA DO XINGU', 'M', 'PA', 'NO', 0),
(1508407, 'Xinguara', 'XINGUARA', 'M', 'PA', 'NO', 0),
(1600000, 'Amapá', 'AMAPA', 'U', 'AP', 'NO', 0),
(1600055, 'Serra do Navio', 'SERRA DO NAVIO', 'M', 'AP', 'NO', 0),
(1600105, 'Amapá', 'AMAPA', 'M', 'AP', 'NO', 0),
(1600154, 'Pedra Branca do Amapari', 'PEDRA BRANCA DO AMAPARI', 'M', 'AP', 'NO', 0),
(1600204, 'Calçoene', 'CALCOENE', 'M', 'AP', 'NO', 0),
(1600212, 'Cutias', 'CUTIAS', 'M', 'AP', 'NO', 0),
(1600238, 'Ferreira Gomes', 'FERREIRA GOMES', 'M', 'AP', 'NO', 0),
(1600253, 'Itaubal', 'ITAUBAL', 'M', 'AP', 'NO', 0),
(1600279, 'Laranjal do Jari', 'LARANJAL DO JARI', 'M', 'AP', 'NO', 0),
(1600303, 'Macapá', 'MACAPA', 'M', 'AP', 'NO', 0),
(1600402, 'Mazagão', 'MAZAGAO', 'M', 'AP', 'NO', 0),
(1600501, 'Oiapoque', 'OIAPOQUE', 'M', 'AP', 'NO', 0),
(1600535, 'Porto Grande', 'PORTO GRANDE', 'M', 'AP', 'NO', 0),
(1600550, 'Pracuúba', 'PRACUUBA', 'M', 'AP', 'NO', 0),
(1600600, 'Santana', 'SANTANA', 'M', 'AP', 'NO', 0),
(1600709, 'Tartarugalzinho', 'TARTARUGALZINHO', 'M', 'AP', 'NO', 0),
(1600808, 'Vitória do Jari', 'VITORIA DO JARI', 'M', 'AP', 'NO', 0),
(1700000, 'Tocantins', 'TOCANTINS', 'U', 'TO', 'NO', 0),
(1700251, 'Abreulândia', 'ABREULANDIA', 'M', 'TO', 'NO', 0),
(1700301, 'Aguiarnópolis', 'AGUIARNOPOLIS', 'M', 'TO', 'NO', 0),
(1700350, 'Aliança do Tocantins', 'ALIANCA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1700400, 'Almas', 'ALMAS', 'M', 'TO', 'NO', 0),
(1700707, 'Alvorada', 'ALVORADA', 'M', 'TO', 'NO', 0),
(1701002, 'Ananás', 'ANANAS', 'M', 'TO', 'NO', 0),
(1701051, 'Angico', 'ANGICO', 'M', 'TO', 'NO', 0),
(1701101, 'Aparecida do Rio Negro', 'APARECIDA DO RIO NEGRO', 'M', 'TO', 'NO', 0),
(1701309, 'Aragominas', 'ARAGOMINAS', 'M', 'TO', 'NO', 0),
(1701903, 'Araguacema', 'ARAGUACEMA', 'M', 'TO', 'NO', 0),
(1702000, 'Araguaçu', 'ARAGUACU', 'M', 'TO', 'NO', 0),
(1702109, 'Araguaína', 'ARAGUAINA', 'M', 'TO', 'NO', 0),
(1702158, 'Araguanã', 'ARAGUANA', 'M', 'TO', 'NO', 0),
(1702208, 'Araguatins', 'ARAGUATINS', 'M', 'TO', 'NO', 0),
(1702307, 'Arapoema', 'ARAPOEMA', 'M', 'TO', 'NO', 0),
(1702406, 'Arraias', 'ARRAIAS', 'M', 'TO', 'NO', 0),
(1702554, 'Augustinópolis', 'AUGUSTINOPOLIS', 'M', 'TO', 'NO', 0),
(1702703, 'Aurora do Tocantins', 'AURORA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1702901, 'Axixá do Tocantins', 'AXIXA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703008, 'Babaçulândia', 'BABACULANDIA', 'M', 'TO', 'NO', 0),
(1703057, 'Bandeirantes do Tocantins', 'BANDEIRANTES DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703073, 'Barra do Ouro', 'BARRA DO OURO', 'M', 'TO', 'NO', 0),
(1703107, 'Barrolândia', 'BARROLANDIA', 'M', 'TO', 'NO', 0),
(1703206, 'Bernardo Sayão', 'BERNARDO SAYAO', 'M', 'TO', 'NO', 0),
(1703305, 'Bom Jesus do Tocantins', 'BOM JESUS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703602, 'Brasilândia do Tocantins', 'BRASILANDIA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703701, 'Brejinho de Nazaré', 'BREJINHO DE NAZARE', 'M', 'TO', 'NO', 0),
(1703800, 'Buriti do Tocantins', 'BURITI DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703826, 'Cachoeirinha', 'CACHOEIRINHA', 'M', 'TO', 'NO', 0),
(1703842, 'Campos Lindos', 'CAMPOS LINDOS', 'M', 'TO', 'NO', 0),
(1703867, 'Cariri do Tocantins', 'CARIRI DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1703883, 'Carmolândia', 'CARMOLANDIA', 'M', 'TO', 'NO', 0),
(1703891, 'Carrasco Bonito', 'CARRASCO BONITO', 'M', 'TO', 'NO', 0),
(1703909, 'Caseara', 'CASEARA', 'M', 'TO', 'NO', 0),
(1704105, 'Centenário', 'CENTENARIO', 'M', 'TO', 'NO', 0),
(1704600, 'Chapada de Areia', 'CHAPADA DE AREIA', 'M', 'TO', 'NO', 0),
(1705102, 'Chapada da Natividade', 'CHAPADA DA NATIVIDADE', 'M', 'TO', 'NO', 0),
(1705508, 'Colinas do Tocantins', 'COLINAS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1705557, 'Combinado', 'COMBINADO', 'M', 'TO', 'NO', 0),
(1705607, 'Conceição do Tocantins', 'CONCEICAO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1706001, 'Couto de Magalhães', 'COUTO DE MAGALHAES', 'M', 'TO', 'NO', 0),
(1706100, 'Cristalândia', 'CRISTALANDIA', 'M', 'TO', 'NO', 0),
(1706258, 'Crixás do Tocantins', 'CRIXAS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1706506, 'Darcinópolis', 'DARCINOPOLIS', 'M', 'TO', 'NO', 0),
(1707009, 'Dianópolis', 'DIANOPOLIS', 'M', 'TO', 'NO', 0),
(1707108, 'Divinópolis do Tocantins', 'DIVINOPOLIS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1707207, 'Dois Irmãos do Tocantins', 'DOIS IRMAOS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1707306, 'Dueré', 'DUERE', 'M', 'TO', 'NO', 0),
(1707405, 'Esperantina', 'ESPERANTINA', 'M', 'TO', 'NO', 0),
(1707553, 'Fátima', 'FATIMA', 'M', 'TO', 'NO', 0),
(1707652, 'Figueirópolis', 'FIGUEIROPOLIS', 'M', 'TO', 'NO', 0),
(1707702, 'Filadélfia', 'FILADELFIA', 'M', 'TO', 'NO', 0),
(1708205, 'Formoso do Araguaia', 'FORMOSO DO ARAGUAIA', 'M', 'TO', 'NO', 0),
(1708254, 'Fortaleza do Tabocão', 'FORTALEZA DO TABOCAO', 'M', 'TO', 'NO', 0),
(1708304, 'Goianorte', 'GOIANORTE', 'M', 'TO', 'NO', 0),
(1709005, 'Goiatins', 'GOIATINS', 'M', 'TO', 'NO', 0),
(1709302, 'Guaraí', 'GUARAI', 'M', 'TO', 'NO', 0),
(1709500, 'Gurupi', 'GURUPI', 'M', 'TO', 'NO', 0),
(1709807, 'Ipueiras', 'IPUEIRAS', 'M', 'TO', 'NO', 0),
(1710508, 'Itacajá', 'ITACAJA', 'M', 'TO', 'NO', 0),
(1710706, 'Itaguatins', 'ITAGUATINS', 'M', 'TO', 'NO', 0),
(1710904, 'Itapiratins', 'ITAPIRATINS', 'M', 'TO', 'NO', 0),
(1711100, 'Itaporã do Tocantins', 'ITAPORA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1711506, 'Jaú do Tocantins', 'JAU DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1711803, 'Juarina', 'JUARINA', 'M', 'TO', 'NO', 0),
(1711902, 'Lagoa da Confusão', 'LAGOA DA CONFUSAO', 'M', 'TO', 'NO', 0),
(1711951, 'Lagoa do Tocantins', 'LAGOA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1712009, 'Lajeado', 'LAJEADO', 'M', 'TO', 'NO', 0),
(1712157, 'Lavandeira', 'LAVANDEIRA', 'M', 'TO', 'NO', 0),
(1712405, 'Lizarda', 'LIZARDA', 'M', 'TO', 'NO', 0),
(1712454, 'Luzinópolis', 'LUZINOPOLIS', 'M', 'TO', 'NO', 0),
(1712504, 'Marianópolis do Tocantins', 'MARIANOPOLIS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1712702, 'Mateiros', 'MATEIROS', 'M', 'TO', 'NO', 0),
(1712801, 'Maurilândia do Tocantins', 'MAURILANDIA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1713205, 'Miracema do Tocantins', 'MIRACEMA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1713304, 'Miranorte', 'MIRANORTE', 'M', 'TO', 'NO', 0),
(1713601, 'Monte do Carmo', 'MONTE DO CARMO', 'M', 'TO', 'NO', 0),
(1713700, 'Monte Santo do Tocantins', 'MONTE SANTO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1713809, 'Mosquito', 'MOSQUITO', 'M', 'TO', 'NO', 0),
(1713957, 'Muricilândia', 'MURICILANDIA', 'M', 'TO', 'NO', 0),
(1714203, 'Natividade', 'NATIVIDADE', 'M', 'TO', 'NO', 0),
(1714302, 'Nazaré', 'NAZARE', 'M', 'TO', 'NO', 0),
(1714880, 'Nova Olinda', 'NOVA OLINDA', 'M', 'TO', 'NO', 0),
(1715002, 'Nova Rosalândia', 'NOVA ROSALANDIA', 'M', 'TO', 'NO', 0),
(1715101, 'Novo Acordo', 'NOVO ACORDO', 'M', 'TO', 'NO', 0),
(1715150, 'Novo Alegre', 'NOVO ALEGRE', 'M', 'TO', 'NO', 0),
(1715259, 'Novo Jardim', 'NOVO JARDIM', 'M', 'TO', 'NO', 0),
(1715507, 'Oliveira de Fátima', 'OLIVEIRA DE FATIMA', 'M', 'TO', 'NO', 0),
(1715705, 'Palmeirante', 'PALMEIRANTE', 'M', 'TO', 'NO', 0),
(1715754, 'Palmeirópolis', 'PALMEIROPOLIS', 'M', 'TO', 'NO', 0),
(1716109, 'Paraíso do Tocantins', 'PARAISO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1716208, 'Paranã', 'PARANA', 'M', 'TO', 'NO', 0),
(1716307, 'Pau D''Arco', 'PAU D''ARCO', 'M', 'TO', 'NO', 0),
(1716505, 'Pedro Afonso', 'PEDRO AFONSO', 'M', 'TO', 'NO', 0),
(1716604, 'Peixe', 'PEIXE', 'M', 'TO', 'NO', 0),
(1716653, 'Pequizeiro', 'PEQUIZEIRO', 'M', 'TO', 'NO', 0),
(1716703, 'Colméia', 'COLMEIA', 'M', 'TO', 'NO', 0),
(1717008, 'Pindorama do Tocantins', 'PINDORAMA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1717206, 'Piraquê', 'PIRAQUE', 'M', 'TO', 'NO', 0),
(1717503, 'Pium', 'PIUM', 'M', 'TO', 'NO', 0),
(1717800, 'Ponte Alta do Bom Jesus', 'PONTE ALTA DO BOM JESUS', 'M', 'TO', 'NO', 0),
(1717909, 'Ponte Alta do Tocantins', 'PONTE ALTA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1718006, 'Porto Alegre do Tocantins', 'PORTO ALEGRE DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1718204, 'Porto Nacional', 'PORTO NACIONAL', 'M', 'TO', 'NO', 0),
(1718303, 'Praia Norte', 'PRAIA NORTE', 'M', 'TO', 'NO', 0),
(1718402, 'Presidente Kennedy', 'PRESIDENTE KENNEDY', 'M', 'TO', 'NO', 0),
(1718451, 'Pugmil', 'PUGMIL', 'M', 'TO', 'NO', 0),
(1718501, 'Recursolândia', 'RECURSOLANDIA', 'M', 'TO', 'NO', 0),
(1718550, 'Riachinho', 'RIACHINHO', 'M', 'TO', 'NO', 0),
(1718659, 'Rio da Conceição', 'RIO DA CONCEICAO', 'M', 'TO', 'NO', 0),
(1718709, 'Rio dos Bois', 'RIO DOS BOIS', 'M', 'TO', 'NO', 0),
(1718758, 'Rio Sono', 'RIO SONO', 'M', 'TO', 'NO', 0),
(1718808, 'Sampaio', 'SAMPAIO', 'M', 'TO', 'NO', 0),
(1718840, 'Sandolândia', 'SANDOLANDIA', 'M', 'TO', 'NO', 0),
(1718865, 'Santa Fé do Araguaia', 'SANTA FE DO ARAGUAIA', 'M', 'TO', 'NO', 0),
(1718881, 'Santa Maria do Tocantins', 'SANTA MARIA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1718899, 'Santa Rita do Tocantins', 'SANTA RITA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1718907, 'Santa Rosa do Tocantins', 'SANTA ROSA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1719004, 'Santa Tereza do Tocantins', 'SANTA TEREZA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720002, 'Santa Terezinha do Tocantins', 'SANTA TEREZINHA DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720101, 'São Bento do Tocantins', 'SAO BENTO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720150, 'São Félix do Tocantins', 'SAO FELIX DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720200, 'São Miguel do Tocantins', 'SAO MIGUEL DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720259, 'São Salvador do Tocantins', 'SAO SALVADOR DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720309, 'São Sebastião do Tocantins', 'SAO SEBASTIAO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720499, 'São Valério da Natividade', 'SAO VALERIO DA NATIVIDADE', 'M', 'TO', 'NO', 0),
(1720655, 'Silvanópolis', 'SILVANOPOLIS', 'M', 'TO', 'NO', 0),
(1720804, 'Sítio Novo do Tocantins', 'SITIO NOVO DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720853, 'Sucupira', 'SUCUPIRA', 'M', 'TO', 'NO', 0),
(1720903, 'Taguatinga', 'TAGUATINGA', 'M', 'TO', 'NO', 0),
(1720937, 'Taipas do Tocantins', 'TAIPAS DO TOCANTINS', 'M', 'TO', 'NO', 0),
(1720978, 'Talismã', 'TALISMA', 'M', 'TO', 'NO', 0),
(1721000, 'Palmas', 'PALMAS', 'M', 'TO', 'NO', 0),
(1721109, 'Tocantínia', 'TOCANTINIA', 'M', 'TO', 'NO', 0),
(1721208, 'Tocantinópolis', 'TOCANTINOPOLIS', 'M', 'TO', 'NO', 0),
(1721257, 'Tupirama', 'TUPIRAMA', 'M', 'TO', 'NO', 0),
(1721307, 'Tupiratins', 'TUPIRATINS', 'M', 'TO', 'NO', 0),
(1722081, 'Wanderlândia', 'WANDERLANDIA', 'M', 'TO', 'NO', 0),
(1722107, 'Xambioá', 'XAMBIOA', 'M', 'TO', 'NO', 0),
(2100000, 'Maranhão', 'MARANHAO', 'U', 'MA', 'NE', 0),
(2100055, 'Açailândia', 'ACAILANDIA', 'M', 'MA', 'NE', 0),
(2100105, 'Afonso Cunha', 'AFONSO CUNHA', 'M', 'MA', 'NE', 0),
(2100154, 'Água Doce do Maranhão', 'AGUA DOCE DO MARANHAO', 'M', 'MA', 'NE', 0),
(2100204, 'Alcântara', 'ALCANTARA', 'M', 'MA', 'NE', 0),
(2100303, 'Aldeias Altas', 'ALDEIAS ALTAS', 'M', 'MA', 'NE', 0),
(2100402, 'Altamira do Maranhão', 'ALTAMIRA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2100436, 'Alto Alegre do Maranhao', 'ALTO ALEGRE DO MARANHAO', 'M', 'MA', 'NE', 0),
(2100477, 'Alto Alegre do Pindaré', 'ALTO ALEGRE DO PINDARE', 'M', 'MA', 'NE', 0),
(2100501, 'Alto Parnaíba', 'ALTO PARNAIBA', 'M', 'MA', 'NE', 0),
(2100550, 'Amapá do Maranhao', 'AMAPA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2100600, 'Amarante do Maranhão', 'AMARANTE DO MARANHAO', 'M', 'MA', 'NE', 0),
(2100709, 'Anajatuba', 'ANAJATUBA', 'M', 'MA', 'NE', 0),
(2100808, 'Anapurus', 'ANAPURUS', 'M', 'MA', 'NE', 0),
(2100832, 'Apicum-acu', 'APICUM-ACU', 'M', 'MA', 'NE', 0),
(2100873, 'Araguanã', 'ARAGUANA', 'M', 'MA', 'NE', 0),
(2100907, 'Araioses', 'ARAIOSES', 'M', 'MA', 'NE', 0),
(2100956, 'Arame', 'ARAME', 'M', 'MA', 'NE', 0),
(2101004, 'Arari', 'ARARI', 'M', 'MA', 'NE', 0),
(2101103, 'Axixá', 'AXIXA', 'M', 'MA', 'NE', 0),
(2101202, 'Bacabal', 'BACABAL', 'M', 'MA', 'NE', 0),
(2101251, 'Bacabeira', 'BACABEIRA', 'M', 'MA', 'NE', 0),
(2101301, 'Bacuri', 'BACURI', 'M', 'MA', 'NE', 0),
(2101350, 'Bacurituba', 'BACURITUBA', 'M', 'MA', 'NE', 0),
(2101400, 'Balsas', 'BALSAS', 'M', 'MA', 'NE', 0),
(2101509, 'Barão de Grajaú', 'BARAO DE GRAJAU', 'M', 'MA', 'NE', 0),
(2101608, 'Barra do Corda', 'BARRA DO CORDA', 'M', 'MA', 'NE', 0),
(2101707, 'Barreirinhas', 'BARREIRINHAS', 'M', 'MA', 'NE', 0),
(2101731, 'Belágua', 'BELAGUA', 'M', 'MA', 'NE', 0),
(2101772, 'Bela Vista do Maranhão', 'BELA VISTA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2101806, 'Benedito Leite', 'BENEDITO LEITE', 'M', 'MA', 'NE', 0),
(2101905, 'Bequimão', 'BEQUIMAO', 'M', 'MA', 'NE', 0),
(2101939, 'Bernardo do Mearim', 'BERNARDO DO MEARIM', 'M', 'MA', 'NE', 0),
(2101970, 'Boa Vista do Gurupi', 'BOA VISTA DO GURUPI', 'M', 'MA', 'NE', 0),
(2102002, 'Bom Jardim', 'BOM JARDIM', 'M', 'MA', 'NE', 0),
(2102036, 'Bom Jesus das Selvas', 'BOM JESUS DAS SELVAS', 'M', 'MA', 'NE', 0),
(2102077, 'Bom Lugar', 'BOM LUGAR', 'M', 'MA', 'NE', 0),
(2102101, 'Brejo', 'BREJO', 'M', 'MA', 'NE', 0),
(2102150, 'Brejo de Areia', 'BREJO DE AREIA', 'M', 'MA', 'NE', 0),
(2102200, 'Buriti', 'BURITI', 'M', 'MA', 'NE', 0),
(2102309, 'Buriti Bravo', 'BURITI BRAVO', 'M', 'MA', 'NE', 0),
(2102325, 'Buriticupu', 'BURITICUPU', 'M', 'MA', 'NE', 0),
(2102358, 'Buritirana', 'BURITIRANA', 'M', 'MA', 'NE', 0),
(2102374, 'Cachoeira Grande', 'CACHOEIRA GRANDE', 'M', 'MA', 'NE', 0),
(2102408, 'Cajapió', 'CAJAPIO', 'M', 'MA', 'NE', 0),
(2102507, 'Cajari', 'CAJARI', 'M', 'MA', 'NE', 0),
(2102556, 'Campestre do Maranhão', 'CAMPESTRE DO MARANHAO', 'M', 'MA', 'NE', 0),
(2102606, 'Candido Mendes', 'CANDIDO MENDES', 'M', 'MA', 'NE', 0),
(2102705, 'Cantanhede', 'CANTANHEDE', 'M', 'MA', 'NE', 0),
(2102754, 'Capinzal do Norte', 'CAPINZAL DO NORTE', 'M', 'MA', 'NE', 0),
(2102804, 'Carolina', 'CAROLINA', 'M', 'MA', 'NE', 0),
(2102903, 'Carutapera', 'CARUTAPERA', 'M', 'MA', 'NE', 0),
(2103000, 'Caxias', 'CAXIAS', 'M', 'MA', 'NE', 0),
(2103109, 'Cedral', 'CEDRAL', 'M', 'MA', 'NE', 0),
(2103125, 'Central do Maranhão', 'CENTRAL DO MARANHAO', 'M', 'MA', 'NE', 0),
(2103158, 'Centro do Guilherme', 'CENTRO DO GUILHERME', 'M', 'MA', 'NE', 0),
(2103174, 'Centro Novo do Maranhão', 'CENTRO NOVO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2103208, 'Chapadinha', 'CHAPADINHA', 'M', 'MA', 'NE', 0),
(2103257, 'Cidelândia', 'CIDELANDIA', 'M', 'MA', 'NE', 0),
(2103307, 'Codó', 'CODO', 'M', 'MA', 'NE', 0),
(2103406, 'Coelho Neto', 'COELHO NETO', 'M', 'MA', 'NE', 0),
(2103505, 'Colinas', 'COLINAS', 'M', 'MA', 'NE', 0),
(2103554, 'Conceicao do Lago-acu', 'CONCEICAO DO LAGO-ACU', 'M', 'MA', 'NE', 0),
(2103604, 'Coroata', 'COROATA', 'M', 'MA', 'NE', 0),
(2103703, 'Cururupu', 'CURURUPU', 'M', 'MA', 'NE', 0),
(2103752, 'Davinópolis', 'DAVINOPOLIS', 'M', 'MA', 'NE', 0),
(2103802, 'Dom Pedro', 'DOM PEDRO', 'M', 'MA', 'NE', 0),
(2103901, 'Duque Bacelar', 'DUQUE BACELAR', 'M', 'MA', 'NE', 0),
(2104008, 'Esperantinópolis', 'ESPERANTINOPOLIS', 'M', 'MA', 'NE', 0),
(2104057, 'Estreito', 'ESTREITO', 'M', 'MA', 'NE', 0),
(2104073, 'Feira Nova do Maranhão', 'FEIRA NOVA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2104081, 'Fernando Falcao', 'FERNANDO FALCAO', 'M', 'MA', 'NE', 0),
(2104099, 'Formosa da Serra Negra', 'FORMOSA DA SERRA NEGRA', 'M', 'MA', 'NE', 0),
(2104107, 'Fortaleza dos Nogueiras', 'FORTALEZA DOS NOGUEIRAS', 'M', 'MA', 'NE', 0),
(2104206, 'Fortuna', 'FORTUNA', 'M', 'MA', 'NE', 0),
(2104305, 'Godofredo Viana', 'GODOFREDO VIANA', 'M', 'MA', 'NE', 0),
(2104404, 'Goncalves Dias', 'GONCALVES DIAS', 'M', 'MA', 'NE', 0),
(2104503, 'Governador Archer', 'GOVERNADOR ARCHER', 'M', 'MA', 'NE', 0),
(2104552, 'Governador Edison Lobão', 'GOVERNADOR EDISON LOBAO', 'M', 'MA', 'NE', 0),
(2104602, 'Governador Eugênio Barros', 'GOVERNADOR EUGENIO BARROS', 'M', 'MA', 'NE', 0),
(2104628, 'Governador Luiz Rocha', 'GOVERNADOR LUIZ ROCHA', 'M', 'MA', 'NE', 0),
(2104651, 'Governador Newton Bello', 'GOVERNADOR NEWTON BELLO', 'M', 'MA', 'NE', 0),
(2104677, 'Governador Nunes Freire', 'GOVERNADOR NUNES FREIRE', 'M', 'MA', 'NE', 0),
(2104701, 'Graca Aranha', 'GRACA ARANHA', 'M', 'MA', 'NE', 0),
(2104800, 'Grajaú', 'GRAJAU', 'M', 'MA', 'NE', 0),
(2104909, 'Guimarães', 'GUIMARAES', 'M', 'MA', 'NE', 0),
(2105005, 'Humberto de Campos', 'HUMBERTO DE CAMPOS', 'M', 'MA', 'NE', 0),
(2105104, 'Icatu', 'ICATU', 'M', 'MA', 'NE', 0),
(2105153, 'Igarapé do Meio', 'IGARAPE DO MEIO', 'M', 'MA', 'NE', 0),
(2105203, 'Igarapé Grande', 'IGARAPE GRANDE', 'M', 'MA', 'NE', 0),
(2105302, 'Imperatriz', 'IMPERATRIZ', 'M', 'MA', 'NE', 0),
(2105351, 'Itaipava do Grajaú', 'ITAIPAVA DO GRAJAU', 'M', 'MA', 'NE', 0),
(2105401, 'Itapecuru Mirim', 'ITAPECURU MIRIM', 'M', 'MA', 'NE', 0),
(2105427, 'Itinga do Maranhão', 'ITINGA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2105450, 'Jatobá', 'JATOBA', 'M', 'MA', 'NE', 0),
(2105476, 'Jenipapo dos Vieiras', 'JENIPAPO DOS VIEIRAS', 'M', 'MA', 'NE', 0),
(2105500, 'João Lisboa', 'JOAO LISBOA', 'M', 'MA', 'NE', 0),
(2105609, 'Joselândia', 'JOSELANDIA', 'M', 'MA', 'NE', 0),
(2105658, 'Junco do Maranhao', 'JUNCO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2105708, 'Lago da Pedra', 'LAGO DA PEDRA', 'M', 'MA', 'NE', 0),
(2105807, 'Lago do Junco', 'LAGO DO JUNCO', 'M', 'MA', 'NE', 0),
(2105906, 'Lago Verde', 'LAGO VERDE', 'M', 'MA', 'NE', 0),
(2105922, 'Lagoa do Mato', 'LAGOA DO MATO', 'M', 'MA', 'NE', 0),
(2105948, 'Lago dos Rodrigues', 'LAGO DOS RODRIGUES', 'M', 'MA', 'NE', 0),
(2105963, 'Lagoa Grande do Maranhão', 'LAGOA GRANDE DO MARANHAO', 'M', 'MA', 'NE', 0),
(2105989, 'Lajeado Novo', 'LAJEADO NOVO', 'M', 'MA', 'NE', 0),
(2106003, 'Lima Campos', 'LIMA CAMPOS', 'M', 'MA', 'NE', 0),
(2106102, 'Loreto', 'LORETO', 'M', 'MA', 'NE', 0),
(2106201, 'Luis Domingues', 'LUIS DOMINGUES', 'M', 'MA', 'NE', 0),
(2106300, 'Magalhães de Almeida', 'MAGALHAES DE ALMEIDA', 'M', 'MA', 'NE', 0),
(2106326, 'Maracaçumé', 'MARACACUME', 'M', 'MA', 'NE', 0),
(2106359, 'Marajá do Sena', 'MARAJA DO SENA', 'M', 'MA', 'NE', 0),
(2106375, 'Maranhãozinho', 'MARANHAOZINHO', 'M', 'MA', 'NE', 0),
(2106409, 'Mata Roma', 'MATA ROMA', 'M', 'MA', 'NE', 0),
(2106508, 'Matinha', 'MATINHA', 'M', 'MA', 'NE', 0),
(2106607, 'Matões', 'MATOES', 'M', 'MA', 'NE', 0),
(2106631, 'Matões do Norte', 'MATOES DO NORTE', 'M', 'MA', 'NE', 0),
(2106672, 'Milagres do Maranhão', 'MILAGRES DO MARANHAO', 'M', 'MA', 'NE', 0),
(2106706, 'Mirador', 'MIRADOR', 'M', 'MA', 'NE', 0),
(2106755, 'Miranda do Norte', 'MIRANDA DO NORTE', 'M', 'MA', 'NE', 0),
(2106805, 'Mirinzal', 'MIRINZAL', 'M', 'MA', 'NE', 0),
(2106904, 'Monção', 'MONCAO', 'M', 'MA', 'NE', 0),
(2107001, 'Montes Altos', 'MONTES ALTOS', 'M', 'MA', 'NE', 0),
(2107100, 'Morros', 'MORROS', 'M', 'MA', 'NE', 0),
(2107209, 'Nina Rodrigues', 'NINA RODRIGUES', 'M', 'MA', 'NE', 0),
(2107258, 'Nova Colinas', 'NOVA COLINAS', 'M', 'MA', 'NE', 0),
(2107308, 'Nova Iorque', 'NOVA IORQUE', 'M', 'MA', 'NE', 0),
(2107357, 'Nova Olinda do Maranhão', 'NOVA OLINDA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2107407, 'Olho D''agua das Cunhas', 'OLHO D''AGUA DAS CUNHAS', 'M', 'MA', 'NE', 0),
(2107456, 'Olinda Nova do Maranhão', 'OLINDA NOVA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2107506, 'Paço do Lumiar', 'PACO DO LUMIAR', 'M', 'MA', 'NE', 0),
(2107605, 'Palmeirândia', 'PALMEIRANDIA', 'M', 'MA', 'NE', 0),
(2107704, 'Paraibano', 'PARAIBANO', 'M', 'MA', 'NE', 0),
(2107803, 'Parnarama', 'PARNARAMA', 'M', 'MA', 'NE', 0),
(2107902, 'Passagem Franca', 'PASSAGEM FRANCA', 'M', 'MA', 'NE', 0),
(2108009, 'Pastos Bons', 'PASTOS BONS', 'M', 'MA', 'NE', 0),
(2108058, 'Paulino Neves', 'PAULINO NEVES', 'M', 'MA', 'NE', 0),
(2108108, 'Paulo Ramos', 'PAULO RAMOS', 'M', 'MA', 'NE', 0),
(2108207, 'Pedreiras', 'PEDREIRAS', 'M', 'MA', 'NE', 0),
(2108256, 'Pedro do Rosário', 'PEDRO DO ROSARIO', 'M', 'MA', 'NE', 0),
(2108306, 'Penalva', 'PENALVA', 'M', 'MA', 'NE', 0),
(2108405, 'Peri Mirim', 'PERI MIRIM', 'M', 'MA', 'NE', 0),
(2108454, 'Peritoró', 'PERITORO', 'M', 'MA', 'NE', 0),
(2108504, 'Pindaré Mirim', 'PINDARE MIRIM', 'M', 'MA', 'NE', 0),
(2108603, 'Pinheiro', 'PINHEIRO', 'M', 'MA', 'NE', 0),
(2108702, 'Pio Xii', 'PIO XII', 'M', 'MA', 'NE', 0),
(2108801, 'Pirapemas', 'PIRAPEMAS', 'M', 'MA', 'NE', 0),
(2108900, 'Poção de Pedras', 'POCAO DE PEDRAS', 'M', 'MA', 'NE', 0),
(2109007, 'Porto Franco', 'PORTO FRANCO', 'M', 'MA', 'NE', 0),
(2109056, 'Porto Rico do Maranhão', 'PORTO RICO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2109106, 'Presidente Dutra', 'PRESIDENTE DUTRA', 'M', 'MA', 'NE', 0),
(2109205, 'Presidente Juscelino', 'PRESIDENTE JUSCELINO', 'M', 'MA', 'NE', 0),
(2109239, 'Presidente Médici', 'PRESIDENTE MEDICI', 'M', 'MA', 'NE', 0),
(2109270, 'Presidente Sarney', 'PRESIDENTE SARNEY', 'M', 'MA', 'NE', 0),
(2109304, 'Presidente Vargas', 'PRESIDENTE VARGAS', 'M', 'MA', 'NE', 0),
(2109403, 'Primeira Cruz', 'PRIMEIRA CRUZ', 'M', 'MA', 'NE', 0),
(2109452, 'Raposa', 'RAPOSA', 'M', 'MA', 'NE', 0),
(2109502, 'Riachão', 'RIACHAO', 'M', 'MA', 'NE', 0),
(2109551, 'Ribamar Fiquene', 'RIBAMAR FIQUENE', 'M', 'MA', 'NE', 0),
(2109601, 'Rosário', 'ROSARIO', 'M', 'MA', 'NE', 0),
(2109700, 'Sambaíba', 'SAMBAIBA', 'M', 'MA', 'NE', 0),
(2109759, 'Santa Filomena do Maranhao', 'SANTA FILOMENA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2109809, 'Santa Helena', 'SANTA HELENA', 'M', 'MA', 'NE', 0),
(2109908, 'Santa Inês', 'SANTA INES', 'M', 'MA', 'NE', 0),
(2110005, 'Santa Luzia', 'SANTA LUZIA', 'M', 'MA', 'NE', 0),
(2110039, 'Santa Luzia do Paruá', 'SANTA LUZIA DO PARUA', 'M', 'MA', 'NE', 0),
(2110104, 'Santa Quiteria do Maranhão', 'SANTA QUITERIA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2110203, 'Santa Rita', 'SANTA RITA', 'M', 'MA', 'NE', 0),
(2110237, 'Santana do Maranhão', 'SANTANA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2110278, 'Santo Amaro do Maranhão', 'SANTO AMARO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2110302, 'Santo Antônio dos Lopes', 'SANTO ANTONIO DOS LOPES', 'M', 'MA', 'NE', 0),
(2110401, 'São Benedito do Rio Preto', 'SAO BENEDITO DO RIO PRETO', 'M', 'MA', 'NE', 0),
(2110500, 'São Bento', 'SAO BENTO', 'M', 'MA', 'NE', 0),
(2110609, 'São Bernardo', 'SAO BERNARDO', 'M', 'MA', 'NE', 0),
(2110658, 'São Domingos do Azeitão', 'SAO DOMINGOS DO AZEITAO', 'M', 'MA', 'NE', 0),
(2110708, 'São Domingos do Maranhão', 'SAO DOMINGOS DO MARANHAO', 'M', 'MA', 'NE', 0),
(2110807, 'São Felix de Balsas', 'SAO FELIX DE BALSAS', 'M', 'MA', 'NE', 0),
(2110856, 'São Francisco do Brejão', 'SAO FRANCISCO DO BREJAO', 'M', 'MA', 'NE', 0),
(2110906, 'São Francisco do Maranhão', 'SAO FRANCISCO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2111003, 'São João Batista', 'SAO JOAO BATISTA', 'M', 'MA', 'NE', 0),
(2111029, 'São João do Caru', 'SAO JOAO DO CARU', 'M', 'MA', 'NE', 0),
(2111052, 'São João do Paraíso', 'SAO JOAO DO PARAISO', 'M', 'MA', 'NE', 0),
(2111078, 'São João do Soter', 'SAO JOAO DO SOTER', 'M', 'MA', 'NE', 0),
(2111102, 'São João dos Patos', 'SAO JOAO DOS PATOS', 'M', 'MA', 'NE', 0),
(2111201, 'São José de Ribamar', 'SAO JOSE DE RIBAMAR', 'M', 'MA', 'NE', 0),
(2111250, 'São José dos Basílios', 'SAO JOSE DOS BASILIOS', 'M', 'MA', 'NE', 0),
(2111300, 'São Luís', 'SAO LUIS', 'M', 'MA', 'NE', 0),
(2111409, 'São Luís Gonzaga do Maranhão', 'SAO LUIS GONZAGA DO MARANHAO', 'M', 'MA', 'NE', 0),
(2111508, 'São Mateus do Maranhão', 'SAO MATEUS DO MARANHAO', 'M', 'MA', 'NE', 0),
(2111532, 'São Pedro da Água Branca', 'SAO PEDRO DA AGUA BRANCA', 'M', 'MA', 'NE', 0),
(2111573, 'São Pedro dos Crentes', 'SAO PEDRO DOS CRENTES', 'M', 'MA', 'NE', 0),
(2111607, 'São Raimundo das Mangabeiras', 'SAO RAIMUNDO DAS MANGABEIRAS', 'M', 'MA', 'NE', 0),
(2111631, 'São Raimundo do Doca Bezerra', 'SAO RAIMUNDO DO DOCA BEZERRA', 'M', 'MA', 'NE', 0),
(2111672, 'São Roberto', 'SAO ROBERTO', 'M', 'MA', 'NE', 0),
(2111706, 'São Vicente Ferrer', 'SAO VICENTE FERRER', 'M', 'MA', 'NE', 0),
(2111722, 'Satubinha', 'SATUBINHA', 'M', 'MA', 'NE', 0),
(2111748, 'Senador Alexandre Costa', 'SENADOR ALEXANDRE COSTA', 'M', 'MA', 'NE', 0),
(2111763, 'Senador La Rocque', 'SENADOR LA ROCQUE', 'M', 'MA', 'NE', 0),
(2111789, 'Serrano do Maranhao', 'SERRANO DO MARANHAO', 'M', 'MA', 'NE', 0),
(2111805, 'Sítio Novo', 'SITIO NOVO', 'M', 'MA', 'NE', 0),
(2111904, 'Sucupira do Norte', 'SUCUPIRA DO NORTE', 'M', 'MA', 'NE', 0),
(2111953, 'Sucupira do Riachão', 'SUCUPIRA DO RIACHAO', 'M', 'MA', 'NE', 0),
(2112001, 'Tasso Fragoso', 'TASSO FRAGOSO', 'M', 'MA', 'NE', 0),
(2112100, 'Timbiras', 'TIMBIRAS', 'M', 'MA', 'NE', 0),
(2112209, 'Timon', 'TIMON', 'M', 'MA', 'NE', 0),
(2112233, 'Trizidela do Vale', 'TRIZIDELA DO VALE', 'M', 'MA', 'NE', 0),
(2112274, 'Tufilândia', 'TUFILANDIA', 'M', 'MA', 'NE', 0),
(2112308, 'Tuntum', 'TUNTUM', 'M', 'MA', 'NE', 0),
(2112407, 'Turiaçu', 'TURIACU', 'M', 'MA', 'NE', 0),
(2112456, 'Turilândia', 'TURILANDIA', 'M', 'MA', 'NE', 0),
(2112506, 'Tutóia', 'TUTOIA', 'M', 'MA', 'NE', 0),
(2112605, 'Urbano Santos', 'URBANO SANTOS', 'M', 'MA', 'NE', 0),
(2112704, 'Vargem Grande', 'VARGEM GRANDE', 'M', 'MA', 'NE', 0),
(2112803, 'Viana', 'VIANA', 'M', 'MA', 'NE', 0),
(2112852, 'Vila Nova dos Martírios', 'VILA NOVA DOS MARTIRIOS', 'M', 'MA', 'NE', 0),
(2112902, 'Vitória do Mearim', 'VITORIA DO MEARIM', 'M', 'MA', 'NE', 0),
(2113009, 'Vitorino Freire', 'VITORINO FREIRE', 'M', 'MA', 'NE', 0),
(2114007, 'Zé Doca', 'ZE DOCA', 'M', 'MA', 'NE', 0),
(2200000, 'Piauí', 'PIAUI', 'U', 'PI', 'NE', 0),
(2200053, 'Acauã', 'ACAUA', 'M', 'PI', 'NE', 0),
(2200103, 'Agricolândia', 'AGRICOLANDIA', 'M', 'PI', 'NE', 0),
(2200202, 'Água Branca', 'AGUA BRANCA', 'M', 'PI', 'NE', 0),
(2200251, 'Alagoinha do Piauí', 'ALAGOINHA DO PIAUI', 'M', 'PI', 'NE', 0),
(2200277, 'Alegrete do Piauí', 'ALEGRETE DO PIAUI', 'M', 'PI', 'NE', 0),
(2200301, 'Alto Longa', 'ALTO LONGA', 'M', 'PI', 'NE', 0),
(2200400, 'Altos', 'ALTOS', 'M', 'PI', 'NE', 0),
(2200459, 'Alvorada do Gurguéia', 'ALVORADA DO GURGUEIA', 'M', 'PI', 'NE', 0),
(2200509, 'Amarante', 'AMARANTE', 'M', 'PI', 'NE', 0),
(2200608, 'Angical do Piauí', 'ANGICAL DO PIAUI', 'M', 'PI', 'NE', 0),
(2200707, 'Anísio de Abreu', 'ANISIO DE ABREU', 'M', 'PI', 'NE', 0),
(2200806, 'Antônio Almeida', 'ANTONIO ALMEIDA', 'M', 'PI', 'NE', 0),
(2200905, 'Aroazes', 'AROAZES', 'M', 'PI', 'NE', 0),
(2201002, 'Arraial', 'ARRAIAL', 'M', 'PI', 'NE', 0),
(2201051, 'Assunção do Piauí', 'ASSUNCAO DO PIAUI', 'M', 'PI', 'NE', 0),
(2201101, 'Avelino Lopes', 'AVELINO LOPES', 'M', 'PI', 'NE', 0),
(2201150, 'Baixa Grande do Ribeiro', 'BAIXA GRANDE DO RIBEIRO', 'M', 'PI', 'NE', 0),
(2201176, 'Barra D''Alcântara', 'BARRA D''ALCANTARA', 'M', 'PI', 'NE', 0),
(2201200, 'Barras', 'BARRAS', 'M', 'PI', 'NE', 0),
(2201309, 'Barreiras do Piauí', 'BARREIRAS DO PIAUI', 'M', 'PI', 'NE', 0),
(2201408, 'Barro Duro', 'BARRO DURO', 'M', 'PI', 'NE', 0),
(2201507, 'Batalha', 'BATALHA', 'M', 'PI', 'NE', 0),
(2201556, 'Bela Vista do Piauí', 'BELA VISTA DO PIAUI', 'M', 'PI', 'NE', 0),
(2201572, 'Belem do Piauí', 'BELEM DO PIAUI', 'M', 'PI', 'NE', 0),
(2201606, 'Beneditinos', 'BENEDITINOS', 'M', 'PI', 'NE', 0),
(2201705, 'Bertolínia', 'BERTOLINIA', 'M', 'PI', 'NE', 0),
(2201739, 'Betânia do Piauí', 'BETANIA DO PIAUI', 'M', 'PI', 'NE', 0),
(2201770, 'Boa Hora', 'BOA HORA', 'M', 'PI', 'NE', 0),
(2201804, 'Bocaina', 'BOCAINA', 'M', 'PI', 'NE', 0),
(2201903, 'Bom Jesus', 'BOM JESUS', 'M', 'PI', 'NE', 0),
(2201919, 'Bom Princípio do Piauí', 'BOM PRINCIPIO DO PIAUI', 'M', 'PI', 'NE', 0),
(2201929, 'Bonfim do Piauí', 'BONFIM DO PIAUI', 'M', 'PI', 'NE', 0),
(2201945, 'Boqueirão do Piauí', 'BOQUEIRAO DO PIAUI', 'M', 'PI', 'NE', 0),
(2201960, 'Brasileira', 'BRASILEIRA', 'M', 'PI', 'NE', 0),
(2201988, 'Brejo do Piauí', 'BREJO DO PIAUI', 'M', 'PI', 'NE', 0),
(2202000, 'Buriti dos Lopes', 'BURITI DOS LOPES', 'M', 'PI', 'NE', 0),
(2202026, 'Buriti dos Montes', 'BURITI DOS MONTES', 'M', 'PI', 'NE', 0),
(2202059, 'Cabeceiras do Piauí', 'CABECEIRAS DO PIAUI', 'M', 'PI', 'NE', 0),
(2202075, 'Cajazeiras do Piauí', 'CAJAZEIRAS DO PIAUI', 'M', 'PI', 'NE', 0),
(2202083, 'Cajueiro da Praia', 'CAJUEIRO DA PRAIA', 'M', 'PI', 'NE', 0),
(2202091, 'Caldeirão Grande do Piauí', 'CALDEIRAO GRANDE DO PIAUI', 'M', 'PI', 'NE', 0),
(2202109, 'Campinas do Piauí', 'CAMPINAS DO PIAUI', 'M', 'PI', 'NE', 0),
(2202117, 'Campo Alegre do Fidalgo', 'CAMPO ALEGRE DO FIDALGO', 'M', 'PI', 'NE', 0),
(2202133, 'Campo Grande do Piauí', 'CAMPO GRANDE DO PIAUI', 'M', 'PI', 'NE', 0),
(2202174, 'Campo Largo do Piauí', 'CAMPO LARGO DO PIAUI', 'M', 'PI', 'NE', 0),
(2202208, 'Campo Maior', 'CAMPO MAIOR', 'M', 'PI', 'NE', 0),
(2202251, 'Canavieira', 'CANAVIEIRA', 'M', 'PI', 'NE', 0),
(2202307, 'Canto do Buriti', 'CANTO DO BURITI', 'M', 'PI', 'NE', 0),
(2202406, 'Capitao de Campos', 'CAPITAO DE CAMPOS', 'M', 'PI', 'NE', 0),
(2202455, 'Capitão Gervásio Oliveira', 'CAPITAO GERVASIO OLIVEIRA', 'M', 'PI', 'NE', 0),
(2202505, 'Caracol', 'CARACOL', 'M', 'PI', 'NE', 0),
(2202539, 'Caraubas do Piauí', 'CARAUBAS DO PIAUI', 'M', 'PI', 'NE', 0),
(2202554, 'Caridade do Piauí', 'CARIDADE DO PIAUI', 'M', 'PI', 'NE', 0),
(2202604, 'Castelo do Piauí', 'CASTELO DO PIAUI', 'M', 'PI', 'NE', 0),
(2202653, 'Caxingo', 'CAXINGO', 'M', 'PI', 'NE', 0),
(2202703, 'Cocal', 'COCAL', 'M', 'PI', 'NE', 0),
(2202711, 'Cocal de Telha', 'COCAL DE TELHA', 'M', 'PI', 'NE', 0),
(2202729, 'Cocal dos Alves', 'COCAL DOS ALVES', 'M', 'PI', 'NE', 0),
(2202737, 'Coivaras', 'COIVARAS', 'M', 'PI', 'NE', 0),
(2202752, 'Colônia do Gurgueia', 'COLONIA DO GURGUEIA', 'M', 'PI', 'NE', 0),
(2202778, 'Colônia do Piaui', 'COLONIA DO PIAUI', 'M', 'PI', 'NE', 0),
(2202802, 'Conceição do Canindé', 'CONCEICAO DO CANINDE', 'M', 'PI', 'NE', 0),
(2202851, 'Coronel José Dias', 'CORONEL JOSE DIAS', 'M', 'PI', 'NE', 0),
(2202901, 'Corrente', 'CORRENTE', 'M', 'PI', 'NE', 0),
(2203008, 'Cristalândia do Piauí', 'CRISTALANDIA DO PIAUI', 'M', 'PI', 'NE', 0),
(2203107, 'Cristino Castro', 'CRISTINO CASTRO', 'M', 'PI', 'NE', 0),
(2203206, 'Curimatá', 'CURIMATA', 'M', 'PI', 'NE', 0),
(2203230, 'Currais', 'CURRAIS', 'M', 'PI', 'NE', 0),
(2203255, 'Curralinhos', 'CURRALINHOS', 'M', 'PI', 'NE', 0),
(2203271, 'Curral Novo do Piauí', 'CURRAL NOVO DO PIAUI', 'M', 'PI', 'NE', 0),
(2203305, 'Demerval Lobão', 'DEMERVAL LOBAO', 'M', 'PI', 'NE', 0),
(2203354, 'Dirceu Arcoverde', 'DIRCEU ARCOVERDE', 'M', 'PI', 'NE', 0),
(2203404, 'Dom Expedito Lopes', 'DOM EXPEDITO LOPES', 'M', 'PI', 'NE', 0),
(2203420, 'Domingos Mourão', 'DOMINGOS MOURAO', 'M', 'PI', 'NE', 0),
(2203453, 'Dom Inocêncio', 'DOM INOCENCIO', 'M', 'PI', 'NE', 0),
(2203503, 'Elesbão Veloso', 'ELESBAO VELOSO', 'M', 'PI', 'NE', 0),
(2203602, 'Eliseu Martins', 'ELISEU MARTINS', 'M', 'PI', 'NE', 0),
(2203701, 'Esperantina', 'ESPERANTINA', 'M', 'PI', 'NE', 0),
(2203750, 'Fartura do Piauí', 'FARTURA DO PIAUI', 'M', 'PI', 'NE', 0),
(2203800, 'Flores do Piauí', 'FLORES DO PIAUI', 'M', 'PI', 'NE', 0),
(2203859, 'Floresta do Piauí', 'FLORESTA DO PIAUI', 'M', 'PI', 'NE', 0),
(2203909, 'Floriano', 'FLORIANO', 'M', 'PI', 'NE', 0),
(2204006, 'Francinópolis', 'FRANCINOPOLIS', 'M', 'PI', 'NE', 0),
(2204105, 'Francisco Ayres', 'FRANCISCO AYRES', 'M', 'PI', 'NE', 0),
(2204154, 'Francisco Macedo', 'FRANCISCO MACEDO', 'M', 'PI', 'NE', 0),
(2204204, 'Francisco Santos', 'FRANCISCO SANTOS', 'M', 'PI', 'NE', 0),
(2204303, 'Fronteiras', 'FRONTEIRAS', 'M', 'PI', 'NE', 0),
(2204352, 'Geminiano', 'GEMINIANO', 'M', 'PI', 'NE', 0),
(2204402, 'Gilbués', 'GILBUES', 'M', 'PI', 'NE', 0),
(2204501, 'Guadalupe', 'GUADALUPE', 'M', 'PI', 'NE', 0),
(2204550, 'Guaribas', 'GUARIBAS', 'M', 'PI', 'NE', 0),
(2204600, 'Hugo Napoleão', 'HUGO NAPOLEAO', 'M', 'PI', 'NE', 0),
(2204659, 'Ilha Grande', 'ILHA GRANDE', 'M', 'PI', 'NE', 0),
(2204709, 'Inhuma', 'INHUMA', 'M', 'PI', 'NE', 0),
(2204808, 'Ipiranga do Piauí', 'IPIRANGA DO PIAUI', 'M', 'PI', 'NE', 0),
(2204907, 'Isaías Coelho', 'ISAIAS COELHO', 'M', 'PI', 'NE', 0),
(2205003, 'Itainópolis', 'ITAINOPOLIS', 'M', 'PI', 'NE', 0),
(2205102, 'Itaueira', 'ITAUEIRA', 'M', 'PI', 'NE', 0),
(2205151, 'Jacobina do Piauí', 'JACOBINA DO PIAUI', 'M', 'PI', 'NE', 0),
(2205201, 'Jaicós', 'JAICOS', 'M', 'PI', 'NE', 0),
(2205250, 'Jardim do Mulato', 'JARDIM DO MULATO', 'M', 'PI', 'NE', 0),
(2205276, 'Jatoba do Piauí', 'JATOBA DO PIAUI', 'M', 'PI', 'NE', 0),
(2205300, 'Jerumenha', 'JERUMENHA', 'M', 'PI', 'NE', 0),
(2205359, 'João Costa', 'JOAO COSTA', 'M', 'PI', 'NE', 0),
(2205409, 'Joaquim Pires', 'JOAQUIM PIRES', 'M', 'PI', 'NE', 0),
(2205458, 'Joca Marques', 'JOCA MARQUES', 'M', 'PI', 'NE', 0),
(2205508, 'José de Freitas', 'JOSE DE FREITAS', 'M', 'PI', 'NE', 0),
(2205516, 'Juazeiro do Piauí', 'JUAZEIRO DO PIAUI', 'M', 'PI', 'NE', 0),
(2205524, 'Júlio Borges', 'JULIO BORGES', 'M', 'PI', 'NE', 0),
(2205532, 'Jurema', 'JUREMA', 'M', 'PI', 'NE', 0),
(2205540, 'Lagoinha do Piauí', 'LAGOINHA DO PIAUI', 'M', 'PI', 'NE', 0),
(2205557, 'Lagoa Alegre', 'LAGOA ALEGRE', 'M', 'PI', 'NE', 0),
(2205565, 'Lagoa do Barro do Piauí', 'LAGOA DO BARRO DO PIAUI', 'M', 'PI', 'NE', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(2205573, 'Lagoa de São Francisco', 'LAGOA DE SAO FRANCISCO', 'M', 'PI', 'NE', 0),
(2205581, 'Lagoa do Piauí', 'LAGOA DO PIAUI', 'M', 'PI', 'NE', 0),
(2205599, 'Lagoa do Sítio', 'LAGOA DO SITIO', 'M', 'PI', 'NE', 0),
(2205607, 'Landri Sales', 'LANDRI SALES', 'M', 'PI', 'NE', 0),
(2205706, 'Luís Correia', 'LUIS CORREIA', 'M', 'PI', 'NE', 0),
(2205805, 'Luzilândia', 'LUZILANDIA', 'M', 'PI', 'NE', 0),
(2205854, 'Madeiro', 'MADEIRO', 'M', 'PI', 'NE', 0),
(2205904, 'Manoel Emidio', 'MANOEL EMIDIO', 'M', 'PI', 'NE', 0),
(2205953, 'Marcolândia', 'MARCOLANDIA', 'M', 'PI', 'NE', 0),
(2206001, 'Marcos Parente', 'MARCOS PARENTE', 'M', 'PI', 'NE', 0),
(2206050, 'Massâpe do Piauí', 'MASSAPE DO PIAUI', 'M', 'PI', 'NE', 0),
(2206100, 'Matias Olímpio', 'MATIAS OLIMPIO', 'M', 'PI', 'NE', 0),
(2206209, 'Miguel Alves', 'MIGUEL ALVES', 'M', 'PI', 'NE', 0),
(2206308, 'Miguel Leão', 'MIGUEL LEAO', 'M', 'PI', 'NE', 0),
(2206357, 'Milton Brandão', 'MILTON BRANDAO', 'M', 'PI', 'NE', 0),
(2206407, 'Monsenhor Gil', 'MONSENHOR GIL', 'M', 'PI', 'NE', 0),
(2206506, 'Monsenhor Hipólito', 'MONSENHOR HIPOLITO', 'M', 'PI', 'NE', 0),
(2206605, 'Monte Alegre do Piauí', 'MONTE ALEGRE DO PIAUI', 'M', 'PI', 'NE', 0),
(2206654, 'Morro Cabeça No Tempo', 'MORRO CABECA NO TEMPO', 'M', 'PI', 'NE', 0),
(2206670, 'Morro do Chapeu do Piauí', 'MORRO DO CHAPEU DO PIAUI', 'M', 'PI', 'NE', 0),
(2206696, 'Murici dos Portelas', 'MURICI DOS PORTELAS', 'M', 'PI', 'NE', 0),
(2206704, 'Nazaré do Piauí', 'NAZARE DO PIAUI', 'M', 'PI', 'NE', 0),
(2206753, 'Nossa Senhora de Nazaré', 'NOSSA SENHORA DE NAZARE', 'M', 'PI', 'NE', 0),
(2206803, 'Nossa Senhora dos Remédios', 'NOSSA SENHORA DOS REMEDIOS', 'M', 'PI', 'NE', 0),
(2206902, 'Novo Oriente do Piauí', 'NOVO ORIENTE DO PIAUI', 'M', 'PI', 'NE', 0),
(2206951, 'Novo Santo Antônio', 'NOVO SANTO ANTONIO', 'M', 'PI', 'NE', 0),
(2207009, 'Oeiras', 'OEIRAS', 'M', 'PI', 'NE', 0),
(2207108, 'Olho D''Água do Piauí', 'OLHO D''AGUA DO PIAUI', 'M', 'PI', 'NE', 0),
(2207207, 'Padre Marcos', 'PADRE MARCOS', 'M', 'PI', 'NE', 0),
(2207306, 'Paes Landim', 'PAES LANDIM', 'M', 'PI', 'NE', 0),
(2207355, 'Pajeu do Piauí', 'PAJEU DO PIAUI', 'M', 'PI', 'NE', 0),
(2207405, 'Palmeira do Piauí', 'PALMEIRA DO PIAUI', 'M', 'PI', 'NE', 0),
(2207504, 'Palmeirais', 'PALMEIRAIS', 'M', 'PI', 'NE', 0),
(2207553, 'Paquetá', 'PAQUETA', 'M', 'PI', 'NE', 0),
(2207603, 'Parnaguá', 'PARNAGUA', 'M', 'PI', 'NE', 0),
(2207702, 'Parnaíba', 'PARNAIBA', 'M', 'PI', 'NE', 0),
(2207751, 'Passagem Franca do Piauí', 'PASSAGEM FRANCA DO PIAUI', 'M', 'PI', 'NE', 0),
(2207777, 'Patos do Piauí', 'PATOS DO PIAUI', 'M', 'PI', 'NE', 0),
(2207793, 'Pau D''Arco do Piauí', 'PAU D''ARCO DO PIAUI', 'M', 'PI', 'NE', 0),
(2207801, 'Paulistana', 'PAULISTANA', 'M', 'PI', 'NE', 0),
(2207850, 'Pavussu', 'PAVUSSU', 'M', 'PI', 'NE', 0),
(2207900, 'Pedro II', 'PEDRO II', 'M', 'PI', 'NE', 0),
(2207934, 'Pedro Laurentino', 'PEDRO LAURENTINO', 'M', 'PI', 'NE', 0),
(2207959, 'Nova Santa Rita', 'NOVA SANTA RITA', 'M', 'PI', 'NE', 0),
(2208007, 'Picos', 'PICOS', 'M', 'PI', 'NE', 0),
(2208106, 'Pimenteiras', 'PIMENTEIRAS', 'M', 'PI', 'NE', 0),
(2208205, 'Pio IX', 'PIO IX', 'M', 'PI', 'NE', 0),
(2208304, 'Piracuruca', 'PIRACURUCA', 'M', 'PI', 'NE', 0),
(2208403, 'Piripiri', 'PIRIPIRI', 'M', 'PI', 'NE', 0),
(2208502, 'Porto', 'PORTO', 'M', 'PI', 'NE', 0),
(2208551, 'Porto Alegre do Piauí', 'PORTO ALEGRE DO PIAUI', 'M', 'PI', 'NE', 0),
(2208601, 'Prata do Piauí', 'PRATA DO PIAUI', 'M', 'PI', 'NE', 0),
(2208650, 'Queimada Nova', 'QUEIMADA NOVA', 'M', 'PI', 'NE', 0),
(2208700, 'Redencao do Gurgueia', 'REDENCAO DO GURGUEIA', 'M', 'PI', 'NE', 0),
(2208809, 'Regeneração', 'REGENERACAO', 'M', 'PI', 'NE', 0),
(2208858, 'Riacho Frio', 'RIACHO FRIO', 'M', 'PI', 'NE', 0),
(2208874, 'Ribeira do Piauí', 'RIBEIRA DO PIAUI', 'M', 'PI', 'NE', 0),
(2208908, 'Ribeiro Gonçalves', 'RIBEIRO GONCALVES', 'M', 'PI', 'NE', 0),
(2209005, 'Rio Grande do Piauí', 'RIO GRANDE DO PIAUI', 'M', 'PI', 'NE', 0),
(2209104, 'Santa Cruz do Piauí', 'SANTA CRUZ DO PIAUI', 'M', 'PI', 'NE', 0),
(2209153, 'Santa Cruz dos Milagres', 'SANTA CRUZ DOS MILAGRES', 'M', 'PI', 'NE', 0),
(2209203, 'Santa Filomena', 'SANTA FILOMENA', 'M', 'PI', 'NE', 0),
(2209302, 'Santa Luz', 'SANTA LUZ', 'M', 'PI', 'NE', 0),
(2209351, 'Santana do Piauí', 'SANTANA DO PIAUI', 'M', 'PI', 'NE', 0),
(2209377, 'Santa Rosa do Piauí', 'SANTA ROSA DO PIAUI', 'M', 'PI', 'NE', 0),
(2209401, 'Santo Antônio de Lisboa', 'SANTO ANTONIO DE LISBOA', 'M', 'PI', 'NE', 0),
(2209450, 'Santo Antônio dos Milagres', 'SANTO ANTONIO DOS MILAGRES', 'M', 'PI', 'NE', 0),
(2209500, 'Santo Inácio do Piauí', 'SANTO INACIO DO PIAUI', 'M', 'PI', 'NE', 0),
(2209559, 'São Braz do Piauí', 'SAO BRAZ DO PIAUI', 'M', 'PI', 'NE', 0),
(2209609, 'São Félix do Piauí', 'SAO FELIX DO PIAUI', 'M', 'PI', 'NE', 0),
(2209658, 'São Francisco de Assis do Piauí', 'SAO FRANCISCO DE ASSIS DO PIAUI', 'M', 'PI', 'NE', 0),
(2209708, 'São Francisco do Piauí', 'SAO FRANCISCO DO PIAUI', 'M', 'PI', 'NE', 0),
(2209757, 'São Goncalo do Gurgueia', 'SAO GONCALO DO GURGUEIA', 'M', 'PI', 'NE', 0),
(2209807, 'São Goncalo do Piauí', 'SAO GONCALO DO PIAUI', 'M', 'PI', 'NE', 0),
(2209856, 'São João da Canabrava', 'SAO JOAO DA CANABRAVA', 'M', 'PI', 'NE', 0),
(2209872, 'São João da Fronteira', 'SAO JOAO DA FRONTEIRA', 'M', 'PI', 'NE', 0),
(2209906, 'São João da Serra', 'SAO JOAO DA SERRA', 'M', 'PI', 'NE', 0),
(2209955, 'São João da Varjota', 'SAO JOAO DA VARJOTA', 'M', 'PI', 'NE', 0),
(2209971, 'São João do Arraial', 'SAO JOAO DO ARRAIAL', 'M', 'PI', 'NE', 0),
(2210003, 'São João do Piauí', 'SAO JOAO DO PIAUI', 'M', 'PI', 'NE', 0),
(2210052, 'São José do Divino', 'SAO JOSE DO DIVINO', 'M', 'PI', 'NE', 0),
(2210102, 'São José do Peixe', 'SAO JOSE DO PEIXE', 'M', 'PI', 'NE', 0),
(2210201, 'São Jose do Piauí', 'SAO JOSE DO PIAUI', 'M', 'PI', 'NE', 0),
(2210300, 'São Julião', 'SAO JULIAO', 'M', 'PI', 'NE', 0),
(2210359, 'São Lourenço do Piauí', 'SAO LOURENCO DO PIAUI', 'M', 'PI', 'NE', 0),
(2210375, 'São Luis do Piauí', 'SAO LUIS DO PIAUI', 'M', 'PI', 'NE', 0),
(2210383, 'São Miguel da Baixa Grande', 'SAO MIGUEL DA BAIXA GRANDE', 'M', 'PI', 'NE', 0),
(2210391, 'São Miguel do Fidalgo', 'SAO MIGUEL DO FIDALGO', 'M', 'PI', 'NE', 0),
(2210409, 'São Miguel do Tapuio', 'SAO MIGUEL DO TAPUIO', 'M', 'PI', 'NE', 0),
(2210508, 'São Pedro do Piaui', 'SAO PEDRO DO PIAUI', 'M', 'PI', 'NE', 0),
(2210607, 'São Raimundo Nonato', 'SAO RAIMUNDO NONATO', 'M', 'PI', 'NE', 0),
(2210623, 'Sebastiao Barros', 'SEBASTIAO BARROS', 'M', 'PI', 'NE', 0),
(2210631, 'Sebastiao Leal', 'SEBASTIAO LEAL', 'M', 'PI', 'NE', 0),
(2210656, 'Sigefredo Pacheco', 'SIGEFREDO PACHECO', 'M', 'PI', 'NE', 0),
(2210706, 'Simões', 'SIMOES', 'M', 'PI', 'NE', 0),
(2210805, 'Simplício Mendes', 'SIMPLICIO MENDES', 'M', 'PI', 'NE', 0),
(2210904, 'Socorro do Piauí', 'SOCORRO DO PIAUI', 'M', 'PI', 'NE', 0),
(2210938, 'Sussuapara', 'SUSSUAPARA', 'M', 'PI', 'NE', 0),
(2210953, 'Tamboril do Piauí', 'TAMBORIL DO PIAUI', 'M', 'PI', 'NE', 0),
(2210979, 'Tanque do Piauí', 'TANQUE DO PIAUI', 'M', 'PI', 'NE', 0),
(2211001, 'Teresina', 'TERESINA', 'M', 'PI', 'NE', 0),
(2211100, 'União', 'UNIAO', 'M', 'PI', 'NE', 0),
(2211209, 'Uruçuí', 'URUCUI', 'M', 'PI', 'NE', 0),
(2211308, 'Valença do Piauí', 'VALENCA DO PIAUI', 'M', 'PI', 'NE', 0),
(2211357, 'Várzea Branca', 'VARZEA BRANCA', 'M', 'PI', 'NE', 0),
(2211407, 'Várzea Grande', 'VARZEA GRANDE', 'M', 'PI', 'NE', 0),
(2211506, 'Vera Mendes', 'VERA MENDES', 'M', 'PI', 'NE', 0),
(2211605, 'Vila Nova do Piauí', 'VILA NOVA DO PIAUI', 'M', 'PI', 'NE', 0),
(2211704, 'Wall Ferraz', 'WALL FERRAZ', 'M', 'PI', 'NE', 0),
(2300000, 'Ceará', 'CEARA', 'U', 'CE', 'NE', 0),
(2300101, 'Abaiara', 'ABAIARA', 'M', 'CE', 'NE', 0),
(2300150, 'Acarapé', 'ACARAPE', 'M', 'CE', 'NE', 0),
(2300200, 'Acaraú', 'ACARAU', 'M', 'CE', 'NE', 0),
(2300309, 'Acopiara', 'ACOPIARA', 'M', 'CE', 'NE', 0),
(2300408, 'Aiuaba', 'AIUABA', 'M', 'CE', 'NE', 0),
(2300507, 'Alcântaras', 'ALCANTARAS', 'M', 'CE', 'NE', 0),
(2300606, 'Altaneira', 'ALTANEIRA', 'M', 'CE', 'NE', 0),
(2300705, 'Alto Santo', 'ALTO SANTO', 'M', 'CE', 'NE', 0),
(2300754, 'Amontada', 'AMONTADA', 'M', 'CE', 'NE', 0),
(2300804, 'Antonina do Norte', 'ANTONINA DO NORTE', 'M', 'CE', 'NE', 0),
(2300903, 'Apuiarés', 'APUIARES', 'M', 'CE', 'NE', 0),
(2301000, 'Aquiraz', 'AQUIRAZ', 'M', 'CE', 'NE', 0),
(2301109, 'Aracati', 'ARACATI', 'M', 'CE', 'NE', 0),
(2301208, 'Aracoiaba', 'ARACOIABA', 'M', 'CE', 'NE', 0),
(2301257, 'Ararendá', 'ARARENDA', 'M', 'CE', 'NE', 0),
(2301307, 'Araripe', 'ARARIPE', 'M', 'CE', 'NE', 0),
(2301406, 'Aratuba', 'ARATUBA', 'M', 'CE', 'NE', 0),
(2301505, 'Arneiroz', 'ARNEIROZ', 'M', 'CE', 'NE', 0),
(2301604, 'Assaré', 'ASSARE', 'M', 'CE', 'NE', 0),
(2301703, 'Aurora', 'AURORA', 'M', 'CE', 'NE', 0),
(2301802, 'Baixio', 'BAIXIO', 'M', 'CE', 'NE', 0),
(2301851, 'Banabuiú', 'BANABUIU', 'M', 'CE', 'NE', 0),
(2301901, 'Barbalha', 'BARBALHA', 'M', 'CE', 'NE', 0),
(2301950, 'Barreira', 'BARREIRA', 'M', 'CE', 'NE', 0),
(2302008, 'Barro', 'BARRO', 'M', 'CE', 'NE', 0),
(2302057, 'Barroquinha', 'BARROQUINHA', 'M', 'CE', 'NE', 0),
(2302107, 'Baturité', 'BATURITE', 'M', 'CE', 'NE', 0),
(2302206, 'Beberibe', 'BEBERIBE', 'M', 'CE', 'NE', 0),
(2302305, 'Bela Cruz', 'BELA CRUZ', 'M', 'CE', 'NE', 0),
(2302404, 'Boa Viagem', 'BOA VIAGEM', 'M', 'CE', 'NE', 0),
(2302503, 'Brejo Santo', 'BREJO SANTO', 'M', 'CE', 'NE', 0),
(2302602, 'Camocim', 'CAMOCIM', 'M', 'CE', 'NE', 0),
(2302701, 'Campos Sales', 'CAMPOS SALES', 'M', 'CE', 'NE', 0),
(2302800, 'Caninde', 'CANINDE', 'M', 'CE', 'NE', 0),
(2302909, 'Capistrano', 'CAPISTRANO', 'M', 'CE', 'NE', 0),
(2303006, 'Caridade', 'CARIDADE', 'M', 'CE', 'NE', 0),
(2303105, 'Cariré', 'CARIRE', 'M', 'CE', 'NE', 0),
(2303204, 'Caririacu', 'CARIRIACU', 'M', 'CE', 'NE', 0),
(2303303, 'Cariús', 'CARIUS', 'M', 'CE', 'NE', 0),
(2303402, 'Carnaubal', 'CARNAUBAL', 'M', 'CE', 'NE', 0),
(2303501, 'Cascavél', 'CASCAVEL', 'M', 'CE', 'NE', 0),
(2303600, 'Catarina', 'CATARINA', 'M', 'CE', 'NE', 0),
(2303659, 'Catunda', 'CATUNDA', 'M', 'CE', 'NE', 0),
(2303709, 'Caucaia', 'CAUCAIA', 'M', 'CE', 'NE', 0),
(2303808, 'Cedro', 'CEDRO', 'M', 'CE', 'NE', 0),
(2303907, 'Chaval', 'CHAVAL', 'M', 'CE', 'NE', 0),
(2303931, 'Choró', 'CHORO', 'M', 'CE', 'NE', 0),
(2303956, 'Chorozinho', 'CHOROZINHO', 'M', 'CE', 'NE', 0),
(2304004, 'Coreaú', 'COREAU', 'M', 'CE', 'NE', 0),
(2304103, 'Crateus', 'CRATEUS', 'M', 'CE', 'NE', 0),
(2304202, 'Crato', 'CRATO', 'M', 'CE', 'NE', 0),
(2304236, 'Croata', 'CROATA', 'M', 'CE', 'NE', 0),
(2304251, 'Cruz', 'CRUZ', 'M', 'CE', 'NE', 0),
(2304269, 'Deputado Irapuan Pinheiro', 'DEPUTADO IRAPUAN PINHEIRO', 'M', 'CE', 'NE', 0),
(2304277, 'Erere', 'ERERE', 'M', 'CE', 'NE', 0),
(2304285, 'Eusébio', 'EUSEBIO', 'M', 'CE', 'NE', 0),
(2304301, 'Farias Brito', 'FARIAS BRITO', 'M', 'CE', 'NE', 0),
(2304350, 'Forquilha', 'FORQUILHA', 'M', 'CE', 'NE', 0),
(2304400, 'Fortaleza', 'FORTALEZA', 'M', 'CE', 'NE', 0),
(2304459, 'Fortim', 'FORTIM', 'M', 'CE', 'NE', 0),
(2304509, 'Frecheirinha', 'FRECHEIRINHA', 'M', 'CE', 'NE', 0),
(2304608, 'General Sampaio', 'GENERAL SAMPAIO', 'M', 'CE', 'NE', 0),
(2304657, 'Graça', 'GRACA', 'M', 'CE', 'NE', 0),
(2304707, 'Granja', 'GRANJA', 'M', 'CE', 'NE', 0),
(2304806, 'Granjeiro', 'GRANJEIRO', 'M', 'CE', 'NE', 0),
(2304905, 'Groairas', 'GROAIRAS', 'M', 'CE', 'NE', 0),
(2304954, 'Guaiúba', 'GUAIUBA', 'M', 'CE', 'NE', 0),
(2305001, 'Guaraciaba do Norte', 'GUARACIABA DO NORTE', 'M', 'CE', 'NE', 0),
(2305100, 'Guaramiranga', 'GUARAMIRANGA', 'M', 'CE', 'NE', 0),
(2305209, 'Hidrolândia', 'HIDROLANDIA', 'M', 'CE', 'NE', 0),
(2305233, 'Horizonte', 'HORIZONTE', 'M', 'CE', 'NE', 0),
(2305266, 'Ibaretama', 'IBARETAMA', 'M', 'CE', 'NE', 0),
(2305308, 'Ibiapina', 'IBIAPINA', 'M', 'CE', 'NE', 0),
(2305332, 'Ibicuitinga', 'IBICUITINGA', 'M', 'CE', 'NE', 0),
(2305357, 'Icapuí', 'ICAPUI', 'M', 'CE', 'NE', 0),
(2305407, 'Icó', 'ICO', 'M', 'CE', 'NE', 0),
(2305506, 'Iguatú', 'IGUATU', 'M', 'CE', 'NE', 0),
(2305605, 'Independência', 'INDEPENDENCIA', 'M', 'CE', 'NE', 0),
(2305654, 'Ipaporanga', 'IPAPORANGA', 'M', 'CE', 'NE', 0),
(2305704, 'Ipaumirim', 'IPAUMIRIM', 'M', 'CE', 'NE', 0),
(2305803, 'Ipu', 'IPU', 'M', 'CE', 'NE', 0),
(2305902, 'Ipueiras', 'IPUEIRAS', 'M', 'CE', 'NE', 0),
(2306009, 'Iracema', 'IRACEMA', 'M', 'CE', 'NE', 0),
(2306108, 'Iraucuba', 'IRAUCUBA', 'M', 'CE', 'NE', 0),
(2306207, 'Itaiçaba', 'ITAICABA', 'M', 'CE', 'NE', 0),
(2306256, 'Itaitinga', 'ITAITINGA', 'M', 'CE', 'NE', 0),
(2306306, 'Itapaje', 'ITAPAJE', 'M', 'CE', 'NE', 0),
(2306405, 'Itapipoca', 'ITAPIPOCA', 'M', 'CE', 'NE', 0),
(2306504, 'Itapiuna', 'ITAPIUNA', 'M', 'CE', 'NE', 0),
(2306553, 'Itarema', 'ITAREMA', 'M', 'CE', 'NE', 0),
(2306603, 'Itatira', 'ITATIRA', 'M', 'CE', 'NE', 0),
(2306702, 'Jaguaretama', 'JAGUARETAMA', 'M', 'CE', 'NE', 0),
(2306801, 'Jaguaribara', 'JAGUARIBARA', 'M', 'CE', 'NE', 0),
(2306900, 'Jaguaribe', 'JAGUARIBE', 'M', 'CE', 'NE', 0),
(2307007, 'Jaguaruana', 'JAGUARUANA', 'M', 'CE', 'NE', 0),
(2307106, 'Jardim', 'JARDIM', 'M', 'CE', 'NE', 0),
(2307205, 'Jati', 'JATI', 'M', 'CE', 'NE', 0),
(2307254, 'Jijoca de Jericoacoara', 'JIJOCA DE JERICOACOARA', 'M', 'CE', 'NE', 0),
(2307304, 'Juazeiro do Norte', 'JUAZEIRO DO NORTE', 'M', 'CE', 'NE', 0),
(2307403, 'Jucás', 'JUCAS', 'M', 'CE', 'NE', 0),
(2307502, 'Lavras da Mangabeira', 'LAVRAS DA MANGABEIRA', 'M', 'CE', 'NE', 0),
(2307601, 'Limoeiro do Norte', 'LIMOEIRO DO NORTE', 'M', 'CE', 'NE', 0),
(2307635, 'Madalena', 'MADALENA', 'M', 'CE', 'NE', 0),
(2307650, 'Maracanaú', 'MARACANAU', 'M', 'CE', 'NE', 0),
(2307700, 'Maranguape', 'MARANGUAPE', 'M', 'CE', 'NE', 0),
(2307809, 'Marco', 'MARCO', 'M', 'CE', 'NE', 0),
(2307908, 'Martinoópole', 'MARTINOPOLE', 'M', 'CE', 'NE', 0),
(2308005, 'Massape', 'MASSAPE', 'M', 'CE', 'NE', 0),
(2308104, 'Mauriti', 'MAURITI', 'M', 'CE', 'NE', 0),
(2308203, 'Meruoca', 'MERUOCA', 'M', 'CE', 'NE', 0),
(2308302, 'Milagres', 'MILAGRES', 'M', 'CE', 'NE', 0),
(2308351, 'Milhã', 'MILHA', 'M', 'CE', 'NE', 0),
(2308377, 'Miraíma', 'MIRAIMA', 'M', 'CE', 'NE', 0),
(2308401, 'Missão Velha', 'MISSAO VELHA', 'M', 'CE', 'NE', 0),
(2308500, 'Mombaca', 'MOMBACA', 'M', 'CE', 'NE', 0),
(2308609, 'Monsenhor Tabosa', 'MONSENHOR TABOSA', 'M', 'CE', 'NE', 0),
(2308708, 'Morada Nova', 'MORADA NOVA', 'M', 'CE', 'NE', 0),
(2308807, 'Moraújo', 'MORAUJO', 'M', 'CE', 'NE', 0),
(2308906, 'Morrinhos', 'MORRINHOS', 'M', 'CE', 'NE', 0),
(2309003, 'Mucambo', 'MUCAMBO', 'M', 'CE', 'NE', 0),
(2309102, 'Mulungu', 'MULUNGU', 'M', 'CE', 'NE', 0),
(2309201, 'Nova Olinda', 'NOVA OLINDA', 'M', 'CE', 'NE', 0),
(2309300, 'Nova Russas', 'NOVA RUSSAS', 'M', 'CE', 'NE', 0),
(2309409, 'Novo Oriente', 'NOVO ORIENTE', 'M', 'CE', 'NE', 0),
(2309458, 'Ocara', 'OCARA', 'M', 'CE', 'NE', 0),
(2309508, 'Orós', 'OROS', 'M', 'CE', 'NE', 0),
(2309607, 'Pacajus', 'PACAJUS', 'M', 'CE', 'NE', 0),
(2309706, 'Pacatuba', 'PACATUBA', 'M', 'CE', 'NE', 0),
(2309805, 'Pacoti', 'PACOTI', 'M', 'CE', 'NE', 0),
(2309904, 'Pacujá', 'PACUJA', 'M', 'CE', 'NE', 0),
(2310001, 'Palhano', 'PALHANO', 'M', 'CE', 'NE', 0),
(2310100, 'Palmácia', 'PALMACIA', 'M', 'CE', 'NE', 0),
(2310209, 'Paracuru', 'PARACURU', 'M', 'CE', 'NE', 0),
(2310258, 'Paraipaba', 'PARAIPABA', 'M', 'CE', 'NE', 0),
(2310308, 'Parambu', 'PARAMBU', 'M', 'CE', 'NE', 0),
(2310407, 'Paramoti', 'PARAMOTI', 'M', 'CE', 'NE', 0),
(2310506, 'Pedra Branca', 'PEDRA BRANCA', 'M', 'CE', 'NE', 0),
(2310605, 'Penaforte', 'PENAFORTE', 'M', 'CE', 'NE', 0),
(2310704, 'Pentecoste', 'PENTECOSTE', 'M', 'CE', 'NE', 0),
(2310803, 'Pereiro', 'PEREIRO', 'M', 'CE', 'NE', 0),
(2310852, 'Pindoretama', 'PINDORETAMA', 'M', 'CE', 'NE', 0),
(2310902, 'Piquet Carneiro', 'PIQUET CARNEIRO', 'M', 'CE', 'NE', 0),
(2310951, 'Pires Ferreira', 'PIRES FERREIRA', 'M', 'CE', 'NE', 0),
(2311009, 'Poranga', 'PORANGA', 'M', 'CE', 'NE', 0),
(2311108, 'Porteiras', 'PORTEIRAS', 'M', 'CE', 'NE', 0),
(2311207, 'Potengi', 'POTENGI', 'M', 'CE', 'NE', 0),
(2311231, 'Potiretama', 'POTIRETAMA', 'M', 'CE', 'NE', 0),
(2311264, 'Quiterianópolis', 'QUITERIANOPOLIS', 'M', 'CE', 'NE', 0),
(2311306, 'Quixada', 'QUIXADA', 'M', 'CE', 'NE', 0),
(2311355, 'Quixelo', 'QUIXELO', 'M', 'CE', 'NE', 0),
(2311405, 'Quixeramobim', 'QUIXERAMOBIM', 'M', 'CE', 'NE', 0),
(2311504, 'Quixeré', 'QUIXERE', 'M', 'CE', 'NE', 0),
(2311603, 'Redenção', 'REDENCAO', 'M', 'CE', 'NE', 0),
(2311702, 'Reriutaba', 'RERIUTABA', 'M', 'CE', 'NE', 0),
(2311801, 'Russas', 'RUSSAS', 'M', 'CE', 'NE', 0),
(2311900, 'Saboeiro', 'SABOEIRO', 'M', 'CE', 'NE', 0),
(2311959, 'Salitre', 'SALITRE', 'M', 'CE', 'NE', 0),
(2312007, 'Santana do Acaraú', 'SANTANA DO ACARAU', 'M', 'CE', 'NE', 0),
(2312106, 'Santana do Cariri', 'SANTANA DO CARIRI', 'M', 'CE', 'NE', 0),
(2312205, 'Santa Quitéria', 'SANTA QUITERIA', 'M', 'CE', 'NE', 0),
(2312304, 'São Benedito', 'SAO BENEDITO', 'M', 'CE', 'NE', 0),
(2312403, 'São Gonçalo do Amarante', 'SAO GONCALO DO AMARANTE', 'M', 'CE', 'NE', 0),
(2312502, 'São João do Jaguaribe', 'SAO JOAO DO JAGUARIBE', 'M', 'CE', 'NE', 0),
(2312601, 'São Luís do Curu', 'SAO LUIS DO CURU', 'M', 'CE', 'NE', 0),
(2312700, 'Senador Pompeu', 'SENADOR POMPEU', 'M', 'CE', 'NE', 0),
(2312809, 'Senador Sá', 'SENADOR SA', 'M', 'CE', 'NE', 0),
(2312908, 'Sobral', 'SOBRAL', 'M', 'CE', 'NE', 0),
(2313005, 'Solonópole', 'SOLONOPOLE', 'M', 'CE', 'NE', 0),
(2313104, 'Tabuleiro do Norte', 'TABULEIRO DO NORTE', 'M', 'CE', 'NE', 0),
(2313203, 'Tamboril', 'TAMBORIL', 'M', 'CE', 'NE', 0),
(2313252, 'Tarrafas', 'TARRAFAS', 'M', 'CE', 'NE', 0),
(2313302, 'Tauá', 'TAUA', 'M', 'CE', 'NE', 0),
(2313351, 'Tejucuoca', 'TEJUCUOCA', 'M', 'CE', 'NE', 0),
(2313401, 'Tianguá', 'TIANGUA', 'M', 'CE', 'NE', 0),
(2313500, 'Trairi', 'TRAIRI', 'M', 'CE', 'NE', 0),
(2313559, 'Tururu', 'TURURU', 'M', 'CE', 'NE', 0),
(2313609, 'Ubajara', 'UBAJARA', 'M', 'CE', 'NE', 0),
(2313708, 'Umari', 'UMARI', 'M', 'CE', 'NE', 0),
(2313757, 'Umirim', 'UMIRIM', 'M', 'CE', 'NE', 0),
(2313807, 'Uruburetama', 'URUBURETAMA', 'M', 'CE', 'NE', 0),
(2313906, 'Uruoca', 'URUOCA', 'M', 'CE', 'NE', 0),
(2313955, 'Varjota', 'VARJOTA', 'M', 'CE', 'NE', 0),
(2314003, 'Varzea Alegre', 'VARZEA ALEGRE', 'M', 'CE', 'NE', 0),
(2314102, 'Viçosa do Ceará', 'VICOSA DO CEARA', 'M', 'CE', 'NE', 0),
(2400000, 'Rio Grande do Norte', 'RIO GRANDE DO NORTE', 'U', 'RN', 'NE', 0),
(2400109, 'Acari', 'ACARI', 'M', 'RN', 'NE', 0),
(2400208, 'Açu', 'ACU', 'M', 'RN', 'NE', 0),
(2400307, 'Afonso Bezerra', 'AFONSO BEZERRA', 'M', 'RN', 'NE', 0),
(2400406, 'Água Nova', 'AGUA NOVA', 'M', 'RN', 'NE', 0),
(2400505, 'Alexandria', 'ALEXANDRIA', 'M', 'RN', 'NE', 0),
(2400604, 'Almino Afonso', 'ALMINO AFONSO', 'M', 'RN', 'NE', 0),
(2400703, 'Alto do Rodrigues', 'ALTO DO RODRIGUES', 'M', 'RN', 'NE', 0),
(2400802, 'Angicos', 'ANGICOS', 'M', 'RN', 'NE', 0),
(2400901, 'Antônio Martins', 'ANTONIO MARTINS', 'M', 'RN', 'NE', 0),
(2401008, 'Apodi', 'APODI', 'M', 'RN', 'NE', 0),
(2401107, 'Areia Branca', 'AREIA BRANCA', 'M', 'RN', 'NE', 0),
(2401206, 'Arês', 'ARES', 'M', 'RN', 'NE', 0),
(2401305, 'Augusto Severo', 'AUGUSTO SEVERO', 'M', 'RN', 'NE', 0),
(2401404, 'Baia Formosa', 'BAIA FORMOSA', 'M', 'RN', 'NE', 0),
(2401453, 'Barauú', 'BARAUNA', 'M', 'RN', 'NE', 0),
(2401503, 'Barcelona', 'BARCELONA', 'M', 'RN', 'NE', 0),
(2401602, 'Bento Fernandes', 'BENTO FERNANDES', 'M', 'RN', 'NE', 0),
(2401651, 'Bodó', 'BODO', 'M', 'RN', 'NE', 0),
(2401701, 'Bom Jesus', 'BOM JESUS', 'M', 'RN', 'NE', 0),
(2401800, 'Brejinho', 'BREJINHO', 'M', 'RN', 'NE', 0),
(2401859, 'Caiçara do Norte', 'CAICARA DO NORTE', 'M', 'RN', 'NE', 0),
(2401909, 'Caiçara do Rio do Vento', 'CAICARA DO RIO DO VENTO', 'M', 'RN', 'NE', 0),
(2402006, 'Caicó', 'CAICO', 'M', 'RN', 'NE', 0),
(2402105, 'Campo Redondo', 'CAMPO REDONDO', 'M', 'RN', 'NE', 0),
(2402204, 'Canguaretama', 'CANGUARETAMA', 'M', 'RN', 'NE', 0),
(2402303, 'Caraúbas', 'CARAUBAS', 'M', 'RN', 'NE', 0),
(2402402, 'Carnaúba dos Dantas', 'CARNAUBA DOS DANTAS', 'M', 'RN', 'NE', 0),
(2402501, 'Carnaubais', 'CARNAUBAIS', 'M', 'RN', 'NE', 0),
(2402600, 'Ceará-mirim', 'CEARA-MIRIM', 'M', 'RN', 'NE', 0),
(2402709, 'Cerro Cora', 'CERRO CORA', 'M', 'RN', 'NE', 0),
(2402808, 'Coronel Ezequiel', 'CORONEL EZEQUIEL', 'M', 'RN', 'NE', 0),
(2402907, 'Coronel João Pessoa', 'CORONEL JOAO PESSOA', 'M', 'RN', 'NE', 0),
(2403004, 'Cruzeta', 'CRUZETA', 'M', 'RN', 'NE', 0),
(2403103, 'Currais Novos', 'CURRAIS NOVOS', 'M', 'RN', 'NE', 0),
(2403202, 'Doutor Severiano', 'DOUTOR SEVERIANO', 'M', 'RN', 'NE', 0),
(2403251, 'Parnamirim', 'PARNAMIRIM', 'M', 'RN', 'NE', 0),
(2403301, 'Encanto', 'ENCANTO', 'M', 'RN', 'NE', 0),
(2403400, 'Equador', 'EQUADOR', 'M', 'RN', 'NE', 0),
(2403509, 'Espírito Santo', 'ESPIRITO SANTO', 'M', 'RN', 'NE', 0),
(2403608, 'Extremoz', 'EXTREMOZ', 'M', 'RN', 'NE', 0),
(2403707, 'Felipe Guerra', 'FELIPE GUERRA', 'M', 'RN', 'NE', 0),
(2403756, 'Fernando Pedroza', 'FERNANDO PEDROZA', 'M', 'RN', 'NE', 0),
(2403806, 'Florânia', 'FLORANIA', 'M', 'RN', 'NE', 0),
(2403905, 'Francisco Dantas', 'FRANCISCO DANTAS', 'M', 'RN', 'NE', 0),
(2404002, 'Frutuoso Gomes', 'FRUTUOSO GOMES', 'M', 'RN', 'NE', 0),
(2404101, 'Galinhos', 'GALINHOS', 'M', 'RN', 'NE', 0),
(2404200, 'Goianinha', 'GOIANINHA', 'M', 'RN', 'NE', 0),
(2404309, 'Governador Dix-sept Rosado', 'GOVERNADOR DIX-SEPT ROSADO', 'M', 'RN', 'NE', 0),
(2404408, 'Grossos', 'GROSSOS', 'M', 'RN', 'NE', 0),
(2404507, 'Guamare', 'GUAMARE', 'M', 'RN', 'NE', 0),
(2404606, 'Ielmo Marinho', 'IELMO MARINHO', 'M', 'RN', 'NE', 0),
(2404705, 'Ipanguacu', 'IPANGUACU', 'M', 'RN', 'NE', 0),
(2404804, 'Ipueira', 'IPUEIRA', 'M', 'RN', 'NE', 0),
(2404853, 'Itaja', 'ITAJA', 'M', 'RN', 'NE', 0),
(2404903, 'Itaú', 'ITAU', 'M', 'RN', 'NE', 0),
(2405009, 'Jaçanã', 'JACANA', 'M', 'RN', 'NE', 0),
(2405108, 'Jandaira', 'JANDAIRA', 'M', 'RN', 'NE', 0),
(2405207, 'Janduís', 'JANDUIS', 'M', 'RN', 'NE', 0),
(2405306, 'Januário Cicco', 'JANUARIO CICCO', 'M', 'RN', 'NE', 0),
(2405405, 'Japi', 'JAPI', 'M', 'RN', 'NE', 0),
(2405504, 'Jardim de Angicos', 'JARDIM DE ANGICOS', 'M', 'RN', 'NE', 0),
(2405603, 'Jardim de Piranhas', 'JARDIM DE PIRANHAS', 'M', 'RN', 'NE', 0),
(2405702, 'Jardim do Seridó', 'JARDIM DO SERIDO', 'M', 'RN', 'NE', 0),
(2405801, 'João Câmara', 'JOAO CAMARA', 'M', 'RN', 'NE', 0),
(2405900, 'João Dias', 'JOAO DIAS', 'M', 'RN', 'NE', 0),
(2406007, 'José da Penha', 'JOSE DA PENHA', 'M', 'RN', 'NE', 0),
(2406106, 'Jucurutu', 'JUCURUTU', 'M', 'RN', 'NE', 0),
(2406155, 'Jundiá', 'JUNDIA', 'M', 'RN', 'NE', 0),
(2406205, 'Lagoa D''Anta', 'LAGOA D''ANTA', 'M', 'RN', 'NE', 0),
(2406304, 'Lagoa de Pedras', 'LAGOA DE PEDRAS', 'M', 'RN', 'NE', 0),
(2406403, 'Lagoa de Velhos', 'LAGOA DE VELHOS', 'M', 'RN', 'NE', 0),
(2406502, 'Lagoa Nova', 'LAGOA NOVA', 'M', 'RN', 'NE', 0),
(2406601, 'Lagoa Salgada', 'LAGOA SALGADA', 'M', 'RN', 'NE', 0),
(2406700, 'Lajes', 'LAJES', 'M', 'RN', 'NE', 0),
(2406809, 'Lajes Pintadas', 'LAJES PINTADAS', 'M', 'RN', 'NE', 0),
(2406908, 'Lucrécia', 'LUCRECIA', 'M', 'RN', 'NE', 0),
(2407005, 'Luís Gomes', 'LUIS GOMES', 'M', 'RN', 'NE', 0),
(2407104, 'Macaíba', 'MACAIBA', 'M', 'RN', 'NE', 0),
(2407203, 'Macau', 'MACAU', 'M', 'RN', 'NE', 0),
(2407252, 'Major Sales', 'MAJOR SALES', 'M', 'RN', 'NE', 0),
(2407302, 'Marcelino Vieira', 'MARCELINO VIEIRA', 'M', 'RN', 'NE', 0),
(2407401, 'Martins', 'MARTINS', 'M', 'RN', 'NE', 0),
(2407500, 'Maxaranguape', 'MAXARANGUAPE', 'M', 'RN', 'NE', 0),
(2407609, 'Messias Targino', 'MESSIAS TARGINO', 'M', 'RN', 'NE', 0),
(2407708, 'Montanhas', 'MONTANHAS', 'M', 'RN', 'NE', 0),
(2407807, 'Monte Alegre', 'MONTE ALEGRE', 'M', 'RN', 'NE', 0),
(2407906, 'Monte das Gameleiras', 'MONTE DAS GAMELEIRAS', 'M', 'RN', 'NE', 0),
(2408003, 'Mossoró', 'MOSSORO', 'M', 'RN', 'NE', 0),
(2408102, 'Natal', 'NATAL', 'M', 'RN', 'NE', 0),
(2408201, 'Nísia Floresta', 'NISIA FLORESTA', 'M', 'RN', 'NE', 0),
(2408300, 'Nova Cruz', 'NOVA CRUZ', 'M', 'RN', 'NE', 0),
(2408409, 'Olho-d''Água do Borges', 'OLHO-D''AGUA DO BORGES', 'M', 'RN', 'NE', 0),
(2408508, 'Ouro Branco', 'OURO BRANCO', 'M', 'RN', 'NE', 0),
(2408607, 'Paranã', 'PARANA', 'M', 'RN', 'NE', 0),
(2408706, 'Paraú', 'PARAU', 'M', 'RN', 'NE', 0),
(2408805, 'Parazinho', 'PARAZINHO', 'M', 'RN', 'NE', 0),
(2408904, 'Parelhas', 'PARELHAS', 'M', 'RN', 'NE', 0),
(2408953, 'Rio do Fogo', 'RIO DO FOGO', 'M', 'RN', 'NE', 0),
(2409100, 'Passa e Fica', 'PASSA E FICA', 'M', 'RN', 'NE', 0),
(2409209, 'Passagem', 'PASSAGEM', 'M', 'RN', 'NE', 0),
(2409308, 'Patu', 'PATU', 'M', 'RN', 'NE', 0),
(2409332, 'Santa Maria', 'SANTA MARIA', 'M', 'RN', 'NE', 0),
(2409407, 'Pau dos Ferros', 'PAU DOS FERROS', 'M', 'RN', 'NE', 0),
(2409506, 'Pedra Grande', 'PEDRA GRANDE', 'M', 'RN', 'NE', 0),
(2409605, 'Pedra Preta', 'PEDRA PRETA', 'M', 'RN', 'NE', 0),
(2409704, 'Pedro Avelino', 'PEDRO AVELINO', 'M', 'RN', 'NE', 0),
(2409803, 'Pedro Velho', 'PEDRO VELHO', 'M', 'RN', 'NE', 0),
(2409902, 'Pendências', 'PENDENCIAS', 'M', 'RN', 'NE', 0),
(2410009, 'Pilões', 'PILOES', 'M', 'RN', 'NE', 0),
(2410108, 'Poço Branco', 'POCO BRANCO', 'M', 'RN', 'NE', 0),
(2410207, 'Portalegre', 'PORTALEGRE', 'M', 'RN', 'NE', 0),
(2410256, 'Porto do Mangue', 'PORTO DO MANGUE', 'M', 'RN', 'NE', 0),
(2410306, 'Presidente Juscelino', 'PRESIDENTE JUSCELINO', 'M', 'RN', 'NE', 0),
(2410405, 'Pureza', 'PUREZA', 'M', 'RN', 'NE', 0),
(2410504, 'Rafael Fernandes', 'RAFAEL FERNANDES', 'M', 'RN', 'NE', 0),
(2410603, 'Rafael Godeiro', 'RAFAEL GODEIRO', 'M', 'RN', 'NE', 0),
(2410702, 'Riacho da Cruz', 'RIACHO DA CRUZ', 'M', 'RN', 'NE', 0),
(2410801, 'Riacho de Santana', 'RIACHO DE SANTANA', 'M', 'RN', 'NE', 0),
(2410900, 'Riachuelo', 'RIACHUELO', 'M', 'RN', 'NE', 0),
(2411007, 'Rodolfo Fernandes', 'RODOLFO FERNANDES', 'M', 'RN', 'NE', 0),
(2411056, 'Tibau', 'TIBAU', 'M', 'RN', 'NE', 0),
(2411106, 'Ruy Barbosa', 'RUY BARBOSA', 'M', 'RN', 'NE', 0),
(2411205, 'Santa Cruz', 'SANTA CRUZ', 'M', 'RN', 'NE', 0),
(2411403, 'Santana do Matos', 'SANTANA DO MATOS', 'M', 'RN', 'NE', 0),
(2411429, 'Santana do Seridó', 'SANTANA DO SERIDO', 'M', 'RN', 'NE', 0),
(2411502, 'Santo Antônio', 'SANTO ANTONIO', 'M', 'RN', 'NE', 0),
(2411601, 'São Bento do Norte', 'SAO BENTO DO NORTE', 'M', 'RN', 'NE', 0),
(2411700, 'São Bento do Trairí', 'SAO BENTO DO TRAIRI', 'M', 'RN', 'NE', 0),
(2411809, 'São Fernando', 'SAO FERNANDO', 'M', 'RN', 'NE', 0),
(2411908, 'São Francisco do Oeste', 'SAO FRANCISCO DO OESTE', 'M', 'RN', 'NE', 0),
(2412005, 'São Gonçalo do Amarante', 'SAO GONCALO DO AMARANTE', 'M', 'RN', 'NE', 0),
(2412104, 'São João do Sabugi', 'SAO JOAO DO SABUGI', 'M', 'RN', 'NE', 0),
(2412203, 'São José de Mipibu', 'SAO JOSE DE MIPIBU', 'M', 'RN', 'NE', 0),
(2412302, 'São José do Campestre', 'SAO JOSE DO CAMPESTRE', 'M', 'RN', 'NE', 0),
(2412401, 'São José do Seridó', 'SAO JOSE DO SERIDO', 'M', 'RN', 'NE', 0),
(2412500, 'São Miguel', 'SAO MIGUEL', 'M', 'RN', 'NE', 0),
(2412559, 'São Miguel de Touros', 'SAO MIGUEL DE TOUROS', 'M', 'RN', 'NE', 0),
(2412609, 'São Paulo do Potengi', 'SAO PAULO DO POTENGI', 'M', 'RN', 'NE', 0),
(2412708, 'São Pedro', 'SAO PEDRO', 'M', 'RN', 'NE', 0),
(2412807, 'São Rafael', 'SAO RAFAEL', 'M', 'RN', 'NE', 0),
(2412906, 'São Tomé', 'SAO TOME', 'M', 'RN', 'NE', 0),
(2413003, 'São Vicente', 'SAO VICENTE', 'M', 'RN', 'NE', 0),
(2413102, 'Senador Elói de Souza', 'SENADOR ELOI DE SOUZA', 'M', 'RN', 'NE', 0),
(2413201, 'Senador Georgino Avelino', 'SENADOR GEORGINO AVELINO', 'M', 'RN', 'NE', 0),
(2413300, 'Serra de São Bento', 'SERRA DE SAO BENTO', 'M', 'RN', 'NE', 0),
(2413359, 'Serra do Mel', 'SERRA DO MEL', 'M', 'RN', 'NE', 0),
(2413409, 'Serra Negra do Norte', 'SERRA NEGRA DO NORTE', 'M', 'RN', 'NE', 0),
(2413508, 'Serrinha', 'SERRINHA', 'M', 'RN', 'NE', 0),
(2413557, 'Serrinha dos Pintos', 'SERRINHA DOS PINTOS', 'M', 'RN', 'NE', 0),
(2413607, 'Severiano Melo', 'SEVERIANO MELO', 'M', 'RN', 'NE', 0),
(2413706, 'Sítio Novo', 'SITIO NOVO', 'M', 'RN', 'NE', 0),
(2413805, 'Taboleiro Grande', 'TABOLEIRO GRANDE', 'M', 'RN', 'NE', 0),
(2413904, 'Taipu', 'TAIPU', 'M', 'RN', 'NE', 0),
(2414001, 'Tangará', 'TANGARA', 'M', 'RN', 'NE', 0),
(2414100, 'Tenente Ananias', 'TENENTE ANANIAS', 'M', 'RN', 'NE', 0),
(2414159, 'Tenente Laurentino Cruz', 'TENENTE LAURENTINO CRUZ', 'M', 'RN', 'NE', 0),
(2414209, 'Tibau do Sul', 'TIBAU DO SUL', 'M', 'RN', 'NE', 0),
(2414308, 'Timbaúba dos Batistas', 'TIMBAUBA DOS BATISTAS', 'M', 'RN', 'NE', 0),
(2414407, 'Touros', 'TOUROS', 'M', 'RN', 'NE', 0),
(2414456, 'Triunfo Potiguar', 'TRIUNFO POTIGUAR', 'M', 'RN', 'NE', 0),
(2414506, 'Umarizal', 'UMARIZAL', 'M', 'RN', 'NE', 0),
(2414605, 'Upanema', 'UPANEMA', 'M', 'RN', 'NE', 0),
(2414704, 'Várzea', 'VARZEA', 'M', 'RN', 'NE', 0),
(2414753, 'Venha-ver', 'VENHA-VER', 'M', 'RN', 'NE', 0),
(2414803, 'Vera Cruz', 'VERA CRUZ', 'M', 'RN', 'NE', 0),
(2414902, 'Viçosa', 'VICOSA', 'M', 'RN', 'NE', 0),
(2415008, 'Vila Flor', 'VILA FLOR', 'M', 'RN', 'NE', 0),
(2500000, 'Paraíba', 'PARAIBA', 'U', 'PB', 'NE', 0),
(2500106, 'Água Branca', 'AGUA BRANCA', 'M', 'PB', 'NE', 0),
(2500205, 'Aguiar', 'AGUIAR', 'M', 'PB', 'NE', 0),
(2500304, 'Alagoa Grande', 'ALAGOA GRANDE', 'M', 'PB', 'NE', 0),
(2500403, 'Alagoa Nova', 'ALAGOA NOVA', 'M', 'PB', 'NE', 0),
(2500502, 'Alagoinha', 'ALAGOINHA', 'M', 'PB', 'NE', 0),
(2500536, 'Alcantil', 'ALCANTIL', 'M', 'PB', 'NE', 0),
(2500577, 'Algodão de Jandaíra', 'ALGODAO DE JANDAIRA', 'M', 'PB', 'NE', 0),
(2500601, 'Alhandra', 'ALHANDRA', 'M', 'PB', 'NE', 0),
(2500700, 'São João do Rio do Peixe', 'SAO JOAO DO RIO DO PEIXE', 'M', 'PB', 'NE', 0),
(2500734, 'Amparo', 'AMPARO', 'M', 'PB', 'NE', 0),
(2500775, 'Aparecida', 'APARECIDA', 'M', 'PB', 'NE', 0),
(2500809, 'Araçagi', 'ARACAGI', 'M', 'PB', 'NE', 0),
(2500908, 'Arara', 'ARARA', 'M', 'PB', 'NE', 0),
(2501005, 'Araruna', 'ARARUNA', 'M', 'PB', 'NE', 0),
(2501104, 'Areia', 'AREIA', 'M', 'PB', 'NE', 0),
(2501153, 'Areia de Baraúnas', 'AREIA DE BARAUNAS', 'M', 'PB', 'NE', 0),
(2501203, 'Areial', 'AREIAL', 'M', 'PB', 'NE', 0),
(2501302, 'Aroeiras', 'AROEIRAS', 'M', 'PB', 'NE', 0),
(2501351, 'Assunção', 'ASSUNCAO', 'M', 'PB', 'NE', 0),
(2501401, 'Baía da Traição', 'BAIA DA TRAICAO', 'M', 'PB', 'NE', 0),
(2501500, 'Bananeiras', 'BANANEIRAS', 'M', 'PB', 'NE', 0),
(2501534, 'Baraúna', 'BARAUNA', 'M', 'PB', 'NE', 0),
(2501575, 'Barra de Santana', 'BARRA DE SANTANA', 'M', 'PB', 'NE', 0),
(2501609, 'Barra de Santa Rosa', 'BARRA DE SANTA ROSA', 'M', 'PB', 'NE', 0),
(2501708, 'Barra de São Miguel', 'BARRA DE SAO MIGUEL', 'M', 'PB', 'NE', 0),
(2501807, 'Bayeux', 'BAYEUX', 'M', 'PB', 'NE', 0),
(2501906, 'Belém', 'BELEM', 'M', 'PB', 'NE', 0),
(2502003, 'Belém do Brejo do Cruz', 'BELEM DO BREJO DO CRUZ', 'M', 'PB', 'NE', 0),
(2502052, 'Bernardino Batista', 'BERNARDINO BATISTA', 'M', 'PB', 'NE', 0),
(2502102, 'Boa Ventura', 'BOA VENTURA', 'M', 'PB', 'NE', 0),
(2502151, 'Boa Vista', 'BOA VISTA', 'M', 'PB', 'NE', 0),
(2502201, 'Bom Jesus', 'BOM JESUS', 'M', 'PB', 'NE', 0),
(2502300, 'Bom Sucesso', 'BOM SUCESSO', 'M', 'PB', 'NE', 0),
(2502409, 'Bonito de Santa Fé', 'BONITO DE SANTA FE', 'M', 'PB', 'NE', 0),
(2502508, 'Boqueirão', 'BOQUEIRAO', 'M', 'PB', 'NE', 0),
(2502607, 'Igaracy', 'IGARACY', 'M', 'PB', 'NE', 0),
(2502706, 'Borborema', 'BORBOREMA', 'M', 'PB', 'NE', 0),
(2502805, 'Brejo do Cruz', 'BREJO DO CRUZ', 'M', 'PB', 'NE', 0),
(2502904, 'Brejo dos Santos', 'BREJO DOS SANTOS', 'M', 'PB', 'NE', 0),
(2503001, 'Caaporã', 'CAAPORA', 'M', 'PB', 'NE', 0),
(2503100, 'Cabaceiras', 'CABACEIRAS', 'M', 'PB', 'NE', 0),
(2503209, 'Cabedelo', 'CABEDELO', 'M', 'PB', 'NE', 0),
(2503308, 'Cachoeira dos Índios', 'CACHOEIRA DOS INDIOS', 'M', 'PB', 'NE', 0),
(2503407, 'Cacimba de Areia', 'CACIMBA DE AREIA', 'M', 'PB', 'NE', 0),
(2503506, 'Cacimba de Dentro', 'CACIMBA DE DENTRO', 'M', 'PB', 'NE', 0),
(2503555, 'Cacimbas', 'CACIMBAS', 'M', 'PB', 'NE', 0),
(2503605, 'Caiçara', 'CAICARA', 'M', 'PB', 'NE', 0),
(2503704, 'Cajazeiras', 'CAJAZEIRAS', 'M', 'PB', 'NE', 0),
(2503753, 'Cajazeirinhas', 'CAJAZEIRINHAS', 'M', 'PB', 'NE', 0),
(2503803, 'Caldas Brandao', 'CALDAS BRANDAO', 'M', 'PB', 'NE', 0),
(2503902, 'Camalau', 'CAMALAU', 'M', 'PB', 'NE', 0),
(2504009, 'Campina Grande', 'CAMPINA GRANDE', 'M', 'PB', 'NE', 0),
(2504033, 'Capim', 'CAPIM', 'M', 'PB', 'NE', 0),
(2504074, 'Caraúbas', 'CARAUBAS', 'M', 'PB', 'NE', 0),
(2504108, 'Carrapateira', 'CARRAPATEIRA', 'M', 'PB', 'NE', 0),
(2504157, 'Casserengue', 'CASSERENGUE', 'M', 'PB', 'NE', 0),
(2504207, 'Catingueira', 'CATINGUEIRA', 'M', 'PB', 'NE', 0),
(2504306, 'Catolé do Rocha', 'CATOLE DO ROCHA', 'M', 'PB', 'NE', 0),
(2504355, 'Caturité', 'CATURITE', 'M', 'PB', 'NE', 0),
(2504405, 'Conceição', 'CONCEICAO', 'M', 'PB', 'NE', 0),
(2504504, 'Condado', 'CONDADO', 'M', 'PB', 'NE', 0),
(2504603, 'Conde', 'CONDE', 'M', 'PB', 'NE', 0),
(2504702, 'Congo', 'CONGO', 'M', 'PB', 'NE', 0),
(2504801, 'Coremas', 'COREMAS', 'M', 'PB', 'NE', 0),
(2504850, 'Coxixola', 'COXIXOLA', 'M', 'PB', 'NE', 0),
(2504900, 'Cruz do Espírito Santo', 'CRUZ DO ESPIRITO SANTO', 'M', 'PB', 'NE', 0),
(2505006, 'Cubati', 'CUBATI', 'M', 'PB', 'NE', 0),
(2505105, 'Cuité', 'CUITE', 'M', 'PB', 'NE', 0),
(2505204, 'Cuitegi', 'CUITEGI', 'M', 'PB', 'NE', 0),
(2505238, 'Cuité de Mamanguape', 'CUITE DE MAMANGUAPE', 'M', 'PB', 'NE', 0),
(2505279, 'Curral de Cima', 'CURRAL DE CIMA', 'M', 'PB', 'NE', 0),
(2505303, 'Curral Velho', 'CURRAL VELHO', 'M', 'PB', 'NE', 0),
(2505352, 'Damião', 'DAMIAO', 'M', 'PB', 'NE', 0),
(2505402, 'Desterro', 'DESTERRO', 'M', 'PB', 'NE', 0),
(2505501, 'Vista Serrana', 'VISTA SERRANA', 'M', 'PB', 'NE', 0),
(2505600, 'Diamante', 'DIAMANTE', 'M', 'PB', 'NE', 0),
(2505709, 'Dona Inês', 'DONA INES', 'M', 'PB', 'NE', 0),
(2505808, 'Duas Estradas', 'DUAS ESTRADAS', 'M', 'PB', 'NE', 0),
(2505907, 'Emas', 'EMAS', 'M', 'PB', 'NE', 0),
(2506004, 'Esperanca', 'ESPERANCA', 'M', 'PB', 'NE', 0),
(2506103, 'Fagundes', 'FAGUNDES', 'M', 'PB', 'NE', 0),
(2506202, 'Frei Martinho', 'FREI MARTINHO', 'M', 'PB', 'NE', 0),
(2506251, 'Gado Bravo', 'GADO BRAVO', 'M', 'PB', 'NE', 0),
(2506301, 'Guarabira', 'GUARABIRA', 'M', 'PB', 'NE', 0),
(2506400, 'Gurinhem', 'GURINHEM', 'M', 'PB', 'NE', 0),
(2506509, 'Gurjao', 'GURJAO', 'M', 'PB', 'NE', 0),
(2506608, 'Ibiara', 'IBIARA', 'M', 'PB', 'NE', 0),
(2506707, 'Imaculada', 'IMACULADA', 'M', 'PB', 'NE', 0),
(2506806, 'Ingá', 'INGA', 'M', 'PB', 'NE', 0),
(2506905, 'Itabaiana', 'ITABAIANA', 'M', 'PB', 'NE', 0),
(2507002, 'Itaporanga', 'ITAPORANGA', 'M', 'PB', 'NE', 0),
(2507101, 'Itapororoca', 'ITAPOROROCA', 'M', 'PB', 'NE', 0),
(2507200, 'Itatuba', 'ITATUBA', 'M', 'PB', 'NE', 0),
(2507309, 'Jacaraú', 'JACARAU', 'M', 'PB', 'NE', 0),
(2507408, 'Jericó', 'JERICO', 'M', 'PB', 'NE', 0),
(2507507, 'João Pessoa', 'JOAO PESSOA', 'M', 'PB', 'NE', 0),
(2507606, 'Juarez Távora', 'JUAREZ TAVORA', 'M', 'PB', 'NE', 0),
(2507705, 'Juazeirinho', 'JUAZEIRINHO', 'M', 'PB', 'NE', 0),
(2507804, 'Junco do Seridó', 'JUNCO DO SERIDO', 'M', 'PB', 'NE', 0),
(2507903, 'Juripiranga', 'JURIPIRANGA', 'M', 'PB', 'NE', 0),
(2508000, 'Juru', 'JURU', 'M', 'PB', 'NE', 0),
(2508109, 'Lagoa', 'LAGOA', 'M', 'PB', 'NE', 0),
(2508208, 'Lagoa de Dentro', 'LAGOA DE DENTRO', 'M', 'PB', 'NE', 0),
(2508307, 'Lagoa Seca', 'LAGOA SECA', 'M', 'PB', 'NE', 0),
(2508406, 'Lastro', 'LASTRO', 'M', 'PB', 'NE', 0),
(2508505, 'Livramento', 'LIVRAMENTO', 'M', 'PB', 'NE', 0),
(2508554, 'Logradouro', 'LOGRADOURO', 'M', 'PB', 'NE', 0),
(2508604, 'Lucena', 'LUCENA', 'M', 'PB', 'NE', 0),
(2508703, 'Mãe D''Água', 'MAE D''AGUA', 'M', 'PB', 'NE', 0),
(2508802, 'Malta', 'MALTA', 'M', 'PB', 'NE', 0),
(2508901, 'Mamanguape', 'MAMANGUAPE', 'M', 'PB', 'NE', 0),
(2509008, 'Manaíra', 'MANAIRA', 'M', 'PB', 'NE', 0),
(2509057, 'Marcação', 'MARCACAO', 'M', 'PB', 'NE', 0),
(2509107, 'Mari', 'MARI', 'M', 'PB', 'NE', 0),
(2509156, 'Marizópolis', 'MARIZOPOLIS', 'M', 'PB', 'NE', 0),
(2509206, 'Massaranduba', 'MASSARANDUBA', 'M', 'PB', 'NE', 0),
(2509305, 'Mataraca', 'MATARACA', 'M', 'PB', 'NE', 0),
(2509339, 'Matinhas', 'MATINHAS', 'M', 'PB', 'NE', 0),
(2509370, 'Mato Grosso', 'MATO GROSSO', 'M', 'PB', 'NE', 0),
(2509396, 'Maturéia', 'MATUREIA', 'M', 'PB', 'NE', 0),
(2509404, 'Mogeiro', 'MOGEIRO', 'M', 'PB', 'NE', 0),
(2509503, 'Montadas', 'MONTADAS', 'M', 'PB', 'NE', 0),
(2509602, 'Monte Horebe', 'MONTE HOREBE', 'M', 'PB', 'NE', 0),
(2509701, 'Monteiro', 'MONTEIRO', 'M', 'PB', 'NE', 0),
(2509800, 'Mulungu', 'MULUNGU', 'M', 'PB', 'NE', 0),
(2509909, 'Natuba', 'NATUBA', 'M', 'PB', 'NE', 0),
(2510006, 'Nazarezinho', 'NAZAREZINHO', 'M', 'PB', 'NE', 0),
(2510105, 'Nova Floresta', 'NOVA FLORESTA', 'M', 'PB', 'NE', 0),
(2510204, 'Nova Olinda', 'NOVA OLINDA', 'M', 'PB', 'NE', 0),
(2510303, 'Nova Palmeira', 'NOVA PALMEIRA', 'M', 'PB', 'NE', 0),
(2510402, 'Olho D''Água', 'OLHO D''AGUA', 'M', 'PB', 'NE', 0),
(2510501, 'Olivedos', 'OLIVEDOS', 'M', 'PB', 'NE', 0),
(2510600, 'Ouro Velho', 'OURO VELHO', 'M', 'PB', 'NE', 0),
(2510659, 'Parari', 'PARARI', 'M', 'PB', 'NE', 0),
(2510709, 'Passagem', 'PASSAGEM', 'M', 'PB', 'NE', 0),
(2510808, 'Patos', 'PATOS', 'M', 'PB', 'NE', 0),
(2510907, 'Paulista', 'PAULISTA', 'M', 'PB', 'NE', 0),
(2511004, 'Pedra Branca', 'PEDRA BRANCA', 'M', 'PB', 'NE', 0),
(2511103, 'Pedra Lavrada', 'PEDRA LAVRADA', 'M', 'PB', 'NE', 0),
(2511202, 'Pedras de Fogo', 'PEDRAS DE FOGO', 'M', 'PB', 'NE', 0),
(2511301, 'Piancó', 'PIANCO', 'M', 'PB', 'NE', 0),
(2511400, 'Picuí', 'PICUI', 'M', 'PB', 'NE', 0),
(2511509, 'Pilar', 'PILAR', 'M', 'PB', 'NE', 0),
(2511608, 'Pilões', 'PILOES', 'M', 'PB', 'NE', 0),
(2511707, 'Piloezinhos', 'PILOEZINHOS', 'M', 'PB', 'NE', 0),
(2511806, 'Pirpirituba', 'PIRPIRITUBA', 'M', 'PB', 'NE', 0),
(2511905, 'Pitimbu', 'PITIMBU', 'M', 'PB', 'NE', 0),
(2512002, 'Pocinhos', 'POCINHOS', 'M', 'PB', 'NE', 0),
(2512036, 'Poço Dantas', 'POCO DANTAS', 'M', 'PB', 'NE', 0),
(2512077, 'Poço de José de Moura', 'POCO DE JOSE DE MOURA', 'M', 'PB', 'NE', 0),
(2512101, 'Pombal', 'POMBAL', 'M', 'PB', 'NE', 0),
(2512200, 'Prata', 'PRATA', 'M', 'PB', 'NE', 0),
(2512309, 'Princesa Isabel', 'PRINCESA ISABEL', 'M', 'PB', 'NE', 0),
(2512408, 'Puxinana', 'PUXINANA', 'M', 'PB', 'NE', 0),
(2512507, 'Queimadas', 'QUEIMADAS', 'M', 'PB', 'NE', 0),
(2512606, 'Quixabá', 'QUIXABA', 'M', 'PB', 'NE', 0),
(2512705, 'Remígio', 'REMIGIO', 'M', 'PB', 'NE', 0),
(2512721, 'Pedro Régis', 'PEDRO REGIS', 'M', 'PB', 'NE', 0),
(2512747, 'Riachão', 'RIACHAO', 'M', 'PB', 'NE', 0),
(2512754, 'Riachão do Bacamarte', 'RIACHAO DO BACAMARTE', 'M', 'PB', 'NE', 0),
(2512762, 'Riachão do Poco', 'RIACHAO DO POCO', 'M', 'PB', 'NE', 0),
(2512788, 'Riacho de Santo Antônio', 'RIACHO DE SANTO ANTONIO', 'M', 'PB', 'NE', 0),
(2512804, 'Riacho dos Cavalos', 'RIACHO DOS CAVALOS', 'M', 'PB', 'NE', 0),
(2512903, 'Rio Tinto', 'RIO TINTO', 'M', 'PB', 'NE', 0),
(2513000, 'Salgadinho', 'SALGADINHO', 'M', 'PB', 'NE', 0),
(2513109, 'Salgado de São Félix', 'SALGADO DE SAO FELIX', 'M', 'PB', 'NE', 0),
(2513158, 'Santa Cecília de Umbuzeiro', 'SANTA CECILIA DE UMBUZEIRO', 'M', 'PB', 'NE', 0),
(2513208, 'Santa Cruz', 'SANTA CRUZ', 'M', 'PB', 'NE', 0),
(2513307, 'Santa Helena', 'SANTA HELENA', 'M', 'PB', 'NE', 0),
(2513356, 'Santa Inês', 'SANTA INES', 'M', 'PB', 'NE', 0),
(2513406, 'Santa Luzia', 'SANTA LUZIA', 'M', 'PB', 'NE', 0),
(2513505, 'Santana de Mangueira', 'SANTANA DE MANGUEIRA', 'M', 'PB', 'NE', 0),
(2513604, 'Santana dos Garrotes', 'SANTANA DOS GARROTES', 'M', 'PB', 'NE', 0),
(2513653, 'Santarém', 'SANTAREM', 'M', 'PB', 'NE', 0),
(2513703, 'Santa Rita', 'SANTA RITA', 'M', 'PB', 'NE', 0),
(2513802, 'Santa Teresinha', 'SANTA TERESINHA', 'M', 'PB', 'NE', 0),
(2513851, 'Santo Andre', 'SANTO ANDRE', 'M', 'PB', 'NE', 0),
(2513901, 'São Bento', 'SAO BENTO', 'M', 'PB', 'NE', 0),
(2513927, 'São Bentinho', 'SAO BENTINHO', 'M', 'PB', 'NE', 0),
(2513943, 'São Domingos do Cariri', 'SAO DOMINGOS DO CARIRI', 'M', 'PB', 'NE', 0),
(2513968, 'São Domingos de Pombal', 'SAO DOMINGOS DE POMBAL', 'M', 'PB', 'NE', 0),
(2513984, 'São Francisco', 'SAO FRANCISCO', 'M', 'PB', 'NE', 0),
(2514008, 'São João do Cariri', 'SAO JOAO DO CARIRI', 'M', 'PB', 'NE', 0),
(2514107, 'São João do Tigre', 'SAO JOAO DO TIGRE', 'M', 'PB', 'NE', 0),
(2514206, 'São José da Lagoa Tapada', 'SAO JOSE DA LAGOA TAPADA', 'M', 'PB', 'NE', 0),
(2514305, 'São José de Caiana', 'SAO JOSE DE CAIANA', 'M', 'PB', 'NE', 0),
(2514404, 'São José de Espinharas', 'SAO JOSE DE ESPINHARAS', 'M', 'PB', 'NE', 0),
(2514453, 'São José dos Ramos', 'SAO JOSE DOS RAMOS', 'M', 'PB', 'NE', 0),
(2514503, 'São José de Piranhas', 'SAO JOSE DE PIRANHAS', 'M', 'PB', 'NE', 0),
(2514552, 'São José de Princesa', 'SAO JOSE DE PRINCESA', 'M', 'PB', 'NE', 0),
(2514602, 'São José do Bonfim', 'SAO JOSE DO BONFIM', 'M', 'PB', 'NE', 0),
(2514651, 'São José do Brejo do Cruz', 'SAO JOSE DO BREJO DO CRUZ', 'M', 'PB', 'NE', 0),
(2514701, 'São José do Sabugi', 'SAO JOSE DO SABUGI', 'M', 'PB', 'NE', 0),
(2514800, 'São José dos Cordeiros', 'SAO JOSE DOS CORDEIROS', 'M', 'PB', 'NE', 0),
(2514909, 'São Mamede', 'SAO MAMEDE', 'M', 'PB', 'NE', 0),
(2515005, 'São Miguel de Taipu', 'SAO MIGUEL DE TAIPU', 'M', 'PB', 'NE', 0),
(2515104, 'São Sebastiao de Lagoa de Roca', 'SAO SEBASTIAO DE LAGOA DE ROCA', 'M', 'PB', 'NE', 0),
(2515203, 'São Sebastiao do Umbuzeiro', 'SAO SEBASTIAO DO UMBUZEIRO', 'M', 'PB', 'NE', 0),
(2515302, 'Sapé', 'SAPE', 'M', 'PB', 'NE', 0),
(2515401, 'Seridó', 'SERIDO', 'M', 'PB', 'NE', 0),
(2515500, 'Serra Branca', 'SERRA BRANCA', 'M', 'PB', 'NE', 0),
(2515609, 'Serra da Raiz', 'SERRA DA RAIZ', 'M', 'PB', 'NE', 0),
(2515708, 'Serra Grande', 'SERRA GRANDE', 'M', 'PB', 'NE', 0),
(2515807, 'Serra Redonda', 'SERRA REDONDA', 'M', 'PB', 'NE', 0),
(2515906, 'Serraria', 'SERRARIA', 'M', 'PB', 'NE', 0),
(2515930, 'Sertãozinho', 'SERTAOZINHO', 'M', 'PB', 'NE', 0),
(2515971, 'Sobrado', 'SOBRADO', 'M', 'PB', 'NE', 0),
(2516003, 'Solânea', 'SOLANEA', 'M', 'PB', 'NE', 0),
(2516102, 'Soledade', 'SOLEDADE', 'M', 'PB', 'NE', 0),
(2516151, 'Sossêgo', 'SOSSEGO', 'M', 'PB', 'NE', 0),
(2516201, 'Sousa', 'SOUSA', 'M', 'PB', 'NE', 0),
(2516300, 'Sumé', 'SUME', 'M', 'PB', 'NE', 0),
(2516409, 'Tacima', 'TACIMA', 'M', 'PB', 'NE', 0),
(2516508, 'Taperoá', 'TAPEROA', 'M', 'PB', 'NE', 0),
(2516607, 'Tavares', 'TAVARES', 'M', 'PB', 'NE', 0),
(2516706, 'Teixeira', 'TEIXEIRA', 'M', 'PB', 'NE', 0),
(2516755, 'Tenório', 'TENORIO', 'M', 'PB', 'NE', 0),
(2516805, 'Triunfo', 'TRIUNFO', 'M', 'PB', 'NE', 0),
(2516904, 'Uiraúna', 'UIRAUNA', 'M', 'PB', 'NE', 0),
(2517001, 'Umbuzeiro', 'UMBUZEIRO', 'M', 'PB', 'NE', 0),
(2517100, 'Várzea', 'VARZEA', 'M', 'PB', 'NE', 0),
(2517209, 'Vieirópolis', 'VIEIROPOLIS', 'M', 'PB', 'NE', 0),
(2517407, 'Zabelê', 'ZABELE', 'M', 'PB', 'NE', 0),
(2600000, 'Pernambuco', 'PERNAMBUCO', 'U', 'PE', 'NE', 0),
(2600054, 'Abreu e Lima', 'ABREU E LIMA', 'M', 'PE', 'NE', 0),
(2600104, 'Afogados da Ingazeira', 'AFOGADOS DA INGAZEIRA', 'M', 'PE', 'NE', 0),
(2600203, 'Afrânio', 'AFRANIO', 'M', 'PE', 'NE', 0),
(2600302, 'Agrestina', 'AGRESTINA', 'M', 'PE', 'NE', 0),
(2600401, 'Água Preta', 'AGUA PRETA', 'M', 'PE', 'NE', 0),
(2600500, 'Águas Belas', 'AGUAS BELAS', 'M', 'PE', 'NE', 0),
(2600609, 'Alagoinha', 'ALAGOINHA', 'M', 'PE', 'NE', 0),
(2600708, 'Aliança', 'ALIANCA', 'M', 'PE', 'NE', 0),
(2600807, 'Altinho', 'ALTINHO', 'M', 'PE', 'NE', 0),
(2600906, 'Amaraji', 'AMARAJI', 'M', 'PE', 'NE', 0),
(2601003, 'Angelim', 'ANGELIM', 'M', 'PE', 'NE', 0),
(2601052, 'Aracoiaba', 'ARACOIABA', 'M', 'PE', 'NE', 0),
(2601102, 'Araripina', 'ARARIPINA', 'M', 'PE', 'NE', 0),
(2601201, 'Arcoverde', 'ARCOVERDE', 'M', 'PE', 'NE', 0),
(2601300, 'Barra de Guabiraba', 'BARRA DE GUABIRABA', 'M', 'PE', 'NE', 0),
(2601409, 'Barreiros', 'BARREIROS', 'M', 'PE', 'NE', 0),
(2601508, 'Belém de Maria', 'BELEM DE MARIA', 'M', 'PE', 'NE', 0),
(2601607, 'Belém de São Francisco', 'BELEM DE SAO FRANCISCO', 'M', 'PE', 'NE', 0),
(2601706, 'Belo Jardim', 'BELO JARDIM', 'M', 'PE', 'NE', 0),
(2601805, 'Betânia', 'BETANIA', 'M', 'PE', 'NE', 0),
(2601904, 'Bezerros', 'BEZERROS', 'M', 'PE', 'NE', 0),
(2602001, 'Bodocó', 'BODOCO', 'M', 'PE', 'NE', 0),
(2602100, 'Bom Conselho', 'BOM CONSELHO', 'M', 'PE', 'NE', 0),
(2602209, 'Bom Jardim', 'BOM JARDIM', 'M', 'PE', 'NE', 0),
(2602308, 'Bonito', 'BONITO', 'M', 'PE', 'NE', 0),
(2602407, 'Brejão', 'BREJAO', 'M', 'PE', 'NE', 0),
(2602506, 'Brejinho', 'BREJINHO', 'M', 'PE', 'NE', 0),
(2602605, 'Brejo da Madre de Deus', 'BREJO DA MADRE DE DEUS', 'M', 'PE', 'NE', 0),
(2602704, 'Buenos Aires', 'BUENOS AIRES', 'M', 'PE', 'NE', 0),
(2602803, 'Buíque', 'BUIQUE', 'M', 'PE', 'NE', 0),
(2602902, 'Cabo de Santo Agostinho', 'CABO DE SANTO AGOSTINHO', 'M', 'PE', 'NE', 0),
(2603009, 'Cabrobó', 'CABROBO', 'M', 'PE', 'NE', 0),
(2603108, 'Cachoeirinha', 'CACHOEIRINHA', 'M', 'PE', 'NE', 0),
(2603207, 'Caetés', 'CAETES', 'M', 'PE', 'NE', 0),
(2603306, 'Calçado', 'CALCADO', 'M', 'PE', 'NE', 0),
(2603405, 'Calumbi', 'CALUMBI', 'M', 'PE', 'NE', 0),
(2603454, 'Camaragibe', 'CAMARAGIBE', 'M', 'PE', 'NE', 0),
(2603504, 'Camocim de São Félix', 'CAMOCIM DE SAO FELIX', 'M', 'PE', 'NE', 0),
(2603603, 'Camutanga', 'CAMUTANGA', 'M', 'PE', 'NE', 0),
(2603702, 'Canhotinho', 'CANHOTINHO', 'M', 'PE', 'NE', 0),
(2603801, 'Capoeiras', 'CAPOEIRAS', 'M', 'PE', 'NE', 0),
(2603900, 'Carnaíba', 'CARNAIBA', 'M', 'PE', 'NE', 0),
(2603926, 'Carnaubeira da Penha', 'CARNAUBEIRA DA PENHA', 'M', 'PE', 'NE', 0),
(2604007, 'Carpina', 'CARPINA', 'M', 'PE', 'NE', 0),
(2604106, 'Caruaru', 'CARUARU', 'M', 'PE', 'NE', 0),
(2604155, 'Casinhas', 'CASINHAS', 'M', 'PE', 'NE', 0),
(2604205, 'Catende', 'CATENDE', 'M', 'PE', 'NE', 0),
(2604304, 'Cedro', 'CEDRO', 'M', 'PE', 'NE', 0),
(2604403, 'Chã de Alegria', 'CHA DE ALEGRIA', 'M', 'PE', 'NE', 0),
(2604502, 'Chã Grande', 'CHA GRANDE', 'M', 'PE', 'NE', 0),
(2604601, 'Condado', 'CONDADO', 'M', 'PE', 'NE', 0),
(2604700, 'Correntes', 'CORRENTES', 'M', 'PE', 'NE', 0),
(2604809, 'Cortês', 'CORTES', 'M', 'PE', 'NE', 0),
(2604908, 'Cumaru', 'CUMARU', 'M', 'PE', 'NE', 0),
(2605004, 'Cupira', 'CUPIRA', 'M', 'PE', 'NE', 0),
(2605103, 'Custodia', 'CUSTODIA', 'M', 'PE', 'NE', 0),
(2605152, 'Dormentes', 'DORMENTES', 'M', 'PE', 'NE', 0),
(2605202, 'Escada', 'ESCADA', 'M', 'PE', 'NE', 0),
(2605301, 'Exu', 'EXU', 'M', 'PE', 'NE', 0),
(2605400, 'Feira Nova', 'FEIRA NOVA', 'M', 'PE', 'NE', 0),
(2605459, 'Fernando de Noronha', 'FERNANDO DE NORONHA', 'M', 'PE', 'NE', 0),
(2605509, 'Ferreiros', 'FERREIROS', 'M', 'PE', 'NE', 0),
(2605608, 'Flores', 'FLORES', 'M', 'PE', 'NE', 0),
(2605707, 'Floresta', 'FLORESTA', 'M', 'PE', 'NE', 0),
(2605806, 'Frei Miguelinho', 'FREI MIGUELINHO', 'M', 'PE', 'NE', 0),
(2605905, 'Gameleira', 'GAMELEIRA', 'M', 'PE', 'NE', 0),
(2606002, 'Garanhuns', 'GARANHUNS', 'M', 'PE', 'NE', 0),
(2606101, 'Glória do Goitá', 'GLORIA DO GOITA', 'M', 'PE', 'NE', 0),
(2606200, 'Goiana', 'GOIANA', 'M', 'PE', 'NE', 0),
(2606309, 'Granito', 'GRANITO', 'M', 'PE', 'NE', 0),
(2606408, 'Gravatá', 'GRAVATA', 'M', 'PE', 'NE', 0),
(2606507, 'Iati', 'IATI', 'M', 'PE', 'NE', 0),
(2606606, 'Ibimirim', 'IBIMIRIM', 'M', 'PE', 'NE', 0),
(2606705, 'Ibirajuba', 'IBIRAJUBA', 'M', 'PE', 'NE', 0),
(2606804, 'Igarassu', 'IGARASSU', 'M', 'PE', 'NE', 0),
(2606903, 'Iguaraci', 'IGUARACI', 'M', 'PE', 'NE', 0),
(2607000, 'Inajá', 'INAJA', 'M', 'PE', 'NE', 0),
(2607109, 'Ingazeira', 'INGAZEIRA', 'M', 'PE', 'NE', 0),
(2607208, 'Ipojuca', 'IPOJUCA', 'M', 'PE', 'NE', 0),
(2607307, 'Ipubi', 'IPUBI', 'M', 'PE', 'NE', 0),
(2607406, 'Itacuruba', 'ITACURUBA', 'M', 'PE', 'NE', 0),
(2607505, 'Itaíba', 'ITAIBA', 'M', 'PE', 'NE', 0),
(2607604, 'Itamaracá', 'ITAMARACA', 'M', 'PE', 'NE', 0),
(2607653, 'Itambé', 'ITAMBE', 'M', 'PE', 'NE', 0),
(2607703, 'Itapetim', 'ITAPETIM', 'M', 'PE', 'NE', 0),
(2607752, 'Itapissuma', 'ITAPISSUMA', 'M', 'PE', 'NE', 0),
(2607802, 'Itaquitinga', 'ITAQUITINGA', 'M', 'PE', 'NE', 0),
(2607901, 'Jaboatão dos Guararapes', 'JABOATAO DOS GUARARAPES', 'M', 'PE', 'NE', 0),
(2607950, 'Jaqueira', 'JAQUEIRA', 'M', 'PE', 'NE', 0),
(2608008, 'Jataúba', 'JATAUBA', 'M', 'PE', 'NE', 0),
(2608057, 'Jatobá', 'JATOBA', 'M', 'PE', 'NE', 0),
(2608107, 'João Alfredo', 'JOAO ALFREDO', 'M', 'PE', 'NE', 0),
(2608206, 'Joaquim Nabuco', 'JOAQUIM NABUCO', 'M', 'PE', 'NE', 0),
(2608255, 'Jucati', 'JUCATI', 'M', 'PE', 'NE', 0),
(2608305, 'Jupi', 'JUPI', 'M', 'PE', 'NE', 0),
(2608404, 'Jurema', 'JUREMA', 'M', 'PE', 'NE', 0),
(2608453, 'Lagoa do Carro', 'LAGOA DO CARRO', 'M', 'PE', 'NE', 0),
(2608503, 'Lagoa do Itaenga', 'LAGOA DO ITAENGA', 'M', 'PE', 'NE', 0),
(2608602, 'Lagoa do Ouro', 'LAGOA DO OURO', 'M', 'PE', 'NE', 0),
(2608701, 'Lagoa dos Gatos', 'LAGOA DOS GATOS', 'M', 'PE', 'NE', 0),
(2608750, 'Lagoa Grande', 'LAGOA GRANDE', 'M', 'PE', 'NE', 0),
(2608800, 'Lajedo', 'LAJEDO', 'M', 'PE', 'NE', 0),
(2608909, 'Limoeiro', 'LIMOEIRO', 'M', 'PE', 'NE', 0),
(2609006, 'Macaparana', 'MACAPARANA', 'M', 'PE', 'NE', 0),
(2609105, 'Machados', 'MACHADOS', 'M', 'PE', 'NE', 0),
(2609154, 'Manari', 'MANARI', 'M', 'PE', 'NE', 0),
(2609204, 'Maraial', 'MARAIAL', 'M', 'PE', 'NE', 0),
(2609303, 'Mirandiba', 'MIRANDIBA', 'M', 'PE', 'NE', 0),
(2609402, 'Moreno', 'MORENO', 'M', 'PE', 'NE', 0),
(2609501, 'Nazaré da Mata', 'NAZARE DA MATA', 'M', 'PE', 'NE', 0),
(2609600, 'Olinda', 'OLINDA', 'M', 'PE', 'NE', 0),
(2609709, 'Orobó', 'OROBO', 'M', 'PE', 'NE', 0),
(2609808, 'Orocó', 'OROCO', 'M', 'PE', 'NE', 0),
(2609907, 'Ouricuri', 'OURICURI', 'M', 'PE', 'NE', 0),
(2610004, 'Palmares', 'PALMARES', 'M', 'PE', 'NE', 0),
(2610103, 'Palmeirina', 'PALMEIRINA', 'M', 'PE', 'NE', 0),
(2610202, 'Panelas', 'PANELAS', 'M', 'PE', 'NE', 0),
(2610301, 'Paranatama', 'PARANATAMA', 'M', 'PE', 'NE', 0),
(2610400, 'Parnamirim', 'PARNAMIRIM', 'M', 'PE', 'NE', 0),
(2610509, 'Passira', 'PASSIRA', 'M', 'PE', 'NE', 0),
(2610608, 'Paudalho', 'PAUDALHO', 'M', 'PE', 'NE', 0),
(2610707, 'Paulista', 'PAULISTA', 'M', 'PE', 'NE', 0),
(2610806, 'Pedra', 'PEDRA', 'M', 'PE', 'NE', 0),
(2610905, 'Pesqueira', 'PESQUEIRA', 'M', 'PE', 'NE', 0),
(2611002, 'Petrolândia', 'PETROLANDIA', 'M', 'PE', 'NE', 0),
(2611101, 'Petrolina', 'PETROLINA', 'M', 'PE', 'NE', 0),
(2611200, 'Poção', 'POCAO', 'M', 'PE', 'NE', 0),
(2611309, 'Pombos', 'POMBOS', 'M', 'PE', 'NE', 0),
(2611408, 'Primavera', 'PRIMAVERA', 'M', 'PE', 'NE', 0),
(2611507, 'Quipapa', 'QUIPAPA', 'M', 'PE', 'NE', 0),
(2611533, 'Quixabá', 'QUIXABA', 'M', 'PE', 'NE', 0),
(2611606, 'Recife', 'RECIFE', 'M', 'PE', 'NE', 0),
(2611705, 'Riacho das Almas', 'RIACHO DAS ALMAS', 'M', 'PE', 'NE', 0),
(2611804, 'Ribeirão', 'RIBEIRAO', 'M', 'PE', 'NE', 0),
(2611903, 'Rio Formoso', 'RIO FORMOSO', 'M', 'PE', 'NE', 0),
(2612000, 'Sairé', 'SAIRE', 'M', 'PE', 'NE', 0),
(2612109, 'Salgadinho', 'SALGADINHO', 'M', 'PE', 'NE', 0),
(2612208, 'Salgueiro', 'SALGUEIRO', 'M', 'PE', 'NE', 0),
(2612307, 'Saloá', 'SALOA', 'M', 'PE', 'NE', 0),
(2612406, 'Sanharó', 'SANHARO', 'M', 'PE', 'NE', 0),
(2612455, 'Santa Cruz', 'SANTA CRUZ', 'M', 'PE', 'NE', 0),
(2612471, 'Santa Cruz da Baixa Verde', 'SANTA CRUZ DA BAIXA VERDE', 'M', 'PE', 'NE', 0),
(2612505, 'Santa Cruz do Capibaribe', 'SANTA CRUZ DO CAPIBARIBE', 'M', 'PE', 'NE', 0),
(2612554, 'Santa Filomena', 'SANTA FILOMENA', 'M', 'PE', 'NE', 0),
(2612604, 'Santa Maria da Boa Vista', 'SANTA MARIA DA BOA VISTA', 'M', 'PE', 'NE', 0),
(2612703, 'Santa Maria do Cambucá', 'SANTA MARIA DO CAMBUCA', 'M', 'PE', 'NE', 0),
(2612802, 'Santa Terezinha', 'SANTA TEREZINHA', 'M', 'PE', 'NE', 0),
(2612901, 'São Benedito do Sul', 'SAO BENEDITO DO SUL', 'M', 'PE', 'NE', 0),
(2613008, 'São Bento do Una', 'SAO BENTO DO UNA', 'M', 'PE', 'NE', 0),
(2613107, 'São Caitano', 'SAO CAITANO', 'M', 'PE', 'NE', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(2613206, 'São João', 'SAO JOAO', 'M', 'PE', 'NE', 0),
(2613305, 'São Joaquim do Monte', 'SAO JOAQUIM DO MONTE', 'M', 'PE', 'NE', 0),
(2613404, 'São José da Coroa Grande', 'SAO JOSE DA COROA GRANDE', 'M', 'PE', 'NE', 0),
(2613503, 'São José do Belmonte', 'SAO JOSE DO BELMONTE', 'M', 'PE', 'NE', 0),
(2613602, 'São José do Egito', 'SAO JOSE DO EGITO', 'M', 'PE', 'NE', 0),
(2613701, 'São Lourenco da Mata', 'SAO LOURENCO DA MATA', 'M', 'PE', 'NE', 0),
(2613800, 'São Vicente Ferrer', 'SAO VICENTE FERRER', 'M', 'PE', 'NE', 0),
(2613909, 'Serra Talhada', 'SERRA TALHADA', 'M', 'PE', 'NE', 0),
(2614006, 'Serrita', 'SERRITA', 'M', 'PE', 'NE', 0),
(2614105, 'Sertânia', 'SERTANIA', 'M', 'PE', 'NE', 0),
(2614204, 'Sirinhaém', 'SIRINHAEM', 'M', 'PE', 'NE', 0),
(2614303, 'Moreilândia', 'MOREILANDIA', 'M', 'PE', 'NE', 0),
(2614402, 'Solidao', 'SOLIDAO', 'M', 'PE', 'NE', 0),
(2614501, 'Surubim', 'SURUBIM', 'M', 'PE', 'NE', 0),
(2614600, 'Tabira', 'TABIRA', 'M', 'PE', 'NE', 0),
(2614709, 'Tacaimbó', 'TACAIMBO', 'M', 'PE', 'NE', 0),
(2614808, 'Tacaratu', 'TACARATU', 'M', 'PE', 'NE', 0),
(2614857, 'Tamandaré', 'TAMANDARE', 'M', 'PE', 'NE', 0),
(2615003, 'Taquaritinga do Norte', 'TAQUARITINGA DO NORTE', 'M', 'PE', 'NE', 0),
(2615102, 'Terezinha', 'TEREZINHA', 'M', 'PE', 'NE', 0),
(2615201, 'Terra Nova', 'TERRA NOVA', 'M', 'PE', 'NE', 0),
(2615300, 'Timbaúba', 'TIMBAUBA', 'M', 'PE', 'NE', 0),
(2615409, 'Toritama', 'TORITAMA', 'M', 'PE', 'NE', 0),
(2615508, 'Tracunhaem', 'TRACUNHAEM', 'M', 'PE', 'NE', 0),
(2615607, 'Trindade', 'TRINDADE', 'M', 'PE', 'NE', 0),
(2615706, 'Triunfo', 'TRIUNFO', 'M', 'PE', 'NE', 0),
(2615805, 'Tupanatinga', 'TUPANATINGA', 'M', 'PE', 'NE', 0),
(2615904, 'Tuparetama', 'TUPARETAMA', 'M', 'PE', 'NE', 0),
(2616001, 'Venturosa', 'VENTUROSA', 'M', 'PE', 'NE', 0),
(2616100, 'Verdejante', 'VERDEJANTE', 'M', 'PE', 'NE', 0),
(2616183, 'Vertente do Lério', 'VERTENTE DO LERIO', 'M', 'PE', 'NE', 0),
(2616209, 'Vertentes', 'VERTENTES', 'M', 'PE', 'NE', 0),
(2616308, 'Vicência', 'VICENCIA', 'M', 'PE', 'NE', 0),
(2616407, 'Vitória de Santo Antão', 'VITORIA DE SANTO ANTAO', 'M', 'PE', 'NE', 0),
(2616506, 'Xexéu', 'XEXEU', 'M', 'PE', 'NE', 0),
(2700000, 'Alagoas', 'ALAGOAS', 'U', 'AL', 'NE', 0),
(2700102, 'Água Branca', 'AGUA BRANCA', 'M', 'AL', 'NE', 0),
(2700201, 'Anadia', 'ANADIA', 'M', 'AL', 'NE', 0),
(2700300, 'Arapiraca', 'ARAPIRACA', 'M', 'AL', 'NE', 0),
(2700409, 'Atalaia', 'ATALAIA', 'M', 'AL', 'NE', 0),
(2700508, 'Barra de Santo Antônio', 'BARRA DE SANTO ANTONIO', 'M', 'AL', 'NE', 0),
(2700607, 'Barra de São Miguel', 'BARRA DE SAO MIGUEL', 'M', 'AL', 'NE', 0),
(2700706, 'Batalha', 'BATALHA', 'M', 'AL', 'NE', 0),
(2700805, 'Belém', 'BELEM', 'M', 'AL', 'NE', 0),
(2700904, 'Belo Monte', 'BELO MONTE', 'M', 'AL', 'NE', 0),
(2701001, 'Boca da Mata', 'BOCA DA MATA', 'M', 'AL', 'NE', 0),
(2701100, 'Branquinha', 'BRANQUINHA', 'M', 'AL', 'NE', 0),
(2701209, 'Cacimbinhas', 'CACIMBINHAS', 'M', 'AL', 'NE', 0),
(2701308, 'Cajueiro', 'CAJUEIRO', 'M', 'AL', 'NE', 0),
(2701357, 'Campestre', 'CAMPESTRE', 'M', 'AL', 'NE', 0),
(2701407, 'Campo Alegre', 'CAMPO ALEGRE', 'M', 'AL', 'NE', 0),
(2701506, 'Campo Grande', 'CAMPO GRANDE', 'M', 'AL', 'NE', 0),
(2701605, 'Canapi', 'CANAPI', 'M', 'AL', 'NE', 0),
(2701704, 'Capela', 'CAPELA', 'M', 'AL', 'NE', 0),
(2701803, 'Carneiros', 'CARNEIROS', 'M', 'AL', 'NE', 0),
(2701902, 'Chã Preta', 'CHA PRETA', 'M', 'AL', 'NE', 0),
(2702009, 'Coité do Nóia', 'COITE DO NOIA', 'M', 'AL', 'NE', 0),
(2702108, 'Colônia Leopoldina', 'COLONIA LEOPOLDINA', 'M', 'AL', 'NE', 0),
(2702207, 'Coqueiro Seco', 'COQUEIRO SECO', 'M', 'AL', 'NE', 0),
(2702306, 'Coruripe', 'CORURIPE', 'M', 'AL', 'NE', 0),
(2702355, 'Craíbas', 'CRAIBAS', 'M', 'AL', 'NE', 0),
(2702405, 'Delmiro Gouveia', 'DELMIRO GOUVEIA', 'M', 'AL', 'NE', 0),
(2702504, 'Dois Riachos', 'DOIS RIACHOS', 'M', 'AL', 'NE', 0),
(2702553, 'Estrela de Alagoas', 'ESTRELA DE ALAGOAS', 'M', 'AL', 'NE', 0),
(2702603, 'Feira Grande', 'FEIRA GRANDE', 'M', 'AL', 'NE', 0),
(2702702, 'Feliz Deserto', 'FELIZ DESERTO', 'M', 'AL', 'NE', 0),
(2702801, 'Flexeiras', 'FLEXEIRAS', 'M', 'AL', 'NE', 0),
(2702900, 'Girau do Ponciano', 'GIRAU DO PONCIANO', 'M', 'AL', 'NE', 0),
(2703007, 'Ibateguara', 'IBATEGUARA', 'M', 'AL', 'NE', 0),
(2703106, 'Igaci', 'IGACI', 'M', 'AL', 'NE', 0),
(2703205, 'Igreja Nova', 'IGREJA NOVA', 'M', 'AL', 'NE', 0),
(2703304, 'Inhapi', 'INHAPI', 'M', 'AL', 'NE', 0),
(2703403, 'Jacaré dos Homens', 'JACARE DOS HOMENS', 'M', 'AL', 'NE', 0),
(2703502, 'Jacuípe', 'JACUIPE', 'M', 'AL', 'NE', 0),
(2703601, 'Japaratinga', 'JAPARATINGA', 'M', 'AL', 'NE', 0),
(2703700, 'Jaramataia', 'JARAMATAIA', 'M', 'AL', 'NE', 0),
(2703759, 'Jequiá da Praia', 'JEQUIA DA PRAIA', 'M', 'AL', 'NE', 0),
(2703809, 'Joaquim Gomes', 'JOAQUIM GOMES', 'M', 'AL', 'NE', 0),
(2703908, 'Jundiá', 'JUNDIA', 'M', 'AL', 'NE', 0),
(2704005, 'Junqueiro', 'JUNQUEIRO', 'M', 'AL', 'NE', 0),
(2704104, 'Lagoa da Canoa', 'LAGOA DA CANOA', 'M', 'AL', 'NE', 0),
(2704203, 'Limoeiro de Anadia', 'LIMOEIRO DE ANADIA', 'M', 'AL', 'NE', 0),
(2704302, 'Maceió', 'MACEIO', 'M', 'AL', 'NE', 0),
(2704401, 'Major Isidoro', 'MAJOR ISIDORO', 'M', 'AL', 'NE', 0),
(2704500, 'Maragogi', 'MARAGOGI', 'M', 'AL', 'NE', 0),
(2704609, 'Maravilha', 'MARAVILHA', 'M', 'AL', 'NE', 0),
(2704708, 'Marechal Deodoro', 'MARECHAL DEODORO', 'M', 'AL', 'NE', 0),
(2704807, 'Maribondo', 'MARIBONDO', 'M', 'AL', 'NE', 0),
(2704906, 'Mar Vermelho', 'MAR VERMELHO', 'M', 'AL', 'NE', 0),
(2705002, 'Mata Grande', 'MATA GRANDE', 'M', 'AL', 'NE', 0),
(2705101, 'Matriz de Camaragibe', 'MATRIZ DE CAMARAGIBE', 'M', 'AL', 'NE', 0),
(2705200, 'Messias', 'MESSIAS', 'M', 'AL', 'NE', 0),
(2705309, 'Minador do Negrão', 'MINADOR DO NEGRAO', 'M', 'AL', 'NE', 0),
(2705408, 'Monteirópolis', 'MONTEIROPOLIS', 'M', 'AL', 'NE', 0),
(2705507, 'Murici', 'MURICI', 'M', 'AL', 'NE', 0),
(2705606, 'Novo Lino', 'NOVO LINO', 'M', 'AL', 'NE', 0),
(2705705, 'Olho D''Água das Flores', 'OLHO D''AGUA DAS FLORES', 'M', 'AL', 'NE', 0),
(2705804, 'Olho D''Água do Casado', 'OLHO D''AGUA DO CASADO', 'M', 'AL', 'NE', 0),
(2705903, 'Olho D''Água Grande', 'OLHO D''AGUA GRANDE', 'M', 'AL', 'NE', 0),
(2706000, 'Olivença', 'OLIVENCA', 'M', 'AL', 'NE', 0),
(2706109, 'Ouro Branco', 'OURO BRANCO', 'M', 'AL', 'NE', 0),
(2706208, 'Palestina', 'PALESTINA', 'M', 'AL', 'NE', 0),
(2706307, 'Palmeira dos Índios', 'PALMEIRA DOS INDIOS', 'M', 'AL', 'NE', 0),
(2706406, 'Pão de Açúcar', 'PAO DE ACUCAR', 'M', 'AL', 'NE', 0),
(2706422, 'Pariconha', 'PARICONHA', 'M', 'AL', 'NE', 0),
(2706448, 'Paripueira', 'PARIPUEIRA', 'M', 'AL', 'NE', 0),
(2706505, 'Passo de Camaragibe', 'PASSO DE CAMARAGIBE', 'M', 'AL', 'NE', 0),
(2706604, 'Paulo Jacinto', 'PAULO JACINTO', 'M', 'AL', 'NE', 0),
(2706703, 'Penedo', 'PENEDO', 'M', 'AL', 'NE', 0),
(2706802, 'Piaçabuçu', 'PIACABUCU', 'M', 'AL', 'NE', 0),
(2706901, 'Pilar', 'PILAR', 'M', 'AL', 'NE', 0),
(2707008, 'Pindoba', 'PINDOBA', 'M', 'AL', 'NE', 0),
(2707107, 'Piranhas', 'PIRANHAS', 'M', 'AL', 'NE', 0),
(2707206, 'Poco das Trincheiras', 'POCO DAS TRINCHEIRAS', 'M', 'AL', 'NE', 0),
(2707305, 'Porto Calvo', 'PORTO CALVO', 'M', 'AL', 'NE', 0),
(2707404, 'Porto de Pedras', 'PORTO DE PEDRAS', 'M', 'AL', 'NE', 0),
(2707503, 'Porto Real do Colégio', 'PORTO REAL DO COLEGIO', 'M', 'AL', 'NE', 0),
(2707602, 'Quebrangulo', 'QUEBRANGULO', 'M', 'AL', 'NE', 0),
(2707701, 'Rio Largo', 'RIO LARGO', 'M', 'AL', 'NE', 0),
(2707800, 'Roteiro', 'ROTEIRO', 'M', 'AL', 'NE', 0),
(2707909, 'Santa Luzia do Norte', 'SANTA LUZIA DO NORTE', 'M', 'AL', 'NE', 0),
(2708006, 'Santana do Ipanema', 'SANTANA DO IPANEMA', 'M', 'AL', 'NE', 0),
(2708105, 'Santana do Mundaú', 'SANTANA DO MUNDAU', 'M', 'AL', 'NE', 0),
(2708204, 'São Brás', 'SAO BRAS', 'M', 'AL', 'NE', 0),
(2708303, 'São José da Laje', 'SAO JOSE DA LAJE', 'M', 'AL', 'NE', 0),
(2708402, 'São José da Tapera', 'SAO JOSE DA TAPERA', 'M', 'AL', 'NE', 0),
(2708501, 'São Luís do Quitunde', 'SAO LUIS DO QUITUNDE', 'M', 'AL', 'NE', 0),
(2708600, 'São Miguel dos Campos', 'SAO MIGUEL DOS CAMPOS', 'M', 'AL', 'NE', 0),
(2708709, 'São Miguel dos Milagres', 'SAO MIGUEL DOS MILAGRES', 'M', 'AL', 'NE', 0),
(2708808, 'São Sebastião', 'SAO SEBASTIAO', 'M', 'AL', 'NE', 0),
(2708907, 'Satuba', 'SATUBA', 'M', 'AL', 'NE', 0),
(2708956, 'Senador Rui Palmeira', 'SENADOR RUI PALMEIRA', 'M', 'AL', 'NE', 0),
(2709004, 'Tanque D''arca', 'TANQUE D''ARCA', 'M', 'AL', 'NE', 0),
(2709103, 'Taquarana', 'TAQUARANA', 'M', 'AL', 'NE', 0),
(2709152, 'Teotônio Vilela', 'TEOTONIO VILELA', 'M', 'AL', 'NE', 0),
(2709202, 'Traipu', 'TRAIPU', 'M', 'AL', 'NE', 0),
(2709301, 'Uniao dos Palmares', 'UNIAO DOS PALMARES', 'M', 'AL', 'NE', 0),
(2709400, 'Viçosa', 'VICOSA', 'M', 'AL', 'NE', 0),
(2800000, 'Sergipe', 'SERGIPE', 'U', 'SE', 'NE', 0),
(2800100, 'Amparo de São Francisco', 'AMPARO DE SAO FRANCISCO', 'M', 'SE', 'NE', 0),
(2800209, 'Aquidabã', 'AQUIDABA', 'M', 'SE', 'NE', 0),
(2800308, 'Aracaju', 'ARACAJU', 'M', 'SE', 'NE', 0),
(2800407, 'Arauá', 'ARAUA', 'M', 'SE', 'NE', 0),
(2800506, 'Areia Branca', 'AREIA BRANCA', 'M', 'SE', 'NE', 0),
(2800605, 'Barra dos Coqueiros', 'BARRA DOS COQUEIROS', 'M', 'SE', 'NE', 0),
(2800670, 'Boquim', 'BOQUIM', 'M', 'SE', 'NE', 0),
(2800704, 'Brejo Grande', 'BREJO GRANDE', 'M', 'SE', 'NE', 0),
(2801009, 'Campo do Brito', 'CAMPO DO BRITO', 'M', 'SE', 'NE', 0),
(2801108, 'Canhoba', 'CANHOBA', 'M', 'SE', 'NE', 0),
(2801207, 'Canindé de São Francisco', 'CANINDE DE SAO FRANCISCO', 'M', 'SE', 'NE', 0),
(2801306, 'Capela', 'CAPELA', 'M', 'SE', 'NE', 0),
(2801405, 'Carira', 'CARIRA', 'M', 'SE', 'NE', 0),
(2801504, 'Carmópolis', 'CARMOPOLIS', 'M', 'SE', 'NE', 0),
(2801603, 'Cedro de São João', 'CEDRO DE SAO JOAO', 'M', 'SE', 'NE', 0),
(2801702, 'Cristinápolis', 'CRISTINAPOLIS', 'M', 'SE', 'NE', 0),
(2801900, 'Cumbe', 'CUMBE', 'M', 'SE', 'NE', 0),
(2802007, 'Divina Pastora', 'DIVINA PASTORA', 'M', 'SE', 'NE', 0),
(2802106, 'Estância', 'ESTANCIA', 'M', 'SE', 'NE', 0),
(2802205, 'Feira Nova', 'FEIRA NOVA', 'M', 'SE', 'NE', 0),
(2802304, 'Frei Paulo', 'FREI PAULO', 'M', 'SE', 'NE', 0),
(2802403, 'Gararu', 'GARARU', 'M', 'SE', 'NE', 0),
(2802502, 'General Maynard', 'GENERAL MAYNARD', 'M', 'SE', 'NE', 0),
(2802601, 'Gracho Cardoso', 'GRACHO CARDOSO', 'M', 'SE', 'NE', 0),
(2802700, 'Ilha das Flores', 'ILHA DAS FLORES', 'M', 'SE', 'NE', 0),
(2802809, 'Indiaroba', 'INDIAROBA', 'M', 'SE', 'NE', 0),
(2802908, 'Itabaiana', 'ITABAIANA', 'M', 'SE', 'NE', 0),
(2803005, 'Itabaianinha', 'ITABAIANINHA', 'M', 'SE', 'NE', 0),
(2803104, 'Itabi', 'ITABI', 'M', 'SE', 'NE', 0),
(2803203, 'Itaporanga D''ajuda', 'ITAPORANGA D''AJUDA', 'M', 'SE', 'NE', 0),
(2803302, 'Japaratuba', 'JAPARATUBA', 'M', 'SE', 'NE', 0),
(2803401, 'Japoatã', 'JAPOATA', 'M', 'SE', 'NE', 0),
(2803500, 'Lagarto', 'LAGARTO', 'M', 'SE', 'NE', 0),
(2803609, 'Laranjeiras', 'LARANJEIRAS', 'M', 'SE', 'NE', 0),
(2803708, 'Macambira', 'MACAMBIRA', 'M', 'SE', 'NE', 0),
(2803807, 'Malhada dos Bois', 'MALHADA DOS BOIS', 'M', 'SE', 'NE', 0),
(2803906, 'Malhador', 'MALHADOR', 'M', 'SE', 'NE', 0),
(2804003, 'Maruim', 'MARUIM', 'M', 'SE', 'NE', 0),
(2804102, 'Moita Bonita', 'MOITA BONITA', 'M', 'SE', 'NE', 0),
(2804201, 'Monte Alegre de Sergipe', 'MONTE ALEGRE DE SERGIPE', 'M', 'SE', 'NE', 0),
(2804300, 'Muribeca', 'MURIBECA', 'M', 'SE', 'NE', 0),
(2804409, 'Neópolis', 'NEOPOLIS', 'M', 'SE', 'NE', 0),
(2804458, 'Nossa Senhora Aparecida', 'NOSSA SENHORA APARECIDA', 'M', 'SE', 'NE', 0),
(2804508, 'Nossa Senhora da Glória', 'NOSSA SENHORA DA GLORIA', 'M', 'SE', 'NE', 0),
(2804607, 'Nossa Senhora das Dores', 'NOSSA SENHORA DAS DORES', 'M', 'SE', 'NE', 0),
(2804706, 'Nossa Senhora de Lourdes', 'NOSSA SENHORA DE LOURDES', 'M', 'SE', 'NE', 0),
(2804805, 'Nossa Senhora do Socorro', 'NOSSA SENHORA DO SOCORRO', 'M', 'SE', 'NE', 0),
(2804904, 'Pacatuba', 'PACATUBA', 'M', 'SE', 'NE', 0),
(2805000, 'Pedra Mole', 'PEDRA MOLE', 'M', 'SE', 'NE', 0),
(2805109, 'Pedrinhas', 'PEDRINHAS', 'M', 'SE', 'NE', 0),
(2805208, 'Pinhão', 'PINHAO', 'M', 'SE', 'NE', 0),
(2805307, 'Pirambu', 'PIRAMBU', 'M', 'SE', 'NE', 0),
(2805406, 'Poço Redondo', 'POCO REDONDO', 'M', 'SE', 'NE', 0),
(2805505, 'Poço Verde', 'POCO VERDE', 'M', 'SE', 'NE', 0),
(2805604, 'Porto da Folha', 'PORTO DA FOLHA', 'M', 'SE', 'NE', 0),
(2805703, 'Propriá', 'PROPRIA', 'M', 'SE', 'NE', 0),
(2805802, 'Riachaão do Dantas', 'RIACHAO DO DANTAS', 'M', 'SE', 'NE', 0),
(2805901, 'Riachuelo', 'RIACHUELO', 'M', 'SE', 'NE', 0),
(2806008, 'Ribeirópolis', 'RIBEIROPOLIS', 'M', 'SE', 'NE', 0),
(2806107, 'Rosário do Catete', 'ROSARIO DO CATETE', 'M', 'SE', 'NE', 0),
(2806206, 'Salgado', 'SALGADO', 'M', 'SE', 'NE', 0),
(2806305, 'Santa Luzia do Itanhy', 'SANTA LUZIA DO ITANHY', 'M', 'SE', 'NE', 0),
(2806404, 'Santana de São Francisco', 'SANTANA DO SAO FRANCISCO', 'M', 'SE', 'NE', 0),
(2806503, 'Santa Rosa de Lima', 'SANTA ROSA DE LIMA', 'M', 'SE', 'NE', 0),
(2806602, 'Santo Amaro das Brotas', 'SANTO AMARO DAS BROTAS', 'M', 'SE', 'NE', 0),
(2806701, 'São Cristóvão', 'SAO CRISTOVAO', 'M', 'SE', 'NE', 0),
(2806800, 'São Domingos', 'SAO DOMINGOS', 'M', 'SE', 'NE', 0),
(2806909, 'São Francisco', 'SAO FRANCISCO', 'M', 'SE', 'NE', 0),
(2807006, 'São Miguel do Aleixo', 'SAO MIGUEL DO ALEIXO', 'M', 'SE', 'NE', 0),
(2807105, 'Simão Dias', 'SIMAO DIAS', 'M', 'SE', 'NE', 0),
(2807204, 'Siriri', 'SIRIRI', 'M', 'SE', 'NE', 0),
(2807303, 'Telha', 'TELHA', 'M', 'SE', 'NE', 0),
(2807402, 'Tobias Barreto', 'TOBIAS BARRETO', 'M', 'SE', 'NE', 0),
(2807501, 'Tomar do Geru', 'TOMAR DO GERU', 'M', 'SE', 'NE', 0),
(2807600, 'Umbaúba', 'UMBAUBA', 'M', 'SE', 'NE', 0),
(2900000, 'Bahia', 'BAHIA', 'U', 'BA', 'NE', 0),
(2900108, 'Abaíra', 'ABAIRA', 'M', 'BA', 'NE', 0),
(2900207, 'Abaré', 'ABARE', 'M', 'BA', 'NE', 0),
(2900306, 'Acajutiba', 'ACAJUTIBA', 'M', 'BA', 'NE', 0),
(2900355, 'Adustina', 'ADUSTINA', 'M', 'BA', 'NE', 0),
(2900405, 'Água Fria', 'AGUA FRIA', 'M', 'BA', 'NE', 0),
(2900504, 'Erico Cardoso', 'ERICO CARDOSO', 'M', 'BA', 'NE', 0),
(2900603, 'Aiquara', 'AIQUARA', 'M', 'BA', 'NE', 0),
(2900702, 'Alagoinhas', 'ALAGOINHAS', 'M', 'BA', 'NE', 0),
(2900801, 'Alcobaça', 'ALCOBACA', 'M', 'BA', 'NE', 0),
(2900900, 'Almadina', 'ALMADINA', 'M', 'BA', 'NE', 0),
(2901007, 'Amargosa', 'AMARGOSA', 'M', 'BA', 'NE', 0),
(2901106, 'Amélia Rodrigues', 'AMELIA RODRIGUES', 'M', 'BA', 'NE', 0),
(2901155, 'América Dourada', 'AMERICA DOURADA', 'M', 'BA', 'NE', 0),
(2901205, 'Anagé', 'ANAGE', 'M', 'BA', 'NE', 0),
(2901304, 'Andaraí', 'ANDARAI', 'M', 'BA', 'NE', 0),
(2901353, 'Andorinha', 'ANDORINHA', 'M', 'BA', 'NE', 0),
(2901403, 'Angical', 'ANGICAL', 'M', 'BA', 'NE', 0),
(2901502, 'Anguera', 'ANGUERA', 'M', 'BA', 'NE', 0),
(2901601, 'Antas', 'ANTAS', 'M', 'BA', 'NE', 0),
(2901700, 'Antônio Cardoso', 'ANTONIO CARDOSO', 'M', 'BA', 'NE', 0),
(2901809, 'Antônio Goncalves', 'ANTONIO GONCALVES', 'M', 'BA', 'NE', 0),
(2901908, 'Aporá', 'APORA', 'M', 'BA', 'NE', 0),
(2901957, 'Apuarema', 'APUAREMA', 'M', 'BA', 'NE', 0),
(2902005, 'Aracatu', 'ARACATU', 'M', 'BA', 'NE', 0),
(2902054, 'Aracas', 'ARACAS', 'M', 'BA', 'NE', 0),
(2902104, 'Araci', 'ARACI', 'M', 'BA', 'NE', 0),
(2902203, 'Aramari', 'ARAMARI', 'M', 'BA', 'NE', 0),
(2902252, 'Arataca', 'ARATACA', 'M', 'BA', 'NE', 0),
(2902302, 'Aratuípe', 'ARATUIPE', 'M', 'BA', 'NE', 0),
(2902401, 'Aurelino Leal', 'AURELINO LEAL', 'M', 'BA', 'NE', 0),
(2902500, 'Baianópolis', 'BAIANOPOLIS', 'M', 'BA', 'NE', 0),
(2902609, 'Baixa Grande', 'BAIXA GRANDE', 'M', 'BA', 'NE', 0),
(2902658, 'Banzaê', 'BANZAE', 'M', 'BA', 'NE', 0),
(2902708, 'Barra', 'BARRA', 'M', 'BA', 'NE', 0),
(2902807, 'Barra da Estiva', 'BARRA DA ESTIVA', 'M', 'BA', 'NE', 0),
(2902906, 'Barra do Choça', 'BARRA DO CHOCA', 'M', 'BA', 'NE', 0),
(2903003, 'Barra do Mendes', 'BARRA DO MENDES', 'M', 'BA', 'NE', 0),
(2903102, 'Barra do Rocha', 'BARRA DO ROCHA', 'M', 'BA', 'NE', 0),
(2903201, 'Barreiras', 'BARREIRAS', 'M', 'BA', 'NE', 0),
(2903235, 'Barro Alto', 'BARRO ALTO', 'M', 'BA', 'NE', 0),
(2903276, 'Barrocas', 'BARROCAS', 'M', 'BA', 'NE', 0),
(2903300, 'Barro Preto', 'BARRO PRETO', 'M', 'BA', 'NE', 0),
(2903409, 'Belmonte', 'BELMONTE', 'M', 'BA', 'NE', 0),
(2903508, 'Belo Campo', 'BELO CAMPO', 'M', 'BA', 'NE', 0),
(2903607, 'Biritinga', 'BIRITINGA', 'M', 'BA', 'NE', 0),
(2903706, 'Boa Nova', 'BOA NOVA', 'M', 'BA', 'NE', 0),
(2903805, 'Boa Vista do Tupim', 'BOA VISTA DO TUPIM', 'M', 'BA', 'NE', 0),
(2903904, 'Bom Jesus da Lapa', 'BOM JESUS DA LAPA', 'M', 'BA', 'NE', 0),
(2903953, 'Bom Jesus da Serra', 'BOM JESUS DA SERRA', 'M', 'BA', 'NE', 0),
(2904001, 'Boninal', 'BONINAL', 'M', 'BA', 'NE', 0),
(2904050, 'Bonito', 'BONITO', 'M', 'BA', 'NE', 0),
(2904100, 'Boquira', 'BOQUIRA', 'M', 'BA', 'NE', 0),
(2904209, 'Botuporã', 'BOTUPORA', 'M', 'BA', 'NE', 0),
(2904308, 'Brejões', 'BREJOES', 'M', 'BA', 'NE', 0),
(2904407, 'Brejolândia', 'BREJOLANDIA', 'M', 'BA', 'NE', 0),
(2904506, 'Brotas de Macaúbas', 'BROTAS DE MACAUBAS', 'M', 'BA', 'NE', 0),
(2904605, 'Brumado', 'BRUMADO', 'M', 'BA', 'NE', 0),
(2904704, 'Buerarema', 'BUERAREMA', 'M', 'BA', 'NE', 0),
(2904753, 'Buritirama', 'BURITIRAMA', 'M', 'BA', 'NE', 0),
(2904803, 'Caatiba', 'CAATIBA', 'M', 'BA', 'NE', 0),
(2904852, 'Cabaceiras do Paraguaçu', 'CABACEIRAS DO PARAGUACU', 'M', 'BA', 'NE', 0),
(2904902, 'Cachoeira', 'CACHOEIRA', 'M', 'BA', 'NE', 0),
(2905008, 'Caculé', 'CACULE', 'M', 'BA', 'NE', 0),
(2905107, 'Caém', 'CAEM', 'M', 'BA', 'NE', 0),
(2905156, 'Caetanos', 'CAETANOS', 'M', 'BA', 'NE', 0),
(2905206, 'Caetite', 'CAETITE', 'M', 'BA', 'NE', 0),
(2905305, 'Cafarnaum', 'CAFARNAUM', 'M', 'BA', 'NE', 0),
(2905404, 'Cairu', 'CAIRU', 'M', 'BA', 'NE', 0),
(2905503, 'Caldeirão Grande', 'CALDEIRAO GRANDE', 'M', 'BA', 'NE', 0),
(2905602, 'Camacan', 'CAMACAN', 'M', 'BA', 'NE', 0),
(2905701, 'Camaçari', 'CAMACARI', 'M', 'BA', 'NE', 0),
(2905800, 'Camamu', 'CAMAMU', 'M', 'BA', 'NE', 0),
(2905909, 'Campo Alegre de Lourdes', 'CAMPO ALEGRE DE LOURDES', 'M', 'BA', 'NE', 0),
(2906006, 'Campo Formoso', 'CAMPO FORMOSO', 'M', 'BA', 'NE', 0),
(2906105, 'Canápolis', 'CANAPOLIS', 'M', 'BA', 'NE', 0),
(2906204, 'Canarana', 'CANARANA', 'M', 'BA', 'NE', 0),
(2906303, 'Canavieiras', 'CANAVIEIRAS', 'M', 'BA', 'NE', 0),
(2906402, 'Candeal', 'CANDEAL', 'M', 'BA', 'NE', 0),
(2906501, 'Candeias', 'CANDEIAS', 'M', 'BA', 'NE', 0),
(2906600, 'Candiba', 'CANDIBA', 'M', 'BA', 'NE', 0),
(2906709, 'Cândido Sales', 'CANDIDO SALES', 'M', 'BA', 'NE', 0),
(2906808, 'Cansanção', 'CANSANCAO', 'M', 'BA', 'NE', 0),
(2906824, 'Canudos', 'CANUDOS', 'M', 'BA', 'NE', 0),
(2906857, 'Capela do Alto Alegre', 'CAPELA DO ALTO ALEGRE', 'M', 'BA', 'NE', 0),
(2906873, 'Capim Grosso', 'CAPIM GROSSO', 'M', 'BA', 'NE', 0),
(2906899, 'Caraíbas', 'CARAIBAS', 'M', 'BA', 'NE', 0),
(2906907, 'Caravelas', 'CARAVELAS', 'M', 'BA', 'NE', 0),
(2907004, 'Cardeal da Silva', 'CARDEAL DA SILVA', 'M', 'BA', 'NE', 0),
(2907103, 'Carinhanha', 'CARINHANHA', 'M', 'BA', 'NE', 0),
(2907202, 'Casa Nova', 'CASA NOVA', 'M', 'BA', 'NE', 0),
(2907301, 'Castro Alves', 'CASTRO ALVES', 'M', 'BA', 'NE', 0),
(2907400, 'Catolandia', 'CATOLANDIA', 'M', 'BA', 'NE', 0),
(2907509, 'Catu', 'CATU', 'M', 'BA', 'NE', 0),
(2907558, 'Caturama', 'CATURAMA', 'M', 'BA', 'NE', 0),
(2907608, 'Central', 'CENTRAL', 'M', 'BA', 'NE', 0),
(2907707, 'Chorrochó', 'CHORROCHO', 'M', 'BA', 'NE', 0),
(2907806, 'Cícero Dantas', 'CICERO DANTAS', 'M', 'BA', 'NE', 0),
(2907905, 'Cipó', 'CIPO', 'M', 'BA', 'NE', 0),
(2908002, 'Coaraci', 'COARACI', 'M', 'BA', 'NE', 0),
(2908101, 'Cocos', 'COCOS', 'M', 'BA', 'NE', 0),
(2908200, 'Conceição da Feira', 'CONCEICAO DA FEIRA', 'M', 'BA', 'NE', 0),
(2908309, 'Conceição do Almeida', 'CONCEICAO DO ALMEIDA', 'M', 'BA', 'NE', 0),
(2908408, 'Conceição do Coité', 'CONCEICAO DO COITE', 'M', 'BA', 'NE', 0),
(2908507, 'Conceicao do Jacuípe', 'CONCEICAO DO JACUIPE', 'M', 'BA', 'NE', 0),
(2908606, 'Conde', 'CONDE', 'M', 'BA', 'NE', 0),
(2908705, 'Condeúba', 'CONDEUBA', 'M', 'BA', 'NE', 0),
(2908804, 'Contendas do Sincorá', 'CONTENDAS DO SINCORA', 'M', 'BA', 'NE', 0),
(2908903, 'Coração de Maria', 'CORACAO DE MARIA', 'M', 'BA', 'NE', 0),
(2909000, 'Cordeiros', 'CORDEIROS', 'M', 'BA', 'NE', 0),
(2909109, 'Coribe', 'CORIBE', 'M', 'BA', 'NE', 0),
(2909208, 'Coronel João Sá', 'CORONEL JOAO SA', 'M', 'BA', 'NE', 0),
(2909307, 'Correntina', 'CORRENTINA', 'M', 'BA', 'NE', 0),
(2909406, 'Cotegipe', 'COTEGIPE', 'M', 'BA', 'NE', 0),
(2909505, 'Cravolândia', 'CRAVOLANDIA', 'M', 'BA', 'NE', 0),
(2909604, 'Crisópolis', 'CRISOPOLIS', 'M', 'BA', 'NE', 0),
(2909703, 'Cristópolis', 'CRISTOPOLIS', 'M', 'BA', 'NE', 0),
(2909802, 'Cruz das Almas', 'CRUZ DAS ALMAS', 'M', 'BA', 'NE', 0),
(2909901, 'Curaçá', 'CURACA', 'M', 'BA', 'NE', 0),
(2910008, 'Dário Meira', 'DARIO MEIRA', 'M', 'BA', 'NE', 0),
(2910057, 'Dias D''Ávila', 'DIAS D''AVILA', 'M', 'BA', 'NE', 0),
(2910107, 'Dom Basílio', 'DOM BASILIO', 'M', 'BA', 'NE', 0),
(2910206, 'Dom Macedo Costa', 'DOM MACEDO COSTA', 'M', 'BA', 'NE', 0),
(2910305, 'Elísio Medrado', 'ELISIO MEDRADO', 'M', 'BA', 'NE', 0),
(2910404, 'Encruzilhada', 'ENCRUZILHADA', 'M', 'BA', 'NE', 0),
(2910503, 'Entre Rios', 'ENTRE RIOS', 'M', 'BA', 'NE', 0),
(2910602, 'Esplanada', 'ESPLANADA', 'M', 'BA', 'NE', 0),
(2910701, 'Euclides da Cunha', 'EUCLIDES DA CUNHA', 'M', 'BA', 'NE', 0),
(2910727, 'Eunápolis', 'EUNAPOLIS', 'M', 'BA', 'NE', 0),
(2910750, 'Fátima', 'FATIMA', 'M', 'BA', 'NE', 0),
(2910776, 'Feira da Mata', 'FEIRA DA MATA', 'M', 'BA', 'NE', 0),
(2910800, 'Feira de Santana', 'FEIRA DE SANTANA', 'M', 'BA', 'NE', 0),
(2910859, 'Filadélfia', 'FILADELFIA', 'M', 'BA', 'NE', 0),
(2910909, 'Firmino Alves', 'FIRMINO ALVES', 'M', 'BA', 'NE', 0),
(2911006, 'Floresta Azul', 'FLORESTA AZUL', 'M', 'BA', 'NE', 0),
(2911105, 'Formosa do Rio Preto', 'FORMOSA DO RIO PRETO', 'M', 'BA', 'NE', 0),
(2911204, 'Gandu', 'GANDU', 'M', 'BA', 'NE', 0),
(2911253, 'Gavião', 'GAVIAO', 'M', 'BA', 'NE', 0),
(2911303, 'Gentio do Ouro', 'GENTIO DO OURO', 'M', 'BA', 'NE', 0),
(2911402, 'Glória', 'GLORIA', 'M', 'BA', 'NE', 0),
(2911501, 'Gongogi', 'GONGOGI', 'M', 'BA', 'NE', 0),
(2911600, 'Governador Mangabeira', 'GOVERNADOR MANGABEIRA', 'M', 'BA', 'NE', 0),
(2911659, 'Guajeru', 'GUAJERU', 'M', 'BA', 'NE', 0),
(2911709, 'Guanambi', 'GUANAMBI', 'M', 'BA', 'NE', 0),
(2911808, 'Guaratinga', 'GUARATINGA', 'M', 'BA', 'NE', 0),
(2911857, 'Heliópolis', 'HELIOPOLIS', 'M', 'BA', 'NE', 0),
(2911907, 'Iacu', 'IACU', 'M', 'BA', 'NE', 0),
(2912004, 'Ibiassucê', 'IBIASSUCE', 'M', 'BA', 'NE', 0),
(2912103, 'Ibicaraí', 'IBICARAI', 'M', 'BA', 'NE', 0),
(2912202, 'Ibicoara', 'IBICOARA', 'M', 'BA', 'NE', 0),
(2912301, 'Ibicuí', 'IBICUI', 'M', 'BA', 'NE', 0),
(2912400, 'Ibipeba', 'IBIPEBA', 'M', 'BA', 'NE', 0),
(2912509, 'Ibipitanga', 'IBIPITANGA', 'M', 'BA', 'NE', 0),
(2912608, 'Ibiquera', 'IBIQUERA', 'M', 'BA', 'NE', 0),
(2912707, 'Ibirapitanga', 'IBIRAPITANGA', 'M', 'BA', 'NE', 0),
(2912806, 'Ibirapuã', 'IBIRAPUA', 'M', 'BA', 'NE', 0),
(2912905, 'Ibirataia', 'IBIRATAIA', 'M', 'BA', 'NE', 0),
(2913002, 'Ibitiara', 'IBITIARA', 'M', 'BA', 'NE', 0),
(2913101, 'Ibititá', 'IBITITA', 'M', 'BA', 'NE', 0),
(2913200, 'Ibotirama', 'IBOTIRAMA', 'M', 'BA', 'NE', 0),
(2913309, 'Ichu', 'ICHU', 'M', 'BA', 'NE', 0),
(2913408, 'Igaporã', 'IGAPORA', 'M', 'BA', 'NE', 0),
(2913457, 'Igrapiúna', 'IGRAPIUNA', 'M', 'BA', 'NE', 0),
(2913507, 'Iguaí', 'IGUAI', 'M', 'BA', 'NE', 0),
(2913606, 'Ilhéus', 'ILHEUS', 'M', 'BA', 'NE', 0),
(2913705, 'Inhambupe', 'INHAMBUPE', 'M', 'BA', 'NE', 0),
(2913804, 'Ipecaetá', 'IPECAETA', 'M', 'BA', 'NE', 0),
(2913903, 'Ipiaú', 'IPIAU', 'M', 'BA', 'NE', 0),
(2914000, 'Ipirá', 'IPIRA', 'M', 'BA', 'NE', 0),
(2914109, 'Ipupiara', 'IPUPIARA', 'M', 'BA', 'NE', 0),
(2914208, 'Irajuba', 'IRAJUBA', 'M', 'BA', 'NE', 0),
(2914307, 'Iramaia', 'IRAMAIA', 'M', 'BA', 'NE', 0),
(2914406, 'Iraquara', 'IRAQUARA', 'M', 'BA', 'NE', 0),
(2914505, 'Irará', 'IRARA', 'M', 'BA', 'NE', 0),
(2914604, 'Irecê', 'IRECE', 'M', 'BA', 'NE', 0),
(2914653, 'Itabela', 'ITABELA', 'M', 'BA', 'NE', 0),
(2914703, 'Itaberaba', 'ITABERABA', 'M', 'BA', 'NE', 0),
(2914802, 'Itabuna', 'ITABUNA', 'M', 'BA', 'NE', 0),
(2914901, 'Itacare', 'ITACARE', 'M', 'BA', 'NE', 0),
(2915007, 'Itaete', 'ITAETE', 'M', 'BA', 'NE', 0),
(2915106, 'Itagi', 'ITAGI', 'M', 'BA', 'NE', 0),
(2915205, 'Itagibá', 'ITAGIBA', 'M', 'BA', 'NE', 0),
(2915304, 'Itagimirim', 'ITAGIMIRIM', 'M', 'BA', 'NE', 0),
(2915353, 'Itaguaçu da Bahia', 'ITAGUACU DA BAHIA', 'M', 'BA', 'NE', 0),
(2915403, 'Itaju do Colônia', 'ITAJU DO COLONIA', 'M', 'BA', 'NE', 0),
(2915502, 'Itajuípe', 'ITAJUIPE', 'M', 'BA', 'NE', 0),
(2915601, 'Itamaraju', 'ITAMARAJU', 'M', 'BA', 'NE', 0),
(2915700, 'Itamari', 'ITAMARI', 'M', 'BA', 'NE', 0),
(2915809, 'Itambé', 'ITAMBE', 'M', 'BA', 'NE', 0),
(2915908, 'Itanagra', 'ITANAGRA', 'M', 'BA', 'NE', 0),
(2916005, 'Itanhem', 'ITANHEM', 'M', 'BA', 'NE', 0),
(2916104, 'Itaparica', 'ITAPARICA', 'M', 'BA', 'NE', 0),
(2916203, 'Itapeé', 'ITAPE', 'M', 'BA', 'NE', 0),
(2916302, 'Itapebi', 'ITAPEBI', 'M', 'BA', 'NE', 0),
(2916401, 'Itapetinga', 'ITAPETINGA', 'M', 'BA', 'NE', 0),
(2916500, 'Itapicuru', 'ITAPICURU', 'M', 'BA', 'NE', 0),
(2916609, 'Itapitanga', 'ITAPITANGA', 'M', 'BA', 'NE', 0),
(2916708, 'Itaquara', 'ITAQUARA', 'M', 'BA', 'NE', 0),
(2916807, 'Itarantim', 'ITARANTIM', 'M', 'BA', 'NE', 0),
(2916856, 'Itatim', 'ITATIM', 'M', 'BA', 'NE', 0),
(2916906, 'Itiruçu', 'ITIRUCU', 'M', 'BA', 'NE', 0),
(2917003, 'Itiuba', 'ITIUBA', 'M', 'BA', 'NE', 0),
(2917102, 'Itororo', 'ITORORO', 'M', 'BA', 'NE', 0),
(2917201, 'Ituacu', 'ITUACU', 'M', 'BA', 'NE', 0),
(2917300, 'Itubera', 'ITUBERA', 'M', 'BA', 'NE', 0),
(2917334, 'Iuiú', 'IUIU', 'M', 'BA', 'NE', 0),
(2917359, 'Jaborandi', 'JABORANDI', 'M', 'BA', 'NE', 0),
(2917409, 'Jacaraci', 'JACARACI', 'M', 'BA', 'NE', 0),
(2917508, 'Jacobina', 'JACOBINA', 'M', 'BA', 'NE', 0),
(2917607, 'Jaguaquara', 'JAGUAQUARA', 'M', 'BA', 'NE', 0),
(2917706, 'Jaguarari', 'JAGUARARI', 'M', 'BA', 'NE', 0),
(2917805, 'Jaguaripe', 'JAGUARIPE', 'M', 'BA', 'NE', 0),
(2917904, 'Jandaira', 'JANDAIRA', 'M', 'BA', 'NE', 0),
(2918001, 'Jequié', 'JEQUIE', 'M', 'BA', 'NE', 0),
(2918100, 'Jeremoabo', 'JEREMOABO', 'M', 'BA', 'NE', 0),
(2918209, 'Jiquiriçá', 'JIQUIRICA', 'M', 'BA', 'NE', 0),
(2918308, 'Jitaúna', 'JITAUNA', 'M', 'BA', 'NE', 0),
(2918357, 'João Dourado', 'JOAO DOURADO', 'M', 'BA', 'NE', 0),
(2918407, 'Juazeiro', 'JUAZEIRO', 'M', 'BA', 'NE', 0),
(2918456, 'Jucuruçu', 'JUCURUCU', 'M', 'BA', 'NE', 0),
(2918506, 'Jussara', 'JUSSARA', 'M', 'BA', 'NE', 0),
(2918555, 'Jussari', 'JUSSARI', 'M', 'BA', 'NE', 0),
(2918605, 'Jussiape', 'JUSSIAPE', 'M', 'BA', 'NE', 0),
(2918704, 'Lafaiete Coutinho', 'LAFAIETE COUTINHO', 'M', 'BA', 'NE', 0),
(2918753, 'Lagoa Real', 'LAGOA REAL', 'M', 'BA', 'NE', 0),
(2918803, 'Laje', 'LAJE', 'M', 'BA', 'NE', 0),
(2918902, 'Lajedão', 'LAJEDAO', 'M', 'BA', 'NE', 0),
(2919009, 'Lajedinho', 'LAJEDINHO', 'M', 'BA', 'NE', 0),
(2919058, 'Lajedo do Tabocal', 'LAJEDO DO TABOCAL', 'M', 'BA', 'NE', 0),
(2919108, 'Lamarão', 'LAMARAO', 'M', 'BA', 'NE', 0),
(2919157, 'Lapão', 'LAPAO', 'M', 'BA', 'NE', 0),
(2919207, 'Lauro de Freitas', 'LAURO DE FREITAS', 'M', 'BA', 'NE', 0),
(2919306, 'Lençóis', 'LENCOIS', 'M', 'BA', 'NE', 0),
(2919405, 'Licínio de Almeida', 'LICINIO DE ALMEIDA', 'M', 'BA', 'NE', 0),
(2919450, 'Livramento de Nossa Senhora', 'LIVRAMENTO DE NOSSA SENHORA', 'M', 'BA', 'NE', 0),
(2919553, 'Luís Eduardo Magalhães', 'LUIS EDUARDO MAGALHAES', 'M', 'BA', 'NE', 0),
(2919603, 'Macajuba', 'MACAJUBA', 'M', 'BA', 'NE', 0),
(2919702, 'Macarani', 'MACARANI', 'M', 'BA', 'NE', 0),
(2919801, 'Macaúbas', 'MACAUBAS', 'M', 'BA', 'NE', 0),
(2919900, 'Macururé', 'MACURURE', 'M', 'BA', 'NE', 0),
(2919926, 'Madre de Deus', 'MADRE DE DEUS', 'M', 'BA', 'NE', 0),
(2919959, 'Maetinga', 'MAETINGA', 'M', 'BA', 'NE', 0),
(2920007, 'Maiquinique', 'MAIQUINIQUE', 'M', 'BA', 'NE', 0),
(2920106, 'Mairi', 'MAIRI', 'M', 'BA', 'NE', 0),
(2920205, 'Malhada', 'MALHADA', 'M', 'BA', 'NE', 0),
(2920304, 'Malhada de Pedras', 'MALHADA DE PEDRAS', 'M', 'BA', 'NE', 0),
(2920403, 'Manoel Vitorino', 'MANOEL VITORINO', 'M', 'BA', 'NE', 0),
(2920452, 'Mansidão', 'MANSIDAO', 'M', 'BA', 'NE', 0),
(2920502, 'Maracas', 'MARACAS', 'M', 'BA', 'NE', 0),
(2920601, 'Maragogipe', 'MARAGOGIPE', 'M', 'BA', 'NE', 0),
(2920700, 'Maraú', 'MARAU', 'M', 'BA', 'NE', 0),
(2920809, 'Marcionílio Souza', 'MARCIONILIO SOUZA', 'M', 'BA', 'NE', 0),
(2920908, 'Mascote', 'MASCOTE', 'M', 'BA', 'NE', 0),
(2921005, 'Mata de São João', 'MATA DE SAO JOAO', 'M', 'BA', 'NE', 0),
(2921054, 'Matina', 'MATINA', 'M', 'BA', 'NE', 0),
(2921104, 'Medeiros Neto', 'MEDEIROS NETO', 'M', 'BA', 'NE', 0),
(2921203, 'Miguel Calmon', 'MIGUEL CALMON', 'M', 'BA', 'NE', 0),
(2921302, 'Milagres', 'MILAGRES', 'M', 'BA', 'NE', 0),
(2921401, 'Mirangaba', 'MIRANGABA', 'M', 'BA', 'NE', 0),
(2921450, 'Mirante', 'MIRANTE', 'M', 'BA', 'NE', 0),
(2921500, 'Monte Santo', 'MONTE SANTO', 'M', 'BA', 'NE', 0),
(2921609, 'Morpará', 'MORPARA', 'M', 'BA', 'NE', 0),
(2921708, 'Morro do Chapéu', 'MORRO DO CHAPEU', 'M', 'BA', 'NE', 0),
(2921807, 'Mortugaba', 'MORTUGABA', 'M', 'BA', 'NE', 0),
(2921906, 'Mucugê', 'MUCUGE', 'M', 'BA', 'NE', 0),
(2922003, 'Mucuri', 'MUCURI', 'M', 'BA', 'NE', 0),
(2922052, 'Mulungu do Morro', 'MULUNGU DO MORRO', 'M', 'BA', 'NE', 0),
(2922102, 'Mundo Novo', 'MUNDO NOVO', 'M', 'BA', 'NE', 0),
(2922201, 'Muniz Ferreira', 'MUNIZ FERREIRA', 'M', 'BA', 'NE', 0),
(2922250, 'Muquem de São Francisco', 'MUQUEM DE SAO FRANCISCO', 'M', 'BA', 'NE', 0),
(2922300, 'Muritiba', 'MURITIBA', 'M', 'BA', 'NE', 0),
(2922409, 'Mutuípe', 'MUTUIPE', 'M', 'BA', 'NE', 0),
(2922508, 'Nazaré', 'NAZARE', 'M', 'BA', 'NE', 0),
(2922607, 'Nilo Peçanha', 'NILO PECANHA', 'M', 'BA', 'NE', 0),
(2922656, 'Nordestina', 'NORDESTINA', 'M', 'BA', 'NE', 0),
(2922706, 'Nova Canaã', 'NOVA CANAA', 'M', 'BA', 'NE', 0),
(2922730, 'Nova Fátima', 'NOVA FATIMA', 'M', 'BA', 'NE', 0),
(2922755, 'Nova Ibiá', 'NOVA IBIA', 'M', 'BA', 'NE', 0),
(2922805, 'Nova Itarana', 'NOVA ITARANA', 'M', 'BA', 'NE', 0),
(2922854, 'Nova Redenção', 'NOVA REDENCAO', 'M', 'BA', 'NE', 0),
(2922904, 'Nova Soure', 'NOVA SOURE', 'M', 'BA', 'NE', 0),
(2923001, 'Nova Viçosa', 'NOVA VICOSA', 'M', 'BA', 'NE', 0),
(2923035, 'Novo Horizonte', 'NOVO HORIZONTE', 'M', 'BA', 'NE', 0),
(2923050, 'Novo Triunfo', 'NOVO TRIUNFO', 'M', 'BA', 'NE', 0),
(2923100, 'Olindina', 'OLINDINA', 'M', 'BA', 'NE', 0),
(2923209, 'Oliveira dos Brejinhos', 'OLIVEIRA DOS BREJINHOS', 'M', 'BA', 'NE', 0),
(2923308, 'Ouriçangas', 'OURICANGAS', 'M', 'BA', 'NE', 0),
(2923357, 'Ourolândia', 'OUROLANDIA', 'M', 'BA', 'NE', 0),
(2923407, 'Palmas de Monte Alto', 'PALMAS DE MONTE ALTO', 'M', 'BA', 'NE', 0),
(2923506, 'Palmeiras', 'PALMEIRAS', 'M', 'BA', 'NE', 0),
(2923605, 'Paramirim', 'PARAMIRIM', 'M', 'BA', 'NE', 0),
(2923704, 'Paratinga', 'PARATINGA', 'M', 'BA', 'NE', 0),
(2923803, 'Paripiranga', 'PARIPIRANGA', 'M', 'BA', 'NE', 0),
(2923902, 'Pau Brasil', 'PAU BRASIL', 'M', 'BA', 'NE', 0),
(2924009, 'Paulo Afonso', 'PAULO AFONSO', 'M', 'BA', 'NE', 0),
(2924058, 'Pé de Serra', 'PE DE SERRA', 'M', 'BA', 'NE', 0),
(2924108, 'Pedrão', 'PEDRAO', 'M', 'BA', 'NE', 0),
(2924207, 'Pedro Alexandre', 'PEDRO ALEXANDRE', 'M', 'BA', 'NE', 0),
(2924306, 'Piatã', 'PIATA', 'M', 'BA', 'NE', 0),
(2924405, 'Pilão Arcado', 'PILAO ARCADO', 'M', 'BA', 'NE', 0),
(2924504, 'Pindaí', 'PINDAI', 'M', 'BA', 'NE', 0),
(2924603, 'Pindobacu', 'PINDOBACU', 'M', 'BA', 'NE', 0),
(2924652, 'Pintadas', 'PINTADAS', 'M', 'BA', 'NE', 0),
(2924678, 'Piraí do Norte', 'PIRAI DO NORTE', 'M', 'BA', 'NE', 0),
(2924702, 'Piripá', 'PIRIPA', 'M', 'BA', 'NE', 0),
(2924801, 'Piritiba', 'PIRITIBA', 'M', 'BA', 'NE', 0),
(2924900, 'Planaltino', 'PLANALTINO', 'M', 'BA', 'NE', 0),
(2925006, 'Planalto', 'PLANALTO', 'M', 'BA', 'NE', 0),
(2925105, 'Poções', 'POCOES', 'M', 'BA', 'NE', 0),
(2925204, 'Pojuca', 'POJUCA', 'M', 'BA', 'NE', 0),
(2925253, 'Ponto Novo', 'PONTO NOVO', 'M', 'BA', 'NE', 0),
(2925303, 'Porto Seguro', 'PORTO SEGURO', 'M', 'BA', 'NE', 0),
(2925402, 'Potiraguá', 'POTIRAGUA', 'M', 'BA', 'NE', 0),
(2925501, 'Prado', 'PRADO', 'M', 'BA', 'NE', 0),
(2925600, 'Presidente Dutra', 'PRESIDENTE DUTRA', 'M', 'BA', 'NE', 0),
(2925709, 'Presidente Jânio Quadros', 'PRESIDENTE JANIO QUADROS', 'M', 'BA', 'NE', 0),
(2925758, 'Presidente Tancredo Neves', 'PRESIDENTE TANCREDO NEVES', 'M', 'BA', 'NE', 0),
(2925808, 'Queimadas', 'QUEIMADAS', 'M', 'BA', 'NE', 0),
(2925907, 'Quijingue', 'QUIJINGUE', 'M', 'BA', 'NE', 0),
(2925931, 'Quixabeira', 'QUIXABEIRA', 'M', 'BA', 'NE', 0),
(2925956, 'Rafael Jambeiro', 'RAFAEL JAMBEIRO', 'M', 'BA', 'NE', 0),
(2926004, 'Remanso', 'REMANSO', 'M', 'BA', 'NE', 0),
(2926103, 'Retirolândia', 'RETIROLANDIA', 'M', 'BA', 'NE', 0),
(2926202, 'Riachão das Neves', 'RIACHAO DAS NEVES', 'M', 'BA', 'NE', 0),
(2926301, 'Riachão do Jacuípe', 'RIACHAO DO JACUIPE', 'M', 'BA', 'NE', 0),
(2926400, 'Riacho de Santana', 'RIACHO DE SANTANA', 'M', 'BA', 'NE', 0),
(2926509, 'Ribeira do Amparo', 'RIBEIRA DO AMPARO', 'M', 'BA', 'NE', 0),
(2926608, 'Ribeira do Pombal', 'RIBEIRA DO POMBAL', 'M', 'BA', 'NE', 0),
(2926657, 'Ribeirão do Largo', 'RIBEIRAO DO LARGO', 'M', 'BA', 'NE', 0),
(2926707, 'Rio de Contas', 'RIO DE CONTAS', 'M', 'BA', 'NE', 0),
(2926806, 'Rio do Antonio', 'RIO DO ANTONIO', 'M', 'BA', 'NE', 0),
(2926905, 'Rio do Pires', 'RIO DO PIRES', 'M', 'BA', 'NE', 0),
(2927002, 'Rio Real', 'RIO REAL', 'M', 'BA', 'NE', 0),
(2927101, 'Rodelas', 'RODELAS', 'M', 'BA', 'NE', 0),
(2927200, 'Ruy Barbosa', 'RUY BARBOSA', 'M', 'BA', 'NE', 0),
(2927309, 'Salinas da Margarida', 'SALINAS DA MARGARIDA', 'M', 'BA', 'NE', 0),
(2927408, 'Salvador', 'SALVADOR', 'M', 'BA', 'NE', 0),
(2927507, 'Santa Barbara', 'SANTA BARBARA', 'M', 'BA', 'NE', 0),
(2927606, 'Santa Brígida', 'SANTA BRIGIDA', 'M', 'BA', 'NE', 0),
(2927705, 'Santa Cruz Cabrália', 'SANTA CRUZ CABRALIA', 'M', 'BA', 'NE', 0),
(2927804, 'Santa Cruz da Vitoria', 'SANTA CRUZ DA VITORIA', 'M', 'BA', 'NE', 0),
(2927903, 'Santa Inês', 'SANTA INES', 'M', 'BA', 'NE', 0),
(2928000, 'Santaluz', 'SANTALUZ', 'M', 'BA', 'NE', 0),
(2928059, 'Santa Luzia', 'SANTA LUZIA', 'M', 'BA', 'NE', 0),
(2928109, 'Santa Maria da Vitória', 'SANTA MARIA DA VITORIA', 'M', 'BA', 'NE', 0),
(2928208, 'Santana', 'SANTANA', 'M', 'BA', 'NE', 0),
(2928307, 'Santanópolis', 'SANTANOPOLIS', 'M', 'BA', 'NE', 0),
(2928406, 'Santa Rita de Cássia', 'SANTA RITA DE CASSIA', 'M', 'BA', 'NE', 0),
(2928505, 'Santa Teresinha', 'SANTA TERESINHA', 'M', 'BA', 'NE', 0),
(2928604, 'Santo Amaro', 'SANTO AMARO', 'M', 'BA', 'NE', 0),
(2928703, 'Santo Antônio de Jesus', 'SANTO ANTONIO DE JESUS', 'M', 'BA', 'NE', 0),
(2928802, 'Santo Estevão', 'SANTO ESTEVAO', 'M', 'BA', 'NE', 0),
(2928901, 'São Desidério', 'SAO DESIDERIO', 'M', 'BA', 'NE', 0),
(2928950, 'São Domingos', 'SAO DOMINGOS', 'M', 'BA', 'NE', 0),
(2929008, 'São Félix', 'SAO FELIX', 'M', 'BA', 'NE', 0),
(2929057, 'São Félix do Coribe', 'SAO FELIX DO CORIBE', 'M', 'BA', 'NE', 0),
(2929107, 'São Felipe', 'SAO FELIPE', 'M', 'BA', 'NE', 0),
(2929206, 'São Francisco do Conde', 'SAO FRANCISCO DO CONDE', 'M', 'BA', 'NE', 0),
(2929255, 'São Gabriel', 'SAO GABRIEL', 'M', 'BA', 'NE', 0),
(2929305, 'São Gonçalo dos Campos', 'SAO GONCALO DOS CAMPOS', 'M', 'BA', 'NE', 0),
(2929354, 'São Jose da Vitoria', 'SAO JOSE DA VITORIA', 'M', 'BA', 'NE', 0),
(2929370, 'São Jose do Jacuipe', 'SAO JOSE DO JACUIPE', 'M', 'BA', 'NE', 0),
(2929404, 'São Miguel das Matas', 'SAO MIGUEL DAS MATAS', 'M', 'BA', 'NE', 0),
(2929503, 'São Sebastião do Passe', 'SAO SEBASTIAO DO PASSE', 'M', 'BA', 'NE', 0),
(2929602, 'Sapeacu', 'SAPEACU', 'M', 'BA', 'NE', 0),
(2929701, 'Sátiro Dias', 'SATIRO DIAS', 'M', 'BA', 'NE', 0),
(2929750, 'Saubara', 'SAUBARA', 'M', 'BA', 'NE', 0),
(2929800, 'Saúde', 'SAUDE', 'M', 'BA', 'NE', 0),
(2929909, 'Seabra', 'SEABRA', 'M', 'BA', 'NE', 0),
(2930006, 'Sebastião Laranjeiras', 'SEBASTIAO LARANJEIRAS', 'M', 'BA', 'NE', 0),
(2930105, 'Senhor do Bonfim', 'SENHOR DO BONFIM', 'M', 'BA', 'NE', 0),
(2930154, 'Serra do Ramalho', 'SERRA DO RAMALHO', 'M', 'BA', 'NE', 0),
(2930204, 'Sento Sé', 'SENTO SE', 'M', 'BA', 'NE', 0),
(2930303, 'Serra Dourada', 'SERRA DOURADA', 'M', 'BA', 'NE', 0),
(2930402, 'Serra Preta', 'SERRA PRETA', 'M', 'BA', 'NE', 0),
(2930501, 'Serrinha', 'SERRINHA', 'M', 'BA', 'NE', 0),
(2930600, 'Serrolândia', 'SERROLANDIA', 'M', 'BA', 'NE', 0),
(2930709, 'Simões Filho', 'SIMOES FILHO', 'M', 'BA', 'NE', 0),
(2930758, 'Sítio do Mato', 'SITIO DO MATO', 'M', 'BA', 'NE', 0),
(2930766, 'Sítio do Quinto', 'SITIO DO QUINTO', 'M', 'BA', 'NE', 0),
(2930774, 'Sobradinho', 'SOBRADINHO', 'M', 'BA', 'NE', 0),
(2930808, 'Souto Soares', 'SOUTO SOARES', 'M', 'BA', 'NE', 0),
(2930907, 'Tabocas do Brejo Velho', 'TABOCAS DO BREJO VELHO', 'M', 'BA', 'NE', 0),
(2931004, 'Tanhacu', 'TANHACU', 'M', 'BA', 'NE', 0),
(2931053, 'Tanque Novo', 'TANQUE NOVO', 'M', 'BA', 'NE', 0),
(2931103, 'Tanquinho', 'TANQUINHO', 'M', 'BA', 'NE', 0),
(2931202, 'Taperoá', 'TAPEROA', 'M', 'BA', 'NE', 0),
(2931301, 'Tapiramuta', 'TAPIRAMUTA', 'M', 'BA', 'NE', 0),
(2931350, 'Teixeira de Freitas', 'TEIXEIRA DE FREITAS', 'M', 'BA', 'NE', 0),
(2931400, 'Teodoro Sampaio', 'TEODORO SAMPAIO', 'M', 'BA', 'NE', 0),
(2931509, 'Teofilândia', 'TEOFILANDIA', 'M', 'BA', 'NE', 0),
(2931608, 'Teolândia', 'TEOLANDIA', 'M', 'BA', 'NE', 0),
(2931707, 'Terra Nova', 'TERRA NOVA', 'M', 'BA', 'NE', 0),
(2931806, 'Tremedal', 'TREMEDAL', 'M', 'BA', 'NE', 0),
(2931905, 'Tucano', 'TUCANO', 'M', 'BA', 'NE', 0),
(2932002, 'Uauá', 'UAUA', 'M', 'BA', 'NE', 0),
(2932101, 'Ubaíra', 'UBAIRA', 'M', 'BA', 'NE', 0),
(2932200, 'Ubaitaba', 'UBAITABA', 'M', 'BA', 'NE', 0),
(2932309, 'Ubatã', 'UBATA', 'M', 'BA', 'NE', 0),
(2932408, 'Uibaí', 'UIBAI', 'M', 'BA', 'NE', 0),
(2932457, 'Umburanas', 'UMBURANAS', 'M', 'BA', 'NE', 0),
(2932507, 'Una', 'UNA', 'M', 'BA', 'NE', 0),
(2932606, 'Urandi', 'URANDI', 'M', 'BA', 'NE', 0),
(2932705, 'Uruçuca', 'URUCUCA', 'M', 'BA', 'NE', 0),
(2932804, 'Utinga', 'UTINGA', 'M', 'BA', 'NE', 0),
(2932903, 'Valença', 'VALENCA', 'M', 'BA', 'NE', 0),
(2933000, 'Valente', 'VALENTE', 'M', 'BA', 'NE', 0),
(2933059, 'Várzea da Roca', 'VARZEA DA ROCA', 'M', 'BA', 'NE', 0),
(2933109, 'Várzea do Poço', 'VARZEA DO POCO', 'M', 'BA', 'NE', 0),
(2933158, 'Várzea Nova', 'VARZEA NOVA', 'M', 'BA', 'NE', 0),
(2933174, 'Varzedo', 'VARZEDO', 'M', 'BA', 'NE', 0),
(2933208, 'Vera Cruz', 'VERA CRUZ', 'M', 'BA', 'NE', 0),
(2933257, 'Vereda', 'VEREDA', 'M', 'BA', 'NE', 0),
(2933307, 'Vitória da Conquista', 'VITORIA DA CONQUISTA', 'M', 'BA', 'NE', 0),
(2933406, 'Wagner', 'WAGNER', 'M', 'BA', 'NE', 0),
(2933455, 'Wanderley', 'WANDERLEY', 'M', 'BA', 'NE', 0),
(2933505, 'Wenceslau Guimarães', 'WENCESLAU GUIMARAES', 'M', 'BA', 'NE', 0),
(2933604, 'Xique-Xique', 'XIQUE-XIQUE', 'M', 'BA', 'NE', 0),
(3100000, 'Minas Gerais', 'MINAS GERAIS', 'U', 'MG', 'SD', 0),
(3100104, 'Abadia dos Dourados', 'ABADIA DOS DOURADOS', 'M', 'MG', 'SD', 0),
(3100203, 'Abaeté', 'ABAETE', 'M', 'MG', 'SD', 0),
(3100302, 'Abre Campo', 'ABRE CAMPO', 'M', 'MG', 'SD', 0),
(3100401, 'Acaiaca', 'ACAIACA', 'M', 'MG', 'SD', 0),
(3100500, 'Açucena', 'ACUCENA', 'M', 'MG', 'SD', 0),
(3100609, 'Agua Boa', 'AGUA BOA', 'M', 'MG', 'SD', 0),
(3100708, 'Água Comprida', 'AGUA COMPRIDA', 'M', 'MG', 'SD', 0),
(3100807, 'Aguanil', 'AGUANIL', 'M', 'MG', 'SD', 0),
(3100906, 'Águas Formosas', 'AGUAS FORMOSAS', 'M', 'MG', 'SD', 0),
(3101003, 'Águas Vermelhas', 'AGUAS VERMELHAS', 'M', 'MG', 'SD', 0),
(3101102, 'Aimorés', 'AIMORES', 'M', 'MG', 'SD', 0),
(3101201, 'Aiuruoca', 'AIURUOCA', 'M', 'MG', 'SD', 0),
(3101300, 'Alagoa', 'ALAGOA', 'M', 'MG', 'SD', 0),
(3101409, 'Albertina', 'ALBERTINA', 'M', 'MG', 'SD', 0),
(3101508, 'Além Paraíba', 'ALEM PARAIBA', 'M', 'MG', 'SD', 0),
(3101607, 'Alfenas', 'ALFENAS', 'M', 'MG', 'SD', 0),
(3101631, 'Alfredo Vasconcelos', 'ALFREDO VASCONCELOS', 'M', 'MG', 'SD', 0),
(3101706, 'Almenara', 'ALMENARA', 'M', 'MG', 'SD', 0),
(3101805, 'Alpercata', 'ALPERCATA', 'M', 'MG', 'SD', 0),
(3101904, 'Alpinópolis', 'ALPINOPOLIS', 'M', 'MG', 'SD', 0),
(3102001, 'Alterosa', 'ALTEROSA', 'M', 'MG', 'SD', 0),
(3102050, 'Alto Caparaó', 'ALTO CAPARAO', 'M', 'MG', 'SD', 0),
(3102100, 'Alto Rio Doce', 'ALTO RIO DOCE', 'M', 'MG', 'SD', 0),
(3102209, 'Alvarenga', 'ALVARENGA', 'M', 'MG', 'SD', 0),
(3102308, 'Alvinópolis', 'ALVINOPOLIS', 'M', 'MG', 'SD', 0),
(3102407, 'Alvorada de Minas', 'ALVORADA DE MINAS', 'M', 'MG', 'SD', 0),
(3102506, 'Amparo do Serra', 'AMPARO DO SERRA', 'M', 'MG', 'SD', 0),
(3102605, 'Andradas', 'ANDRADAS', 'M', 'MG', 'SD', 0),
(3102704, 'Cachoeira de Pajeú', 'CACHOEIRA DE PAJEU', 'M', 'MG', 'SD', 0),
(3102803, 'Andrelandia', 'ANDRELANDIA', 'M', 'MG', 'SD', 0),
(3102852, 'Angelandia', 'ANGELANDIA', 'M', 'MG', 'SD', 0),
(3102902, 'Antônio Carlos', 'ANTONIO CARLOS', 'M', 'MG', 'SD', 0),
(3103009, 'Antônio Dias', 'ANTONIO DIAS', 'M', 'MG', 'SD', 0),
(3103108, 'Antônio Prado de Minas', 'ANTONIO PRADO DE MINAS', 'M', 'MG', 'SD', 0),
(3103207, 'Araçaí', 'ARACAI', 'M', 'MG', 'SD', 0),
(3103306, 'Aracitaba', 'ARACITABA', 'M', 'MG', 'SD', 0),
(3103405, 'Araçuaí', 'ARACUAI', 'M', 'MG', 'SD', 0),
(3103504, 'Araguari', 'ARAGUARI', 'M', 'MG', 'SD', 0),
(3103603, 'Arantina', 'ARANTINA', 'M', 'MG', 'SD', 0),
(3103702, 'Araponga', 'ARAPONGA', 'M', 'MG', 'SD', 0),
(3103751, 'Arapora', 'ARAPORA', 'M', 'MG', 'SD', 0),
(3103801, 'Arapuá', 'ARAPUA', 'M', 'MG', 'SD', 0),
(3103900, 'Araújos', 'ARAUJOS', 'M', 'MG', 'SD', 0),
(3104007, 'Araxá', 'ARAXA', 'M', 'MG', 'SD', 0),
(3104106, 'Arceburgo', 'ARCEBURGO', 'M', 'MG', 'SD', 0),
(3104205, 'Arcos', 'ARCOS', 'M', 'MG', 'SD', 0),
(3104304, 'Areado', 'AREADO', 'M', 'MG', 'SD', 0),
(3104403, 'Argirita', 'ARGIRITA', 'M', 'MG', 'SD', 0),
(3104452, 'Aricanduva', 'ARICANDUVA', 'M', 'MG', 'SD', 0),
(3104502, 'Arinos', 'ARINOS', 'M', 'MG', 'SD', 0),
(3104601, 'Astolfo Dutra', 'ASTOLFO DUTRA', 'M', 'MG', 'SD', 0),
(3104700, 'Ataléia', 'ATALEIA', 'M', 'MG', 'SD', 0),
(3104809, 'Augusto de Lima', 'AUGUSTO DE LIMA', 'M', 'MG', 'SD', 0),
(3104908, 'Baependi', 'BAEPENDI', 'M', 'MG', 'SD', 0),
(3105004, 'Baldim', 'BALDIM', 'M', 'MG', 'SD', 0),
(3105103, 'Bambuí', 'BAMBUI', 'M', 'MG', 'SD', 0),
(3105202, 'Bandeira', 'BANDEIRA', 'M', 'MG', 'SD', 0),
(3105301, 'Bandeira do Sul', 'BANDEIRA DO SUL', 'M', 'MG', 'SD', 0),
(3105400, 'Barão de Cocais', 'BARAO DE COCAIS', 'M', 'MG', 'SD', 0),
(3105509, 'Barão de Monte Alto', 'BARAO DE MONTE ALTO', 'M', 'MG', 'SD', 0),
(3105608, 'Barbacena', 'BARBACENA', 'M', 'MG', 'SD', 0),
(3105707, 'Barra Longa', 'BARRA LONGA', 'M', 'MG', 'SD', 0),
(3105905, 'Barroso', 'BARROSO', 'M', 'MG', 'SD', 0),
(3106002, 'Bela Vista de Minas', 'BELA VISTA DE MINAS', 'M', 'MG', 'SD', 0),
(3106101, 'Belmiro Braga', 'BELMIRO BRAGA', 'M', 'MG', 'SD', 0),
(3106200, 'Belo Horizonte', 'BELO HORIZONTE', 'M', 'MG', 'SD', 0),
(3106309, 'Belo Oriente', 'BELO ORIENTE', 'M', 'MG', 'SD', 0),
(3106408, 'Belo Vale', 'BELO VALE', 'M', 'MG', 'SD', 0),
(3106507, 'Berilo', 'BERILO', 'M', 'MG', 'SD', 0),
(3106606, 'Bertópolis', 'BERTOPOLIS', 'M', 'MG', 'SD', 0),
(3106655, 'Berizal', 'BERIZAL', 'M', 'MG', 'SD', 0),
(3106705, 'Betim', 'BETIM', 'M', 'MG', 'SD', 0),
(3106804, 'Bias Fortes', 'BIAS FORTES', 'M', 'MG', 'SD', 0),
(3106903, 'Bicas', 'BICAS', 'M', 'MG', 'SD', 0),
(3107000, 'Biquinhas', 'BIQUINHAS', 'M', 'MG', 'SD', 0),
(3107109, 'Boa Esperanca', 'BOA ESPERANCA', 'M', 'MG', 'SD', 0),
(3107208, 'Bocaina de Minas', 'BOCAINA DE MINAS', 'M', 'MG', 'SD', 0),
(3107307, 'Bocaiúva', 'BOCAIUVA', 'M', 'MG', 'SD', 0),
(3107406, 'Bom Despacho', 'BOM DESPACHO', 'M', 'MG', 'SD', 0),
(3107505, 'Bom Jardim de Minas', 'BOM JARDIM DE MINAS', 'M', 'MG', 'SD', 0),
(3107604, 'Bom Jesus da Penha', 'BOM JESUS DA PENHA', 'M', 'MG', 'SD', 0),
(3107703, 'Bom Jesus do Amparo', 'BOM JESUS DO AMPARO', 'M', 'MG', 'SD', 0),
(3107802, 'Bom Jesus do Galho', 'BOM JESUS DO GALHO', 'M', 'MG', 'SD', 0),
(3107901, 'Bom Repouso', 'BOM REPOUSO', 'M', 'MG', 'SD', 0),
(3108008, 'Bom Sucesso', 'BOM SUCESSO', 'M', 'MG', 'SD', 0),
(3108107, 'Bonfim', 'BONFIM', 'M', 'MG', 'SD', 0),
(3108206, 'Bonfinópolis de Minas', 'BONFINOPOLIS DE MINAS', 'M', 'MG', 'SD', 0),
(3108255, 'Bonito de Minas', 'BONITO DE MINAS', 'M', 'MG', 'SD', 0),
(3108305, 'Borda da Mata', 'BORDA DA MATA', 'M', 'MG', 'SD', 0),
(3108404, 'Botelhos', 'BOTELHOS', 'M', 'MG', 'SD', 0),
(3108503, 'Botumirim', 'BOTUMIRIM', 'M', 'MG', 'SD', 0),
(3108552, 'Brasilândia de Minas', 'BRASILANDIA DE MINAS', 'M', 'MG', 'SD', 0),
(3108602, 'Brasília de Minas', 'BRASILIA DE MINAS', 'M', 'MG', 'SD', 0),
(3108701, 'Brás Pires', 'BRAS PIRES', 'M', 'MG', 'SD', 0),
(3108800, 'Braúnas', 'BRAUNAS', 'M', 'MG', 'SD', 0),
(3108909, 'Brasópolis', 'BRASOPOLIS', 'M', 'MG', 'SD', 0),
(3109006, 'Brumadinho', 'BRUMADINHO', 'M', 'MG', 'SD', 0),
(3109105, 'Bueno Brandão', 'BUENO BRANDAO', 'M', 'MG', 'SD', 0),
(3109204, 'Buenópolis', 'BUENOPOLIS', 'M', 'MG', 'SD', 0),
(3109253, 'Bugre', 'BUGRE', 'M', 'MG', 'SD', 0),
(3109303, 'Buritis', 'BURITIS', 'M', 'MG', 'SD', 0),
(3109402, 'Buritizeiro', 'BURITIZEIRO', 'M', 'MG', 'SD', 0),
(3109451, 'Cabeceira Grande', 'CABECEIRA GRANDE', 'M', 'MG', 'SD', 0),
(3109501, 'Cabo Verde', 'CABO VERDE', 'M', 'MG', 'SD', 0),
(3109600, 'Cachoeira da Prata', 'CACHOEIRA DA PRATA', 'M', 'MG', 'SD', 0),
(3109709, 'Cachoeira de Minas', 'CACHOEIRA DE MINAS', 'M', 'MG', 'SD', 0),
(3109808, 'Cachoeira Dourada', 'CACHOEIRA DOURADA', 'M', 'MG', 'SD', 0),
(3109907, 'Caetanópolis', 'CAETANOPOLIS', 'M', 'MG', 'SD', 0),
(3110004, 'Caeté', 'CAETE', 'M', 'MG', 'SD', 0),
(3110103, 'Caiana', 'CAIANA', 'M', 'MG', 'SD', 0),
(3110202, 'Cajuri', 'CAJURI', 'M', 'MG', 'SD', 0),
(3110301, 'Caldas', 'CALDAS', 'M', 'MG', 'SD', 0),
(3110400, 'Camacho', 'CAMACHO', 'M', 'MG', 'SD', 0),
(3110509, 'Camanducaia', 'CAMANDUCAIA', 'M', 'MG', 'SD', 0),
(3110608, 'Cambuí', 'CAMBUI', 'M', 'MG', 'SD', 0),
(3110707, 'Cambuquira', 'CAMBUQUIRA', 'M', 'MG', 'SD', 0),
(3110806, 'Campanário', 'CAMPANARIO', 'M', 'MG', 'SD', 0),
(3110905, 'Campanha', 'CAMPANHA', 'M', 'MG', 'SD', 0),
(3111002, 'Campestre', 'CAMPESTRE', 'M', 'MG', 'SD', 0),
(3111101, 'Campina Verde', 'CAMPINA VERDE', 'M', 'MG', 'SD', 0),
(3111150, 'Campo Azul', 'CAMPO AZUL', 'M', 'MG', 'SD', 0),
(3111200, 'Campo Belo', 'CAMPO BELO', 'M', 'MG', 'SD', 0),
(3111309, 'Campo do Meio', 'CAMPO DO MEIO', 'M', 'MG', 'SD', 0),
(3111408, 'Campo Florido', 'CAMPO FLORIDO', 'M', 'MG', 'SD', 0),
(3111507, 'Campos Altos', 'CAMPOS ALTOS', 'M', 'MG', 'SD', 0),
(3111606, 'Campos Gerais', 'CAMPOS GERAIS', 'M', 'MG', 'SD', 0),
(3111705, 'Canaã', 'CANAA', 'M', 'MG', 'SD', 0),
(3111804, 'Canápolis', 'CANAPOLIS', 'M', 'MG', 'SD', 0),
(3111903, 'Cana Verde', 'CANA VERDE', 'M', 'MG', 'SD', 0),
(3112000, 'Candeias', 'CANDEIAS', 'M', 'MG', 'SD', 0),
(3112059, 'Cantagalo', 'CANTAGALO', 'M', 'MG', 'SD', 0),
(3112109, 'Caparaó', 'CAPARAO', 'M', 'MG', 'SD', 0),
(3112208, 'Capela Nova', 'CAPELA NOVA', 'M', 'MG', 'SD', 0),
(3112307, 'Capelinha', 'CAPELINHA', 'M', 'MG', 'SD', 0),
(3112406, 'Capetinga', 'CAPETINGA', 'M', 'MG', 'SD', 0),
(3112505, 'Capim Branco', 'CAPIM BRANCO', 'M', 'MG', 'SD', 0),
(3112604, 'Capinópolis', 'CAPINOPOLIS', 'M', 'MG', 'SD', 0),
(3112653, 'Capitão Andrade', 'CAPITAO ANDRADE', 'M', 'MG', 'SD', 0),
(3112703, 'Capitão Eneas', 'CAPITAO ENEAS', 'M', 'MG', 'SD', 0),
(3112802, 'Capitólio', 'CAPITOLIO', 'M', 'MG', 'SD', 0),
(3112901, 'Caputira', 'CAPUTIRA', 'M', 'MG', 'SD', 0),
(3113008, 'Caraí', 'CARAI', 'M', 'MG', 'SD', 0),
(3113107, 'Caranaíba', 'CARANAIBA', 'M', 'MG', 'SD', 0),
(3113206, 'Carandaí', 'CARANDAI', 'M', 'MG', 'SD', 0),
(3113305, 'Carangola', 'CARANGOLA', 'M', 'MG', 'SD', 0),
(3113404, 'Caratinga', 'CARATINGA', 'M', 'MG', 'SD', 0),
(3113503, 'Carbonita', 'CARBONITA', 'M', 'MG', 'SD', 0),
(3113602, 'Careaçu', 'CAREACU', 'M', 'MG', 'SD', 0),
(3113701, 'Carlos Chagas', 'CARLOS CHAGAS', 'M', 'MG', 'SD', 0),
(3113800, 'Carmésia', 'CARMESIA', 'M', 'MG', 'SD', 0),
(3113909, 'Carmo da Cachoeira', 'CARMO DA CACHOEIRA', 'M', 'MG', 'SD', 0),
(3114006, 'Carmo da Mata', 'CARMO DA MATA', 'M', 'MG', 'SD', 0),
(3114105, 'Carmo de Minas', 'CARMO DE MINAS', 'M', 'MG', 'SD', 0),
(3114204, 'Carmo do Cajuru', 'CARMO DO CAJURU', 'M', 'MG', 'SD', 0),
(3114303, 'Carmo do Paranaíba', 'CARMO DO PARANAIBA', 'M', 'MG', 'SD', 0),
(3114402, 'Carmo do Rio Claro', 'CARMO DO RIO CLARO', 'M', 'MG', 'SD', 0),
(3114501, 'Carmópolis de Minas', 'CARMOPOLIS DE MINAS', 'M', 'MG', 'SD', 0),
(3114550, 'Carneirinho', 'CARNEIRINHO', 'M', 'MG', 'SD', 0),
(3114600, 'Carrancas', 'CARRANCAS', 'M', 'MG', 'SD', 0),
(3114709, 'Carvalhópolis', 'CARVALHOPOLIS', 'M', 'MG', 'SD', 0),
(3114808, 'Carvalhos', 'CARVALHOS', 'M', 'MG', 'SD', 0),
(3114907, 'Casa Grande', 'CASA GRANDE', 'M', 'MG', 'SD', 0),
(3115003, 'Cascalho Rico', 'CASCALHO RICO', 'M', 'MG', 'SD', 0),
(3115102, 'Cássia', 'CASSIA', 'M', 'MG', 'SD', 0),
(3115201, 'Conceição da Barra de Minas', 'CONCEICAO DA BARRA DE MINAS', 'M', 'MG', 'SD', 0),
(3115300, 'Cataguases', 'CATAGUASES', 'M', 'MG', 'SD', 0),
(3115359, 'Catas Altas', 'CATAS ALTAS', 'M', 'MG', 'SD', 0),
(3115409, 'Catas Altas da Noruega', 'CATAS ALTAS DA NORUEGA', 'M', 'MG', 'SD', 0),
(3115458, 'Catuji', 'CATUJI', 'M', 'MG', 'SD', 0),
(3115474, 'Catuti', 'CATUTI', 'M', 'MG', 'SD', 0),
(3115508, 'Caxambu', 'CAXAMBU', 'M', 'MG', 'SD', 0),
(3115607, 'Cedro do Abaeté', 'CEDRO DO ABAETE', 'M', 'MG', 'SD', 0),
(3115706, 'Central de Minas', 'CENTRAL DE MINAS', 'M', 'MG', 'SD', 0),
(3115805, 'Centralina', 'CENTRALINA', 'M', 'MG', 'SD', 0),
(3115904, 'Chácara', 'CHACARA', 'M', 'MG', 'SD', 0),
(3116001, 'Chale', 'CHALE', 'M', 'MG', 'SD', 0),
(3116100, 'Chapada do Norte', 'CHAPADA DO NORTE', 'M', 'MG', 'SD', 0),
(3116159, 'Chapada Gaúcha', 'CHAPADA GAUCHA', 'M', 'MG', 'SD', 0),
(3116209, 'Chiador', 'CHIADOR', 'M', 'MG', 'SD', 0),
(3116308, 'Cipotânea', 'CIPOTANEA', 'M', 'MG', 'SD', 0),
(3116407, 'Claraval', 'CLARAVAL', 'M', 'MG', 'SD', 0),
(3116506, 'Claro dos Pocoes', 'CLARO DOS POCOES', 'M', 'MG', 'SD', 0),
(3116605, 'Cláudio', 'CLAUDIO', 'M', 'MG', 'SD', 0),
(3116704, 'Coimbra', 'COIMBRA', 'M', 'MG', 'SD', 0),
(3116803, 'Coluna', 'COLUNA', 'M', 'MG', 'SD', 0),
(3116902, 'Comendador Gomes', 'COMENDADOR GOMES', 'M', 'MG', 'SD', 0),
(3117009, 'Comercinho', 'COMERCINHO', 'M', 'MG', 'SD', 0),
(3117108, 'Conceição da Aparecida', 'CONCEICAO DA APARECIDA', 'M', 'MG', 'SD', 0),
(3117207, 'Conceição das Pedras', 'CONCEICAO DAS PEDRAS', 'M', 'MG', 'SD', 0),
(3117306, 'Conceição das Alagoas', 'CONCEICAO DAS ALAGOAS', 'M', 'MG', 'SD', 0),
(3117405, 'Conceição de Ipanema', 'CONCEICAO DE IPANEMA', 'M', 'MG', 'SD', 0),
(3117504, 'Conceição do Mato Dentro', 'CONCEICAO DO MATO DENTRO', 'M', 'MG', 'SD', 0),
(3117603, 'Conceição do Pará', 'CONCEICAO DO PARA', 'M', 'MG', 'SD', 0),
(3117702, 'Conceição do Rio Verde', 'CONCEICAO DO RIO VERDE', 'M', 'MG', 'SD', 0),
(3117801, 'Conceição dos Ouros', 'CONCEICAO DOS OUROS', 'M', 'MG', 'SD', 0),
(3117836, 'Cônego Marinho', 'CONEGO MARINHO', 'M', 'MG', 'SD', 0),
(3117876, 'Confins', 'CONFINS', 'M', 'MG', 'SD', 0),
(3117900, 'Congonhal', 'CONGONHAL', 'M', 'MG', 'SD', 0),
(3118007, 'Congonhas', 'CONGONHAS', 'M', 'MG', 'SD', 0),
(3118106, 'Congonhas do Norte', 'CONGONHAS DO NORTE', 'M', 'MG', 'SD', 0),
(3118205, 'Conquista', 'CONQUISTA', 'M', 'MG', 'SD', 0),
(3118304, 'Conselheiro Lafaiete', 'CONSELHEIRO LAFAIETE', 'M', 'MG', 'SD', 0),
(3118403, 'Conselheiro Pena', 'CONSELHEIRO PENA', 'M', 'MG', 'SD', 0),
(3118502, 'Consolação', 'CONSOLACAO', 'M', 'MG', 'SD', 0),
(3118601, 'Contagem', 'CONTAGEM', 'M', 'MG', 'SD', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(3118700, 'Coqueiral', 'COQUEIRAL', 'M', 'MG', 'SD', 0),
(3118809, 'Coração de Jesus', 'CORACAO DE JESUS', 'M', 'MG', 'SD', 0),
(3118908, 'Cordisburgo', 'CORDISBURGO', 'M', 'MG', 'SD', 0),
(3119005, 'Cordislândia', 'CORDISLANDIA', 'M', 'MG', 'SD', 0),
(3119104, 'Corinto', 'CORINTO', 'M', 'MG', 'SD', 0),
(3119203, 'Coroaci', 'COROACI', 'M', 'MG', 'SD', 0),
(3119302, 'Coromandel', 'COROMANDEL', 'M', 'MG', 'SD', 0),
(3119401, 'Coronel Fabriciano', 'CORONEL FABRICIANO', 'M', 'MG', 'SD', 0),
(3119500, 'Coronel Murta', 'CORONEL MURTA', 'M', 'MG', 'SD', 0),
(3119609, 'Coronel Pacheco', 'CORONEL PACHECO', 'M', 'MG', 'SD', 0),
(3119708, 'Coronel Xavier Chaves', 'CORONEL XAVIER CHAVES', 'M', 'MG', 'SD', 0),
(3119807, 'Corrego Danta', 'CORREGO DANTA', 'M', 'MG', 'SD', 0),
(3119906, 'Corrego do Bom Jesus', 'CORREGO DO BOM JESUS', 'M', 'MG', 'SD', 0),
(3119955, 'Corrego Fundo', 'CORREGO FUNDO', 'M', 'MG', 'SD', 0),
(3120003, 'Corrego Novo', 'CORREGO NOVO', 'M', 'MG', 'SD', 0),
(3120102, 'Couto de Magalhães de Minas', 'COUTO DE MAGALHAES DE MINAS', 'M', 'MG', 'SD', 0),
(3120151, 'Crisólita', 'CRISOLITA', 'M', 'MG', 'SD', 0),
(3120201, 'Cristais', 'CRISTAIS', 'M', 'MG', 'SD', 0),
(3120300, 'Cristália', 'CRISTALIA', 'M', 'MG', 'SD', 0),
(3120409, 'Cristiano Otoni', 'CRISTIANO OTONI', 'M', 'MG', 'SD', 0),
(3120508, 'Cristina', 'CRISTINA', 'M', 'MG', 'SD', 0),
(3120607, 'Crucilândia', 'CRUCILANDIA', 'M', 'MG', 'SD', 0),
(3120706, 'Cruzeiro da Fortaleza', 'CRUZEIRO DA FORTALEZA', 'M', 'MG', 'SD', 0),
(3120805, 'Cruzília', 'CRUZILIA', 'M', 'MG', 'SD', 0),
(3120839, 'Cuparaque', 'CUPARAQUE', 'M', 'MG', 'SD', 0),
(3120870, 'Curral de Dentro', 'CURRAL DE DENTRO', 'M', 'MG', 'SD', 0),
(3120904, 'Curvelo', 'CURVELO', 'M', 'MG', 'SD', 0),
(3121001, 'Datas', 'DATAS', 'M', 'MG', 'SD', 0),
(3121100, 'Delfim Moreira', 'DELFIM MOREIRA', 'M', 'MG', 'SD', 0),
(3121209, 'Delfinópolis', 'DELFINOPOLIS', 'M', 'MG', 'SD', 0),
(3121258, 'Delta', 'DELTA', 'M', 'MG', 'SD', 0),
(3121308, 'Descoberto', 'DESCOBERTO', 'M', 'MG', 'SD', 0),
(3121407, 'Desterro de Entre Rios', 'DESTERRO DE ENTRE RIOS', 'M', 'MG', 'SD', 0),
(3121506, 'Desterro do Melo', 'DESTERRO DO MELO', 'M', 'MG', 'SD', 0),
(3121605, 'Diamantina', 'DIAMANTINA', 'M', 'MG', 'SD', 0),
(3121704, 'Diogo de Vasconcelos', 'DIOGO DE VASCONCELOS', 'M', 'MG', 'SD', 0),
(3121803, 'Dionísio', 'DIONISIO', 'M', 'MG', 'SD', 0),
(3121902, 'Divinésia', 'DIVINESIA', 'M', 'MG', 'SD', 0),
(3122009, 'Divino', 'DIVINO', 'M', 'MG', 'SD', 0),
(3122108, 'Divino das Laranjeiras', 'DIVINO DAS LARANJEIRAS', 'M', 'MG', 'SD', 0),
(3122207, 'Divinolândia de Minas', 'DIVINOLANDIA DE MINAS', 'M', 'MG', 'SD', 0),
(3122306, 'Divinópolis', 'DIVINOPOLIS', 'M', 'MG', 'SD', 0),
(3122355, 'Divisa Alegre', 'DIVISA ALEGRE', 'M', 'MG', 'SD', 0),
(3122405, 'Divisa Nova', 'DIVISA NOVA', 'M', 'MG', 'SD', 0),
(3122454, 'Divisópolis', 'DIVISOPOLIS', 'M', 'MG', 'SD', 0),
(3122470, 'Dom Bosco', 'DOM BOSCO', 'M', 'MG', 'SD', 0),
(3122504, 'Dom Cavati', 'DOM CAVATI', 'M', 'MG', 'SD', 0),
(3122603, 'Dom Joaquim', 'DOM JOAQUIM', 'M', 'MG', 'SD', 0),
(3122702, 'Dom Silvério', 'DOM SILVERIO', 'M', 'MG', 'SD', 0),
(3122801, 'Dom Viçoso', 'DOM VICOSO', 'M', 'MG', 'SD', 0),
(3122900, 'Dona Euzébia', 'DONA EUZEBIA', 'M', 'MG', 'SD', 0),
(3123007, 'Dores de Campos', 'DORES DE CAMPOS', 'M', 'MG', 'SD', 0),
(3123106, 'Dores de Guanhaes', 'DORES DE GUANHAES', 'M', 'MG', 'SD', 0),
(3123205, 'Dores do Indaiá', 'DORES DO INDAIA', 'M', 'MG', 'SD', 0),
(3123304, 'Dores do Turvo', 'DORES DO TURVO', 'M', 'MG', 'SD', 0),
(3123403, 'Doresópolis', 'DORESOPOLIS', 'M', 'MG', 'SD', 0),
(3123502, 'Douradoquara', 'DOURADOQUARA', 'M', 'MG', 'SD', 0),
(3123528, 'Durandé', 'DURANDE', 'M', 'MG', 'SD', 0),
(3123601, 'Elói Mendes', 'ELOI MENDES', 'M', 'MG', 'SD', 0),
(3123700, 'Engenheiro Caldas', 'ENGENHEIRO CALDAS', 'M', 'MG', 'SD', 0),
(3123809, 'Engenheiro Navarro', 'ENGENHEIRO NAVARRO', 'M', 'MG', 'SD', 0),
(3123858, 'Entre Folhas', 'ENTRE FOLHAS', 'M', 'MG', 'SD', 0),
(3123908, 'Entre Rios de Minas', 'ENTRE RIOS DE MINAS', 'M', 'MG', 'SD', 0),
(3124005, 'Ervália', 'ERVALIA', 'M', 'MG', 'SD', 0),
(3124104, 'Esmeraldas', 'ESMERALDAS', 'M', 'MG', 'SD', 0),
(3124203, 'Espera Feliz', 'ESPERA FELIZ', 'M', 'MG', 'SD', 0),
(3124302, 'Espinosa', 'ESPINOSA', 'M', 'MG', 'SD', 0),
(3124401, 'Espírito Santo do Dourado', 'ESPIRITO SANTO DO DOURADO', 'M', 'MG', 'SD', 0),
(3124500, 'Estiva', 'ESTIVA', 'M', 'MG', 'SD', 0),
(3124609, 'Estrela Dalva', 'ESTRELA DALVA', 'M', 'MG', 'SD', 0),
(3124708, 'Estrela do Indaiá', 'ESTRELA DO INDAIA', 'M', 'MG', 'SD', 0),
(3124807, 'Estrela do Sul', 'ESTRELA DO SUL', 'M', 'MG', 'SD', 0),
(3124906, 'Eugenópolis', 'EUGENOPOLIS', 'M', 'MG', 'SD', 0),
(3125002, 'Ewbank da Camara', 'EWBANK DA CAMARA', 'M', 'MG', 'SD', 0),
(3125101, 'Extrema', 'EXTREMA', 'M', 'MG', 'SD', 0),
(3125200, 'Fama', 'FAMA', 'M', 'MG', 'SD', 0),
(3125309, 'Faria Lemos', 'FARIA LEMOS', 'M', 'MG', 'SD', 0),
(3125408, 'Felício dos Santos', 'FELICIO DOS SANTOS', 'M', 'MG', 'SD', 0),
(3125507, 'São Gonçalo do Rio Preto', 'SAO GONCALO DO RIO PRETO', 'M', 'MG', 'SD', 0),
(3125606, 'Felisburgo', 'FELISBURGO', 'M', 'MG', 'SD', 0),
(3125705, 'Felixlândia', 'FELIXLANDIA', 'M', 'MG', 'SD', 0),
(3125804, 'Fernandes Tourinho', 'FERNANDES TOURINHO', 'M', 'MG', 'SD', 0),
(3125903, 'Ferros', 'FERROS', 'M', 'MG', 'SD', 0),
(3125952, 'Fervedouro', 'FERVEDOURO', 'M', 'MG', 'SD', 0),
(3126000, 'Florestal', 'FLORESTAL', 'M', 'MG', 'SD', 0),
(3126109, 'Formiga', 'FORMIGA', 'M', 'MG', 'SD', 0),
(3126208, 'Formoso', 'FORMOSO', 'M', 'MG', 'SD', 0),
(3126307, 'Fortaleza de Minas', 'FORTALEZA DE MINAS', 'M', 'MG', 'SD', 0),
(3126406, 'Fortuna de Minas', 'FORTUNA DE MINAS', 'M', 'MG', 'SD', 0),
(3126505, 'Francisco Badaró', 'FRANCISCO BADARO', 'M', 'MG', 'SD', 0),
(3126604, 'Francisco Dumont', 'FRANCISCO DUMONT', 'M', 'MG', 'SD', 0),
(3126703, 'Francisco Sá', 'FRANCISCO SA', 'M', 'MG', 'SD', 0),
(3126752, 'Franciscópolis', 'FRANCISCOPOLIS', 'M', 'MG', 'SD', 0),
(3126802, 'Frei Gaspar', 'FREI GASPAR', 'M', 'MG', 'SD', 0),
(3126901, 'Frei Inocêncio', 'FREI INOCENCIO', 'M', 'MG', 'SD', 0),
(3126950, 'Frei Lagonegro', 'FREI LAGONEGRO', 'M', 'MG', 'SD', 0),
(3127008, 'Fronteira', 'FRONTEIRA', 'M', 'MG', 'SD', 0),
(3127057, 'Fronteira dos Vales', 'FRONTEIRA DOS VALES', 'M', 'MG', 'SD', 0),
(3127073, 'Fruta de Leite', 'FRUTA DE LEITE', 'M', 'MG', 'SD', 0),
(3127107, 'Frutal', 'FRUTAL', 'M', 'MG', 'SD', 0),
(3127206, 'Funilândia', 'FUNILANDIA', 'M', 'MG', 'SD', 0),
(3127305, 'Galiléia', 'GALILEIA', 'M', 'MG', 'SD', 0),
(3127339, 'Gameleiras', 'GAMELEIRAS', 'M', 'MG', 'SD', 0),
(3127354, 'Glaucilândia', 'GLAUCILANDIA', 'M', 'MG', 'SD', 0),
(3127370, 'Goiabeira', 'GOIABEIRA', 'M', 'MG', 'SD', 0),
(3127388, 'Goiana', 'GOIANA', 'M', 'MG', 'SD', 0),
(3127404, 'Gonçalves', 'GONCALVES', 'M', 'MG', 'SD', 0),
(3127503, 'Gonzaga', 'GONZAGA', 'M', 'MG', 'SD', 0),
(3127602, 'Gouvêa', 'GOUVEA', 'M', 'MG', 'SD', 0),
(3127701, 'Governador Valadares', 'GOVERNADOR VALADARES', 'M', 'MG', 'SD', 0),
(3127800, 'Grão Mogol', 'GRAO MOGOL', 'M', 'MG', 'SD', 0),
(3127909, 'Grupiara', 'GRUPIARA', 'M', 'MG', 'SD', 0),
(3128006, 'Guanhães', 'GUANHAES', 'M', 'MG', 'SD', 0),
(3128105, 'Guapé', 'GUAPE', 'M', 'MG', 'SD', 0),
(3128204, 'Guaraciaba', 'GUARACIABA', 'M', 'MG', 'SD', 0),
(3128253, 'Guaraciama', 'GUARACIAMA', 'M', 'MG', 'SD', 0),
(3128303, 'Guaranésia', 'GUARANESIA', 'M', 'MG', 'SD', 0),
(3128402, 'Guarani', 'GUARANI', 'M', 'MG', 'SD', 0),
(3128501, 'Guarará', 'GUARARA', 'M', 'MG', 'SD', 0),
(3128600, 'Guarda-mor', 'GUARDA-MOR', 'M', 'MG', 'SD', 0),
(3128709, 'Guaxupé', 'GUAXUPE', 'M', 'MG', 'SD', 0),
(3128808, 'Guidoval', 'GUIDOVAL', 'M', 'MG', 'SD', 0),
(3128907, 'Guimarania', 'GUIMARANIA', 'M', 'MG', 'SD', 0),
(3129004, 'Guiricema', 'GUIRICEMA', 'M', 'MG', 'SD', 0),
(3129103, 'Gurinhata', 'GURINHATA', 'M', 'MG', 'SD', 0),
(3129202, 'Heliodora', 'HELIODORA', 'M', 'MG', 'SD', 0),
(3129301, 'Iapu', 'IAPU', 'M', 'MG', 'SD', 0),
(3129400, 'Ibertioga', 'IBERTIOGA', 'M', 'MG', 'SD', 0),
(3129509, 'Ibiá', 'IBIA', 'M', 'MG', 'SD', 0),
(3129608, 'Ibiaí', 'IBIAI', 'M', 'MG', 'SD', 0),
(3129657, 'Ibiracatu', 'IBIRACATU', 'M', 'MG', 'SD', 0),
(3129707, 'Ibiraci', 'IBIRACI', 'M', 'MG', 'SD', 0),
(3129806, 'Ibirité', 'IBIRITE', 'M', 'MG', 'SD', 0),
(3129905, 'Ibitiura de Minas', 'IBITIURA DE MINAS', 'M', 'MG', 'SD', 0),
(3130002, 'Ibituruna', 'IBITURUNA', 'M', 'MG', 'SD', 0),
(3130051, 'Icaraí de Minas', 'ICARAI DE MINAS', 'M', 'MG', 'SD', 0),
(3130101, 'Igarapé', 'IGARAPE', 'M', 'MG', 'SD', 0),
(3130200, 'Igaratinga', 'IGARATINGA', 'M', 'MG', 'SD', 0),
(3130309, 'Iguatama', 'IGUATAMA', 'M', 'MG', 'SD', 0),
(3130408, 'Ijaci', 'IJACI', 'M', 'MG', 'SD', 0),
(3130507, 'Ilicinea', 'ILICINEA', 'M', 'MG', 'SD', 0),
(3130556, 'Imbé de Minas', 'IMBE DE MINAS', 'M', 'MG', 'SD', 0),
(3130606, 'Inconfidentes', 'INCONFIDENTES', 'M', 'MG', 'SD', 0),
(3130655, 'Indaiabira', 'INDAIABIRA', 'M', 'MG', 'SD', 0),
(3130705, 'Indianópolis', 'INDIANOPOLIS', 'M', 'MG', 'SD', 0),
(3130804, 'Ingaí', 'INGAI', 'M', 'MG', 'SD', 0),
(3130903, 'Inhapim', 'INHAPIM', 'M', 'MG', 'SD', 0),
(3131000, 'Inhaúma', 'INHAUMA', 'M', 'MG', 'SD', 0),
(3131109, 'Inimutaba', 'INIMUTABA', 'M', 'MG', 'SD', 0),
(3131158, 'Ipaba', 'IPABA', 'M', 'MG', 'SD', 0),
(3131208, 'Ipanema', 'IPANEMA', 'M', 'MG', 'SD', 0),
(3131307, 'Ipatinga', 'IPATINGA', 'M', 'MG', 'SD', 0),
(3131406, 'Ipiaçu', 'IPIACU', 'M', 'MG', 'SD', 0),
(3131505, 'Ipuiúna', 'IPUIUNA', 'M', 'MG', 'SD', 0),
(3131604, 'Iraí de Minas', 'IRAI DE MINAS', 'M', 'MG', 'SD', 0),
(3131703, 'Itabira', 'ITABIRA', 'M', 'MG', 'SD', 0),
(3131802, 'Itabirinha de Mantena', 'ITABIRINHA DE MANTENA', 'M', 'MG', 'SD', 0),
(3131901, 'Itabirito', 'ITABIRITO', 'M', 'MG', 'SD', 0),
(3132008, 'Itacambira', 'ITACAMBIRA', 'M', 'MG', 'SD', 0),
(3132107, 'Itacarambi', 'ITACARAMBI', 'M', 'MG', 'SD', 0),
(3132206, 'Itaguara', 'ITAGUARA', 'M', 'MG', 'SD', 0),
(3132305, 'Itaipé', 'ITAIPE', 'M', 'MG', 'SD', 0),
(3132404, 'Itajubá', 'ITAJUBA', 'M', 'MG', 'SD', 0),
(3132503, 'Itamarandiba', 'ITAMARANDIBA', 'M', 'MG', 'SD', 0),
(3132602, 'Itamarati de Minas', 'ITAMARATI DE MINAS', 'M', 'MG', 'SD', 0),
(3132701, 'Itambacuri', 'ITAMBACURI', 'M', 'MG', 'SD', 0),
(3132800, 'Itambé do Mato Dentro', 'ITAMBE DO MATO DENTRO', 'M', 'MG', 'SD', 0),
(3132909, 'Itamogi', 'ITAMOGI', 'M', 'MG', 'SD', 0),
(3133006, 'Itamonte', 'ITAMONTE', 'M', 'MG', 'SD', 0),
(3133105, 'Itanhandu', 'ITANHANDU', 'M', 'MG', 'SD', 0),
(3133204, 'Itanhomi', 'ITANHOMI', 'M', 'MG', 'SD', 0),
(3133303, 'Itaobim', 'ITAOBIM', 'M', 'MG', 'SD', 0),
(3133402, 'Itapagipe', 'ITAPAGIPE', 'M', 'MG', 'SD', 0),
(3133501, 'Itapecerica', 'ITAPECERICA', 'M', 'MG', 'SD', 0),
(3133600, 'Itapeva', 'ITAPEVA', 'M', 'MG', 'SD', 0),
(3133709, 'Itatiaiucu', 'ITATIAIUCU', 'M', 'MG', 'SD', 0),
(3133758, 'Itaú de Minas', 'ITAU DE MINAS', 'M', 'MG', 'SD', 0),
(3133808, 'Itaúna', 'ITAUNA', 'M', 'MG', 'SD', 0),
(3133907, 'Itaverava', 'ITAVERAVA', 'M', 'MG', 'SD', 0),
(3134004, 'Itinga', 'ITINGA', 'M', 'MG', 'SD', 0),
(3134103, 'Itueta', 'ITUETA', 'M', 'MG', 'SD', 0),
(3134202, 'Ituiutaba', 'ITUIUTABA', 'M', 'MG', 'SD', 0),
(3134301, 'Itumirim', 'ITUMIRIM', 'M', 'MG', 'SD', 0),
(3134400, 'Iturama', 'ITURAMA', 'M', 'MG', 'SD', 0),
(3134509, 'Itutinga', 'ITUTINGA', 'M', 'MG', 'SD', 0),
(3134608, 'Jaboticatubas', 'JABOTICATUBAS', 'M', 'MG', 'SD', 0),
(3134707, 'Jacinto', 'JACINTO', 'M', 'MG', 'SD', 0),
(3134806, 'Jacuí', 'JACUI', 'M', 'MG', 'SD', 0),
(3134905, 'Jacutinga', 'JACUTINGA', 'M', 'MG', 'SD', 0),
(3135001, 'Jaguaraçu', 'JAGUARACU', 'M', 'MG', 'SD', 0),
(3135050, 'Jaíba', 'JAIBA', 'M', 'MG', 'SD', 0),
(3135076, 'Jampruca', 'JAMPRUCA', 'M', 'MG', 'SD', 0),
(3135100, 'Janaúba', 'JANAUBA', 'M', 'MG', 'SD', 0),
(3135209, 'Januária', 'JANUARIA', 'M', 'MG', 'SD', 0),
(3135308, 'Japaraíba', 'JAPARAIBA', 'M', 'MG', 'SD', 0),
(3135357, 'Japonvar', 'JAPONVAR', 'M', 'MG', 'SD', 0),
(3135407, 'Jeceaba', 'JECEABA', 'M', 'MG', 'SD', 0),
(3135456, 'Jenipapo de Minas', 'JENIPAPO DE MINAS', 'M', 'MG', 'SD', 0),
(3135506, 'Jequeri', 'JEQUERI', 'M', 'MG', 'SD', 0),
(3135605, 'Jequitaí', 'JEQUITAI', 'M', 'MG', 'SD', 0),
(3135704, 'Jequitibá', 'JEQUITIBA', 'M', 'MG', 'SD', 0),
(3135803, 'Jequitinhonha', 'JEQUITINHONHA', 'M', 'MG', 'SD', 0),
(3135902, 'Jesuânia', 'JESUANIA', 'M', 'MG', 'SD', 0),
(3136009, 'Joaima', 'JOAIMA', 'M', 'MG', 'SD', 0),
(3136108, 'Joanésia', 'JOANESIA', 'M', 'MG', 'SD', 0),
(3136207, 'João Monlevade', 'JOAO MONLEVADE', 'M', 'MG', 'SD', 0),
(3136306, 'João Pinheiro', 'JOAO PINHEIRO', 'M', 'MG', 'SD', 0),
(3136405, 'Joaquim Felício', 'JOAQUIM FELICIO', 'M', 'MG', 'SD', 0),
(3136504, 'Jordânia', 'JORDANIA', 'M', 'MG', 'SD', 0),
(3136520, 'José Goncalves de Minas', 'JOSE GONCALVES DE MINAS', 'M', 'MG', 'SD', 0),
(3136553, 'José Raydan', 'JOSE RAYDAN', 'M', 'MG', 'SD', 0),
(3136579, 'Josenópolis', 'JOSENOPOLIS', 'M', 'MG', 'SD', 0),
(3136603, 'Nova União', 'NOVA UNIAO', 'M', 'MG', 'SD', 0),
(3136652, 'Juatuba', 'JUATUBA', 'M', 'MG', 'SD', 0),
(3136702, 'Juiz de Fora', 'JUIZ DE FORA', 'M', 'MG', 'SD', 0),
(3136801, 'Juramento', 'JURAMENTO', 'M', 'MG', 'SD', 0),
(3136900, 'Juruaia', 'JURUAIA', 'M', 'MG', 'SD', 0),
(3136959, 'Juvenília', 'JUVENILIA', 'M', 'MG', 'SD', 0),
(3137007, 'Ladainha', 'LADAINHA', 'M', 'MG', 'SD', 0),
(3137106, 'Lagamar', 'LAGAMAR', 'M', 'MG', 'SD', 0),
(3137205, 'Lagoa da Prata', 'LAGOA DA PRATA', 'M', 'MG', 'SD', 0),
(3137304, 'Lagoa dos Patos', 'LAGOA DOS PATOS', 'M', 'MG', 'SD', 0),
(3137403, 'Lagoa Dourada', 'LAGOA DOURADA', 'M', 'MG', 'SD', 0),
(3137502, 'Lagoa Formosa', 'LAGOA FORMOSA', 'M', 'MG', 'SD', 0),
(3137536, 'Lagoa Grande', 'LAGOA GRANDE', 'M', 'MG', 'SD', 0),
(3137601, 'Lagoa Santa', 'LAGOA SANTA', 'M', 'MG', 'SD', 0),
(3137700, 'Lajinha', 'LAJINHA', 'M', 'MG', 'SD', 0),
(3137809, 'Lambari', 'LAMBARI', 'M', 'MG', 'SD', 0),
(3137908, 'Lamim', 'LAMIM', 'M', 'MG', 'SD', 0),
(3138005, 'Laranjal', 'LARANJAL', 'M', 'MG', 'SD', 0),
(3138104, 'Lassance', 'LASSANCE', 'M', 'MG', 'SD', 0),
(3138203, 'Lavras', 'LAVRAS', 'M', 'MG', 'SD', 0),
(3138302, 'Leandro Ferreira', 'LEANDRO FERREIRA', 'M', 'MG', 'SD', 0),
(3138351, 'Leme do Prado', 'LEME DO PRADO', 'M', 'MG', 'SD', 0),
(3138401, 'Leopoldina', 'LEOPOLDINA', 'M', 'MG', 'SD', 0),
(3138500, 'Liberdade', 'LIBERDADE', 'M', 'MG', 'SD', 0),
(3138609, 'Lima Duarte', 'LIMA DUARTE', 'M', 'MG', 'SD', 0),
(3138625, 'Limeira do Oeste', 'LIMEIRA DO OESTE', 'M', 'MG', 'SD', 0),
(3138658, 'Lontra', 'LONTRA', 'M', 'MG', 'SD', 0),
(3138674, 'Luisburgo', 'LUISBURGO', 'M', 'MG', 'SD', 0),
(3138682, 'Luislândia', 'LUISLANDIA', 'M', 'MG', 'SD', 0),
(3138708, 'Luminárias', 'LUMINARIAS', 'M', 'MG', 'SD', 0),
(3138807, 'Luz', 'LUZ', 'M', 'MG', 'SD', 0),
(3138906, 'Machacalis', 'MACHACALIS', 'M', 'MG', 'SD', 0),
(3139003, 'Machado', 'MACHADO', 'M', 'MG', 'SD', 0),
(3139102, 'Madre de Deus de Minas', 'MADRE DE DEUS DE MINAS', 'M', 'MG', 'SD', 0),
(3139201, 'Malacacheta', 'MALACACHETA', 'M', 'MG', 'SD', 0),
(3139250, 'Mamonas', 'MAMONAS', 'M', 'MG', 'SD', 0),
(3139300, 'Manga', 'MANGA', 'M', 'MG', 'SD', 0),
(3139409, 'Manhuaçu', 'MANHUACU', 'M', 'MG', 'SD', 0),
(3139508, 'Manhumirim', 'MANHUMIRIM', 'M', 'MG', 'SD', 0),
(3139607, 'Mantena', 'MANTENA', 'M', 'MG', 'SD', 0),
(3139706, 'Maravilhas', 'MARAVILHAS', 'M', 'MG', 'SD', 0),
(3139805, 'Mar de Espanha', 'MAR DE ESPANHA', 'M', 'MG', 'SD', 0),
(3139904, 'Maria da Fé', 'MARIA DA FE', 'M', 'MG', 'SD', 0),
(3140001, 'Mariana', 'MARIANA', 'M', 'MG', 'SD', 0),
(3140100, 'Marilac', 'MARILAC', 'M', 'MG', 'SD', 0),
(3140159, 'Mario Campos', 'MARIO CAMPOS', 'M', 'MG', 'SD', 0),
(3140209, 'Maripá de Minas', 'MARIPA DE MINAS', 'M', 'MG', 'SD', 0),
(3140308, 'Marliéria', 'MARLIERIA', 'M', 'MG', 'SD', 0),
(3140407, 'Marmelópolis', 'MARMELOPOLIS', 'M', 'MG', 'SD', 0),
(3140506, 'Martinho Campos', 'MARTINHO CAMPOS', 'M', 'MG', 'SD', 0),
(3140530, 'Martins Soares', 'MARTINS SOARES', 'M', 'MG', 'SD', 0),
(3140555, 'Mata Verde', 'MATA VERDE', 'M', 'MG', 'SD', 0),
(3140605, 'Materlândia', 'MATERLANDIA', 'M', 'MG', 'SD', 0),
(3140704, 'Mateus Leme', 'MATEUS LEME', 'M', 'MG', 'SD', 0),
(3140803, 'Matias Barbosa', 'MATIAS BARBOSA', 'M', 'MG', 'SD', 0),
(3140852, 'Matias Cardoso', 'MATIAS CARDOSO', 'M', 'MG', 'SD', 0),
(3140902, 'Matipó', 'MATIPO', 'M', 'MG', 'SD', 0),
(3141009, 'Mato Verde', 'MATO VERDE', 'M', 'MG', 'SD', 0),
(3141108, 'Matozinhos', 'MATOZINHOS', 'M', 'MG', 'SD', 0),
(3141207, 'Matutina', 'MATUTINA', 'M', 'MG', 'SD', 0),
(3141306, 'Medeiros', 'MEDEIROS', 'M', 'MG', 'SD', 0),
(3141405, 'Medina', 'MEDINA', 'M', 'MG', 'SD', 0),
(3141504, 'Mendes Pimentel', 'MENDES PIMENTEL', 'M', 'MG', 'SD', 0),
(3141603, 'Mercês', 'MERCES', 'M', 'MG', 'SD', 0),
(3141702, 'Mesquita', 'MESQUITA', 'M', 'MG', 'SD', 0),
(3141801, 'Minas Novas', 'MINAS NOVAS', 'M', 'MG', 'SD', 0),
(3141900, 'Minduri', 'MINDURI', 'M', 'MG', 'SD', 0),
(3142007, 'Mirabela', 'MIRABELA', 'M', 'MG', 'SD', 0),
(3142106, 'Miradouro', 'MIRADOURO', 'M', 'MG', 'SD', 0),
(3142205, 'Miraí', 'MIRAI', 'M', 'MG', 'SD', 0),
(3142254, 'Miravânia', 'MIRAVANIA', 'M', 'MG', 'SD', 0),
(3142304, 'Moeda', 'MOEDA', 'M', 'MG', 'SD', 0),
(3142403, 'Moema', 'MOEMA', 'M', 'MG', 'SD', 0),
(3142502, 'Monjolos', 'MONJOLOS', 'M', 'MG', 'SD', 0),
(3142601, 'Monsenhor Paulo', 'MONSENHOR PAULO', 'M', 'MG', 'SD', 0),
(3142700, 'Montalvânia', 'MONTALVANIA', 'M', 'MG', 'SD', 0),
(3142809, 'Monte Alegre de Minas', 'MONTE ALEGRE DE MINAS', 'M', 'MG', 'SD', 0),
(3142908, 'Monte Azul', 'MONTE AZUL', 'M', 'MG', 'SD', 0),
(3143005, 'Monte Belo', 'MONTE BELO', 'M', 'MG', 'SD', 0),
(3143104, 'Monte Carmelo', 'MONTE CARMELO', 'M', 'MG', 'SD', 0),
(3143153, 'Monte Formoso', 'MONTE FORMOSO', 'M', 'MG', 'SD', 0),
(3143203, 'Monte Santo de Minas', 'MONTE SANTO DE MINAS', 'M', 'MG', 'SD', 0),
(3143302, 'Montes Claros', 'MONTES CLAROS', 'M', 'MG', 'SD', 0),
(3143401, 'Monte Sião', 'MONTE SIAO', 'M', 'MG', 'SD', 0),
(3143450, 'Montezuma', 'MONTEZUMA', 'M', 'MG', 'SD', 0),
(3143500, 'Morada Nova de Minas', 'MORADA NOVA DE MINAS', 'M', 'MG', 'SD', 0),
(3143609, 'Morro da Garça', 'MORRO DA GARCA', 'M', 'MG', 'SD', 0),
(3143708, 'Morro do Pilar', 'MORRO DO PILAR', 'M', 'MG', 'SD', 0),
(3143807, 'Munhoz', 'MUNHOZ', 'M', 'MG', 'SD', 0),
(3143906, 'Muriaé', 'MURIAE', 'M', 'MG', 'SD', 0),
(3144003, 'Mutum', 'MUTUM', 'M', 'MG', 'SD', 0),
(3144102, 'Muzambinho', 'MUZAMBINHO', 'M', 'MG', 'SD', 0),
(3144201, 'Nacip Raydan', 'NACIP RAYDAN', 'M', 'MG', 'SD', 0),
(3144300, 'Nanuque', 'NANUQUE', 'M', 'MG', 'SD', 0),
(3144359, 'Naque', 'NAQUE', 'M', 'MG', 'SD', 0),
(3144375, 'Natalândia', 'NATALANDIA', 'M', 'MG', 'SD', 0),
(3144409, 'Natércia', 'NATERCIA', 'M', 'MG', 'SD', 0),
(3144508, 'Nazareno', 'NAZARENO', 'M', 'MG', 'SD', 0),
(3144607, 'Nepomuceno', 'NEPOMUCENO', 'M', 'MG', 'SD', 0),
(3144656, 'Ninheira', 'NINHEIRA', 'M', 'MG', 'SD', 0),
(3144672, 'Nova Belém', 'NOVA BELEM', 'M', 'MG', 'SD', 0),
(3144706, 'Nova Era', 'NOVA ERA', 'M', 'MG', 'SD', 0),
(3144805, 'Nova Lima', 'NOVA LIMA', 'M', 'MG', 'SD', 0),
(3144904, 'Nova Módica', 'NOVA MODICA', 'M', 'MG', 'SD', 0),
(3145000, 'Nova Ponte', 'NOVA PONTE', 'M', 'MG', 'SD', 0),
(3145059, 'Nova Porteirinha', 'NOVA PORTEIRINHA', 'M', 'MG', 'SD', 0),
(3145109, 'Nova Resende', 'NOVA RESENDE', 'M', 'MG', 'SD', 0),
(3145208, 'Nova Serrana', 'NOVA SERRANA', 'M', 'MG', 'SD', 0),
(3145307, 'Novo Cruzeiro', 'NOVO CRUZEIRO', 'M', 'MG', 'SD', 0),
(3145356, 'Novo Oriente de Minas', 'NOVO ORIENTE DE MINAS', 'M', 'MG', 'SD', 0),
(3145372, 'Novorizonte', 'NOVORIZONTE', 'M', 'MG', 'SD', 0),
(3145406, 'Olaria', 'OLARIA', 'M', 'MG', 'SD', 0),
(3145455, 'Olhos-D''Água', 'OLHOS-D''AGUA', 'M', 'MG', 'SD', 0),
(3145505, 'Olimpio Noronha', 'OLIMPIO NORONHA', 'M', 'MG', 'SD', 0),
(3145604, 'Oliveira', 'OLIVEIRA', 'M', 'MG', 'SD', 0),
(3145703, 'Oliveira Fortes', 'OLIVEIRA FORTES', 'M', 'MG', 'SD', 0),
(3145802, 'Onça de Pitangui', 'ONCA DE PITANGUI', 'M', 'MG', 'SD', 0),
(3145851, 'Oratórios', 'ORATORIOS', 'M', 'MG', 'SD', 0),
(3145877, 'Orizânia', 'ORIZANIA', 'M', 'MG', 'SD', 0),
(3145901, 'Ouro Branco', 'OURO BRANCO', 'M', 'MG', 'SD', 0),
(3146008, 'Ouro Fino', 'OURO FINO', 'M', 'MG', 'SD', 0),
(3146107, 'Ouro Preto', 'OURO PRETO', 'M', 'MG', 'SD', 0),
(3146206, 'Ouro Verde de Minas', 'OURO VERDE DE MINAS', 'M', 'MG', 'SD', 0),
(3146255, 'Padre Carvalho', 'PADRE CARVALHO', 'M', 'MG', 'SD', 0),
(3146305, 'Padre Paraiso', 'PADRE PARAISO', 'M', 'MG', 'SD', 0),
(3146404, 'Paineiras', 'PAINEIRAS', 'M', 'MG', 'SD', 0),
(3146503, 'Pains', 'PAINS', 'M', 'MG', 'SD', 0),
(3146552, 'Pai Pedro', 'PAI PEDRO', 'M', 'MG', 'SD', 0),
(3146602, 'Paiva', 'PAIVA', 'M', 'MG', 'SD', 0),
(3146701, 'Palma', 'PALMA', 'M', 'MG', 'SD', 0),
(3146750, 'Palmópolis', 'PALMOPOLIS', 'M', 'MG', 'SD', 0),
(3146909, 'Papagaios', 'PAPAGAIOS', 'M', 'MG', 'SD', 0),
(3147006, 'Paracatu', 'PARACATU', 'M', 'MG', 'SD', 0),
(3147105, 'Pará de Minas', 'PARA DE MINAS', 'M', 'MG', 'SD', 0),
(3147204, 'Paraguaçu', 'PARAGUACU', 'M', 'MG', 'SD', 0),
(3147303, 'Paraisópolis', 'PARAISOPOLIS', 'M', 'MG', 'SD', 0),
(3147402, 'Paraopeba', 'PARAOPEBA', 'M', 'MG', 'SD', 0),
(3147501, 'Passabem', 'PASSABEM', 'M', 'MG', 'SD', 0),
(3147600, 'Passa Quatro', 'PASSA QUATRO', 'M', 'MG', 'SD', 0),
(3147709, 'Passa Tempo', 'PASSA TEMPO', 'M', 'MG', 'SD', 0),
(3147808, 'Passa Vinte', 'PASSA VINTE', 'M', 'MG', 'SD', 0),
(3147907, 'Passos', 'PASSOS', 'M', 'MG', 'SD', 0),
(3147956, 'Patis', 'PATIS', 'M', 'MG', 'SD', 0),
(3148004, 'Patos de Minas', 'PATOS DE MINAS', 'M', 'MG', 'SD', 0),
(3148103, 'Patrocinio', 'PATROCINIO', 'M', 'MG', 'SD', 0),
(3148202, 'Patrocinio do Muriaé', 'PATROCINIO DO MURIAE', 'M', 'MG', 'SD', 0),
(3148301, 'Paula Cândido', 'PAULA CANDIDO', 'M', 'MG', 'SD', 0),
(3148400, 'Paulistas', 'PAULISTAS', 'M', 'MG', 'SD', 0),
(3148509, 'Pavão', 'PAVAO', 'M', 'MG', 'SD', 0),
(3148608, 'Peçanha', 'PECANHA', 'M', 'MG', 'SD', 0),
(3148707, 'Pedra Azul', 'PEDRA AZUL', 'M', 'MG', 'SD', 0),
(3148756, 'Pedra Bonita', 'PEDRA BONITA', 'M', 'MG', 'SD', 0),
(3148806, 'Pedra do Anta', 'PEDRA DO ANTA', 'M', 'MG', 'SD', 0),
(3148905, 'Pedra do Indaiá', 'PEDRA DO INDAIA', 'M', 'MG', 'SD', 0),
(3149002, 'Pedra Dourada', 'PEDRA DOURADA', 'M', 'MG', 'SD', 0),
(3149101, 'Pedralva', 'PEDRALVA', 'M', 'MG', 'SD', 0),
(3149150, 'Pedras de Maria da Cruz', 'PEDRAS DE MARIA DA CRUZ', 'M', 'MG', 'SD', 0),
(3149200, 'Pedrinópolis', 'PEDRINOPOLIS', 'M', 'MG', 'SD', 0),
(3149309, 'Pedro Leopoldo', 'PEDRO LEOPOLDO', 'M', 'MG', 'SD', 0),
(3149408, 'Pedro Teixeira', 'PEDRO TEIXEIRA', 'M', 'MG', 'SD', 0),
(3149507, 'Pequeri', 'PEQUERI', 'M', 'MG', 'SD', 0),
(3149606, 'Pequi', 'PEQUI', 'M', 'MG', 'SD', 0),
(3149705, 'Perdigão', 'PERDIGAO', 'M', 'MG', 'SD', 0),
(3149804, 'Perdizes', 'PERDIZES', 'M', 'MG', 'SD', 0),
(3149903, 'Perdões', 'PERDOES', 'M', 'MG', 'SD', 0),
(3149952, 'Periquito', 'PERIQUITO', 'M', 'MG', 'SD', 0),
(3150000, 'Pescador', 'PESCADOR', 'M', 'MG', 'SD', 0),
(3150109, 'Piau', 'PIAU', 'M', 'MG', 'SD', 0),
(3150158, 'Piedade de Caratinga', 'PIEDADE DE CARATINGA', 'M', 'MG', 'SD', 0),
(3150208, 'Piedade de Ponte Nova', 'PIEDADE DE PONTE NOVA', 'M', 'MG', 'SD', 0),
(3150307, 'Piedade do Rio Grande', 'PIEDADE DO RIO GRANDE', 'M', 'MG', 'SD', 0),
(3150406, 'Piedade dos Gerais', 'PIEDADE DOS GERAIS', 'M', 'MG', 'SD', 0),
(3150505, 'Pimenta', 'PIMENTA', 'M', 'MG', 'SD', 0),
(3150539, 'Pingo D''agua', 'PINGO D''AGUA', 'M', 'MG', 'SD', 0),
(3150570, 'Pintópolis', 'PINTOPOLIS', 'M', 'MG', 'SD', 0),
(3150604, 'Piracema', 'PIRACEMA', 'M', 'MG', 'SD', 0),
(3150703, 'Pirajuba', 'PIRAJUBA', 'M', 'MG', 'SD', 0),
(3150802, 'Piranga', 'PIRANGA', 'M', 'MG', 'SD', 0),
(3150901, 'Piranguçu', 'PIRANGUCU', 'M', 'MG', 'SD', 0),
(3151008, 'Piranguinho', 'PIRANGUINHO', 'M', 'MG', 'SD', 0),
(3151107, 'Pirapetinga', 'PIRAPETINGA', 'M', 'MG', 'SD', 0),
(3151206, 'Pirapora', 'PIRAPORA', 'M', 'MG', 'SD', 0),
(3151305, 'Piraúba', 'PIRAUBA', 'M', 'MG', 'SD', 0),
(3151404, 'Pitangui', 'PITANGUI', 'M', 'MG', 'SD', 0),
(3151503, 'Piumhi', 'PIUMHI', 'M', 'MG', 'SD', 0),
(3151602, 'Planura', 'PLANURA', 'M', 'MG', 'SD', 0),
(3151701, 'Poço Fundo', 'POCO FUNDO', 'M', 'MG', 'SD', 0),
(3151800, 'Poços de Caldas', 'POCOS DE CALDAS', 'M', 'MG', 'SD', 0),
(3151909, 'Pocrane', 'POCRANE', 'M', 'MG', 'SD', 0),
(3152006, 'Pompéu', 'POMPEU', 'M', 'MG', 'SD', 0),
(3152105, 'Ponte Nova', 'PONTE NOVA', 'M', 'MG', 'SD', 0),
(3152131, 'Ponto Chique', 'PONTO CHIQUE', 'M', 'MG', 'SD', 0),
(3152170, 'Ponto dos Volantes', 'PONTO DOS VOLANTES', 'M', 'MG', 'SD', 0),
(3152204, 'Porteirinha', 'PORTEIRINHA', 'M', 'MG', 'SD', 0),
(3152303, 'Porto Firme', 'PORTO FIRME', 'M', 'MG', 'SD', 0),
(3152402, 'Poté', 'POTE', 'M', 'MG', 'SD', 0),
(3152501, 'Pouso Alegre', 'POUSO ALEGRE', 'M', 'MG', 'SD', 0),
(3152600, 'Pouso Alto', 'POUSO ALTO', 'M', 'MG', 'SD', 0),
(3152709, 'Prados', 'PRADOS', 'M', 'MG', 'SD', 0),
(3152808, 'Prata', 'PRATA', 'M', 'MG', 'SD', 0),
(3152907, 'Pratápolis', 'PRATAPOLIS', 'M', 'MG', 'SD', 0),
(3153004, 'Pratinha', 'PRATINHA', 'M', 'MG', 'SD', 0),
(3153103, 'Presidente Bernardes', 'PRESIDENTE BERNARDES', 'M', 'MG', 'SD', 0),
(3153202, 'Presidente Juscelino', 'PRESIDENTE JUSCELINO', 'M', 'MG', 'SD', 0),
(3153301, 'Presidente Kubitschek', 'PRESIDENTE KUBITSCHEK', 'M', 'MG', 'SD', 0),
(3153400, 'Presidente Olegário', 'PRESIDENTE OLEGARIO', 'M', 'MG', 'SD', 0),
(3153509, 'Alto Jequitibá', 'ALTO JEQUITIBA', 'M', 'MG', 'SD', 0),
(3153608, 'Prudente de Morais', 'PRUDENTE DE MORAIS', 'M', 'MG', 'SD', 0),
(3153707, 'Quartel Geral', 'QUARTEL GERAL', 'M', 'MG', 'SD', 0),
(3153806, 'Queluzita', 'QUELUZITA', 'M', 'MG', 'SD', 0),
(3153905, 'Raposos', 'RAPOSOS', 'M', 'MG', 'SD', 0),
(3154002, 'Raul Soares', 'RAUL SOARES', 'M', 'MG', 'SD', 0),
(3154101, 'Recreio', 'RECREIO', 'M', 'MG', 'SD', 0),
(3154150, 'Reduto', 'REDUTO', 'M', 'MG', 'SD', 0),
(3154200, 'Resende Costa', 'RESENDE COSTA', 'M', 'MG', 'SD', 0),
(3154309, 'Resplendor', 'RESPLENDOR', 'M', 'MG', 'SD', 0),
(3154408, 'Ressaquinha', 'RESSAQUINHA', 'M', 'MG', 'SD', 0),
(3154457, 'Riachinho', 'RIACHINHO', 'M', 'MG', 'SD', 0),
(3154507, 'Riacho dos Machados', 'RIACHO DOS MACHADOS', 'M', 'MG', 'SD', 0),
(3154606, 'Ribeirão das Neves', 'RIBEIRAO DAS NEVES', 'M', 'MG', 'SD', 0),
(3154705, 'Ribeirão Vermelho', 'RIBEIRAO VERMELHO', 'M', 'MG', 'SD', 0),
(3154804, 'Rio Acima', 'RIO ACIMA', 'M', 'MG', 'SD', 0),
(3154903, 'Rio Casca', 'RIO CASCA', 'M', 'MG', 'SD', 0),
(3155009, 'Rio Doce', 'RIO DOCE', 'M', 'MG', 'SD', 0),
(3155108, 'Rio do Prado', 'RIO DO PRADO', 'M', 'MG', 'SD', 0),
(3155207, 'Rio Espera', 'RIO ESPERA', 'M', 'MG', 'SD', 0),
(3155306, 'Rio Manso', 'RIO MANSO', 'M', 'MG', 'SD', 0),
(3155405, 'Rio Novo', 'RIO NOVO', 'M', 'MG', 'SD', 0),
(3155504, 'Rio Paranaíba', 'RIO PARANAIBA', 'M', 'MG', 'SD', 0),
(3155603, 'Rio Pardo de Minas', 'RIO PARDO DE MINAS', 'M', 'MG', 'SD', 0),
(3155702, 'Rio Piracicaba', 'RIO PIRACICABA', 'M', 'MG', 'SD', 0),
(3155801, 'Rio Pomba', 'RIO POMBA', 'M', 'MG', 'SD', 0),
(3155900, 'Rio Preto', 'RIO PRETO', 'M', 'MG', 'SD', 0),
(3156007, 'Rio Vermelho', 'RIO VERMELHO', 'M', 'MG', 'SD', 0),
(3156106, 'Ritápolis', 'RITAPOLIS', 'M', 'MG', 'SD', 0),
(3156205, 'Rochedo de Minas', 'ROCHEDO DE MINAS', 'M', 'MG', 'SD', 0),
(3156304, 'Rodeiro', 'RODEIRO', 'M', 'MG', 'SD', 0),
(3156403, 'Romaria', 'ROMARIA', 'M', 'MG', 'SD', 0),
(3156452, 'Rosário da Limeira', 'ROSARIO DA LIMEIRA', 'M', 'MG', 'SD', 0),
(3156502, 'Rubelita', 'RUBELITA', 'M', 'MG', 'SD', 0),
(3156601, 'Rubim', 'RUBIM', 'M', 'MG', 'SD', 0),
(3156700, 'Sabará', 'SABARA', 'M', 'MG', 'SD', 0),
(3156809, 'Sabinópolis', 'SABINOPOLIS', 'M', 'MG', 'SD', 0),
(3156908, 'Sacramento', 'SACRAMENTO', 'M', 'MG', 'SD', 0),
(3157005, 'Salinas', 'SALINAS', 'M', 'MG', 'SD', 0),
(3157104, 'Salto da Divisa', 'SALTO DA DIVISA', 'M', 'MG', 'SD', 0),
(3157203, 'Santa Barbara', 'SANTA BARBARA', 'M', 'MG', 'SD', 0),
(3157252, 'Santa Bárbara do Leste', 'SANTA BARBARA DO LESTE', 'M', 'MG', 'SD', 0),
(3157278, 'Santa Bárbara do Monte Verde', 'SANTA BARBARA DO MONTE VERDE', 'M', 'MG', 'SD', 0),
(3157302, 'Santa Bárbara do Tugurio', 'SANTA BARBARA DO TUGURIO', 'M', 'MG', 'SD', 0),
(3157336, 'Santa Cruz de Minas', 'SANTA CRUZ DE MINAS', 'M', 'MG', 'SD', 0),
(3157377, 'Santa Cruz de Salinas', 'SANTA CRUZ DE SALINAS', 'M', 'MG', 'SD', 0),
(3157401, 'Santa Cruz do Escalvado', 'SANTA CRUZ DO ESCALVADO', 'M', 'MG', 'SD', 0),
(3157500, 'Santa Efigênia de Minas', 'SANTA EFIGENIA DE MINAS', 'M', 'MG', 'SD', 0),
(3157609, 'Santa Fé de Minas', 'SANTA FE DE MINAS', 'M', 'MG', 'SD', 0),
(3157658, 'Santa Helena de Minas', 'SANTA HELENA DE MINAS', 'M', 'MG', 'SD', 0),
(3157708, 'Santa Juliana', 'SANTA JULIANA', 'M', 'MG', 'SD', 0),
(3157807, 'Santa Luzia', 'SANTA LUZIA', 'M', 'MG', 'SD', 0),
(3157906, 'Santa Margarida', 'SANTA MARGARIDA', 'M', 'MG', 'SD', 0),
(3158003, 'Santa Maria de Itabira', 'SANTA MARIA DE ITABIRA', 'M', 'MG', 'SD', 0),
(3158102, 'Santa Maria do Salto', 'SANTA MARIA DO SALTO', 'M', 'MG', 'SD', 0),
(3158201, 'Santa Maria do Suaçuí', 'SANTA MARIA DO SUACUI', 'M', 'MG', 'SD', 0),
(3158300, 'Santana da Vargem', 'SANTANA DA VARGEM', 'M', 'MG', 'SD', 0),
(3158409, 'Santana de Cataguases', 'SANTANA DE CATAGUASES', 'M', 'MG', 'SD', 0),
(3158508, 'Santana de Pirapama', 'SANTANA DE PIRAPAMA', 'M', 'MG', 'SD', 0),
(3158607, 'Santana do Deserto', 'SANTANA DO DESERTO', 'M', 'MG', 'SD', 0),
(3158706, 'Santana do Garambéu', 'SANTANA DO GARAMBEU', 'M', 'MG', 'SD', 0),
(3158805, 'Santana do Jacaré', 'SANTANA DO JACARE', 'M', 'MG', 'SD', 0),
(3158904, 'Santana do Manhuaçu', 'SANTANA DO MANHUACU', 'M', 'MG', 'SD', 0),
(3158953, 'Santana do Paraíso', 'SANTANA DO PARAISO', 'M', 'MG', 'SD', 0),
(3159001, 'Santana do Riacho', 'SANTANA DO RIACHO', 'M', 'MG', 'SD', 0),
(3159100, 'Santana dos Montes', 'SANTANA DOS MONTES', 'M', 'MG', 'SD', 0),
(3159209, 'Santa Rita de Caldas', 'SANTA RITA DE CALDAS', 'M', 'MG', 'SD', 0),
(3159308, 'Santa Rita de Jacutinga', 'SANTA RITA DE JACUTINGA', 'M', 'MG', 'SD', 0),
(3159357, 'Santa Rita de Minas', 'SANTA RITA DE MINAS', 'M', 'MG', 'SD', 0),
(3159407, 'Santa Rita de Ibitipoca', 'SANTA RITA DE IBITIPOCA', 'M', 'MG', 'SD', 0),
(3159506, 'Santa Rita do Itueto', 'SANTA RITA DO ITUETO', 'M', 'MG', 'SD', 0),
(3159605, 'Santa Rita do Sapucaí', 'SANTA RITA DO SAPUCAI', 'M', 'MG', 'SD', 0),
(3159704, 'Santa Rosa da Serra', 'SANTA ROSA DA SERRA', 'M', 'MG', 'SD', 0),
(3159803, 'Santa Vitória', 'SANTA VITORIA', 'M', 'MG', 'SD', 0),
(3159902, 'Santo Antônio do Amparo', 'SANTO ANTONIO DO AMPARO', 'M', 'MG', 'SD', 0),
(3160009, 'Santo Antônio do Aventureiro', 'SANTO ANTONIO DO AVENTUREIRO', 'M', 'MG', 'SD', 0),
(3160108, 'Santo Antônio do Grama', 'SANTO ANTONIO DO GRAMA', 'M', 'MG', 'SD', 0),
(3160207, 'Santo Antônio do Itambé', 'SANTO ANTONIO DO ITAMBE', 'M', 'MG', 'SD', 0),
(3160306, 'Santo Antônio do Jacinto', 'SANTO ANTONIO DO JACINTO', 'M', 'MG', 'SD', 0),
(3160405, 'Santo Antônio do Monte', 'SANTO ANTONIO DO MONTE', 'M', 'MG', 'SD', 0),
(3160454, 'Santo Antônio do Retiro', 'SANTO ANTONIO DO RETIRO', 'M', 'MG', 'SD', 0),
(3160504, 'Santo Antônio do Rio Abaixo', 'SANTO ANTONIO DO RIO ABAIXO', 'M', 'MG', 'SD', 0),
(3160603, 'Santo Hipólito', 'SANTO HIPOLITO', 'M', 'MG', 'SD', 0),
(3160702, 'Santos Dumont', 'SANTOS DUMONT', 'M', 'MG', 'SD', 0),
(3160801, 'São Bento Abade', 'SAO BENTO ABADE', 'M', 'MG', 'SD', 0),
(3160900, 'São Brás do Suaçuí', 'SAO BRAS DO SUACUI', 'M', 'MG', 'SD', 0),
(3160959, 'São Domingos das Dores', 'SAO DOMINGOS DAS DORES', 'M', 'MG', 'SD', 0),
(3161007, 'São Domingos do Prata', 'SAO DOMINGOS DO PRATA', 'M', 'MG', 'SD', 0),
(3161056, 'São Félix de Minas', 'SAO FELIX DE MINAS', 'M', 'MG', 'SD', 0),
(3161106, 'São Francisco', 'SAO FRANCISCO', 'M', 'MG', 'SD', 0),
(3161205, 'São Francisco de Paula', 'SAO FRANCISCO DE PAULA', 'M', 'MG', 'SD', 0),
(3161304, 'São Francisco de Sales', 'SAO FRANCISCO DE SALES', 'M', 'MG', 'SD', 0),
(3161403, 'São Francisco do Glória', 'SAO FRANCISCO DO GLORIA', 'M', 'MG', 'SD', 0),
(3161502, 'São Geraldo', 'SAO GERALDO', 'M', 'MG', 'SD', 0),
(3161601, 'São Geraldo da Piedade', 'SAO GERALDO DA PIEDADE', 'M', 'MG', 'SD', 0),
(3161650, 'São Geraldo do Baixio', 'SAO GERALDO DO BAIXIO', 'M', 'MG', 'SD', 0),
(3161700, 'São Gonçalo do Abaeté', 'SAO GONCALO DO ABAETE', 'M', 'MG', 'SD', 0),
(3161809, 'São Gonçalo do Pará', 'SAO GONCALO DO PARA', 'M', 'MG', 'SD', 0),
(3161908, 'São Gonçalo do Rio Abaixo', 'SAO GONCALO DO RIO ABAIXO', 'M', 'MG', 'SD', 0),
(3162005, 'São Gonçalo do Sapucaí', 'SAO GONCALO DO SAPUCAI', 'M', 'MG', 'SD', 0),
(3162104, 'São Gotardo', 'SAO GOTARDO', 'M', 'MG', 'SD', 0),
(3162203, 'São João Batista do Gloria', 'SAO JOAO BATISTA DO GLORIA', 'M', 'MG', 'SD', 0),
(3162252, 'São João da Lagoa', 'SAO JOAO DA LAGOA', 'M', 'MG', 'SD', 0),
(3162302, 'São João da Mata', 'SAO JOAO DA MATA', 'M', 'MG', 'SD', 0),
(3162401, 'São João da Ponte', 'SAO JOAO DA PONTE', 'M', 'MG', 'SD', 0),
(3162450, 'São João das Missões', 'SAO JOAO DAS MISSOES', 'M', 'MG', 'SD', 0),
(3162500, 'São João Del Rei', 'SAO JOAO DEL REI', 'M', 'MG', 'SD', 0),
(3162559, 'São João do Manhuaçu', 'SAO JOAO DO MANHUACU', 'M', 'MG', 'SD', 0),
(3162575, 'São João do Manteninha', 'SAO JOAO DO MANTENINHA', 'M', 'MG', 'SD', 0),
(3162609, 'São João do Oriente', 'SAO JOAO DO ORIENTE', 'M', 'MG', 'SD', 0),
(3162658, 'São João do Pacuí', 'SAO JOAO DO PACUI', 'M', 'MG', 'SD', 0),
(3162708, 'São João do Paraiíso', 'SAO JOAO DO PARAISO', 'M', 'MG', 'SD', 0),
(3162807, 'São João Evangelista', 'SAO JOAO EVANGELISTA', 'M', 'MG', 'SD', 0),
(3162906, 'São João Nepomuceno', 'SAO JOAO NEPOMUCENO', 'M', 'MG', 'SD', 0),
(3162922, 'São Joaquim de Bicas', 'SAO JOAQUIM DE BICAS', 'M', 'MG', 'SD', 0),
(3162948, 'São José da Barra', 'SAO JOSE DA BARRA', 'M', 'MG', 'SD', 0),
(3162955, 'São José da Lapa', 'SAO JOSE DA LAPA', 'M', 'MG', 'SD', 0),
(3163003, 'São José da Safira', 'SAO JOSE DA SAFIRA', 'M', 'MG', 'SD', 0),
(3163102, 'São José da Varginha', 'SAO JOSE DA VARGINHA', 'M', 'MG', 'SD', 0),
(3163201, 'São José do Alegre', 'SAO JOSE DO ALEGRE', 'M', 'MG', 'SD', 0),
(3163300, 'São José do Divino', 'SAO JOSE DO DIVINO', 'M', 'MG', 'SD', 0),
(3163409, 'São José do Goiabal', 'SAO JOSE DO GOIABAL', 'M', 'MG', 'SD', 0),
(3163508, 'São José do Jacuri', 'SAO JOSE DO JACURI', 'M', 'MG', 'SD', 0),
(3163607, 'São José do Mantimento', 'SAO JOSE DO MANTIMENTO', 'M', 'MG', 'SD', 0),
(3163706, 'São Lourenço', 'SAO LOURENCO', 'M', 'MG', 'SD', 0),
(3163805, 'São Miguel do Anta', 'SAO MIGUEL DO ANTA', 'M', 'MG', 'SD', 0),
(3163904, 'São Pedro da União', 'SAO PEDRO DA UNIAO', 'M', 'MG', 'SD', 0),
(3164001, 'São Pedro dos Ferros', 'SAO PEDRO DOS FERROS', 'M', 'MG', 'SD', 0),
(3164100, 'São Pedro do Suaçuí', 'SAO PEDRO DO SUACUI', 'M', 'MG', 'SD', 0),
(3164209, 'São Romão', 'SAO ROMAO', 'M', 'MG', 'SD', 0),
(3164308, 'São Roque de Minas', 'SAO ROQUE DE MINAS', 'M', 'MG', 'SD', 0),
(3164407, 'São Sebastião da Bela Vista', 'SAO SEBASTIAO DA BELA VISTA', 'M', 'MG', 'SD', 0),
(3164431, 'São Sebastião da Vargem Alegre', 'SAO SEBASTIAO DA VARGEM ALEGRE', 'M', 'MG', 'SD', 0),
(3164472, 'São Sebastião do Anta', 'SAO SEBASTIAO DO ANTA', 'M', 'MG', 'SD', 0),
(3164506, 'São Sebastião do Maranhão', 'SAO SEBASTIAO DO MARANHAO', 'M', 'MG', 'SD', 0),
(3164605, 'São Sebastião do Oeste', 'SAO SEBASTIAO DO OESTE', 'M', 'MG', 'SD', 0),
(3164704, 'São Sebastião do Paraíso', 'SAO SEBASTIAO DO PARAISO', 'M', 'MG', 'SD', 0),
(3164803, 'São Sebastião do Rio Preto', 'SAO SEBASTIAO DO RIO PRETO', 'M', 'MG', 'SD', 0),
(3164902, 'São Sebastião do Rio Verde', 'SAO SEBASTIAO DO RIO VERDE', 'M', 'MG', 'SD', 0),
(3165008, 'São Tiago', 'SAO TIAGO', 'M', 'MG', 'SD', 0),
(3165107, 'São Tomás de Aquino', 'SAO TOMAS DE AQUINO', 'M', 'MG', 'SD', 0),
(3165206, 'São Thomé das Letras', 'SAO THOME DAS LETRAS', 'M', 'MG', 'SD', 0),
(3165305, 'São Vicente de Minas', 'SAO VICENTE DE MINAS', 'M', 'MG', 'SD', 0),
(3165404, 'Sapucaí-Mirim', 'SAPUCAI-MIRIM', 'M', 'MG', 'SD', 0),
(3165503, 'Sardoa', 'SARDOA', 'M', 'MG', 'SD', 0),
(3165537, 'Sarzedo', 'SARZEDO', 'M', 'MG', 'SD', 0),
(3165552, 'Setubinha', 'SETUBINHA', 'M', 'MG', 'SD', 0),
(3165560, 'Sem-peixe', 'SEM-PEIXE', 'M', 'MG', 'SD', 0),
(3165578, 'Senador Amaral', 'SENADOR AMARAL', 'M', 'MG', 'SD', 0),
(3165602, 'Senador Cortes', 'SENADOR CORTES', 'M', 'MG', 'SD', 0),
(3165701, 'Senador Firmino', 'SENADOR FIRMINO', 'M', 'MG', 'SD', 0),
(3165800, 'Senador José Bento', 'SENADOR JOSE BENTO', 'M', 'MG', 'SD', 0),
(3165909, 'Senador Modestino Gonçalves', 'SENADOR MODESTINO GONCALVES', 'M', 'MG', 'SD', 0),
(3166006, 'Senhora de Oliveira', 'SENHORA DE OLIVEIRA', 'M', 'MG', 'SD', 0),
(3166105, 'Senhora do Porto', 'SENHORA DO PORTO', 'M', 'MG', 'SD', 0),
(3166204, 'Senhora dos Remédios', 'SENHORA DOS REMEDIOS', 'M', 'MG', 'SD', 0),
(3166303, 'Sericita', 'SERICITA', 'M', 'MG', 'SD', 0),
(3166402, 'Seritinga', 'SERITINGA', 'M', 'MG', 'SD', 0),
(3166501, 'Serra Azul de Minas', 'SERRA AZUL DE MINAS', 'M', 'MG', 'SD', 0),
(3166600, 'Serra da Saudade', 'SERRA DA SAUDADE', 'M', 'MG', 'SD', 0),
(3166709, 'Serra dos Aimorés', 'SERRA DOS AIMORES', 'M', 'MG', 'SD', 0),
(3166808, 'Serra do Salitre', 'SERRA DO SALITRE', 'M', 'MG', 'SD', 0),
(3166907, 'Serrania', 'SERRANIA', 'M', 'MG', 'SD', 0),
(3166956, 'Serranópolis de Minas', 'SERRANOPOLIS DE MINAS', 'M', 'MG', 'SD', 0),
(3167004, 'Serranos', 'SERRANOS', 'M', 'MG', 'SD', 0),
(3167103, 'Serro', 'SERRO', 'M', 'MG', 'SD', 0),
(3167202, 'Sete Lagoas', 'SETE LAGOAS', 'M', 'MG', 'SD', 0),
(3167301, 'Silveirânia', 'SILVEIRANIA', 'M', 'MG', 'SD', 0),
(3167400, 'Silvianópolis', 'SILVIANOPOLIS', 'M', 'MG', 'SD', 0),
(3167509, 'Simão Pereira', 'SIMAO PEREIRA', 'M', 'MG', 'SD', 0),
(3167608, 'Simonésia', 'SIMONESIA', 'M', 'MG', 'SD', 0),
(3167707, 'Sobrália', 'SOBRALIA', 'M', 'MG', 'SD', 0),
(3167806, 'Soledade de Minas', 'SOLEDADE DE MINAS', 'M', 'MG', 'SD', 0),
(3167905, 'Tabuleiro', 'TABULEIRO', 'M', 'MG', 'SD', 0),
(3168002, 'Taiobeiras', 'TAIOBEIRAS', 'M', 'MG', 'SD', 0),
(3168051, 'Taparuba', 'TAPARUBA', 'M', 'MG', 'SD', 0),
(3168101, 'Tapira', 'TAPIRA', 'M', 'MG', 'SD', 0),
(3168200, 'Tapiraí', 'TAPIRAI', 'M', 'MG', 'SD', 0),
(3168309, 'Taquaracu de Minas', 'TAQUARACU DE MINAS', 'M', 'MG', 'SD', 0),
(3168408, 'Tarumirim', 'TARUMIRIM', 'M', 'MG', 'SD', 0),
(3168507, 'Teixeiras', 'TEIXEIRAS', 'M', 'MG', 'SD', 0),
(3168606, 'Teófilo Otoni', 'TEOFILO OTONI', 'M', 'MG', 'SD', 0),
(3168705, 'Timóteo', 'TIMOTEO', 'M', 'MG', 'SD', 0),
(3168804, 'Tiradentes', 'TIRADENTES', 'M', 'MG', 'SD', 0),
(3168903, 'Tiros', 'TIROS', 'M', 'MG', 'SD', 0),
(3169000, 'Tocantins', 'TOCANTINS', 'M', 'MG', 'SD', 0),
(3169059, 'Tocos do Moji', 'TOCOS DO MOJI', 'M', 'MG', 'SD', 0),
(3169109, 'Toledo', 'TOLEDO', 'M', 'MG', 'SD', 0),
(3169208, 'Tombos', 'TOMBOS', 'M', 'MG', 'SD', 0),
(3169307, 'Três Corações', 'TRES CORACOES', 'M', 'MG', 'SD', 0),
(3169356, 'Três Marias', 'TRES MARIAS', 'M', 'MG', 'SD', 0),
(3169406, 'Três Pontas', 'TRES PONTAS', 'M', 'MG', 'SD', 0),
(3169505, 'Tumiritinga', 'TUMIRITINGA', 'M', 'MG', 'SD', 0),
(3169604, 'Tupaciguara', 'TUPACIGUARA', 'M', 'MG', 'SD', 0),
(3169703, 'Turmalina', 'TURMALINA', 'M', 'MG', 'SD', 0),
(3169802, 'Turvolandia', 'TURVOLANDIA', 'M', 'MG', 'SD', 0),
(3169901, 'Ubá', 'UBA', 'M', 'MG', 'SD', 0),
(3170008, 'Ubaí', 'UBAI', 'M', 'MG', 'SD', 0),
(3170057, 'Ubaporanga', 'UBAPORANGA', 'M', 'MG', 'SD', 0),
(3170107, 'Uberaba', 'UBERABA', 'M', 'MG', 'SD', 0),
(3170206, 'Uberlândia', 'UBERLANDIA', 'M', 'MG', 'SD', 0),
(3170305, 'Umburatiba', 'UMBURATIBA', 'M', 'MG', 'SD', 0),
(3170404, 'Unaí', 'UNAI', 'M', 'MG', 'SD', 0),
(3170438, 'União de Minas', 'UNIAO DE MINAS', 'M', 'MG', 'SD', 0),
(3170479, 'Uruana de Minas', 'URUANA DE MINAS', 'M', 'MG', 'SD', 0),
(3170503, 'Urucânia', 'URUCANIA', 'M', 'MG', 'SD', 0),
(3170529, 'Urucuia', 'URUCUIA', 'M', 'MG', 'SD', 0),
(3170578, 'Vargem Alegre', 'VARGEM ALEGRE', 'M', 'MG', 'SD', 0),
(3170602, 'Vargem Bonita', 'VARGEM BONITA', 'M', 'MG', 'SD', 0),
(3170651, 'Vargem Grande do Rio Pardo', 'VARGEM GRANDE DO RIO PARDO', 'M', 'MG', 'SD', 0),
(3170701, 'Varginha', 'VARGINHA', 'M', 'MG', 'SD', 0),
(3170750, 'Varjão de Minas', 'VARJAO DE MINAS', 'M', 'MG', 'SD', 0),
(3170800, 'Várzea da Palma', 'VARZEA DA PALMA', 'M', 'MG', 'SD', 0),
(3170909, 'Varzelândia', 'VARZELANDIA', 'M', 'MG', 'SD', 0),
(3171006, 'Vazante', 'VAZANTE', 'M', 'MG', 'SD', 0),
(3171030, 'Verdelândia', 'VERDELANDIA', 'M', 'MG', 'SD', 0),
(3171071, 'Veredinha', 'VEREDINHA', 'M', 'MG', 'SD', 0),
(3171105, 'Veríssimo', 'VERISSIMO', 'M', 'MG', 'SD', 0),
(3171154, 'Vermelho Novo', 'VERMELHO NOVO', 'M', 'MG', 'SD', 0),
(3171204, 'Vespasiano', 'VESPASIANO', 'M', 'MG', 'SD', 0),
(3171303, 'Viçosa', 'VICOSA', 'M', 'MG', 'SD', 0),
(3171402, 'Vieiras', 'VIEIRAS', 'M', 'MG', 'SD', 0),
(3171501, 'Mathias Lobato', 'MATHIAS LOBATO', 'M', 'MG', 'SD', 0),
(3171600, 'Virgem da Lapa', 'VIRGEM DA LAPA', 'M', 'MG', 'SD', 0),
(3171709, 'Virgínia', 'VIRGINIA', 'M', 'MG', 'SD', 0),
(3171808, 'Virginópolis', 'VIRGINOPOLIS', 'M', 'MG', 'SD', 0),
(3171907, 'Virgolândia', 'VIRGOLANDIA', 'M', 'MG', 'SD', 0),
(3172004, 'Visconde do Rio Branco', 'VISCONDE DO RIO BRANCO', 'M', 'MG', 'SD', 0),
(3172103, 'Volta Grande', 'VOLTA GRANDE', 'M', 'MG', 'SD', 0),
(3172202, 'Wenceslau Braz', 'WENCESLAU BRAZ', 'M', 'MG', 'SD', 0),
(3200000, 'Espírito Santo', 'ESPIRITO SANTO', 'U', 'ES', 'SD', 0),
(3200102, 'Afonso Cláudio', 'AFONSO CLAUDIO', 'M', 'ES', 'SD', 0),
(3200136, 'Águia Branca', 'AGUIA BRANCA', 'M', 'ES', 'SD', 0),
(3200169, 'Água Doce do Norte', 'AGUA DOCE DO NORTE', 'M', 'ES', 'SD', 0),
(3200201, 'Alegre', 'ALEGRE', 'M', 'ES', 'SD', 0),
(3200300, 'Alfredo Chaves', 'ALFREDO CHAVES', 'M', 'ES', 'SD', 0),
(3200359, 'Alto Rio Novo', 'ALTO RIO NOVO', 'M', 'ES', 'SD', 0),
(3200409, 'Anchieta', 'ANCHIETA', 'M', 'ES', 'SD', 0),
(3200508, 'Apiacá', 'APIACA', 'M', 'ES', 'SD', 0),
(3200607, 'Aracruz', 'ARACRUZ', 'M', 'ES', 'SD', 0),
(3200706, 'Atilio Vivacqua', 'ATILIO VIVACQUA', 'M', 'ES', 'SD', 0),
(3200805, 'Baixo Guandu', 'BAIXO GUANDU', 'M', 'ES', 'SD', 0),
(3200904, 'Barra de São Francisco', 'BARRA DE SAO FRANCISCO', 'M', 'ES', 'SD', 0),
(3201001, 'Boa Esperanca', 'BOA ESPERANCA', 'M', 'ES', 'SD', 0),
(3201100, 'Bom Jesus do Norte', 'BOM JESUS DO NORTE', 'M', 'ES', 'SD', 0),
(3201159, 'Brejetuba', 'BREJETUBA', 'M', 'ES', 'SD', 0),
(3201209, 'Cachoeiro de Itapemirim', 'CACHOEIRO DE ITAPEMIRIM', 'M', 'ES', 'SD', 0),
(3201308, 'Cariacica', 'CARIACICA', 'M', 'ES', 'SD', 0),
(3201407, 'Castelo', 'CASTELO', 'M', 'ES', 'SD', 0),
(3201506, 'Colatina', 'COLATINA', 'M', 'ES', 'SD', 0),
(3201605, 'Conceicao da Barra', 'CONCEICAO DA BARRA', 'M', 'ES', 'SD', 0),
(3201704, 'Conceicao do Castelo', 'CONCEICAO DO CASTELO', 'M', 'ES', 'SD', 0),
(3201803, 'Divino de São Lourenço', 'DIVINO DE SAO LOURENCO', 'M', 'ES', 'SD', 0),
(3201902, 'Domingos Martins', 'DOMINGOS MARTINS', 'M', 'ES', 'SD', 0),
(3202009, 'Dores do Rio Preto', 'DORES DO RIO PRETO', 'M', 'ES', 'SD', 0),
(3202108, 'Ecoporanga', 'ECOPORANGA', 'M', 'ES', 'SD', 0),
(3202207, 'Fundão', 'FUNDAO', 'M', 'ES', 'SD', 0),
(3202256, 'Governador Lindenberg', 'GOVERNADOR LINDENBERG', 'M', 'ES', 'SD', 0),
(3202306, 'Guaçuí', 'GUACUI', 'M', 'ES', 'SD', 0),
(3202405, 'Guarapari', 'GUARAPARI', 'M', 'ES', 'SD', 0),
(3202454, 'Ibatiba', 'IBATIBA', 'M', 'ES', 'SD', 0),
(3202504, 'Ibiraçu', 'IBIRACU', 'M', 'ES', 'SD', 0),
(3202553, 'Ibitirama', 'IBITIRAMA', 'M', 'ES', 'SD', 0),
(3202603, 'Iconha', 'ICONHA', 'M', 'ES', 'SD', 0),
(3202652, 'Irupi', 'IRUPI', 'M', 'ES', 'SD', 0),
(3202702, 'Itaguaçu', 'ITAGUACU', 'M', 'ES', 'SD', 0),
(3202801, 'Itapemirim', 'ITAPEMIRIM', 'M', 'ES', 'SD', 0),
(3202900, 'Itarana', 'ITARANA', 'M', 'ES', 'SD', 0),
(3203007, 'Iúna', 'IUNA', 'M', 'ES', 'SD', 0),
(3203056, 'Jaguaré', 'JAGUARE', 'M', 'ES', 'SD', 0),
(3203106, 'Jerônimo Monteiro', 'JERONIMO MONTEIRO', 'M', 'ES', 'SD', 0),
(3203130, 'João Neiva', 'JOAO NEIVA', 'M', 'ES', 'SD', 0),
(3203163, 'Laranja da Terra', 'LARANJA DA TERRA', 'M', 'ES', 'SD', 0),
(3203205, 'Linhares', 'LINHARES', 'M', 'ES', 'SD', 0),
(3203304, 'Mantenópolis', 'MANTENOPOLIS', 'M', 'ES', 'SD', 0),
(3203320, 'Marataízes', 'MARATAIZES', 'M', 'ES', 'SD', 0),
(3203346, 'Marechal Floriano', 'MARECHAL FLORIANO', 'M', 'ES', 'SD', 0),
(3203353, 'Marilândia', 'MARILANDIA', 'M', 'ES', 'SD', 0),
(3203403, 'Mimoso do Sul', 'MIMOSO DO SUL', 'M', 'ES', 'SD', 0),
(3203502, 'Montanha', 'MONTANHA', 'M', 'ES', 'SD', 0),
(3203601, 'Mucurici', 'MUCURICI', 'M', 'ES', 'SD', 0),
(3203700, 'Muniz Freire', 'MUNIZ FREIRE', 'M', 'ES', 'SD', 0),
(3203809, 'Muqui', 'MUQUI', 'M', 'ES', 'SD', 0),
(3203908, 'Nova Venécia', 'NOVA VENECIA', 'M', 'ES', 'SD', 0),
(3204005, 'Pancas', 'PANCAS', 'M', 'ES', 'SD', 0),
(3204054, 'Pedro Canário', 'PEDRO CANARIO', 'M', 'ES', 'SD', 0),
(3204104, 'Pinheiros', 'PINHEIROS', 'M', 'ES', 'SD', 0),
(3204203, 'Piúma', 'PIUMA', 'M', 'ES', 'SD', 0),
(3204252, 'Ponto Belo', 'PONTO BELO', 'M', 'ES', 'SD', 0),
(3204302, 'Presidente Kennedy', 'PRESIDENTE KENNEDY', 'M', 'ES', 'SD', 0),
(3204351, 'Rio Bananal', 'RIO BANANAL', 'M', 'ES', 'SD', 0),
(3204401, 'Rio Novo do Sul', 'RIO NOVO DO SUL', 'M', 'ES', 'SD', 0),
(3204500, 'Santa Leopoldina', 'SANTA LEOPOLDINA', 'M', 'ES', 'SD', 0),
(3204559, 'Santa Maria de Jetibá', 'SANTA MARIA DE JETIBA', 'M', 'ES', 'SD', 0),
(3204609, 'Santa Teresa', 'SANTA TERESA', 'M', 'ES', 'SD', 0),
(3204658, 'São Domingos do Norte', 'SAO DOMINGOS DO NORTE', 'M', 'ES', 'SD', 0),
(3204708, 'São Gabriel da Palha', 'SAO GABRIEL DA PALHA', 'M', 'ES', 'SD', 0),
(3204807, 'São José do Calçado', 'SAO JOSE DO CALCADO', 'M', 'ES', 'SD', 0),
(3204906, 'São Mateus', 'SAO MATEUS', 'M', 'ES', 'SD', 0),
(3204955, 'São Roque do Canaã', 'SAO ROQUE DO CANAA', 'M', 'ES', 'SD', 0),
(3205002, 'Serra', 'SERRA', 'M', 'ES', 'SD', 0),
(3205010, 'Sooretama', 'SOORETAMA', 'M', 'ES', 'SD', 0),
(3205036, 'Vargem Alta', 'VARGEM ALTA', 'M', 'ES', 'SD', 0),
(3205069, 'Venda Nova do Imigrante', 'VENDA NOVA DO IMIGRANTE', 'M', 'ES', 'SD', 0),
(3205101, 'Viana', 'VIANA', 'M', 'ES', 'SD', 0),
(3205150, 'Vila Pavão', 'VILA PAVAO', 'M', 'ES', 'SD', 0),
(3205176, 'Vila Valério', 'VILA VALERIO', 'M', 'ES', 'SD', 0),
(3205200, 'Vila Velha', 'VILA VELHA', 'M', 'ES', 'SD', 0),
(3205309, 'Vitória', 'VITORIA', 'M', 'ES', 'SD', 0),
(3300000, 'Rio de Janeiro', 'RIO DE JANEIRO', 'U', 'RJ', 'SD', 0),
(3300100, 'Angra dos Reis', 'ANGRA DOS REIS', 'M', 'RJ', 'SD', 0),
(3300159, 'Aperibé', 'APERIBE', 'M', 'RJ', 'SD', 0),
(3300209, 'Araruama', 'ARARUAMA', 'M', 'RJ', 'SD', 0),
(3300225, 'Areal', 'AREAL', 'M', 'RJ', 'SD', 0),
(3300233, 'Armacao de Búzios', 'ARMACAO DE BUZIOS', 'M', 'RJ', 'SD', 0),
(3300258, 'Arraial do Cabo', 'ARRAIAL DO CABO', 'M', 'RJ', 'SD', 0),
(3300308, 'Barra do Piraí', 'BARRA DO PIRAI', 'M', 'RJ', 'SD', 0),
(3300407, 'Barra Mansa', 'BARRA MANSA', 'M', 'RJ', 'SD', 0),
(3300456, 'Belford Roxo', 'BELFORD ROXO', 'M', 'RJ', 'SD', 0),
(3300506, 'Bom Jardim', 'BOM JARDIM', 'M', 'RJ', 'SD', 0),
(3300605, 'Bom Jesus do Itabapoana', 'BOM JESUS DO ITABAPOANA', 'M', 'RJ', 'SD', 0),
(3300704, 'Cabo Frio', 'CABO FRIO', 'M', 'RJ', 'SD', 0),
(3300803, 'Cachoeiras de Macacu', 'CACHOEIRAS DE MACACU', 'M', 'RJ', 'SD', 0),
(3300902, 'Cambuci', 'CAMBUCI', 'M', 'RJ', 'SD', 0),
(3300936, 'Carapebus', 'CARAPEBUS', 'M', 'RJ', 'SD', 0),
(3300951, 'Comendador Levy Gasparian', 'COMENDADOR LEVY GASPARIAN', 'M', 'RJ', 'SD', 0),
(3301009, 'Campos dos Goytacazes', 'CAMPOS DOS GOYTACAZES', 'M', 'RJ', 'SD', 0),
(3301108, 'Cantagalo', 'CANTAGALO', 'M', 'RJ', 'SD', 0),
(3301157, 'Cardoso Moreira', 'CARDOSO MOREIRA', 'M', 'RJ', 'SD', 0),
(3301207, 'Carmo', 'CARMO', 'M', 'RJ', 'SD', 0),
(3301306, 'Casimiro de Abreu', 'CASIMIRO DE ABREU', 'M', 'RJ', 'SD', 0),
(3301405, 'Conceicao de Macabu', 'CONCEICAO DE MACABU', 'M', 'RJ', 'SD', 0),
(3301504, 'Cordeiro', 'CORDEIRO', 'M', 'RJ', 'SD', 0),
(3301603, 'Duas Barras', 'DUAS BARRAS', 'M', 'RJ', 'SD', 0),
(3301702, 'Duque de Caxias', 'DUQUE DE CAXIAS', 'M', 'RJ', 'SD', 0),
(3301801, 'Engenheiro Paulo de Frontin', 'ENGENHEIRO PAULO DE FRONTIN', 'M', 'RJ', 'SD', 0),
(3301850, 'Guapimirim', 'GUAPIMIRIM', 'M', 'RJ', 'SD', 0),
(3301876, 'Iguaba Grande', 'IGUABA GRANDE', 'M', 'RJ', 'SD', 0),
(3301900, 'Itaboraí', 'ITABORAI', 'M', 'RJ', 'SD', 0),
(3302007, 'Itaguaí', 'ITAGUAI', 'M', 'RJ', 'SD', 0),
(3302056, 'Italva', 'ITALVA', 'M', 'RJ', 'SD', 0),
(3302106, 'Itaocara', 'ITAOCARA', 'M', 'RJ', 'SD', 0),
(3302205, 'Itaperuna', 'ITAPERUNA', 'M', 'RJ', 'SD', 0),
(3302254, 'Itatiaia', 'ITATIAIA', 'M', 'RJ', 'SD', 0),
(3302270, 'Japeri', 'JAPERI', 'M', 'RJ', 'SD', 0),
(3302304, 'Laje do Muriaé', 'LAJE DO MURIAE', 'M', 'RJ', 'SD', 0),
(3302403, 'Macaé', 'MACAE', 'M', 'RJ', 'SD', 0),
(3302452, 'Macuco', 'MACUCO', 'M', 'RJ', 'SD', 0),
(3302502, 'Magé', 'MAGE', 'M', 'RJ', 'SD', 0),
(3302601, 'Mangaratiba', 'MANGARATIBA', 'M', 'RJ', 'SD', 0),
(3302700, 'Maricá', 'MARICA', 'M', 'RJ', 'SD', 0),
(3302809, 'Mendes', 'MENDES', 'M', 'RJ', 'SD', 0),
(3302858, 'Mesquita', 'MESQUITA', 'M', 'RJ', 'SD', 0),
(3302908, 'Miguel Pereira', 'MIGUEL PEREIRA', 'M', 'RJ', 'SD', 0),
(3303005, 'Miracema', 'MIRACEMA', 'M', 'RJ', 'SD', 0),
(3303104, 'Natividade', 'NATIVIDADE', 'M', 'RJ', 'SD', 0),
(3303203, 'Nilópolis', 'NILOPOLIS', 'M', 'RJ', 'SD', 0),
(3303302, 'Niterói', 'NITEROI', 'M', 'RJ', 'SD', 0),
(3303401, 'Nova Friburgo', 'NOVA FRIBURGO', 'M', 'RJ', 'SD', 0),
(3303500, 'Nova Iguaçu', 'NOVA IGUACU', 'M', 'RJ', 'SD', 0),
(3303609, 'Paracambi', 'PARACAMBI', 'M', 'RJ', 'SD', 0),
(3303708, 'Paraíba do Sul', 'PARAIBA DO SUL', 'M', 'RJ', 'SD', 0),
(3303807, 'Parati', 'PARATI', 'M', 'RJ', 'SD', 0),
(3303856, 'Paty do Alferes', 'PATY DO ALFERES', 'M', 'RJ', 'SD', 0),
(3303906, 'Petrópolis', 'PETROPOLIS', 'M', 'RJ', 'SD', 0),
(3303955, 'Pinheiral', 'PINHEIRAL', 'M', 'RJ', 'SD', 0),
(3304003, 'Piraí', 'PIRAI', 'M', 'RJ', 'SD', 0),
(3304102, 'Porciúncula', 'PORCIUNCULA', 'M', 'RJ', 'SD', 0),
(3304110, 'Porto Real', 'PORTO REAL', 'M', 'RJ', 'SD', 0),
(3304128, 'Quatis', 'QUATIS', 'M', 'RJ', 'SD', 0),
(3304144, 'Queimados', 'QUEIMADOS', 'M', 'RJ', 'SD', 0),
(3304151, 'Quissama', 'QUISSAMA', 'M', 'RJ', 'SD', 0),
(3304201, 'Resende', 'RESENDE', 'M', 'RJ', 'SD', 0),
(3304300, 'Rio Bonito', 'RIO BONITO', 'M', 'RJ', 'SD', 0),
(3304409, 'Rio Claro', 'RIO CLARO', 'M', 'RJ', 'SD', 0),
(3304508, 'Rio das Flores', 'RIO DAS FLORES', 'M', 'RJ', 'SD', 0),
(3304524, 'Rio das Ostras', 'RIO DAS OSTRAS', 'M', 'RJ', 'SD', 0),
(3304557, 'Rio de Janeiro', 'RIO DE JANEIRO', 'M', 'RJ', 'SD', 0),
(3304607, 'Santa Maria Madalena', 'SANTA MARIA MADALENA', 'M', 'RJ', 'SD', 0),
(3304706, 'Santo Antônio de Padua', 'SANTO ANTONIO DE PADUA', 'M', 'RJ', 'SD', 0),
(3304755, 'São Francisco de Itabapoana', 'SAO FRANCISCO DE ITABAPOANA', 'M', 'RJ', 'SD', 0),
(3304805, 'São Fidélis', 'SAO FIDELIS', 'M', 'RJ', 'SD', 0),
(3304904, 'São Gonçalo', 'SAO GONCALO', 'M', 'RJ', 'SD', 0),
(3305000, 'São João da Barra', 'SAO JOAO DA BARRA', 'M', 'RJ', 'SD', 0),
(3305109, 'São João de Meriti', 'SAO JOAO DE MERITI', 'M', 'RJ', 'SD', 0),
(3305133, 'São José de Ubá', 'SAO JOSE DE UBA', 'M', 'RJ', 'SD', 0),
(3305158, 'São José do Vale do Rio Preto', 'SAO JOSE DO VALE DO RIO PRETO', 'M', 'RJ', 'SD', 0),
(3305208, 'São Pedro da Aldeia', 'SAO PEDRO DA ALDEIA', 'M', 'RJ', 'SD', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(3305307, 'São Sebastião do Alto', 'SAO SEBASTIAO DO ALTO', 'M', 'RJ', 'SD', 0),
(3305406, 'Sapucaia', 'SAPUCAIA', 'M', 'RJ', 'SD', 0),
(3305505, 'Saquarema', 'SAQUAREMA', 'M', 'RJ', 'SD', 0),
(3305554, 'Seropédica', 'SEROPEDICA', 'M', 'RJ', 'SD', 0),
(3305604, 'Silva Jardim', 'SILVA JARDIM', 'M', 'RJ', 'SD', 0),
(3305703, 'Sumidouro', 'SUMIDOURO', 'M', 'RJ', 'SD', 0),
(3305752, 'Tanguá', 'TANGUA', 'M', 'RJ', 'SD', 0),
(3305802, 'Teresópolis', 'TERESOPOLIS', 'M', 'RJ', 'SD', 0),
(3305901, 'Trajano de Morais', 'TRAJANO DE MORAIS', 'M', 'RJ', 'SD', 0),
(3306008, 'Três Rios', 'TRES RIOS', 'M', 'RJ', 'SD', 0),
(3306107, 'Valença', 'VALENCA', 'M', 'RJ', 'SD', 0),
(3306156, 'Varre-Sai', 'VARRE-SAI', 'M', 'RJ', 'SD', 0),
(3306206, 'Vassouras', 'VASSOURAS', 'M', 'RJ', 'SD', 0),
(3306305, 'Volta Redonda', 'VOLTA REDONDA', 'M', 'RJ', 'SD', 0),
(3500000, 'São Paulo', 'SAO PAULO', 'U', 'SP', 'SD', 0),
(3500105, 'Adamantina', 'ADAMANTINA', 'M', 'SP', 'SD', 0),
(3500204, 'Adolfo', 'ADOLFO', 'M', 'SP', 'SD', 0),
(3500303, 'Aguaí', 'AGUAI', 'M', 'SP', 'SD', 0),
(3500402, 'Aguas da Prata', 'AGUAS DA PRATA', 'M', 'SP', 'SD', 0),
(3500501, 'Aguas de Lindóia', 'AGUAS DE LINDOIA', 'M', 'SP', 'SD', 0),
(3500550, 'Aguas de Santa Bárbara', 'AGUAS DE SANTA BARBARA', 'M', 'SP', 'SD', 0),
(3500600, 'Aguas de São Pedro', 'AGUAS DE SAO PEDRO', 'M', 'SP', 'SD', 0),
(3500709, 'Agudos', 'AGUDOS', 'M', 'SP', 'SD', 0),
(3500758, 'Alambari', 'ALAMBARI', 'M', 'SP', 'SD', 0),
(3500808, 'Alfredo Marcondes', 'ALFREDO MARCONDES', 'M', 'SP', 'SD', 0),
(3500907, 'Altair', 'ALTAIR', 'M', 'SP', 'SD', 0),
(3501004, 'Altinópolis', 'ALTINOPOLIS', 'M', 'SP', 'SD', 0),
(3501103, 'Alto Alegre', 'ALTO ALEGRE', 'M', 'SP', 'SD', 0),
(3501152, 'Alumínio', 'ALUMINIO', 'M', 'SP', 'SD', 0),
(3501202, 'Álvares Florence', 'ALVARES FLORENCE', 'M', 'SP', 'SD', 0),
(3501301, 'Álvares Machado', 'ALVARES MACHADO', 'M', 'SP', 'SD', 0),
(3501400, 'Álvaro de Carvalho', 'ALVARO DE CARVALHO', 'M', 'SP', 'SD', 0),
(3501509, 'Alvinlândia', 'ALVINLANDIA', 'M', 'SP', 'SD', 0),
(3501608, 'Americana', 'AMERICANA', 'M', 'SP', 'SD', 0),
(3501707, 'Américo Brasiliense', 'AMERICO BRASILIENSE', 'M', 'SP', 'SD', 0),
(3501806, 'Américo de Campos', 'AMERICO DE CAMPOS', 'M', 'SP', 'SD', 0),
(3501905, 'Amparo', 'AMPARO', 'M', 'SP', 'SD', 0),
(3502002, 'Analândia', 'ANALANDIA', 'M', 'SP', 'SD', 0),
(3502101, 'Andradina', 'ANDRADINA', 'M', 'SP', 'SD', 0),
(3502200, 'Angatuba', 'ANGATUBA', 'M', 'SP', 'SD', 0),
(3502309, 'Anhembi', 'ANHEMBI', 'M', 'SP', 'SD', 0),
(3502408, 'Anhumas', 'ANHUMAS', 'M', 'SP', 'SD', 0),
(3502507, 'Aparecida', 'APARECIDA', 'M', 'SP', 'SD', 0),
(3502606, 'Aparecida D''oeste', 'APARECIDA D''OESTE', 'M', 'SP', 'SD', 0),
(3502705, 'Apiaí', 'APIAI', 'M', 'SP', 'SD', 0),
(3502754, 'Aracariguama', 'ARACARIGUAMA', 'M', 'SP', 'SD', 0),
(3502804, 'Aracatuba', 'ARACATUBA', 'M', 'SP', 'SD', 0),
(3502903, 'Aracoiaba da Serra', 'ARACOIABA DA SERRA', 'M', 'SP', 'SD', 0),
(3503000, 'Aramina', 'ARAMINA', 'M', 'SP', 'SD', 0),
(3503109, 'Arandu', 'ARANDU', 'M', 'SP', 'SD', 0),
(3503158, 'Arapeí', 'ARAPEI', 'M', 'SP', 'SD', 0),
(3503208, 'Araraquara', 'ARARAQUARA', 'M', 'SP', 'SD', 0),
(3503307, 'Araras', 'ARARAS', 'M', 'SP', 'SD', 0),
(3503356, 'Arco-Íris', 'ARCO-IRIS', 'M', 'SP', 'SD', 0),
(3503406, 'Arealva', 'AREALVA', 'M', 'SP', 'SD', 0),
(3503505, 'Areias', 'AREIAS', 'M', 'SP', 'SD', 0),
(3503604, 'Areiópolis', 'AREIOPOLIS', 'M', 'SP', 'SD', 0),
(3503703, 'Ariranha', 'ARIRANHA', 'M', 'SP', 'SD', 0),
(3503802, 'Artur Nogueira', 'ARTUR NOGUEIRA', 'M', 'SP', 'SD', 0),
(3503901, 'Arujá', 'ARUJA', 'M', 'SP', 'SD', 0),
(3503950, 'Aspásia', 'ASPASIA', 'M', 'SP', 'SD', 0),
(3504008, 'Assis', 'ASSIS', 'M', 'SP', 'SD', 0),
(3504107, 'Atibaia', 'ATIBAIA', 'M', 'SP', 'SD', 0),
(3504206, 'Auriflama', 'AURIFLAMA', 'M', 'SP', 'SD', 0),
(3504305, 'Avaí', 'AVAI', 'M', 'SP', 'SD', 0),
(3504404, 'Avanhandava', 'AVANHANDAVA', 'M', 'SP', 'SD', 0),
(3504503, 'Avaré', 'AVARE', 'M', 'SP', 'SD', 0),
(3504602, 'Bady Bassitt', 'BADY BASSITT', 'M', 'SP', 'SD', 0),
(3504701, 'Balbinos', 'BALBINOS', 'M', 'SP', 'SD', 0),
(3504800, 'Bálsamo', 'BALSAMO', 'M', 'SP', 'SD', 0),
(3504909, 'Bananal', 'BANANAL', 'M', 'SP', 'SD', 0),
(3505005, 'Barão de Antonina', 'BARAO DE ANTONINA', 'M', 'SP', 'SD', 0),
(3505104, 'Barbosa', 'BARBOSA', 'M', 'SP', 'SD', 0),
(3505203, 'Bariri', 'BARIRI', 'M', 'SP', 'SD', 0),
(3505302, 'Barra Bonita', 'BARRA BONITA', 'M', 'SP', 'SD', 0),
(3505351, 'Barra do Chapéu', 'BARRA DO CHAPEU', 'M', 'SP', 'SD', 0),
(3505401, 'Barra do Turvo', 'BARRA DO TURVO', 'M', 'SP', 'SD', 0),
(3505500, 'Barretos', 'BARRETOS', 'M', 'SP', 'SD', 0),
(3505609, 'Barrinha', 'BARRINHA', 'M', 'SP', 'SD', 0),
(3505708, 'Barueri', 'BARUERI', 'M', 'SP', 'SD', 0),
(3505807, 'Bastos', 'BASTOS', 'M', 'SP', 'SD', 0),
(3505906, 'Batatais', 'BATATAIS', 'M', 'SP', 'SD', 0),
(3506003, 'Bauru', 'BAURU', 'M', 'SP', 'SD', 0),
(3506102, 'Bebedouro', 'BEBEDOURO', 'M', 'SP', 'SD', 0),
(3506201, 'Bento de Abreu', 'BENTO DE ABREU', 'M', 'SP', 'SD', 0),
(3506300, 'Bernardino de Campos', 'BERNARDINO DE CAMPOS', 'M', 'SP', 'SD', 0),
(3506359, 'Bertioga', 'BERTIOGA', 'M', 'SP', 'SD', 0),
(3506409, 'Bilac', 'BILAC', 'M', 'SP', 'SD', 0),
(3506508, 'Birigui', 'BIRIGUI', 'M', 'SP', 'SD', 0),
(3506607, 'Biritiba-Mirim', 'BIRITIBA-MIRIM', 'M', 'SP', 'SD', 0),
(3506706, 'Boa Esperança do Sul', 'BOA ESPERANCA DO SUL', 'M', 'SP', 'SD', 0),
(3506805, 'Bocaina', 'BOCAINA', 'M', 'SP', 'SD', 0),
(3506904, 'Bofete', 'BOFETE', 'M', 'SP', 'SD', 0),
(3507001, 'Boituva', 'BOITUVA', 'M', 'SP', 'SD', 0),
(3507100, 'Bom Jesus dos Perdoes', 'BOM JESUS DOS PERDOES', 'M', 'SP', 'SD', 0),
(3507159, 'Bom Sucesso de Itararé', 'BOM SUCESSO DE ITARARE', 'M', 'SP', 'SD', 0),
(3507209, 'Borá', 'BORA', 'M', 'SP', 'SD', 0),
(3507308, 'Boracéia', 'BORACEIA', 'M', 'SP', 'SD', 0),
(3507407, 'Borborema', 'BORBOREMA', 'M', 'SP', 'SD', 0),
(3507456, 'Borebi', 'BOREBI', 'M', 'SP', 'SD', 0),
(3507506, 'Botucatu', 'BOTUCATU', 'M', 'SP', 'SD', 0),
(3507605, 'Braganca Paulista', 'BRAGANCA PAULISTA', 'M', 'SP', 'SD', 0),
(3507704, 'Braúna', 'BRAUNA', 'M', 'SP', 'SD', 0),
(3507753, 'Brejo Alegre', 'BREJO ALEGRE', 'M', 'SP', 'SD', 0),
(3507803, 'Brodósqui', 'BRODOWSKI', 'M', 'SP', 'SD', 0),
(3507902, 'Brotas', 'BROTAS', 'M', 'SP', 'SD', 0),
(3508009, 'Buri', 'BURI', 'M', 'SP', 'SD', 0),
(3508108, 'Buritama', 'BURITAMA', 'M', 'SP', 'SD', 0),
(3508207, 'Buritizal', 'BURITIZAL', 'M', 'SP', 'SD', 0),
(3508306, 'Cabrália Paulista', 'CABRALIA PAULISTA', 'M', 'SP', 'SD', 0),
(3508405, 'Cabreúva', 'CABREUVA', 'M', 'SP', 'SD', 0),
(3508504, 'Caçapava', 'CACAPAVA', 'M', 'SP', 'SD', 0),
(3508603, 'Cachoeira Paulista', 'CACHOEIRA PAULISTA', 'M', 'SP', 'SD', 0),
(3508702, 'Caconde', 'CACONDE', 'M', 'SP', 'SD', 0),
(3508801, 'Cafelândia', 'CAFELANDIA', 'M', 'SP', 'SD', 0),
(3508900, 'Caiabu', 'CAIABU', 'M', 'SP', 'SD', 0),
(3509007, 'Caieiras', 'CAIEIRAS', 'M', 'SP', 'SD', 0),
(3509106, 'Caiuá', 'CAIUA', 'M', 'SP', 'SD', 0),
(3509205, 'Cajamar', 'CAJAMAR', 'M', 'SP', 'SD', 0),
(3509254, 'Cajati', 'CAJATI', 'M', 'SP', 'SD', 0),
(3509304, 'Cajobi', 'CAJOBI', 'M', 'SP', 'SD', 0),
(3509403, 'Cajuru', 'CAJURU', 'M', 'SP', 'SD', 0),
(3509452, 'Campina do Monte Alegre', 'CAMPINA DO MONTE ALEGRE', 'M', 'SP', 'SD', 0),
(3509502, 'Campinas', 'CAMPINAS', 'M', 'SP', 'SD', 0),
(3509601, 'Campo Limpo Paulista', 'CAMPO LIMPO PAULISTA', 'M', 'SP', 'SD', 0),
(3509700, 'Campos do Jordão', 'CAMPOS DO JORDAO', 'M', 'SP', 'SD', 0),
(3509809, 'Campos Novos Paulista', 'CAMPOS NOVOS PAULISTA', 'M', 'SP', 'SD', 0),
(3509908, 'Cananéia', 'CANANEIA', 'M', 'SP', 'SD', 0),
(3509957, 'Canas', 'CANAS', 'M', 'SP', 'SD', 0),
(3510005, 'Cândido Mota', 'CANDIDO MOTA', 'M', 'SP', 'SD', 0),
(3510104, 'Cândido Rodrigues', 'CANDIDO RODRIGUES', 'M', 'SP', 'SD', 0),
(3510153, 'Canitar', 'CANITAR', 'M', 'SP', 'SD', 0),
(3510203, 'Capão Bonito', 'CAPAO BONITO', 'M', 'SP', 'SD', 0),
(3510302, 'Capela do Alto', 'CAPELA DO ALTO', 'M', 'SP', 'SD', 0),
(3510401, 'Capivari', 'CAPIVARI', 'M', 'SP', 'SD', 0),
(3510500, 'Caraguatatuba', 'CARAGUATATUBA', 'M', 'SP', 'SD', 0),
(3510609, 'Carapicuiíba', 'CARAPICUIBA', 'M', 'SP', 'SD', 0),
(3510708, 'Cardoso', 'CARDOSO', 'M', 'SP', 'SD', 0),
(3510807, 'Casa Branca', 'CASA BRANCA', 'M', 'SP', 'SD', 0),
(3510906, 'Cássia dos Coqueiros', 'CASSIA DOS COQUEIROS', 'M', 'SP', 'SD', 0),
(3511003, 'Castilho', 'CASTILHO', 'M', 'SP', 'SD', 0),
(3511102, 'Catanduva', 'CATANDUVA', 'M', 'SP', 'SD', 0),
(3511201, 'Catiguá', 'CATIGUA', 'M', 'SP', 'SD', 0),
(3511300, 'Cedral', 'CEDRAL', 'M', 'SP', 'SD', 0),
(3511409, 'Cerqueira César', 'CERQUEIRA CESAR', 'M', 'SP', 'SD', 0),
(3511508, 'Cerquilho', 'CERQUILHO', 'M', 'SP', 'SD', 0),
(3511607, 'Cesario Lange', 'CESARIO LANGE', 'M', 'SP', 'SD', 0),
(3511706, 'Charqueada', 'CHARQUEADA', 'M', 'SP', 'SD', 0),
(3511904, 'Clementina', 'CLEMENTINA', 'M', 'SP', 'SD', 0),
(3512001, 'Colina', 'COLINA', 'M', 'SP', 'SD', 0),
(3512100, 'Colômbia', 'COLOMBIA', 'M', 'SP', 'SD', 0),
(3512209, 'Conchal', 'CONCHAL', 'M', 'SP', 'SD', 0),
(3512308, 'Conchas', 'CONCHAS', 'M', 'SP', 'SD', 0),
(3512407, 'Cordeirópolis', 'CORDEIROPOLIS', 'M', 'SP', 'SD', 0),
(3512506, 'Coroados', 'COROADOS', 'M', 'SP', 'SD', 0),
(3512605, 'Coronel Macedo', 'CORONEL MACEDO', 'M', 'SP', 'SD', 0),
(3512704, 'Corumbataí', 'CORUMBATAI', 'M', 'SP', 'SD', 0),
(3512803, 'Cosmópolis', 'COSMOPOLIS', 'M', 'SP', 'SD', 0),
(3512902, 'Cosmorama', 'COSMORAMA', 'M', 'SP', 'SD', 0),
(3513009, 'Cotia', 'COTIA', 'M', 'SP', 'SD', 0),
(3513108, 'Cravinhos', 'CRAVINHOS', 'M', 'SP', 'SD', 0),
(3513207, 'Cristais Paulista', 'CRISTAIS PAULISTA', 'M', 'SP', 'SD', 0),
(3513306, 'Cruzália', 'CRUZALIA', 'M', 'SP', 'SD', 0),
(3513405, 'Cruzeiro', 'CRUZEIRO', 'M', 'SP', 'SD', 0),
(3513504, 'Cubatão', 'CUBATAO', 'M', 'SP', 'SD', 0),
(3513603, 'Cunha', 'CUNHA', 'M', 'SP', 'SD', 0),
(3513702, 'Descalvado', 'DESCALVADO', 'M', 'SP', 'SD', 0),
(3513801, 'Diadema', 'DIADEMA', 'M', 'SP', 'SD', 0),
(3513850, 'Dirce Reis', 'DIRCE REIS', 'M', 'SP', 'SD', 0),
(3513900, 'Divinolândia', 'DIVINOLANDIA', 'M', 'SP', 'SD', 0),
(3514007, 'Dobrada', 'DOBRADA', 'M', 'SP', 'SD', 0),
(3514106, 'Dois Córregos', 'DOIS CORREGOS', 'M', 'SP', 'SD', 0),
(3514205, 'Dolcinópolis', 'DOLCINOPOLIS', 'M', 'SP', 'SD', 0),
(3514304, 'Dourado', 'DOURADO', 'M', 'SP', 'SD', 0),
(3514403, 'Dracena', 'DRACENA', 'M', 'SP', 'SD', 0),
(3514502, 'Duartina', 'DUARTINA', 'M', 'SP', 'SD', 0),
(3514601, 'Dumont', 'DUMONT', 'M', 'SP', 'SD', 0),
(3514700, 'Echaporã', 'ECHAPORA', 'M', 'SP', 'SD', 0),
(3514809, 'Eldorado', 'ELDORADO', 'M', 'SP', 'SD', 0),
(3514908, 'Elias Fausto', 'ELIAS FAUSTO', 'M', 'SP', 'SD', 0),
(3514924, 'Elisiário', 'ELISIARIO', 'M', 'SP', 'SD', 0),
(3514957, 'Embaúba', 'EMBAUBA', 'M', 'SP', 'SD', 0),
(3515004, 'Embu', 'EMBU', 'M', 'SP', 'SD', 0),
(3515103, 'Embu-Guaçu', 'EMBU-GUACU', 'M', 'SP', 'SD', 0),
(3515129, 'Emilianópolis', 'EMILIANOPOLIS', 'M', 'SP', 'SD', 0),
(3515152, 'Engenheiro Coelho', 'ENGENHEIRO COELHO', 'M', 'SP', 'SD', 0),
(3515186, 'Espírito Santo do Pinhal', 'ESPIRITO SANTO DO PINHAL', 'M', 'SP', 'SD', 0),
(3515194, 'Espírito Santo do Turvo', 'ESPIRITO SANTO DO TURVO', 'M', 'SP', 'SD', 0),
(3515202, 'Estrela D''Oeste', 'ESTRELA D''OESTE', 'M', 'SP', 'SD', 0),
(3515301, 'Estrela do Norte', 'ESTRELA DO NORTE', 'M', 'SP', 'SD', 0),
(3515350, 'Euclides da Cunha Paulista', 'EUCLIDES DA CUNHA PAULISTA', 'M', 'SP', 'SD', 0),
(3515400, 'Fartura', 'FARTURA', 'M', 'SP', 'SD', 0),
(3515509, 'Fernandópolis', 'FERNANDOPOLIS', 'M', 'SP', 'SD', 0),
(3515608, 'Fernando Prestes', 'FERNANDO PRESTES', 'M', 'SP', 'SD', 0),
(3515657, 'Fernão', 'FERNAO', 'M', 'SP', 'SD', 0),
(3515707, 'Ferraz de Vasconcelos', 'FERRAZ DE VASCONCELOS', 'M', 'SP', 'SD', 0),
(3515806, 'Flora Rica', 'FLORA RICA', 'M', 'SP', 'SD', 0),
(3515905, 'Floreal', 'FLOREAL', 'M', 'SP', 'SD', 0),
(3516002, 'Flórida Paulista', 'FLORIDA PAULISTA', 'M', 'SP', 'SD', 0),
(3516101, 'Florínia', 'FLORINIA', 'M', 'SP', 'SD', 0),
(3516200, 'Franca', 'FRANCA', 'M', 'SP', 'SD', 0),
(3516309, 'Francisco Morato', 'FRANCISCO MORATO', 'M', 'SP', 'SD', 0),
(3516408, 'Franco da Rocha', 'FRANCO DA ROCHA', 'M', 'SP', 'SD', 0),
(3516507, 'Gabriel Monteiro', 'GABRIEL MONTEIRO', 'M', 'SP', 'SD', 0),
(3516606, 'Gália', 'GALIA', 'M', 'SP', 'SD', 0),
(3516705, 'Garça', 'GARCA', 'M', 'SP', 'SD', 0),
(3516804, 'Gastão Vidigal', 'GASTAO VIDIGAL', 'M', 'SP', 'SD', 0),
(3516853, 'Gavião Peixoto', 'GAVIAO PEIXOTO', 'M', 'SP', 'SD', 0),
(3516903, 'General Salgado', 'GENERAL SALGADO', 'M', 'SP', 'SD', 0),
(3517000, 'Getulina', 'GETULINA', 'M', 'SP', 'SD', 0),
(3517109, 'Glicério', 'GLICERIO', 'M', 'SP', 'SD', 0),
(3517208, 'Guaiçara', 'GUAICARA', 'M', 'SP', 'SD', 0),
(3517307, 'Guaimbê', 'GUAIMBE', 'M', 'SP', 'SD', 0),
(3517406, 'Guaíra', 'GUAIRA', 'M', 'SP', 'SD', 0),
(3517505, 'Guapiaçu', 'GUAPIACU', 'M', 'SP', 'SD', 0),
(3517604, 'Guapiara', 'GUAPIARA', 'M', 'SP', 'SD', 0),
(3517703, 'Guará', 'GUARA', 'M', 'SP', 'SD', 0),
(3517802, 'Guaraca', 'GUARACAI', 'M', 'SP', 'SD', 0),
(3517901, 'Guaraçaí', 'GUARACI', 'M', 'SP', 'SD', 0),
(3518008, 'Guarani D''Oeste', 'GUARANI D''OESTE', 'M', 'SP', 'SD', 0),
(3518107, 'Guarantã', 'GUARANTA', 'M', 'SP', 'SD', 0),
(3518206, 'Guararapes', 'GUARARAPES', 'M', 'SP', 'SD', 0),
(3518305, 'Guararema', 'GUARAREMA', 'M', 'SP', 'SD', 0),
(3518404, 'Guaratinguetá', 'GUARATINGUETA', 'M', 'SP', 'SD', 0),
(3518503, 'Guareí', 'GUAREI', 'M', 'SP', 'SD', 0),
(3518602, 'Guariba', 'GUARIBA', 'M', 'SP', 'SD', 0),
(3518701, 'Guarujá', 'GUARUJA', 'M', 'SP', 'SD', 0),
(3518800, 'Guarulhos', 'GUARULHOS', 'M', 'SP', 'SD', 0),
(3518859, 'Guatapará', 'GUATAPARA', 'M', 'SP', 'SD', 0),
(3518909, 'Guzolândia', 'GUZOLANDIA', 'M', 'SP', 'SD', 0),
(3519006, 'Herculândia', 'HERCULANDIA', 'M', 'SP', 'SD', 0),
(3519055, 'Holambra', 'HOLAMBRA', 'M', 'SP', 'SD', 0),
(3519071, 'Hortolandia', 'HORTOLANDIA', 'M', 'SP', 'SD', 0),
(3519105, 'Iacanga', 'IACANGA', 'M', 'SP', 'SD', 0),
(3519204, 'Iacri', 'IACRI', 'M', 'SP', 'SD', 0),
(3519253, 'Iaras', 'IARAS', 'M', 'SP', 'SD', 0),
(3519303, 'Ibaté', 'IBATE', 'M', 'SP', 'SD', 0),
(3519402, 'Ibirá', 'IBIRA', 'M', 'SP', 'SD', 0),
(3519501, 'Ibirarema', 'IBIRAREMA', 'M', 'SP', 'SD', 0),
(3519600, 'Ibitinga', 'IBITINGA', 'M', 'SP', 'SD', 0),
(3519709, 'Ibiúna', 'IBIUNA', 'M', 'SP', 'SD', 0),
(3519808, 'Icém', 'ICEM', 'M', 'SP', 'SD', 0),
(3519907, 'Iepê', 'IEPE', 'M', 'SP', 'SD', 0),
(3520004, 'Igaraçu do Tietê', 'IGARACU DO TIETE', 'M', 'SP', 'SD', 0),
(3520103, 'Igarapava', 'IGARAPAVA', 'M', 'SP', 'SD', 0),
(3520202, 'Igaratá', 'IGARATA', 'M', 'SP', 'SD', 0),
(3520301, 'Iguape', 'IGUAPE', 'M', 'SP', 'SD', 0),
(3520400, 'Ilhabela', 'ILHABELA', 'M', 'SP', 'SD', 0),
(3520426, 'Ilha Comprida', 'ILHA COMPRIDA', 'M', 'SP', 'SD', 0),
(3520442, 'Ilha Solteira', 'ILHA SOLTEIRA', 'M', 'SP', 'SD', 0),
(3520509, 'Indaiatuba', 'INDAIATUBA', 'M', 'SP', 'SD', 0),
(3520608, 'Indiana', 'INDIANA', 'M', 'SP', 'SD', 0),
(3520707, 'Indiaporã', 'INDIAPORA', 'M', 'SP', 'SD', 0),
(3520806, 'Inúbia Paulista', 'INUBIA PAULISTA', 'M', 'SP', 'SD', 0),
(3520905, 'Ipauçu', 'IPAUCU', 'M', 'SP', 'SD', 0),
(3521002, 'Iperó', 'IPERO', 'M', 'SP', 'SD', 0),
(3521101, 'Ipeúna', 'IPEUNA', 'M', 'SP', 'SD', 0),
(3521150, 'Ipiguá', 'IPIGUA', 'M', 'SP', 'SD', 0),
(3521200, 'Iporanga', 'IPORANGA', 'M', 'SP', 'SD', 0),
(3521309, 'Ipuã', 'IPUA', 'M', 'SP', 'SD', 0),
(3521408, 'Iracemápolis', 'IRACEMAPOLIS', 'M', 'SP', 'SD', 0),
(3521507, 'Irapuã', 'IRAPUA', 'M', 'SP', 'SD', 0),
(3521606, 'Irapuru', 'IRAPURU', 'M', 'SP', 'SD', 0),
(3521705, 'Itaberá', 'ITABERA', 'M', 'SP', 'SD', 0),
(3521804, 'Itaí', 'ITAI', 'M', 'SP', 'SD', 0),
(3521903, 'Itajobi', 'ITAJOBI', 'M', 'SP', 'SD', 0),
(3522000, 'Itaju', 'ITAJU', 'M', 'SP', 'SD', 0),
(3522109, 'Itanhaém', 'ITANHAEM', 'M', 'SP', 'SD', 0),
(3522158, 'Itaóca', 'ITAOCA', 'M', 'SP', 'SD', 0),
(3522208, 'Itapecerica da Serra', 'ITAPECERICA DA SERRA', 'M', 'SP', 'SD', 0),
(3522307, 'Itapetininga', 'ITAPETININGA', 'M', 'SP', 'SD', 0),
(3522406, 'Itapeva', 'ITAPEVA', 'M', 'SP', 'SD', 0),
(3522505, 'Itapevi', 'ITAPEVI', 'M', 'SP', 'SD', 0),
(3522604, 'Itapira', 'ITAPIRA', 'M', 'SP', 'SD', 0),
(3522653, 'Itapirapuã Paulista', 'ITAPIRAPUA PAULISTA', 'M', 'SP', 'SD', 0),
(3522703, 'Itápolis', 'ITAPOLIS', 'M', 'SP', 'SD', 0),
(3522802, 'Itaporanga', 'ITAPORANGA', 'M', 'SP', 'SD', 0),
(3522901, 'Itapuí', 'ITAPUI', 'M', 'SP', 'SD', 0),
(3523008, 'Itapura', 'ITAPURA', 'M', 'SP', 'SD', 0),
(3523107, 'Itaquaquecetuba', 'ITAQUAQUECETUBA', 'M', 'SP', 'SD', 0),
(3523206, 'Itararé', 'ITARARE', 'M', 'SP', 'SD', 0),
(3523305, 'Itariri', 'ITARIRI', 'M', 'SP', 'SD', 0),
(3523404, 'Itatiba', 'ITATIBA', 'M', 'SP', 'SD', 0),
(3523503, 'Itatinga', 'ITATINGA', 'M', 'SP', 'SD', 0),
(3523602, 'Itirapina', 'ITIRAPINA', 'M', 'SP', 'SD', 0),
(3523701, 'Itirapuã', 'ITIRAPUA', 'M', 'SP', 'SD', 0),
(3523800, 'Itobi', 'ITOBI', 'M', 'SP', 'SD', 0),
(3523909, 'Itu', 'ITU', 'M', 'SP', 'SD', 0),
(3524006, 'Itupeva', 'ITUPEVA', 'M', 'SP', 'SD', 0),
(3524105, 'Ituverava', 'ITUVERAVA', 'M', 'SP', 'SD', 0),
(3524204, 'Jaborandi', 'JABORANDI', 'M', 'SP', 'SD', 0),
(3524303, 'Jaboticabal', 'JABOTICABAL', 'M', 'SP', 'SD', 0),
(3524402, 'Jacareí', 'JACAREI', 'M', 'SP', 'SD', 0),
(3524501, 'Jaci', 'JACI', 'M', 'SP', 'SD', 0),
(3524600, 'Jacupiranga', 'JACUPIRANGA', 'M', 'SP', 'SD', 0),
(3524709, 'Jaguariúna', 'JAGUARIUNA', 'M', 'SP', 'SD', 0),
(3524808, 'Jales', 'JALES', 'M', 'SP', 'SD', 0),
(3524907, 'Jambeiro', 'JAMBEIRO', 'M', 'SP', 'SD', 0),
(3525003, 'Jandira', 'JANDIRA', 'M', 'SP', 'SD', 0),
(3525102, 'Jardinópolis', 'JARDINOPOLIS', 'M', 'SP', 'SD', 0),
(3525201, 'Jarinu', 'JARINU', 'M', 'SP', 'SD', 0),
(3525300, 'Jaú', 'JAU', 'M', 'SP', 'SD', 0),
(3525409, 'Jeriquara', 'JERIQUARA', 'M', 'SP', 'SD', 0),
(3525508, 'Joanópolis', 'JOANOPOLIS', 'M', 'SP', 'SD', 0),
(3525607, 'João Ramalho', 'JOAO RAMALHO', 'M', 'SP', 'SD', 0),
(3525706, 'José Bonifácio', 'JOSE BONIFACIO', 'M', 'SP', 'SD', 0),
(3525805, 'Juúlio Mesquita', 'JULIO MESQUITA', 'M', 'SP', 'SD', 0),
(3525854, 'Jumirim', 'JUMIRIM', 'M', 'SP', 'SD', 0),
(3525904, 'Jundiaí', 'JUNDIAI', 'M', 'SP', 'SD', 0),
(3526001, 'Junqueirópolis', 'JUNQUEIROPOLIS', 'M', 'SP', 'SD', 0),
(3526100, 'Juquiá', 'JUQUIA', 'M', 'SP', 'SD', 0),
(3526209, 'Juquitiba', 'JUQUITIBA', 'M', 'SP', 'SD', 0),
(3526308, 'Lagoinha', 'LAGOINHA', 'M', 'SP', 'SD', 0),
(3526407, 'Laranjal Paulista', 'LARANJAL PAULISTA', 'M', 'SP', 'SD', 0),
(3526506, 'Lavínia', 'LAVINIA', 'M', 'SP', 'SD', 0),
(3526605, 'Lavrinhas', 'LAVRINHAS', 'M', 'SP', 'SD', 0),
(3526704, 'Leme', 'LEME', 'M', 'SP', 'SD', 0),
(3526803, 'Lençóis Paulista', 'LENCOIS PAULISTA', 'M', 'SP', 'SD', 0),
(3526902, 'Limeira', 'LIMEIRA', 'M', 'SP', 'SD', 0),
(3527009, 'Lindóia', 'LINDOIA', 'M', 'SP', 'SD', 0),
(3527108, 'Lins', 'LINS', 'M', 'SP', 'SD', 0),
(3527207, 'Lorena', 'LORENA', 'M', 'SP', 'SD', 0),
(3527256, 'Lourdes', 'LOURDES', 'M', 'SP', 'SD', 0),
(3527306, 'Louveira', 'LOUVEIRA', 'M', 'SP', 'SD', 0),
(3527405, 'Lucélia', 'LUCELIA', 'M', 'SP', 'SD', 0),
(3527504, 'Lucianópolis', 'LUCIANOPOLIS', 'M', 'SP', 'SD', 0),
(3527603, 'Luis Antônio', 'LUIS ANTONIO', 'M', 'SP', 'SD', 0),
(3527702, 'Luiziânia', 'LUIZIANIA', 'M', 'SP', 'SD', 0),
(3527801, 'Lupércio', 'LUPERCIO', 'M', 'SP', 'SD', 0),
(3527900, 'Lutécia', 'LUTECIA', 'M', 'SP', 'SD', 0),
(3528007, 'Macatuba', 'MACATUBA', 'M', 'SP', 'SD', 0),
(3528106, 'Macaubal', 'MACAUBAL', 'M', 'SP', 'SD', 0),
(3528205, 'Macedônia', 'MACEDONIA', 'M', 'SP', 'SD', 0),
(3528304, 'Magda', 'MAGDA', 'M', 'SP', 'SD', 0),
(3528403, 'Mairinque', 'MAIRINQUE', 'M', 'SP', 'SD', 0),
(3528502, 'Mairipora', 'MAIRIPORA', 'M', 'SP', 'SD', 0),
(3528601, 'Manduri', 'MANDURI', 'M', 'SP', 'SD', 0),
(3528700, 'Maraba Paulista', 'MARABA PAULISTA', 'M', 'SP', 'SD', 0),
(3528809, 'Maracai', 'MARACAI', 'M', 'SP', 'SD', 0),
(3528858, 'Marapoama', 'MARAPOAMA', 'M', 'SP', 'SD', 0),
(3528908, 'Mariápolis', 'MARIAPOLIS', 'M', 'SP', 'SD', 0),
(3529005, 'Marília', 'MARILIA', 'M', 'SP', 'SD', 0),
(3529104, 'Marinópolis', 'MARINOPOLIS', 'M', 'SP', 'SD', 0),
(3529203, 'Martinópolis', 'MARTINOPOLIS', 'M', 'SP', 'SD', 0),
(3529302, 'Matão', 'MATAO', 'M', 'SP', 'SD', 0),
(3529401, 'Mauá', 'MAUA', 'M', 'SP', 'SD', 0),
(3529500, 'Mendonça', 'MENDONCA', 'M', 'SP', 'SD', 0),
(3529609, 'Meridiano', 'MERIDIANO', 'M', 'SP', 'SD', 0),
(3529658, 'Mesópolis', 'MESOPOLIS', 'M', 'SP', 'SD', 0),
(3529708, 'Miguelópolis', 'MIGUELOPOLIS', 'M', 'SP', 'SD', 0),
(3529807, 'Mineiros do Tietê', 'MINEIROS DO TIETE', 'M', 'SP', 'SD', 0),
(3529906, 'Miracatu', 'MIRACATU', 'M', 'SP', 'SD', 0),
(3530003, 'Mira Estrela', 'MIRA ESTRELA', 'M', 'SP', 'SD', 0),
(3530102, 'Mirandópolis', 'MIRANDOPOLIS', 'M', 'SP', 'SD', 0),
(3530201, 'Mirante do Paranapanema', 'MIRANTE DO PARANAPANEMA', 'M', 'SP', 'SD', 0),
(3530300, 'Mirassol', 'MIRASSOL', 'M', 'SP', 'SD', 0),
(3530409, 'Mirassolândia', 'MIRASSOLANDIA', 'M', 'SP', 'SD', 0),
(3530508, 'Mococa', 'MOCOCA', 'M', 'SP', 'SD', 0),
(3530607, 'Mogi das Cruzes', 'MOGI DAS CRUZES', 'M', 'SP', 'SD', 0),
(3530706, 'Mogi Guacu', 'MOGI GUACU', 'M', 'SP', 'SD', 0),
(3530805, 'Moji-Mirim', 'MOJI-MIRIM', 'M', 'SP', 'SD', 0),
(3530904, 'Mombuca', 'MOMBUCA', 'M', 'SP', 'SD', 0),
(3531001, 'Monções', 'MONCOES', 'M', 'SP', 'SD', 0),
(3531100, 'Mongaguá', 'MONGAGUA', 'M', 'SP', 'SD', 0),
(3531209, 'Monte Alegre do Sul', 'MONTE ALEGRE DO SUL', 'M', 'SP', 'SD', 0),
(3531308, 'Monte Alto', 'MONTE ALTO', 'M', 'SP', 'SD', 0),
(3531407, 'Monte Aprazível', 'MONTE APRAZIVEL', 'M', 'SP', 'SD', 0),
(3531506, 'Monte Azul Paulista', 'MONTE AZUL PAULISTA', 'M', 'SP', 'SD', 0),
(3531605, 'Monte Castelo', 'MONTE CASTELO', 'M', 'SP', 'SD', 0),
(3531704, 'Monteiro Lobato', 'MONTEIRO LOBATO', 'M', 'SP', 'SD', 0),
(3531803, 'Monte Mor', 'MONTE MOR', 'M', 'SP', 'SD', 0),
(3531902, 'Morro Agudo', 'MORRO AGUDO', 'M', 'SP', 'SD', 0),
(3532009, 'Morungaba', 'MORUNGABA', 'M', 'SP', 'SD', 0),
(3532058, 'Motuca', 'MOTUCA', 'M', 'SP', 'SD', 0),
(3532108, 'Murutinga do Sul', 'MURUTINGA DO SUL', 'M', 'SP', 'SD', 0),
(3532157, 'Nantes', 'NANTES', 'M', 'SP', 'SD', 0),
(3532207, 'Narandiba', 'NARANDIBA', 'M', 'SP', 'SD', 0),
(3532306, 'Natividade da Serra', 'NATIVIDADE DA SERRA', 'M', 'SP', 'SD', 0),
(3532405, 'Nazaré Paulista', 'NAZARE PAULISTA', 'M', 'SP', 'SD', 0),
(3532504, 'Neves Paulista', 'NEVES PAULISTA', 'M', 'SP', 'SD', 0),
(3532603, 'Nhandeara', 'NHANDEARA', 'M', 'SP', 'SD', 0),
(3532702, 'Nipoã', 'NIPOA', 'M', 'SP', 'SD', 0),
(3532801, 'Nova Aliança', 'NOVA ALIANCA', 'M', 'SP', 'SD', 0),
(3532827, 'Nova Campina', 'NOVA CAMPINA', 'M', 'SP', 'SE', 0),
(3532843, 'Nova Canaã Paulista', 'NOVA CANAA PAULISTA', 'M', 'SP', 'SD', 0),
(3532868, 'Nova Castilho', 'NOVA CASTILHO', 'M', 'SP', 'SD', 0),
(3532900, 'Nova Europa', 'NOVA EUROPA', 'M', 'SP', 'SD', 0),
(3533007, 'Nova Granada', 'NOVA GRANADA', 'M', 'SP', 'SD', 0),
(3533106, 'Nova Guataporanga', 'NOVA GUATAPORANGA', 'M', 'SP', 'SD', 0),
(3533205, 'Nova Independência', 'NOVA INDEPENDENCIA', 'M', 'SP', 'SD', 0),
(3533254, 'Novais', 'NOVAIS', 'M', 'SP', 'SD', 0),
(3533304, 'Nova Luzitânia', 'NOVA LUZITANIA', 'M', 'SP', 'SD', 0),
(3533403, 'Nova Odessa', 'NOVA ODESSA', 'M', 'SP', 'SD', 0),
(3533502, 'Novo Horizonte', 'NOVO HORIZONTE', 'M', 'SP', 'SD', 0),
(3533601, 'Nuporanga', 'NUPORANGA', 'M', 'SP', 'SD', 0),
(3533700, 'Ocauçu', 'OCAUCU', 'M', 'SP', 'SD', 0),
(3533809, 'Óleo', 'OLEO', 'M', 'SP', 'SD', 0),
(3533908, 'Olímpia', 'OLIMPIA', 'M', 'SP', 'SD', 0),
(3534005, 'Onda Verde', 'ONDA VERDE', 'M', 'SP', 'SD', 0),
(3534104, 'Oriente', 'ORIENTE', 'M', 'SP', 'SD', 0),
(3534203, 'Orindiuva', 'ORINDIUVA', 'M', 'SP', 'SD', 0),
(3534302, 'Orlândia', 'ORLANDIA', 'M', 'SP', 'SD', 0),
(3534401, 'Osasco', 'OSASCO', 'M', 'SP', 'SD', 0),
(3534500, 'Oscar Bressane', 'OSCAR BRESSANE', 'M', 'SP', 'SD', 0),
(3534609, 'Osvaldo Cruz', 'OSVALDO CRUZ', 'M', 'SP', 'SD', 0),
(3534708, 'Ourinhos', 'OURINHOS', 'M', 'SP', 'SD', 0),
(3534757, 'Ouroeste', 'OUROESTE', 'M', 'SP', 'SD', 0),
(3534807, 'Ouro Verde', 'OURO VERDE', 'M', 'SP', 'SD', 0),
(3534906, 'Pacaembu', 'PACAEMBU', 'M', 'SP', 'SD', 0),
(3535002, 'Palestina', 'PALESTINA', 'M', 'SP', 'SD', 0),
(3535101, 'Palmares Paulista', 'PALMARES PAULISTA', 'M', 'SP', 'SD', 0),
(3535200, 'Palmeira D''Oeste', 'PALMEIRA D''OESTE', 'M', 'SP', 'SD', 0),
(3535309, 'Palmital', 'PALMITAL', 'M', 'SP', 'SD', 0),
(3535408, 'Panorama', 'PANORAMA', 'M', 'SP', 'SD', 0),
(3535507, 'Paraguaçu Paulista', 'PARAGUACU PAULISTA', 'M', 'SP', 'SD', 0),
(3535606, 'Paraibuna', 'PARAIBUNA', 'M', 'SP', 'SD', 0),
(3535705, 'Paraíso', 'PARAISO', 'M', 'SP', 'SD', 0),
(3535804, 'Paranapanema', 'PARANAPANEMA', 'M', 'SP', 'SD', 0),
(3535903, 'Paranapuã', 'PARANAPUA', 'M', 'SP', 'SD', 0),
(3536000, 'Parapuã', 'PARAPUA', 'M', 'SP', 'SD', 0),
(3536109, 'Pardinho', 'PARDINHO', 'M', 'SP', 'SD', 0),
(3536208, 'Pariquera-Açu', 'PARIQUERA-ACU', 'M', 'SP', 'SD', 0),
(3536257, 'Parisi', 'PARISI', 'M', 'SP', 'SD', 0),
(3536307, 'Patrocinio Paulista', 'PATROCINIO PAULISTA', 'M', 'SP', 'SD', 0),
(3536406, 'Pauliceia', 'PAULICEIA', 'M', 'SP', 'SD', 0),
(3536505, 'Paulínia', 'PAULINIA', 'M', 'SP', 'SD', 0),
(3536570, 'Paulistânia', 'PAULISTANIA', 'M', 'SP', 'SD', 0),
(3536604, 'Paulo de Faria', 'PAULO DE FARIA', 'M', 'SP', 'SD', 0),
(3536703, 'Pederneiras', 'PEDERNEIRAS', 'M', 'SP', 'SD', 0),
(3536802, 'Pedra Bela', 'PEDRA BELA', 'M', 'SP', 'SD', 0),
(3536901, 'Pedranópolis', 'PEDRANOPOLIS', 'M', 'SP', 'SD', 0),
(3537008, 'Pedregulho', 'PEDREGULHO', 'M', 'SP', 'SD', 0),
(3537107, 'Pedreira', 'PEDREIRA', 'M', 'SP', 'SD', 0),
(3537156, 'Pedrinhas Paulista', 'PEDRINHAS PAULISTA', 'M', 'SP', 'SD', 0),
(3537206, 'Pedro de Toledo', 'PEDRO DE TOLEDO', 'M', 'SP', 'SD', 0),
(3537305, 'Penápolis', 'PENAPOLIS', 'M', 'SP', 'SD', 0),
(3537404, 'Pereira Barreto', 'PEREIRA BARRETO', 'M', 'SP', 'SD', 0),
(3537503, 'Pereiras', 'PEREIRAS', 'M', 'SP', 'SD', 0),
(3537602, 'Peruíbe', 'PERUIBE', 'M', 'SP', 'SD', 0),
(3537701, 'Piacatu', 'PIACATU', 'M', 'SP', 'SD', 0),
(3537800, 'Piedade', 'PIEDADE', 'M', 'SP', 'SD', 0),
(3537909, 'Pilar do Sul', 'PILAR DO SUL', 'M', 'SP', 'SD', 0),
(3538006, 'Pindamonhangaba', 'PINDAMONHANGABA', 'M', 'SP', 'SD', 0),
(3538105, 'Pindorama', 'PINDORAMA', 'M', 'SP', 'SD', 0),
(3538204, 'Pinhalzinho', 'PINHALZINHO', 'M', 'SP', 'SD', 0),
(3538303, 'Piquerobi', 'PIQUEROBI', 'M', 'SP', 'SD', 0),
(3538501, 'Piquete', 'PIQUETE', 'M', 'SP', 'SD', 0),
(3538600, 'Piracaia', 'PIRACAIA', 'M', 'SP', 'SD', 0),
(3538709, 'Piracicaba', 'PIRACICABA', 'M', 'SP', 'SD', 0),
(3538808, 'Piraju', 'PIRAJU', 'M', 'SP', 'SD', 0),
(3538907, 'Pirajuí', 'PIRAJUI', 'M', 'SP', 'SD', 0),
(3539004, 'Pirangi', 'PIRANGI', 'M', 'SP', 'SD', 0),
(3539103, 'Pirapora do Bom Jesus', 'PIRAPORA DO BOM JESUS', 'M', 'SP', 'SD', 0),
(3539202, 'Pirapozinho', 'PIRAPOZINHO', 'M', 'SP', 'SD', 0),
(3539301, 'Pirassununga', 'PIRASSUNUNGA', 'M', 'SP', 'SD', 0),
(3539400, 'Piratininga', 'PIRATININGA', 'M', 'SP', 'SD', 0),
(3539509, 'Pitangueiras', 'PITANGUEIRAS', 'M', 'SP', 'SD', 0),
(3539608, 'Planalto', 'PLANALTO', 'M', 'SP', 'SD', 0),
(3539707, 'Platina', 'PLATINA', 'M', 'SP', 'SD', 0),
(3539806, 'Poá', 'POA', 'M', 'SP', 'SD', 0),
(3539905, 'Poloni', 'POLONI', 'M', 'SP', 'SD', 0),
(3540002, 'Pompéia', 'POMPEIA', 'M', 'SP', 'SD', 0),
(3540101, 'Pongaí', 'PONGAI', 'M', 'SP', 'SD', 0),
(3540200, 'Pontal', 'PONTAL', 'M', 'SP', 'SD', 0),
(3540259, 'Pontalinda', 'PONTALINDA', 'M', 'SP', 'SD', 0),
(3540309, 'Pontes Gestal', 'PONTES GESTAL', 'M', 'SP', 'SD', 0),
(3540408, 'Populina', 'POPULINA', 'M', 'SP', 'SD', 0),
(3540507, 'Porangaba', 'PORANGABA', 'M', 'SP', 'SD', 0),
(3540606, 'Porto Feliz', 'PORTO FELIZ', 'M', 'SP', 'SD', 0),
(3540705, 'Porto Ferreira', 'PORTO FERREIRA', 'M', 'SP', 'SD', 0),
(3540754, 'Potim', 'POTIM', 'M', 'SP', 'SD', 0),
(3540804, 'Potirendaba', 'POTIRENDABA', 'M', 'SP', 'SD', 0),
(3540853, 'Pracinha', 'PRACINHA', 'M', 'SP', 'SD', 0),
(3540903, 'Pradópolis', 'PRADOPOLIS', 'M', 'SP', 'SD', 0),
(3541000, 'Praia Grande', 'PRAIA GRANDE', 'M', 'SP', 'SD', 0),
(3541059, 'Pratânia', 'PRATANIA', 'M', 'SP', 'SD', 0),
(3541109, 'Presidente Alves', 'PRESIDENTE ALVES', 'M', 'SP', 'SD', 0),
(3541208, 'Presidente Bernardes', 'PRESIDENTE BERNARDES', 'M', 'SP', 'SD', 0),
(3541307, 'Presidente Epitácio', 'PRESIDENTE EPITACIO', 'M', 'SP', 'SD', 0),
(3541406, 'Presidente Prudente', 'PRESIDENTE PRUDENTE', 'M', 'SP', 'SD', 0),
(3541505, 'Presidente Venceslau', 'PRESIDENTE VENCESLAU', 'M', 'SP', 'SD', 0),
(3541604, 'Promissão', 'PROMISSAO', 'M', 'SP', 'SD', 0),
(3541653, 'Quadra', 'QUADRA', 'M', 'SP', 'SD', 0),
(3541703, 'Quatá', 'QUATA', 'M', 'SP', 'SD', 0),
(3541802, 'Queiroz', 'QUEIROZ', 'M', 'SP', 'SD', 0),
(3541901, 'Queluz', 'QUELUZ', 'M', 'SP', 'SD', 0),
(3542008, 'Quintana', 'QUINTANA', 'M', 'SP', 'SD', 0),
(3542107, 'Rafard', 'RAFARD', 'M', 'SP', 'SD', 0),
(3542206, 'Rancharia', 'RANCHARIA', 'M', 'SP', 'SD', 0),
(3542305, 'Redenção da Serra', 'REDENCAO DA SERRA', 'M', 'SP', 'SD', 0),
(3542404, 'Regente Feijó', 'REGENTE FEIJO', 'M', 'SP', 'SD', 0),
(3542503, 'Reginópolis', 'REGINOPOLIS', 'M', 'SP', 'SD', 0),
(3542602, 'Registro', 'REGISTRO', 'M', 'SP', 'SD', 0),
(3542701, 'Restinga', 'RESTINGA', 'M', 'SP', 'SD', 0),
(3542800, 'Ribeira', 'RIBEIRA', 'M', 'SP', 'SD', 0),
(3542909, 'Ribeirão Bonito', 'RIBEIRAO BONITO', 'M', 'SP', 'SD', 0),
(3543006, 'Ribeirão Branco', 'RIBEIRAO BRANCO', 'M', 'SP', 'SD', 0),
(3543105, 'Ribeirão Corrente', 'RIBEIRAO CORRENTE', 'M', 'SP', 'SD', 0),
(3543204, 'Ribeirão do Sul', 'RIBEIRAO DO SUL', 'M', 'SP', 'SD', 0),
(3543238, 'Ribeirão dos Índios', 'RIBEIRAO DOS INDIOS', 'M', 'SP', 'SD', 0),
(3543253, 'Ribeirão Grande', 'RIBEIRAO GRANDE', 'M', 'SP', 'SD', 0),
(3543303, 'Ribeirão Pires', 'RIBEIRAO PIRES', 'M', 'SP', 'SD', 0),
(3543402, 'Ribeirão Preto', 'RIBEIRAO PRETO', 'M', 'SP', 'SD', 0),
(3543501, 'Riversul', 'RIVERSUL', 'M', 'SP', 'SD', 0),
(3543600, 'Rifaina', 'RIFAINA', 'M', 'SP', 'SD', 0),
(3543709, 'Rinção', 'RINCAO', 'M', 'SP', 'SD', 0),
(3543808, 'Rinópolis', 'RINOPOLIS', 'M', 'SP', 'SD', 0),
(3543907, 'Rio Claro', 'RIO CLARO', 'M', 'SP', 'SD', 0),
(3544004, 'Rio das Pedras', 'RIO DAS PEDRAS', 'M', 'SP', 'SD', 0),
(3544103, 'Rio Grande da Serra', 'RIO GRANDE DA SERRA', 'M', 'SP', 'SD', 0),
(3544202, 'Riolândia', 'RIOLANDIA', 'M', 'SP', 'SD', 0),
(3544251, 'Rosana', 'ROSANA', 'M', 'SP', 'SD', 0),
(3544301, 'Roseira', 'ROSEIRA', 'M', 'SP', 'SD', 0),
(3544400, 'Rubiãcea', 'RUBIACEA', 'M', 'SP', 'SD', 0),
(3544509, 'Rubinéia', 'RUBINEIA', 'M', 'SP', 'SD', 0),
(3544608, 'Sabino', 'SABINO', 'M', 'SP', 'SD', 0),
(3544707, 'Sagres', 'SAGRES', 'M', 'SP', 'SD', 0),
(3544806, 'Sales', 'SALES', 'M', 'SP', 'SD', 0),
(3544905, 'Sales Oliveira', 'SALES OLIVEIRA', 'M', 'SP', 'SD', 0),
(3545001, 'Salesópolis', 'SALESOPOLIS', 'M', 'SP', 'SD', 0),
(3545100, 'Salmourão', 'SALMOURAO', 'M', 'SP', 'SD', 0),
(3545159, 'Saltinho', 'SALTINHO', 'M', 'SP', 'SD', 0),
(3545209, 'Salto', 'SALTO', 'M', 'SP', 'SD', 0),
(3545308, 'Salto de Pirapora', 'SALTO DE PIRAPORA', 'M', 'SP', 'SD', 0),
(3545407, 'Salto Grande', 'SALTO GRANDE', 'M', 'SP', 'SD', 0),
(3545506, 'Sandovalina', 'SANDOVALINA', 'M', 'SP', 'SD', 0),
(3545605, 'Santa Adélia', 'SANTA ADELIA', 'M', 'SP', 'SD', 0),
(3545704, 'Santa Albertina', 'SANTA ALBERTINA', 'M', 'SP', 'SD', 0),
(3545803, 'Santa Bárbara D''oeste', 'SANTA BARBARA D''OESTE', 'M', 'SP', 'SD', 0),
(3546009, 'Santa Branca', 'SANTA BRANCA', 'M', 'SP', 'SD', 0),
(3546108, 'Santa Clara D''Oeste', 'SANTA CLARA D''OESTE', 'M', 'SP', 'SD', 0),
(3546207, 'Santa Cruz da Conceição', 'SANTA CRUZ DA CONCEICAO', 'M', 'SP', 'SD', 0),
(3546256, 'Santa Cruz da Esperança', 'SANTA CRUZ DA ESPERANCA', 'M', 'SP', 'SD', 0),
(3546306, 'Santa Cruz das Palmeiras', 'SANTA CRUZ DAS PALMEIRAS', 'M', 'SP', 'SD', 0),
(3546405, 'Santa Cruz do Rio Pardo', 'SANTA CRUZ DO RIO PARDO', 'M', 'SP', 'SD', 0),
(3546504, 'Santa Ernestina', 'SANTA ERNESTINA', 'M', 'SP', 'SD', 0),
(3546603, 'Santa Fé do Sul', 'SANTA FE DO SUL', 'M', 'SP', 'SD', 0),
(3546702, 'Santa Gertrudes', 'SANTA GERTRUDES', 'M', 'SP', 'SD', 0),
(3546801, 'Santa Isabel', 'SANTA ISABEL', 'M', 'SP', 'SD', 0),
(3546900, 'Santa Lúcia', 'SANTA LUCIA', 'M', 'SP', 'SD', 0),
(3547007, 'Santa Maria da Serra', 'SANTA MARIA DA SERRA', 'M', 'SP', 'SD', 0),
(3547106, 'Santa Mercedes', 'SANTA MERCEDES', 'M', 'SP', 'SD', 0),
(3547205, 'Santana da Ponte Pensa', 'SANTANA DA PONTE PENSA', 'M', 'SP', 'SD', 0),
(3547304, 'Santana de Parnaíba', 'SANTANA DE PARNAIBA', 'M', 'SP', 'SD', 0),
(3547403, 'Santa Rita D''oeste', 'SANTA RITA D''OESTE', 'M', 'SP', 'SD', 0),
(3547502, 'Santa Rita do Passa Quatro', 'SANTA RITA DO PASSA QUATRO', 'M', 'SP', 'SD', 0),
(3547601, 'Santa Rosa de Viterbo', 'SANTA ROSA DE VITERBO', 'M', 'SP', 'SD', 0),
(3547650, 'Santa Salete', 'SANTA SALETE', 'M', 'SP', 'SD', 0),
(3547700, 'Santo Anastácio', 'SANTO ANASTACIO', 'M', 'SP', 'SD', 0),
(3547809, 'Santo Andre', 'SANTO ANDRE', 'M', 'SP', 'SD', 0),
(3547908, 'Santo Antônio da Alegria', 'SANTO ANTONIO DA ALEGRIA', 'M', 'SP', 'SD', 0),
(3548005, 'Santo Antônio de Posse', 'SANTO ANTONIO DE POSSE', 'M', 'SP', 'SD', 0),
(3548054, 'Santo Antônio do Aracanguá', 'SANTO ANTONIO DO ARACANGUA', 'M', 'SP', 'SD', 0),
(3548104, 'Santo Antônio do Jardim', 'SANTO ANTONIO DO JARDIM', 'M', 'SP', 'SD', 0),
(3548203, 'Santo Antônio do Pinhal', 'SANTO ANTONIO DO PINHAL', 'M', 'SP', 'SD', 0),
(3548302, 'Santo Expedito', 'SANTO EXPEDITO', 'M', 'SP', 'SD', 0),
(3548401, 'Santópolis do Aguapeí', 'SANTOPOLIS DO AGUAPEI', 'M', 'SP', 'SD', 0),
(3548500, 'Santos', 'SANTOS', 'M', 'SP', 'SD', 0),
(3548609, 'São Bento do Sapucaí', 'SAO BENTO DO SAPUCAI', 'M', 'SP', 'SD', 0),
(3548708, 'São Bernardo do Campo', 'SAO BERNARDO DO CAMPO', 'M', 'SP', 'SD', 0),
(3548807, 'São Caetano do Sul', 'SAO CAETANO DO SUL', 'M', 'SP', 'SD', 0),
(3548906, 'São Carlos', 'SAO CARLOS', 'M', 'SP', 'SD', 0),
(3549003, 'São Francisco', 'SAO FRANCISCO', 'M', 'SP', 'SD', 0),
(3549102, 'São João da Boa Vista', 'SAO JOAO DA BOA VISTA', 'M', 'SP', 'SD', 0),
(3549201, 'São João das Duas Pontes', 'SAO JOAO DAS DUAS PONTES', 'M', 'SP', 'SD', 0),
(3549250, 'São João de Iracema', 'SAO JOAO DE IRACEMA', 'M', 'SP', 'SD', 0),
(3549300, 'São João do Pau D''alho', 'SAO JOAO DO PAU D''ALHO', 'M', 'SP', 'SD', 0),
(3549409, 'São Joaquim da Barra', 'SAO JOAQUIM DA BARRA', 'M', 'SP', 'SD', 0),
(3549508, 'São José da Bela Vista', 'SAO JOSE DA BELA VISTA', 'M', 'SP', 'SD', 0),
(3549607, 'São José do Barreiro', 'SAO JOSE DO BARREIRO', 'M', 'SP', 'SD', 0),
(3549706, 'São Josédo Rio Pardo', 'SAO JOSE DO RIO PARDO', 'M', 'SP', 'SD', 0),
(3549805, 'São José do Rio Preto', 'SAO JOSE DO RIO PRETO', 'M', 'SP', 'SD', 0),
(3549904, 'São José dos Campos', 'SAO JOSE DOS CAMPOS', 'M', 'SP', 'SD', 0),
(3549953, 'São Lourenço da Serra', 'SAO LOURENCO DA SERRA', 'M', 'SP', 'SD', 0),
(3550001, 'São Luís do Paraitinga', 'SAO LUIS DO PARAITINGA', 'M', 'SP', 'SD', 0),
(3550100, 'São Manuel', 'SAO MANUEL', 'M', 'SP', 'SD', 0),
(3550209, 'São Miguel Arcanjo', 'SAO MIGUEL ARCANJO', 'M', 'SP', 'SD', 0),
(3550308, 'São Paulo', 'SAO PAULO', 'M', 'SP', 'SD', 0),
(3550407, 'São Pedro', 'SAO PEDRO', 'M', 'SP', 'SD', 0),
(3550506, 'São Pedro do Turvo', 'SAO PEDRO DO TURVO', 'M', 'SP', 'SD', 0),
(3550605, 'São Roque', 'SAO ROQUE', 'M', 'SP', 'SD', 0),
(3550704, 'São Sebastião', 'SAO SEBASTIAO', 'M', 'SP', 'SD', 0),
(3550803, 'São Sebastião da Grama', 'SAO SEBASTIAO DA GRAMA', 'M', 'SP', 'SD', 0),
(3550902, 'São Simão', 'SAO SIMAO', 'M', 'SP', 'SD', 0),
(3551009, 'São Vicente', 'SAO VICENTE', 'M', 'SP', 'SD', 0),
(3551108, 'Sarapui', 'SARAPUI', 'M', 'SP', 'SD', 0),
(3551207, 'Sarutaia', 'SARUTAIA', 'M', 'SP', 'SD', 0),
(3551306, 'Sebastianopolis do Sul', 'SEBASTIANOPOLIS DO SUL', 'M', 'SP', 'SD', 0),
(3551405, 'Serra Azul', 'SERRA AZUL', 'M', 'SP', 'SD', 0),
(3551504, 'Serrana', 'SERRANA', 'M', 'SP', 'SD', 0),
(3551603, 'Serra Negra', 'SERRA NEGRA', 'M', 'SP', 'SD', 0),
(3551702, 'Sertãozinho', 'SERTAOZINHO', 'M', 'SP', 'SD', 0),
(3551801, 'Sete Barras', 'SETE BARRAS', 'M', 'SP', 'SD', 0),
(3551900, 'Severínia', 'SEVERINIA', 'M', 'SP', 'SD', 0),
(3552007, 'Silveiras', 'SILVEIRAS', 'M', 'SP', 'SD', 0),
(3552106, 'Socorro', 'SOCORRO', 'M', 'SP', 'SD', 0),
(3552205, 'Sorocaba', 'SOROCABA', 'M', 'SP', 'SD', 0),
(3552304, 'Sud Menucci', 'SUD MENUCCI', 'M', 'SP', 'SD', 0),
(3552403, 'Sumaré', 'SUMARE', 'M', 'SP', 'SD', 0),
(3552502, 'Suzano', 'SUZANO', 'M', 'SP', 'SD', 0),
(3552551, 'Suzanápolis', 'SUZANAPOLIS', 'M', 'SP', 'SD', 0),
(3552601, 'Tabapuã', 'TABAPUA', 'M', 'SP', 'SD', 0),
(3552700, 'Tabatinga', 'TABATINGA', 'M', 'SP', 'SD', 0),
(3552809, 'Taboão da Serra', 'TABOAO DA SERRA', 'M', 'SP', 'SD', 0),
(3552908, 'Taciba', 'TACIBA', 'M', 'SP', 'SD', 0),
(3553005, 'Taguaí', 'TAGUAI', 'M', 'SP', 'SD', 0),
(3553104, 'Taiaçu', 'TAIACU', 'M', 'SP', 'SD', 0),
(3553203, 'Taiúva', 'TAIUVA', 'M', 'SP', 'SD', 0),
(3553302, 'Tambaú', 'TAMBAU', 'M', 'SP', 'SD', 0),
(3553401, 'Tanabi', 'TANABI', 'M', 'SP', 'SD', 0),
(3553500, 'Tapiraí', 'TAPIRAI', 'M', 'SP', 'SD', 0),
(3553609, 'Tapiratiba', 'TAPIRATIBA', 'M', 'SP', 'SD', 0),
(3553658, 'Taquaral', 'TAQUARAL', 'M', 'SP', 'SD', 0),
(3553708, 'Taquaritinga', 'TAQUARITINGA', 'M', 'SP', 'SD', 0),
(3553807, 'Taquarituba', 'TAQUARITUBA', 'M', 'SP', 'SD', 0),
(3553856, 'Taquarivaí', 'TAQUARIVAI', 'M', 'SP', 'SD', 0),
(3553906, 'Tarabai', 'TARABAI', 'M', 'SP', 'SD', 0),
(3553955, 'Taruma', 'TARUMA', 'M', 'SP', 'SD', 0),
(3554003, 'Tatuí', 'TATUI', 'M', 'SP', 'SD', 0),
(3554102, 'Taubaté', 'TAUBATE', 'M', 'SP', 'SD', 0),
(3554201, 'Tejupá', 'TEJUPA', 'M', 'SP', 'SD', 0),
(3554300, 'Teodoro Sampaio', 'TEODORO SAMPAIO', 'M', 'SP', 'SD', 0),
(3554409, 'Terra Roxa', 'TERRA ROXA', 'M', 'SP', 'SD', 0),
(3554508, 'Tietê', 'TIETE', 'M', 'SP', 'SD', 0),
(3554607, 'Timburi', 'TIMBURI', 'M', 'SP', 'SD', 0),
(3554656, 'Torre de Pedra', 'TORRE DE PEDRA', 'M', 'SP', 'SD', 0),
(3554706, 'Torrinha', 'TORRINHA', 'M', 'SP', 'SD', 0),
(3554755, 'Trabiju', 'TRABIJU', 'M', 'SP', 'SD', 0),
(3554805, 'Tremembé', 'TREMEMBE', 'M', 'SP', 'SD', 0),
(3554904, 'Três Fronteiras', 'TRES FRONTEIRAS', 'M', 'SP', 'SD', 0),
(3554953, 'Tuiuti', 'TUIUTI', 'M', 'SP', 'SD', 0),
(3555000, 'Tupã', 'TUPA', 'M', 'SP', 'SD', 0),
(3555109, 'Tupi Paulista', 'TUPI PAULISTA', 'M', 'SP', 'SD', 0),
(3555208, 'Turiúba', 'TURIUBA', 'M', 'SP', 'SD', 0),
(3555307, 'Turmalina', 'TURMALINA', 'M', 'SP', 'SD', 0),
(3555356, 'Ubarana', 'UBARANA', 'M', 'SP', 'SD', 0),
(3555406, 'Ubatuba', 'UBATUBA', 'M', 'SP', 'SD', 0),
(3555505, 'Ubirajara', 'UBIRAJARA', 'M', 'SP', 'SD', 0),
(3555604, 'Uchôa', 'UCHOA', 'M', 'SP', 'SD', 0),
(3555703, 'União Paulista', 'UNIAO PAULISTA', 'M', 'SP', 'SD', 0),
(3555802, 'Urania', 'URANIA', 'M', 'SP', 'SD', 0),
(3555901, 'Uru', 'URU', 'M', 'SP', 'SD', 0),
(3556008, 'Urupês', 'URUPES', 'M', 'SP', 'SD', 0),
(3556107, 'Valentim Gentil', 'VALENTIM GENTIL', 'M', 'SP', 'SD', 0),
(3556206, 'Valinhos', 'VALINHOS', 'M', 'SP', 'SD', 0),
(3556305, 'Valparaíso', 'VALPARAISO', 'M', 'SP', 'SD', 0),
(3556354, 'Vargem', 'VARGEM', 'M', 'SP', 'SD', 0),
(3556404, 'Vargem Grande do Sul', 'VARGEM GRANDE DO SUL', 'M', 'SP', 'SD', 0),
(3556453, 'Vargem Grande Paulista', 'VARGEM GRANDE PAULISTA', 'M', 'SP', 'SD', 0),
(3556503, 'Várzea Paulista', 'VARZEA PAULISTA', 'M', 'SP', 'SD', 0),
(3556602, 'Vera Cruz', 'VERA CRUZ', 'M', 'SP', 'SD', 0),
(3556701, 'Vinhedo', 'VINHEDO', 'M', 'SP', 'SD', 0),
(3556800, 'Viradouro', 'VIRADOURO', 'M', 'SP', 'SD', 0),
(3556909, 'Vista Alegre do Alto', 'VISTA ALEGRE DO ALTO', 'M', 'SP', 'SD', 0),
(3556958, 'Vitória Brasil', 'VITORIA BRASIL', 'M', 'SP', 'SD', 0),
(3557006, 'Votorantim', 'VOTORANTIM', 'M', 'SP', 'SD', 0),
(3557105, 'Votuporanga', 'VOTUPORANGA', 'M', 'SP', 'SD', 0),
(3557154, 'Zacarias', 'ZACARIAS', 'M', 'SP', 'SD', 0),
(3557204, 'Chavantes', 'CHAVANTES', 'M', 'SP', 'SD', 0),
(3557303, 'Estiva Gerbi', 'ESTIVA GERBI', 'M', 'SP', 'SD', 0),
(4100000, 'Paranã', 'PARANA', 'U', 'PR', 'SL', 0),
(4100103, 'Abatiá', 'ABATIA', 'M', 'PR', 'SL', 0),
(4100202, 'Adrianópolis', 'ADRIANOPOLIS', 'M', 'PR', 'SL', 0),
(4100301, 'Agudos do Sul', 'AGUDOS DO SUL', 'M', 'PR', 'SL', 0),
(4100400, 'Almirante Tamandaré', 'ALMIRANTE TAMANDARE', 'M', 'PR', 'SL', 0),
(4100459, 'Altamira do Paraná', 'ALTAMIRA DO PARANA', 'M', 'PR', 'SL', 0),
(4100509, 'Altônia', 'ALTONIA', 'M', 'PR', 'SL', 0),
(4100608, 'Alto Paraná', 'ALTO PARANA', 'M', 'PR', 'SL', 0),
(4100707, 'Alto Piquiri', 'ALTO PIQUIRI', 'M', 'PR', 'SL', 0),
(4100806, 'Alvorada do Sul', 'ALVORADA DO SUL', 'M', 'PR', 'SL', 0),
(4100905, 'Amaporã', 'AMAPORA', 'M', 'PR', 'SL', 0),
(4101002, 'Ampére', 'AMPERE', 'M', 'PR', 'SL', 0),
(4101051, 'Anahy', 'ANAHY', 'M', 'PR', 'SL', 0),
(4101101, 'Andirá', 'ANDIRA', 'M', 'PR', 'SL', 0),
(4101150, 'Ângulo', 'ANGULO', 'M', 'PR', 'SL', 0),
(4101200, 'Antonina', 'ANTONINA', 'M', 'PR', 'SL', 0),
(4101309, 'Antônio Olinto', 'ANTONIO OLINTO', 'M', 'PR', 'SL', 0),
(4101408, 'Apucarana', 'APUCARANA', 'M', 'PR', 'SL', 0),
(4101507, 'Arapongas', 'ARAPONGAS', 'M', 'PR', 'SL', 0),
(4101606, 'Arapoti', 'ARAPOTI', 'M', 'PR', 'SL', 0),
(4101655, 'Arapuá', 'ARAPUA', 'M', 'PR', 'SL', 0),
(4101705, 'Araruna', 'ARARUNA', 'M', 'PR', 'SL', 0),
(4101804, 'Araucária', 'ARAUCARIA', 'M', 'PR', 'SL', 0),
(4101853, 'Ariranha do Ivaí', 'ARIRANHA DO IVAI', 'M', 'PR', 'SL', 0),
(4101903, 'Assaí', 'ASSAI', 'M', 'PR', 'SL', 0),
(4102000, 'Assis Chateaubriand', 'ASSIS CHATEAUBRIAND', 'M', 'PR', 'SL', 0),
(4102109, 'Astorga', 'ASTORGA', 'M', 'PR', 'SL', 0),
(4102208, 'Atalaia', 'ATALAIA', 'M', 'PR', 'SL', 0),
(4102307, 'Balsa Nova', 'BALSA NOVA', 'M', 'PR', 'SL', 0),
(4102406, 'Bandeirantes', 'BANDEIRANTES', 'M', 'PR', 'SL', 0),
(4102505, 'Barbosa Ferraz', 'BARBOSA FERRAZ', 'M', 'PR', 'SL', 0),
(4102604, 'Barracão', 'BARRACAO', 'M', 'PR', 'SL', 0),
(4102703, 'Barra do Jacaré', 'BARRA DO JACARE', 'M', 'PR', 'SL', 0),
(4102752, 'Bela Vista da Caroba', 'BELA VISTA DA CAROBA', 'M', 'PR', 'SL', 0),
(4102802, 'Bela Vista do Paraíso', 'BELA VISTA DO PARAISO', 'M', 'PR', 'SL', 0),
(4102901, 'Bituruna', 'BITURUNA', 'M', 'PR', 'SL', 0),
(4103008, 'Boa Esperanca', 'BOA ESPERANCA', 'M', 'PR', 'SL', 0),
(4103024, 'Boa Esperança do Iguaçu', 'BOA ESPERANCA DO IGUACU', 'M', 'PR', 'SL', 0),
(4103040, 'Boa Ventura de São Roque', 'BOA VENTURA DE SAO ROQUE', 'M', 'PR', 'SL', 0),
(4103057, 'Boa Vista da Aparecida', 'BOA VISTA DA APARECIDA', 'M', 'PR', 'SL', 0),
(4103107, 'Bocaiúva do Sul', 'BOCAIUVA DO SUL', 'M', 'PR', 'SL', 0),
(4103156, 'Bom Jesus do Sul', 'BOM JESUS DO SUL', 'M', 'PR', 'SL', 0),
(4103206, 'Bom Sucesso', 'BOM SUCESSO', 'M', 'PR', 'SL', 0),
(4103222, 'Bom Sucesso do Sul', 'BOM SUCESSO DO SUL', 'M', 'PR', 'SL', 0),
(4103305, 'Borrazópolis', 'BORRAZOPOLIS', 'M', 'PR', 'SL', 0),
(4103354, 'Braganey', 'BRAGANEY', 'M', 'PR', 'SL', 0),
(4103370, 'Brasilândia do Sul', 'BRASILANDIA DO SUL', 'M', 'PR', 'SL', 0),
(4103404, 'Cafeara', 'CAFEARA', 'M', 'PR', 'SL', 0),
(4103453, 'Cafelândia', 'CAFELANDIA', 'M', 'PR', 'SL', 0),
(4103479, 'Cafezal do Sul', 'CAFEZAL DO SUL', 'M', 'PR', 'SL', 0),
(4103503, 'Califórnia', 'CALIFORNIA', 'M', 'PR', 'SL', 0),
(4103602, 'Cambará', 'CAMBARA', 'M', 'PR', 'SL', 0),
(4103701, 'Cambé', 'CAMBE', 'M', 'PR', 'SL', 0),
(4103800, 'Cambira', 'CAMBIRA', 'M', 'PR', 'SL', 0),
(4103909, 'Campina da Lagoa', 'CAMPINA DA LAGOA', 'M', 'PR', 'SL', 0),
(4103958, 'Campina do Simão', 'CAMPINA DO SIMAO', 'M', 'PR', 'SL', 0),
(4104006, 'Campina Grande do Sul', 'CAMPINA GRANDE DO SUL', 'M', 'PR', 'SL', 0),
(4104055, 'Campo Bonito', 'CAMPO BONITO', 'M', 'PR', 'SL', 0),
(4104105, 'Campo do Tenente', 'CAMPO DO TENENTE', 'M', 'PR', 'SL', 0),
(4104204, 'Campo Largo', 'CAMPO LARGO', 'M', 'PR', 'SL', 0),
(4104253, 'Campo Magro', 'CAMPO MAGRO', 'M', 'PR', 'SL', 0),
(4104303, 'Campo Mourão', 'CAMPO MOURAO', 'M', 'PR', 'SL', 0),
(4104402, 'Cândido de Abreu', 'CANDIDO DE ABREU', 'M', 'PR', 'SL', 0),
(4104428, 'Candói', 'CANDOI', 'M', 'PR', 'SL', 0),
(4104451, 'Cantagalo', 'CANTAGALO', 'M', 'PR', 'SL', 0),
(4104501, 'Capanema', 'CAPANEMA', 'M', 'PR', 'SL', 0),
(4104600, 'Capitão Leônidas Marques', 'CAPITAO LEONIDAS MARQUES', 'M', 'PR', 'SL', 0),
(4104659, 'Carambeí', 'CARAMBEI', 'M', 'PR', 'SL', 0),
(4104709, 'Carlópolis', 'CARLOPOLIS', 'M', 'PR', 'SL', 0),
(4104808, 'Cascavél', 'CASCAVEL', 'M', 'PR', 'SL', 0),
(4104907, 'Castro', 'CASTRO', 'M', 'PR', 'SL', 0),
(4105003, 'Catanduvas', 'CATANDUVAS', 'M', 'PR', 'SL', 0),
(4105102, 'Centenário do Sul', 'CENTENARIO DO SUL', 'M', 'PR', 'SL', 0),
(4105201, 'Cerro Azul', 'CERRO AZUL', 'M', 'PR', 'SL', 0),
(4105300, 'Céu Azul', 'CEU AZUL', 'M', 'PR', 'SL', 0),
(4105409, 'Chopinzinho', 'CHOPINZINHO', 'M', 'PR', 'SL', 0),
(4105508, 'Cianorte', 'CIANORTE', 'M', 'PR', 'SL', 0),
(4105607, 'Cidade Gaúcha', 'CIDADE GAUCHA', 'M', 'PR', 'SL', 0),
(4105706, 'Clevelândia', 'CLEVELANDIA', 'M', 'PR', 'SL', 0),
(4105805, 'Colombo', 'COLOMBO', 'M', 'PR', 'SL', 0),
(4105904, 'Colorado', 'COLORADO', 'M', 'PR', 'SL', 0),
(4106001, 'Congonhinhas', 'CONGONHINHAS', 'M', 'PR', 'SL', 0),
(4106100, 'Conselheiro Mairinck', 'CONSELHEIRO MAIRINCK', 'M', 'PR', 'SL', 0),
(4106209, 'Contenda', 'CONTENDA', 'M', 'PR', 'SL', 0),
(4106308, 'Corbélia', 'CORBELIA', 'M', 'PR', 'SL', 0),
(4106407, 'Cornélio Procópio', 'CORNELIO PROCOPIO', 'M', 'PR', 'SL', 0),
(4106456, 'Coronel Domingos Soares', 'CORONEL DOMINGOS SOARES', 'M', 'PR', 'SL', 0),
(4106506, 'Coronel Vivida', 'CORONEL VIVIDA', 'M', 'PR', 'SL', 0),
(4106555, 'Corumbataí do Sul', 'CORUMBATAI DO SUL', 'M', 'PR', 'SL', 0),
(4106571, 'Cruzeiro do Iguaçu', 'CRUZEIRO DO IGUACU', 'M', 'PR', 'SL', 0),
(4106605, 'Cruzeiro do Oeste', 'CRUZEIRO DO OESTE', 'M', 'PR', 'SL', 0),
(4106704, 'Cruzeiro do Sul', 'CRUZEIRO DO SUL', 'M', 'PR', 'SL', 0),
(4106803, 'Cruz Machado', 'CRUZ MACHADO', 'M', 'PR', 'SL', 0),
(4106852, 'Cruzmaltina', 'CRUZMALTINA', 'M', 'PR', 'SL', 0),
(4106902, 'Curitiba', 'CURITIBA', 'M', 'PR', 'SL', 0),
(4107009, 'Curiúva', 'CURIUVA', 'M', 'PR', 'SL', 0),
(4107108, 'Diamante do Norte', 'DIAMANTE DO NORTE', 'M', 'PR', 'SL', 0),
(4107124, 'Diamante do Sul', 'DIAMANTE DO SUL', 'M', 'PR', 'SL', 0),
(4107157, 'Diamante D''Oeste', 'DIAMANTE D''OESTE', 'M', 'PR', 'SL', 0),
(4107207, 'Dois Vizinhos', 'DOIS VIZINHOS', 'M', 'PR', 'SL', 0),
(4107256, 'Douradina', 'DOURADINA', 'M', 'PR', 'SL', 0),
(4107306, 'Doutor Camargo', 'DOUTOR CAMARGO', 'M', 'PR', 'SL', 0),
(4107405, 'Enéas Marques', 'ENEAS MARQUES', 'M', 'PR', 'SL', 0),
(4107504, 'Engenheiro Beltrão', 'ENGENHEIRO BELTRAO', 'M', 'PR', 'SL', 0),
(4107520, 'Esperança Nova', 'ESPERANCA NOVA', 'M', 'PR', 'SL', 0),
(4107538, 'Entre Rios do Oeste', 'ENTRE RIOS DO OESTE', 'M', 'PR', 'SL', 0),
(4107546, 'Espigão Alto do Iguaçu', 'ESPIGAO ALTO DO IGUACU', 'M', 'PR', 'SL', 0),
(4107553, 'Farol', 'FAROL', 'M', 'PR', 'SL', 0),
(4107603, 'Faxinal', 'FAXINAL', 'M', 'PR', 'SL', 0),
(4107652, 'Fazenda Rio Grande', 'FAZENDA RIO GRANDE', 'M', 'PR', 'SL', 0),
(4107702, 'Fênix', 'FENIX', 'M', 'PR', 'SL', 0),
(4107736, 'Fernandes Pinheiro', 'FERNANDES PINHEIRO', 'M', 'PR', 'SL', 0),
(4107751, 'Figueira', 'FIGUEIRA', 'M', 'PR', 'SL', 0),
(4107801, 'Floraí', 'FLORAI', 'M', 'PR', 'SL', 0),
(4107850, 'Flor da Serra do Sul', 'FLOR DA SERRA DO SUL', 'M', 'PR', 'SL', 0),
(4107900, 'Floresta', 'FLORESTA', 'M', 'PR', 'SL', 0),
(4108007, 'Florestópolis', 'FLORESTOPOLIS', 'M', 'PR', 'SL', 0),
(4108106, 'Flórida', 'FLORIDA', 'M', 'PR', 'SL', 0),
(4108205, 'Formosa do Oeste', 'FORMOSA DO OESTE', 'M', 'PR', 'SL', 0),
(4108304, 'Foz do Iguaçu', 'FOZ DO IGUACU', 'M', 'PR', 'SL', 0),
(4108320, 'Francisco Alves', 'FRANCISCO ALVES', 'M', 'PR', 'SL', 0),
(4108403, 'Francisco Beltrão', 'FRANCISCO BELTRAO', 'M', 'PR', 'SL', 0),
(4108452, 'Foz do Jordão', 'FOZ DO JORDAO', 'M', 'PR', 'SL', 0),
(4108502, 'General Carneiro', 'GENERAL CARNEIRO', 'M', 'PR', 'SL', 0),
(4108551, 'Godoy Moreira', 'GODOY MOREIRA', 'M', 'PR', 'SL', 0),
(4108601, 'Goioerê', 'GOIOERE', 'M', 'PR', 'SL', 0),
(4108650, 'Goioxim', 'GOIOXIM', 'M', 'PR', 'SL', 0),
(4108700, 'Grandes Rios', 'GRANDES RIOS', 'M', 'PR', 'SL', 0),
(4108809, 'Guaíra', 'GUAIRA', 'M', 'PR', 'SL', 0),
(4108908, 'Guairaçá', 'GUAIRACA', 'M', 'PR', 'SL', 0),
(4108957, 'Guamiranga', 'GUAMIRANGA', 'M', 'PR', 'SL', 0),
(4109005, 'Guapirama', 'GUAPIRAMA', 'M', 'PR', 'SL', 0),
(4109104, 'Guaporema', 'GUAPOREMA', 'M', 'PR', 'SL', 0),
(4109203, 'Guaraci', 'GUARACI', 'M', 'PR', 'SL', 0),
(4109302, 'Guaraniaçu', 'GUARANIACU', 'M', 'PR', 'SL', 0),
(4109401, 'Guarapuava', 'GUARAPUAVA', 'M', 'PR', 'SL', 0),
(4109500, 'Guaraqueçaba', 'GUARAQUECABA', 'M', 'PR', 'SL', 0),
(4109609, 'Guaratuba', 'GUARATUBA', 'M', 'PR', 'SL', 0),
(4109658, 'Honório Serpa', 'HONORIO SERPA', 'M', 'PR', 'SL', 0),
(4109708, 'Ibaiti', 'IBAITI', 'M', 'PR', 'SL', 0),
(4109757, 'Ibema', 'IBEMA', 'M', 'PR', 'SL', 0),
(4109807, 'Ibiporã', 'IBIPORA', 'M', 'PR', 'SL', 0),
(4109906, 'Icaraíma', 'ICARAIMA', 'M', 'PR', 'SL', 0),
(4110003, 'Iguaraçu', 'IGUARACU', 'M', 'PR', 'SL', 0),
(4110052, 'Iguatú', 'IGUATU', 'M', 'PR', 'SL', 0),
(4110078, 'Imbaú', 'IMBAU', 'M', 'PR', 'SL', 0),
(4110102, 'Imbituva', 'IMBITUVA', 'M', 'PR', 'SL', 0),
(4110201, 'Inácio Martins', 'INACIO MARTINS', 'M', 'PR', 'SL', 0),
(4110300, 'Inajá', 'INAJA', 'M', 'PR', 'SL', 0),
(4110409, 'Indianópolis', 'INDIANOPOLIS', 'M', 'PR', 'SL', 0),
(4110508, 'Ipiranga', 'IPIRANGA', 'M', 'PR', 'SL', 0),
(4110607, 'Iporã', 'IPORA', 'M', 'PR', 'SL', 0),
(4110656, 'Iracema do Oeste', 'IRACEMA DO OESTE', 'M', 'PR', 'SL', 0),
(4110706, 'Irati', 'IRATI', 'M', 'PR', 'SL', 0),
(4110805, 'Iretama', 'IRETAMA', 'M', 'PR', 'SL', 0),
(4110904, 'Itaguajé', 'ITAGUAJE', 'M', 'PR', 'SL', 0),
(4110953, 'Itaipulândia', 'ITAIPULANDIA', 'M', 'PR', 'SL', 0),
(4111001, 'Itambaracá', 'ITAMBARACA', 'M', 'PR', 'SL', 0),
(4111100, 'Itambé', 'ITAMBE', 'M', 'PR', 'SL', 0),
(4111209, 'Itapejara D''Oeste', 'ITAPEJARA D''OESTE', 'M', 'PR', 'SL', 0),
(4111258, 'Itaperuçu', 'ITAPERUCU', 'M', 'PR', 'SL', 0),
(4111308, 'Itaúna do Sul', 'ITAUNA DO SUL', 'M', 'PR', 'SL', 0),
(4111407, 'Ivaí', 'IVAI', 'M', 'PR', 'SL', 0),
(4111506, 'Ivaiporã', 'IVAIPORA', 'M', 'PR', 'SL', 0),
(4111555, 'Ivaté', 'IVATE', 'M', 'PR', 'SL', 0),
(4111605, 'Ivatuba', 'IVATUBA', 'M', 'PR', 'SL', 0),
(4111704, 'Jaboti', 'JABOTI', 'M', 'PR', 'SL', 0),
(4111803, 'Jacarezinho', 'JACAREZINHO', 'M', 'PR', 'SL', 0),
(4111902, 'Jaguapitã', 'JAGUAPITA', 'M', 'PR', 'SL', 0),
(4112009, 'Jaguariaíva', 'JAGUARIAIVA', 'M', 'PR', 'SL', 0),
(4112108, 'Jandaia do Sul', 'JANDAIA DO SUL', 'M', 'PR', 'SL', 0),
(4112207, 'Janiópolis', 'JANIOPOLIS', 'M', 'PR', 'SL', 0),
(4112306, 'Japira', 'JAPIRA', 'M', 'PR', 'SL', 0),
(4112405, 'Japurá', 'JAPURA', 'M', 'PR', 'SL', 0),
(4112504, 'Jardim Alegre', 'JARDIM ALEGRE', 'M', 'PR', 'SL', 0),
(4112603, 'Jardim Olinda', 'JARDIM OLINDA', 'M', 'PR', 'SL', 0),
(4112702, 'Jataizinho', 'JATAIZINHO', 'M', 'PR', 'SL', 0),
(4112751, 'Jesuítas', 'JESUITAS', 'M', 'PR', 'SL', 0),
(4112801, 'Joaquim Távora', 'JOAQUIM TAVORA', 'M', 'PR', 'SL', 0),
(4112900, 'Jundiaí do Sul', 'JUNDIAI DO SUL', 'M', 'PR', 'SL', 0),
(4112959, 'Juranda', 'JURANDA', 'M', 'PR', 'SL', 0),
(4113007, 'Jussara', 'JUSSARA', 'M', 'PR', 'SL', 0),
(4113106, 'Kaloré', 'KALORE', 'M', 'PR', 'SL', 0),
(4113205, 'Lapa', 'LAPA', 'M', 'PR', 'SL', 0),
(4113254, 'Laranjal', 'LARANJAL', 'M', 'PR', 'SL', 0),
(4113304, 'Laranjeiras do Sul', 'LARANJEIRAS DO SUL', 'M', 'PR', 'SL', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(4113403, 'Leópolis', 'LEOPOLIS', 'M', 'PR', 'SL', 0),
(4113429, 'Lidianópolis', 'LIDIANOPOLIS', 'M', 'PR', 'SL', 0),
(4113452, 'Lindoeste', 'LINDOESTE', 'M', 'PR', 'SL', 0),
(4113502, 'Loanda', 'LOANDA', 'M', 'PR', 'SL', 0),
(4113601, 'Lobato', 'LOBATO', 'M', 'PR', 'SL', 0),
(4113700, 'Londrina', 'LONDRINA', 'M', 'PR', 'SL', 0),
(4113734, 'Luiziana', 'LUIZIANA', 'M', 'PR', 'SL', 0),
(4113759, 'Lunardelli', 'LUNARDELLI', 'M', 'PR', 'SL', 0),
(4113809, 'Lupionópolis', 'LUPIONOPOLIS', 'M', 'PR', 'SL', 0),
(4113908, 'Mallet', 'MALLET', 'M', 'PR', 'SL', 0),
(4114005, 'Mamborê', 'MAMBORE', 'M', 'PR', 'SL', 0),
(4114104, 'Mandaguaçu', 'MANDAGUACU', 'M', 'PR', 'SL', 0),
(4114203, 'Mandaguari', 'MANDAGUARI', 'M', 'PR', 'SL', 0),
(4114302, 'Mandirituba', 'MANDIRITUBA', 'M', 'PR', 'SL', 0),
(4114351, 'Manfrinópolis', 'MANFRINOPOLIS', 'M', 'PR', 'SL', 0),
(4114401, 'Mangueirinha', 'MANGUEIRINHA', 'M', 'PR', 'SL', 0),
(4114500, 'Manoel Ribas', 'MANOEL RIBAS', 'M', 'PR', 'SL', 0),
(4114609, 'Marechal Cândido Rondon', 'MARECHAL CANDIDO RONDON', 'M', 'PR', 'SL', 0),
(4114708, 'Maria Helena', 'MARIA HELENA', 'M', 'PR', 'SL', 0),
(4114807, 'Marialva', 'MARIALVA', 'M', 'PR', 'SL', 0),
(4114906, 'Marilândia do Sul', 'MARILANDIA DO SUL', 'M', 'PR', 'SL', 0),
(4115002, 'Marilena', 'MARILENA', 'M', 'PR', 'SL', 0),
(4115101, 'Mariluz', 'MARILUZ', 'M', 'PR', 'SL', 0),
(4115200, 'Maringá', 'MARINGA', 'M', 'PR', 'SL', 0),
(4115309, 'Mariópolis', 'MARIOPOLIS', 'M', 'PR', 'SL', 0),
(4115358, 'Maripá', 'MARIPA', 'M', 'PR', 'SL', 0),
(4115408, 'Marmeleiro', 'MARMELEIRO', 'M', 'PR', 'SL', 0),
(4115457, 'Marquinho', 'MARQUINHO', 'M', 'PR', 'SL', 0),
(4115507, 'Marumbi', 'MARUMBI', 'M', 'PR', 'SL', 0),
(4115606, 'Matelândia', 'MATELANDIA', 'M', 'PR', 'SL', 0),
(4115705, 'Matinhos', 'MATINHOS', 'M', 'PR', 'SL', 0),
(4115739, 'Mato Rico', 'MATO RICO', 'M', 'PR', 'SL', 0),
(4115754, 'Mauá da Serra', 'MAUA DA SERRA', 'M', 'PR', 'SL', 0),
(4115804, 'Medianeira', 'MEDIANEIRA', 'M', 'PR', 'SL', 0),
(4115853, 'Mercedes', 'MERCEDES', 'M', 'PR', 'SL', 0),
(4115903, 'Mirador', 'MIRADOR', 'M', 'PR', 'SL', 0),
(4116000, 'Miraselva', 'MIRASELVA', 'M', 'PR', 'SL', 0),
(4116059, 'Missal', 'MISSAL', 'M', 'PR', 'SL', 0),
(4116109, 'Moreira Sales', 'MOREIRA SALES', 'M', 'PR', 'SL', 0),
(4116208, 'Morretes', 'MORRETES', 'M', 'PR', 'SL', 0),
(4116307, 'Munhoz de Melo', 'MUNHOZ DE MELO', 'M', 'PR', 'SL', 0),
(4116406, 'Nossa Senhora das Gracas', 'NOSSA SENHORA DAS GRACAS', 'M', 'PR', 'SL', 0),
(4116505, 'Nova Alianca do Ivaí', 'NOVA ALIANCA DO IVAI', 'M', 'PR', 'SL', 0),
(4116604, 'Nova América da Colina', 'NOVA AMERICA DA COLINA', 'M', 'PR', 'SL', 0),
(4116703, 'Nova Aurora', 'NOVA AURORA', 'M', 'PR', 'SL', 0),
(4116802, 'Nova Cantu', 'NOVA CANTU', 'M', 'PR', 'SL', 0),
(4116901, 'Nova Esperança', 'NOVA ESPERANCA', 'M', 'PR', 'SL', 0),
(4116950, 'Nova Esperança do Sudoeste', 'NOVA ESPERANCA DO SUDOESTE', 'M', 'PR', 'SL', 0),
(4117008, 'Nova Fátima', 'NOVA FATIMA', 'M', 'PR', 'SL', 0),
(4117057, 'Nova Laranjeiras', 'NOVA LARANJEIRAS', 'M', 'PR', 'SL', 0),
(4117107, 'Nova Londrina', 'NOVA LONDRINA', 'M', 'PR', 'SL', 0),
(4117206, 'Nova Olímpia', 'NOVA OLIMPIA', 'M', 'PR', 'SL', 0),
(4117214, 'Nova Santa Bárbara', 'NOVA SANTA BARBARA', 'M', 'PR', 'SL', 0),
(4117222, 'Nova Santa Rosa', 'NOVA SANTA ROSA', 'M', 'PR', 'SL', 0),
(4117255, 'Nova Prata do Iguaçu', 'NOVA PRATA DO IGUACU', 'M', 'PR', 'SL', 0),
(4117271, 'Nova Tebas', 'NOVA TEBAS', 'M', 'PR', 'SL', 0),
(4117297, 'Novo Itacolomi', 'NOVO ITACOLOMI', 'M', 'PR', 'SL', 0),
(4117305, 'Ortigueira', 'ORTIGUEIRA', 'M', 'PR', 'SL', 0),
(4117404, 'Ourizona', 'OURIZONA', 'M', 'PR', 'SL', 0),
(4117453, 'Ouro Verde do Oeste', 'OURO VERDE DO OESTE', 'M', 'PR', 'SL', 0),
(4117503, 'Paiçandu', 'PAICANDU', 'M', 'PR', 'SL', 0),
(4117602, 'Palmas', 'PALMAS', 'M', 'PR', 'SL', 0),
(4117701, 'Palmeira', 'PALMEIRA', 'M', 'PR', 'SL', 0),
(4117800, 'Palmital', 'PALMITAL', 'M', 'PR', 'SL', 0),
(4117909, 'Palotina', 'PALOTINA', 'M', 'PR', 'SL', 0),
(4118006, 'Paraíso do Norte', 'PARAISO DO NORTE', 'M', 'PR', 'SL', 0),
(4118105, 'Paranacity', 'PARANACITY', 'M', 'PR', 'SL', 0),
(4118204, 'Paranaguá', 'PARANAGUA', 'M', 'PR', 'SL', 0),
(4118303, 'Paranapoema', 'PARANAPOEMA', 'M', 'PR', 'SL', 0),
(4118402, 'Paranavaí', 'PARANAVAI', 'M', 'PR', 'SL', 0),
(4118451, 'Pato Bragado', 'PATO BRAGADO', 'M', 'PR', 'SL', 0),
(4118501, 'Pato Branco', 'PATO BRANCO', 'M', 'PR', 'SL', 0),
(4118600, 'Paula Freitas', 'PAULA FREITAS', 'M', 'PR', 'SL', 0),
(4118709, 'Paulo Frontin', 'PAULO FRONTIN', 'M', 'PR', 'SL', 0),
(4118808, 'Peabiru', 'PEABIRU', 'M', 'PR', 'SL', 0),
(4118857, 'Perobal', 'PEROBAL', 'M', 'PR', 'SL', 0),
(4118907, 'Pérola', 'PEROLA', 'M', 'PR', 'SL', 0),
(4119004, 'Pérola d''Oeste', 'PEROLA D''OESTE', 'M', 'PR', 'SL', 0),
(4119103, 'Piên', 'PIEN', 'M', 'PR', 'SL', 0),
(4119152, 'Pinhais', 'PINHAIS', 'M', 'PR', 'SL', 0),
(4119202, 'Pinhalão', 'PINHALAO', 'M', 'PR', 'SL', 0),
(4119251, 'Pinhal de São Bento', 'PINHAL DE SAO BENTO', 'M', 'PR', 'SL', 0),
(4119301, 'Pinhão', 'PINHAO', 'M', 'PR', 'SL', 0),
(4119400, 'Piraí do Sul', 'PIRAI DO SUL', 'M', 'PR', 'SL', 0),
(4119509, 'Piraquara', 'PIRAQUARA', 'M', 'PR', 'SL', 0),
(4119608, 'Pitanga', 'PITANGA', 'M', 'PR', 'SL', 0),
(4119657, 'Pitangueiras', 'PITANGUEIRAS', 'M', 'PR', 'SL', 0),
(4119707, 'Planaltina do Paraná', 'PLANALTINA DO PARANA', 'M', 'PR', 'SL', 0),
(4119806, 'Planalto', 'PLANALTO', 'M', 'PR', 'SL', 0),
(4119905, 'Ponta Grossa', 'PONTA GROSSA', 'M', 'PR', 'SL', 0),
(4119954, 'Pontal do Parana', 'PONTAL DO PARANA', 'M', 'PR', 'SL', 0),
(4120002, 'Porecatu', 'PORECATU', 'M', 'PR', 'SL', 0),
(4120101, 'Porto Amazonas', 'PORTO AMAZONAS', 'M', 'PR', 'SL', 0),
(4120150, 'Porto Barreiro', 'PORTO BARREIRO', 'M', 'PR', 'SL', 0),
(4120200, 'Porto Rico', 'PORTO RICO', 'M', 'PR', 'SL', 0),
(4120309, 'Porto Vitoria', 'PORTO VITORIA', 'M', 'PR', 'SL', 0),
(4120333, 'Prado Ferreira', 'PRADO FERREIRA', 'M', 'PR', 'SL', 0),
(4120358, 'Pranchita', 'PRANCHITA', 'M', 'PR', 'SL', 0),
(4120408, 'Presidente Castelo Branco', 'PRESIDENTE CASTELO BRANCO', 'M', 'PR', 'SL', 0),
(4120507, 'Primeiro de Maio', 'PRIMEIRO DE MAIO', 'M', 'PR', 'SL', 0),
(4120606, 'Prudentopolis', 'PRUDENTOPOLIS', 'M', 'PR', 'SL', 0),
(4120655, 'Quarto Centenario', 'QUARTO CENTENARIO', 'M', 'PR', 'SL', 0),
(4120705, 'Quatigua', 'QUATIGUA', 'M', 'PR', 'SL', 0),
(4120804, 'Quatro Barras', 'QUATRO BARRAS', 'M', 'PR', 'SL', 0),
(4120853, 'Quatro Pontes', 'QUATRO PONTES', 'M', 'PR', 'SL', 0),
(4120903, 'Quedas do Iguaçu', 'QUEDAS DO IGUACU', 'M', 'PR', 'SL', 0),
(4121000, 'Querencia do Norte', 'QUERENCIA DO NORTE', 'M', 'PR', 'SL', 0),
(4121109, 'Quinta do Sol', 'QUINTA DO SOL', 'M', 'PR', 'SL', 0),
(4121208, 'Quitandinha', 'QUITANDINHA', 'M', 'PR', 'SL', 0),
(4121257, 'Ramilândia', 'RAMILANDIA', 'M', 'PR', 'SL', 0),
(4121307, 'Rancho Alegre', 'RANCHO ALEGRE', 'M', 'PR', 'SL', 0),
(4121356, 'Rancho Alegre D''Oeste', 'RANCHO ALEGRE D''OESTE', 'M', 'PR', 'SL', 0),
(4121406, 'Realeza', 'REALEZA', 'M', 'PR', 'SL', 0),
(4121505, 'Rebouças', 'REBOUCAS', 'M', 'PR', 'SL', 0),
(4121604, 'Renascenca', 'RENASCENCA', 'M', 'PR', 'SL', 0),
(4121703, 'Reserva', 'RESERVA', 'M', 'PR', 'SL', 0),
(4121752, 'Reserva do Iguaçu', 'RESERVA DO IGUACU', 'M', 'PR', 'SL', 0),
(4121802, 'Ribeirão Claro', 'RIBEIRAO CLARO', 'M', 'PR', 'SL', 0),
(4121901, 'Ribeirão do Pinhal', 'RIBEIRAO DO PINHAL', 'M', 'PR', 'SL', 0),
(4122008, 'Rio Azul', 'RIO AZUL', 'M', 'PR', 'SL', 0),
(4122107, 'Rio Bom', 'RIO BOM', 'M', 'PR', 'SL', 0),
(4122156, 'Rio Bonito do Iguaçu', 'RIO BONITO DO IGUACU', 'M', 'PR', 'SL', 0),
(4122172, 'Rio Branco do Ivaí', 'RIO BRANCO DO IVAI', 'M', 'PR', 'SL', 0),
(4122206, 'Rio Branco do Sul', 'RIO BRANCO DO SUL', 'M', 'PR', 'SL', 0),
(4122305, 'Rio Negro', 'RIO NEGRO', 'M', 'PR', 'SL', 0),
(4122404, 'Rolândia', 'ROLANDIA', 'M', 'PR', 'SL', 0),
(4122503, 'Roncador', 'RONCADOR', 'M', 'PR', 'SL', 0),
(4122602, 'Rondon', 'RONDON', 'M', 'PR', 'SL', 0),
(4122651, 'Rosário do Ivaí', 'ROSARIO DO IVAI', 'M', 'PR', 'SL', 0),
(4122701, 'Sabáudia', 'SABAUDIA', 'M', 'PR', 'SL', 0),
(4122800, 'Salgado Filho', 'SALGADO FILHO', 'M', 'PR', 'SL', 0),
(4122909, 'Salto do Itarare', 'SALTO DO ITARARE', 'M', 'PR', 'SL', 0),
(4123006, 'Salto do Lontra', 'SALTO DO LONTRA', 'M', 'PR', 'SL', 0),
(4123105, 'Santa Amelia', 'SANTA AMELIA', 'M', 'PR', 'SL', 0),
(4123204, 'Santa Cecília do Pavão', 'SANTA CECILIA DO PAVAO', 'M', 'PR', 'SL', 0),
(4123303, 'Santa Cruz de Monte Castelo', 'SANTA CRUZ DE MONTE CASTELO', 'M', 'PR', 'SL', 0),
(4123402, 'Santa Fé', 'SANTA FE', 'M', 'PR', 'SL', 0),
(4123501, 'Santa Helena', 'SANTA HELENA', 'M', 'PR', 'SL', 0),
(4123600, 'Santa Inês', 'SANTA INES', 'M', 'PR', 'SL', 0),
(4123709, 'Santa Isabel do Ivaí', 'SANTA ISABEL DO IVAI', 'M', 'PR', 'SL', 0),
(4123808, 'Santa Izabel do Oeste', 'SANTA IZABEL DO OESTE', 'M', 'PR', 'SL', 0),
(4123824, 'Santa Lúcia', 'SANTA LUCIA', 'M', 'PR', 'SL', 0),
(4123857, 'Santa Maria do Oeste', 'SANTA MARIA DO OESTE', 'M', 'PR', 'SL', 0),
(4123907, 'Santa Mariana', 'SANTA MARIANA', 'M', 'PR', 'SL', 0),
(4123956, 'Santa Mônica', 'SANTA MONICA', 'M', 'PR', 'SL', 0),
(4124004, 'Santana do Itararé', 'SANTANA DO ITARARE', 'M', 'PR', 'SL', 0),
(4124020, 'Santa Tereza do Oeste', 'SANTA TEREZA DO OESTE', 'M', 'PR', 'SL', 0),
(4124053, 'Santa Terezinha de Itaipu', 'SANTA TEREZINHA DE ITAIPU', 'M', 'PR', 'SL', 0),
(4124103, 'Santo Antônio da Platina', 'SANTO ANTONIO DA PLATINA', 'M', 'PR', 'SL', 0),
(4124202, 'Santo Antônio do Caiua', 'SANTO ANTONIO DO CAIUA', 'M', 'PR', 'SL', 0),
(4124301, 'Santo Antônio do Paraíso', 'SANTO ANTONIO DO PARAISO', 'M', 'PR', 'SL', 0),
(4124400, 'Santo Antônio do Sudoeste', 'SANTO ANTONIO DO SUDOESTE', 'M', 'PR', 'SL', 0),
(4124509, 'Santo Inacio', 'SANTO INACIO', 'M', 'PR', 'SL', 0),
(4124608, 'São Carlos do Ivai', 'SAO CARLOS DO IVAI', 'M', 'PR', 'SL', 0),
(4124707, 'São Jeronimo da Serra', 'SAO JERONIMO DA SERRA', 'M', 'PR', 'SL', 0),
(4124806, 'São João', 'SAO JOAO', 'M', 'PR', 'SL', 0),
(4124905, 'São João do Caiuá', 'SAO JOAO DO CAIUA', 'M', 'PR', 'SL', 0),
(4125001, 'São João do Ivaí', 'SAO JOAO DO IVAI', 'M', 'PR', 'SL', 0),
(4125100, 'São João do Triunfo', 'SAO JOAO DO TRIUNFO', 'M', 'PR', 'SL', 0),
(4125209, 'São Jorge D''Oeste', 'SAO JORGE D''OESTE', 'M', 'PR', 'SL', 0),
(4125308, 'São Jorge do Ivaí', 'SAO JORGE DO IVAI', 'M', 'PR', 'SL', 0),
(4125357, 'São Jorge do Patrocínio', 'SAO JORGE DO PATROCINIO', 'M', 'PR', 'SL', 0),
(4125407, 'São José da Boa Vista', 'SAO JOSE DA BOA VISTA', 'M', 'PR', 'SL', 0),
(4125456, 'São José das Palmeiras', 'SAO JOSE DAS PALMEIRAS', 'M', 'PR', 'SL', 0),
(4125506, 'São José dos Pinhais', 'SAO JOSE DOS PINHAIS', 'M', 'PR', 'SL', 0),
(4125555, 'São Manoel', 'SAO MANOEL', 'M', 'PR', 'SL', 0),
(4125605, 'São Mateus do Sul', 'SAO MATEUS DO SUL', 'M', 'PR', 'SL', 0),
(4125704, 'São Miguel do Iguaçu', 'SAO MIGUEL DO IGUACU', 'M', 'PR', 'SL', 0),
(4125753, 'São Pedro do Iguaçu', 'SAO PEDRO DO IGUACU', 'M', 'PR', 'SL', 0),
(4125803, 'São Pedro do Ivaí', 'SAO PEDRO DO IVAI', 'M', 'PR', 'SL', 0),
(4125902, 'São Pedro do Paraná', 'SAO PEDRO DO PARANA', 'M', 'PR', 'SL', 0),
(4126009, 'São Sebastiao da Amoreira', 'SAO SEBASTIAO DA AMOREIRA', 'M', 'PR', 'SL', 0),
(4126108, 'São Tomé', 'SAO TOME', 'M', 'PR', 'SL', 0),
(4126207, 'Sapopema', 'SAPOPEMA', 'M', 'PR', 'SL', 0),
(4126256, 'Sarandi', 'SARANDI', 'M', 'PR', 'SL', 0),
(4126272, 'Saudade do Iguaçu', 'SAUDADE DO IGUACU', 'M', 'PR', 'SL', 0),
(4126306, 'Sengés', 'SENGES', 'M', 'PR', 'SL', 0),
(4126355, 'Serranópolis do Iguaçu', 'SERRANOPOLIS DO IGUACU', 'M', 'PR', 'SL', 0),
(4126405, 'Sertaneja', 'SERTANEJA', 'M', 'PR', 'SL', 0),
(4126504, 'Sertanópolis', 'SERTANOPOLIS', 'M', 'PR', 'SL', 0),
(4126603, 'Siqueira Campos', 'SIQUEIRA CAMPOS', 'M', 'PR', 'SL', 0),
(4126652, 'Sulina', 'SULINA', 'M', 'PR', 'SL', 0),
(4126678, 'Tamarana', 'TAMARANA', 'M', 'PR', 'SL', 0),
(4126702, 'Tamboara', 'TAMBOARA', 'M', 'PR', 'SL', 0),
(4126801, 'Tapejara', 'TAPEJARA', 'M', 'PR', 'SL', 0),
(4126900, 'Tapira', 'TAPIRA', 'M', 'PR', 'SL', 0),
(4127007, 'Teixeira Soares', 'TEIXEIRA SOARES', 'M', 'PR', 'SL', 0),
(4127106, 'Telêmaco Borba', 'TELEMACO BORBA', 'M', 'PR', 'SL', 0),
(4127205, 'Terra Boa', 'TERRA BOA', 'M', 'PR', 'SL', 0),
(4127304, 'Terra Rica', 'TERRA RICA', 'M', 'PR', 'SL', 0),
(4127403, 'Terra Roxa', 'TERRA ROXA', 'M', 'PR', 'SL', 0),
(4127502, 'Tibagi', 'TIBAGI', 'M', 'PR', 'SL', 0),
(4127601, 'Tijucas do Sul', 'TIJUCAS DO SUL', 'M', 'PR', 'SL', 0),
(4127700, 'Toledo', 'TOLEDO', 'M', 'PR', 'SL', 0),
(4127809, 'Tomazina', 'TOMAZINA', 'M', 'PR', 'SL', 0),
(4127858, 'Três Barras do Paraná', 'TRES BARRAS DO PARANA', 'M', 'PR', 'SL', 0),
(4127882, 'Tunas', 'TUNAS', 'M', 'PR', 'SL', 0),
(4127908, 'Tuneiras do Oeste', 'TUNEIRAS DO OESTE', 'M', 'PR', 'SL', 0),
(4127957, 'Tupãssi', 'TUPASSI', 'M', 'PR', 'SL', 0),
(4127965, 'Turvo', 'TURVO', 'M', 'PR', 'SL', 0),
(4128005, 'Ubirata', 'UBIRATA', 'M', 'PR', 'SL', 0),
(4128104, 'Umuarama', 'UMUARAMA', 'M', 'PR', 'SL', 0),
(4128203, 'União da Vitória', 'UNIAO DA VITORIA', 'M', 'PR', 'SL', 0),
(4128302, 'Uniflor', 'UNIFLOR', 'M', 'PR', 'SL', 0),
(4128401, 'Uraí', 'URAI', 'M', 'PR', 'SL', 0),
(4128500, 'Wenceslau Braz', 'WENCESLAU BRAZ', 'M', 'PR', 'SL', 0),
(4128534, 'Ventania', 'VENTANIA', 'M', 'PR', 'SL', 0),
(4128559, 'Vera Cruz do Oeste', 'VERA CRUZ DO OESTE', 'M', 'PR', 'SL', 0),
(4128609, 'Verê', 'VERE', 'M', 'PR', 'SL', 0),
(4128625, 'Vila Alta', 'VILA ALTA', 'M', 'PR', 'SL', 0),
(4128633, 'Doutor Ulysses', 'DOUTOR ULYSSES', 'M', 'PR', 'SL', 0),
(4128658, 'Virmond', 'VIRMOND', 'M', 'PR', 'SL', 0),
(4128708, 'Vitorino', 'VITORINO', 'M', 'PR', 'SL', 0),
(4128807, 'Xambre', 'XAMBRE', 'M', 'PR', 'SL', 0),
(4200000, 'Santa Catarina', 'SANTA CATARINA', 'U', 'SC', 'SL', 0),
(4200051, 'Abdon Batista', 'ABDON BATISTA', 'M', 'SC', 'SL', 0),
(4200101, 'Abelardo Luz', 'ABELARDO LUZ', 'M', 'SC', 'SL', 0),
(4200200, 'Agrolândia', 'AGROLANDIA', 'M', 'SC', 'SL', 0),
(4200309, 'Agronômica', 'AGRONOMICA', 'M', 'SC', 'SL', 0),
(4200408, 'Água Doce', 'AGUA DOCE', 'M', 'SC', 'SL', 0),
(4200507, 'Águas de Chapecó', 'AGUAS DE CHAPECO', 'M', 'SC', 'SL', 0),
(4200556, 'Águas Frias', 'AGUAS FRIAS', 'M', 'SC', 'SL', 0),
(4200606, 'Águas Mornas', 'AGUAS MORNAS', 'M', 'SC', 'SL', 0),
(4200705, 'Alfredo Wagner', 'ALFREDO WAGNER', 'M', 'SC', 'SL', 0),
(4200754, 'Alto Bela Vista', 'ALTO BELA VISTA', 'M', 'SC', 'SL', 0),
(4200804, 'Anchieta', 'ANCHIETA', 'M', 'SC', 'SL', 0),
(4200903, 'Angelina', 'ANGELINA', 'M', 'SC', 'SL', 0),
(4201000, 'Anita Garibaldi', 'ANITA GARIBALDI', 'M', 'SC', 'SL', 0),
(4201109, 'Anitápolis', 'ANITAPOLIS', 'M', 'SC', 'SL', 0),
(4201208, 'Antônio Carlos', 'ANTONIO CARLOS', 'M', 'SC', 'SL', 0),
(4201257, 'Apiuna', 'APIUNA', 'M', 'SC', 'SL', 0),
(4201273, 'Arabuta', 'ARABUTA', 'M', 'SC', 'SL', 0),
(4201307, 'Araquari', 'ARAQUARI', 'M', 'SC', 'SL', 0),
(4201406, 'Ararangua', 'ARARANGUA', 'M', 'SC', 'SL', 0),
(4201505, 'Armazém', 'ARMAZEM', 'M', 'SC', 'SL', 0),
(4201604, 'Arroio Trinta', 'ARROIO TRINTA', 'M', 'SC', 'SL', 0),
(4201653, 'Arvoredo', 'ARVOREDO', 'M', 'SC', 'SL', 0),
(4201703, 'Ascurra', 'ASCURRA', 'M', 'SC', 'SL', 0),
(4201802, 'Atalanta', 'ATALANTA', 'M', 'SC', 'SL', 0),
(4201901, 'Aurora', 'AURORA', 'M', 'SC', 'SL', 0),
(4201950, 'Balneário Arroio do Silva', 'BALNEARIO ARROIO DO SILVA', 'M', 'SC', 'SL', 0),
(4202008, 'Balneário Camboriu', 'BALNEARIO CAMBORIU', 'M', 'SC', 'SL', 0),
(4202057, 'Barra do Sul', 'BARRA DO SUL', 'M', 'SC', 'SL', 0),
(4202073, 'Balneário Gaivota', 'BALNEARIO GAIVOTA', 'M', 'SC', 'SL', 0),
(4202081, 'Bandeirante', 'BANDEIRANTE', 'M', 'SC', 'SL', 0),
(4202099, 'Barra Bonita', 'BARRA BONITA', 'M', 'SC', 'SL', 0),
(4202107, 'Barra Velha', 'BARRA VELHA', 'M', 'SC', 'SL', 0),
(4202131, 'Bela Vista do Toldo', 'BELA VISTA DO TOLDO', 'M', 'SC', 'SL', 0),
(4202156, 'Belmonte', 'BELMONTE', 'M', 'SC', 'SL', 0),
(4202206, 'Benedito Novo', 'BENEDITO NOVO', 'M', 'SC', 'SL', 0),
(4202305, 'Biguaçu', 'BIGUACU', 'M', 'SC', 'SL', 0),
(4202404, 'Blumenau', 'BLUMENAU', 'M', 'SC', 'SL', 0),
(4202438, 'Bocaina do Sul', 'BOCAINA DO SUL', 'M', 'SC', 'SL', 0),
(4202453, 'Bombinhas', 'BOMBINHAS', 'M', 'SC', 'SL', 0),
(4202503, 'Bom Jardim da Serra', 'BOM JARDIM DA SERRA', 'M', 'SC', 'SL', 0),
(4202537, 'Bom Jesus', 'BOM JESUS', 'M', 'SC', 'SL', 0),
(4202578, 'Bom Jesus do Oeste', 'BOM JESUS DO OESTE', 'M', 'SC', 'SL', 0),
(4202602, 'Bom Retiro', 'BOM RETIRO', 'M', 'SC', 'SL', 0),
(4202701, 'Botuvera', 'BOTUVERA', 'M', 'SC', 'SL', 0),
(4202800, 'Braço do Norte', 'BRACO DO NORTE', 'M', 'SC', 'SL', 0),
(4202859, 'Braço do Trombudo', 'BRACO DO TROMBUDO', 'M', 'SC', 'SL', 0),
(4202875, 'Brunópolis', 'BRUNOPOLIS', 'M', 'SC', 'SL', 0),
(4202909, 'Brusque', 'BRUSQUE', 'M', 'SC', 'SL', 0),
(4203006, 'Caçador', 'CACADOR', 'M', 'SC', 'SL', 0),
(4203105, 'Caibi', 'CAIBI', 'M', 'SC', 'SL', 0),
(4203154, 'Calmon', 'CALMON', 'M', 'SC', 'SL', 0),
(4203204, 'Camboriú', 'CAMBORIU', 'M', 'SC', 'SL', 0),
(4203253, 'Capão Alto', 'CAPAO ALTO', 'M', 'SC', 'SL', 0),
(4203303, 'Campo Alegre', 'CAMPO ALEGRE', 'M', 'SC', 'SL', 0),
(4203402, 'Campo Belo do Sul', 'CAMPO BELO DO SUL', 'M', 'SC', 'SL', 0),
(4203501, 'Campo Erê', 'CAMPO ERE', 'M', 'SC', 'SL', 0),
(4203600, 'Campos Novos', 'CAMPOS NOVOS', 'M', 'SC', 'SL', 0),
(4203709, 'Canelinha', 'CANELINHA', 'M', 'SC', 'SL', 0),
(4203808, 'Canoinhas', 'CANOINHAS', 'M', 'SC', 'SL', 0),
(4203907, 'Capinzal', 'CAPINZAL', 'M', 'SC', 'SL', 0),
(4203956, 'Capivari de Baixo', 'CAPIVARI DE BAIXO', 'M', 'SC', 'SL', 0),
(4204004, 'Catanduvas', 'CATANDUVAS', 'M', 'SC', 'SL', 0),
(4204103, 'Caxambu do Sul', 'CAXAMBU DO SUL', 'M', 'SC', 'SL', 0),
(4204152, 'Celso Ramos', 'CELSO RAMOS', 'M', 'SC', 'SL', 0),
(4204178, 'Cerro Negro', 'CERRO NEGRO', 'M', 'SC', 'SL', 0),
(4204194, 'Chapadão do Lageado', 'CHAPADAO DO LAGEADO', 'M', 'SC', 'SL', 0),
(4204202, 'Chapeco', 'CHAPECO', 'M', 'SC', 'SL', 0),
(4204251, 'Cocal do Sul', 'COCAL DO SUL', 'M', 'SC', 'SL', 0),
(4204301, 'Concórdia', 'CONCORDIA', 'M', 'SC', 'SL', 0),
(4204350, 'Cordilheira Alta', 'CORDILHEIRA ALTA', 'M', 'SC', 'SL', 0),
(4204400, 'Coronel Freitas', 'CORONEL FREITAS', 'M', 'SC', 'SL', 0),
(4204459, 'Coronel Martins', 'CORONEL MARTINS', 'M', 'SC', 'SL', 0),
(4204509, 'Corupá', 'CORUPA', 'M', 'SC', 'SL', 0),
(4204558, 'Correia Pinto', 'CORREIA PINTO', 'M', 'SC', 'SL', 0),
(4204608, 'Criciúma', 'CRICIUMA', 'M', 'SC', 'SL', 0),
(4204707, 'Cunha Porã', 'CUNHA PORA', 'M', 'SC', 'SL', 0),
(4204756, 'Cunhataí', 'CUNHATAI', 'M', 'SC', 'SL', 0),
(4204806, 'Curitibanos', 'CURITIBANOS', 'M', 'SC', 'SL', 0),
(4204905, 'Descanso', 'DESCANSO', 'M', 'SC', 'SL', 0),
(4205001, 'Dionísio Cerqueira', 'DIONISIO CERQUEIRA', 'M', 'SC', 'SL', 0),
(4205100, 'Dona Emma', 'DONA EMMA', 'M', 'SC', 'SL', 0),
(4205159, 'Doutor Pedrinho', 'DOUTOR PEDRINHO', 'M', 'SC', 'SL', 0),
(4205175, 'Entre Rios', 'ENTRE RIOS', 'M', 'SC', 'SL', 0),
(4205191, 'Ermo', 'ERMO', 'M', 'SC', 'SL', 0),
(4205209, 'Erval Velho', 'ERVAL VELHO', 'M', 'SC', 'SL', 0),
(4205308, 'Faxinal dos Guedes', 'FAXINAL DOS GUEDES', 'M', 'SC', 'SL', 0),
(4205357, 'Flor do Sertão', 'FLOR DO SERTAO', 'M', 'SC', 'SL', 0),
(4205407, 'Florianópolis', 'FLORIANOPOLIS', 'M', 'SC', 'SL', 0),
(4205431, 'Formosa do Sul', 'FORMOSA DO SUL', 'M', 'SC', 'SL', 0),
(4205456, 'Forquilhinha', 'FORQUILHINHA', 'M', 'SC', 'SL', 0),
(4205506, 'Fraiburgo', 'FRAIBURGO', 'M', 'SC', 'SL', 0),
(4205555, 'Frei Rogério', 'FREI ROGERIO', 'M', 'SC', 'SL', 0),
(4205605, 'Galvao', 'GALVAO', 'M', 'SC', 'SL', 0),
(4205704, 'Garopaba', 'GAROPABA', 'M', 'SC', 'SL', 0),
(4205803, 'Garuva', 'GARUVA', 'M', 'SC', 'SL', 0),
(4205902, 'Gaspar', 'GASPAR', 'M', 'SC', 'SL', 0),
(4206009, 'Governador Celso Ramos', 'GOVERNADOR CELSO RAMOS', 'M', 'SC', 'SL', 0),
(4206108, 'Grão Pará', 'GRAO PARA', 'M', 'SC', 'SL', 0),
(4206207, 'Gravatal', 'GRAVATAL', 'M', 'SC', 'SL', 0),
(4206306, 'Guabiruba', 'GUABIRUBA', 'M', 'SC', 'SL', 0),
(4206405, 'Guaraciaba', 'GUARACIABA', 'M', 'SC', 'SL', 0),
(4206504, 'Guaramirim', 'GUARAMIRIM', 'M', 'SC', 'SL', 0),
(4206603, 'Guaruja do Sul', 'GUARUJA DO SUL', 'M', 'SC', 'SL', 0),
(4206652, 'Guatambú', 'GUATAMBU', 'M', 'SC', 'SL', 0),
(4206702, 'Herval D''oeste', 'HERVAL D''OESTE', 'M', 'SC', 'SL', 0),
(4206751, 'Ibiam', 'IBIAM', 'M', 'SC', 'SL', 0),
(4206801, 'Ibicaré', 'IBICARE', 'M', 'SC', 'SL', 0),
(4206900, 'Ibirama', 'IBIRAMA', 'M', 'SC', 'SL', 0),
(4207007, 'Içara', 'ICARA', 'M', 'SC', 'SL', 0),
(4207106, 'Ilhota', 'ILHOTA', 'M', 'SC', 'SL', 0),
(4207205, 'Imaruí', 'IMARUI', 'M', 'SC', 'SL', 0),
(4207304, 'Imbituba', 'IMBITUBA', 'M', 'SC', 'SL', 0),
(4207403, 'Imbuia', 'IMBUIA', 'M', 'SC', 'SL', 0),
(4207502, 'Indaial', 'INDAIAL', 'M', 'SC', 'SL', 0),
(4207577, 'Iomerê', 'IOMERE', 'M', 'SC', 'SL', 0),
(4207601, 'Ipirá', 'IPIRA', 'M', 'SC', 'SL', 0),
(4207650, 'Iporã do Oeste', 'IPORA DO OESTE', 'M', 'SC', 'SL', 0),
(4207684, 'Ipuaçu', 'IPUACU', 'M', 'SC', 'SL', 0),
(4207700, 'Ipumirim', 'IPUMIRIM', 'M', 'SC', 'SL', 0),
(4207759, 'Iraceminha', 'IRACEMINHA', 'M', 'SC', 'SL', 0),
(4207809, 'Irani', 'IRANI', 'M', 'SC', 'SL', 0),
(4207858, 'Irati', 'IRATI', 'M', 'SC', 'SL', 0),
(4207908, 'Irineópolis', 'IRINEOPOLIS', 'M', 'SC', 'SL', 0),
(4208005, 'Itá', 'ITA', 'M', 'SC', 'SL', 0),
(4208104, 'Itaiópolis', 'ITAIOPOLIS', 'M', 'SC', 'SL', 0),
(4208203, 'Itajaí', 'ITAJAI', 'M', 'SC', 'SL', 0),
(4208302, 'Itapema', 'ITAPEMA', 'M', 'SC', 'SL', 0),
(4208401, 'Itapiranga', 'ITAPIRANGA', 'M', 'SC', 'SL', 0),
(4208450, 'Itapoá', 'ITAPOA', 'M', 'SC', 'SL', 0),
(4208500, 'Ituporanga', 'ITUPORANGA', 'M', 'SC', 'SL', 0),
(4208609, 'Jaborá', 'JABORA', 'M', 'SC', 'SL', 0),
(4208708, 'Jacinto Machado', 'JACINTO MACHADO', 'M', 'SC', 'SL', 0),
(4208807, 'Jaguaruna', 'JAGUARUNA', 'M', 'SC', 'SL', 0),
(4208906, 'Jaraguá do Sul', 'JARAGUA DO SUL', 'M', 'SC', 'SL', 0),
(4208955, 'Jardinópolis', 'JARDINOPOLIS', 'M', 'SC', 'SL', 0),
(4209003, 'Joaçaba', 'JOACABA', 'M', 'SC', 'SL', 0),
(4209102, 'Joinville', 'JOINVILLE', 'M', 'SC', 'SL', 0),
(4209151, 'José Boiteux', 'JOSE BOITEUX', 'M', 'SC', 'SL', 0),
(4209177, 'Jupiá', 'JUPIA', 'M', 'SC', 'SL', 0),
(4209201, 'Lacerdópolis', 'LACERDOPOLIS', 'M', 'SC', 'SL', 0),
(4209300, 'Lages', 'LAGES', 'M', 'SC', 'SL', 0),
(4209409, 'Laguna', 'LAGUNA', 'M', 'SC', 'SL', 0),
(4209458, 'Lajeado Grande', 'LAJEADO GRANDE', 'M', 'SC', 'SL', 0),
(4209508, 'Laurentino', 'LAURENTINO', 'M', 'SC', 'SL', 0),
(4209607, 'Lauro Muller', 'LAURO MULLER', 'M', 'SC', 'SL', 0),
(4209706, 'Lebon Régis', 'LEBON REGIS', 'M', 'SC', 'SL', 0),
(4209805, 'Leoberto Leal', 'LEOBERTO LEAL', 'M', 'SC', 'SL', 0),
(4209854, 'Lindóia do Sul', 'LINDOIA DO SUL', 'M', 'SC', 'SL', 0),
(4209904, 'Lontras', 'LONTRAS', 'M', 'SC', 'SL', 0),
(4210001, 'Luiz Alves', 'LUIZ ALVES', 'M', 'SC', 'SL', 0),
(4210035, 'Luzerna', 'LUZERNA', 'M', 'SC', 'SL', 0),
(4210050, 'Macieira', 'MACIEIRA', 'M', 'SC', 'SL', 0),
(4210100, 'Mafra', 'MAFRA', 'M', 'SC', 'SL', 0),
(4210209, 'Major Gercino', 'MAJOR GERCINO', 'M', 'SC', 'SL', 0),
(4210308, 'Major Vieira', 'MAJOR VIEIRA', 'M', 'SC', 'SL', 0),
(4210407, 'Maracajá', 'MARACAJA', 'M', 'SC', 'SL', 0),
(4210506, 'Maravilha', 'MARAVILHA', 'M', 'SC', 'SL', 0),
(4210555, 'Marema', 'MAREMA', 'M', 'SC', 'SL', 0),
(4210605, 'Massaranduba', 'MASSARANDUBA', 'M', 'SC', 'SL', 0),
(4210704, 'Matos Costa', 'MATOS COSTA', 'M', 'SC', 'SL', 0),
(4210803, 'Meleiro', 'MELEIRO', 'M', 'SC', 'SL', 0),
(4210852, 'Mirim Doce', 'MIRIM DOCE', 'M', 'SC', 'SL', 0),
(4210902, 'Modelo', 'MODELO', 'M', 'SC', 'SL', 0),
(4211009, 'Mondaí', 'MONDAI', 'M', 'SC', 'SL', 0),
(4211058, 'Monte Carlo', 'MONTE CARLO', 'M', 'SC', 'SL', 0),
(4211108, 'Monte Castelo', 'MONTE CASTELO', 'M', 'SC', 'SL', 0),
(4211207, 'Morro da Fumaca', 'MORRO DA FUMACA', 'M', 'SC', 'SL', 0),
(4211256, 'Morro Grande', 'MORRO GRANDE', 'M', 'SC', 'SL', 0),
(4211306, 'Navegantes', 'NAVEGANTES', 'M', 'SC', 'SL', 0),
(4211405, 'Nova Erechim', 'NOVA ERECHIM', 'M', 'SC', 'SL', 0),
(4211454, 'Nova Itaberaba', 'NOVA ITABERABA', 'M', 'SC', 'SL', 0),
(4211504, 'Nova Trento', 'NOVA TRENTO', 'M', 'SC', 'SL', 0),
(4211603, 'Nova Veneza', 'NOVA VENEZA', 'M', 'SC', 'SL', 0),
(4211652, 'Novo Horizonte', 'NOVO HORIZONTE', 'M', 'SC', 'SL', 0),
(4211702, 'Orleans', 'ORLEANS', 'M', 'SC', 'SL', 0),
(4211751, 'Otacílio Costa', 'OTACILIO COSTA', 'M', 'SC', 'SL', 0),
(4211801, 'Ouro', 'OURO', 'M', 'SC', 'SL', 0),
(4211850, 'Ouro Verde', 'OURO VERDE', 'M', 'SC', 'SL', 0),
(4211876, 'Paial', 'PAIAL', 'M', 'SC', 'SL', 0),
(4211892, 'Painel', 'PAINEL', 'M', 'SC', 'SL', 0),
(4211900, 'Palhoça', 'PALHOCA', 'M', 'SC', 'SL', 0),
(4212007, 'Palma Sola', 'PALMA SOLA', 'M', 'SC', 'SL', 0),
(4212056, 'Palmeira', 'PALMEIRA', 'M', 'SC', 'SL', 0),
(4212106, 'Palmitos', 'PALMITOS', 'M', 'SC', 'SL', 0),
(4212205, 'Papanduva', 'PAPANDUVA', 'M', 'SC', 'SL', 0),
(4212239, 'Paraíso', 'PARAISO', 'M', 'SC', 'SL', 0),
(4212254, 'Passo de Torres', 'PASSO DE TORRES', 'M', 'SC', 'SL', 0),
(4212270, 'Passos Maia', 'PASSOS MAIA', 'M', 'SC', 'SL', 0),
(4212304, 'Paulo Lopes', 'PAULO LOPES', 'M', 'SC', 'SL', 0),
(4212403, 'Pedras Grandes', 'PEDRAS GRANDES', 'M', 'SC', 'SL', 0),
(4212502, 'Penha', 'PENHA', 'M', 'SC', 'SL', 0),
(4212601, 'Peritiba', 'PERITIBA', 'M', 'SC', 'SL', 0),
(4212700, 'Petrolândia', 'PETROLANDIA', 'M', 'SC', 'SL', 0),
(4212809, 'Piçarras', 'PICARRAS', 'M', 'SC', 'SL', 0),
(4212908, 'Pinhalzinho', 'PINHALZINHO', 'M', 'SC', 'SL', 0),
(4213005, 'Pinheiro Preto', 'PINHEIRO PRETO', 'M', 'SC', 'SL', 0),
(4213104, 'Piratuba', 'PIRATUBA', 'M', 'SC', 'SL', 0),
(4213153, 'Planalto Alegre', 'PLANALTO ALEGRE', 'M', 'SC', 'SL', 0),
(4213203, 'Pomerode', 'POMERODE', 'M', 'SC', 'SL', 0),
(4213302, 'Ponte Alta', 'PONTE ALTA', 'M', 'SC', 'SL', 0),
(4213351, 'Ponte Alta do Norte', 'PONTE ALTA DO NORTE', 'M', 'SC', 'SL', 0),
(4213401, 'Ponte Serrada', 'PONTE SERRADA', 'M', 'SC', 'SL', 0),
(4213500, 'Porto Belo', 'PORTO BELO', 'M', 'SC', 'SL', 0),
(4213609, 'Porto União', 'PORTO UNIAO', 'M', 'SC', 'SL', 0),
(4213708, 'Pouso Redondo', 'POUSO REDONDO', 'M', 'SC', 'SL', 0),
(4213807, 'Praia Grande', 'PRAIA GRANDE', 'M', 'SC', 'SL', 0),
(4213906, 'Presidente Castelo Branco', 'PRESIDENTE CASTELO BRANCO', 'M', 'SC', 'SL', 0),
(4214003, 'Presidente Getúlio', 'PRESIDENTE GETULIO', 'M', 'SC', 'SL', 0),
(4214102, 'Presidente Nereu', 'PRESIDENTE NEREU', 'M', 'SC', 'SL', 0),
(4214151, 'Princesa', 'PRINCESA', 'M', 'SC', 'SL', 0),
(4214201, 'Quilombo', 'QUILOMBO', 'M', 'SC', 'SL', 0),
(4214300, 'Rancho Queimado', 'RANCHO QUEIMADO', 'M', 'SC', 'SL', 0),
(4214409, 'Rio das Antas', 'RIO DAS ANTAS', 'M', 'SC', 'SL', 0),
(4214508, 'Rio do Campo', 'RIO DO CAMPO', 'M', 'SC', 'SL', 0),
(4214607, 'Rio do Oeste', 'RIO DO OESTE', 'M', 'SC', 'SL', 0),
(4214706, 'Rio dos Cedros', 'RIO DOS CEDROS', 'M', 'SC', 'SL', 0),
(4214805, 'Rio do Sul', 'RIO DO SUL', 'M', 'SC', 'SL', 0),
(4214904, 'Rio Fortuna', 'RIO FORTUNA', 'M', 'SC', 'SL', 0),
(4215000, 'Rio Negrinho', 'RIO NEGRINHO', 'M', 'SC', 'SL', 0),
(4215059, 'Rio Rufino', 'RIO RUFINO', 'M', 'SC', 'SL', 0),
(4215075, 'Riqueza', 'RIQUEZA', 'M', 'SC', 'SL', 0),
(4215109, 'Rodeio', 'RODEIO', 'M', 'SC', 'SL', 0),
(4215208, 'Romelândia', 'ROMELANDIA', 'M', 'SC', 'SL', 0),
(4215307, 'Salete', 'SALETE', 'M', 'SC', 'SL', 0),
(4215356, 'Saltinho', 'SALTINHO', 'M', 'SC', 'SL', 0),
(4215406, 'Salto Veloso', 'SALTO VELOSO', 'M', 'SC', 'SL', 0),
(4215455, 'Sangao', 'SANGAO', 'M', 'SC', 'SL', 0),
(4215505, 'Santa Cecília', 'SANTA CECILIA', 'M', 'SC', 'SL', 0),
(4215554, 'Santa Helena', 'SANTA HELENA', 'M', 'SC', 'SL', 0),
(4215604, 'Santa Rosa de Lima', 'SANTA ROSA DE LIMA', 'M', 'SC', 'SL', 0),
(4215653, 'Santa Rosa do Sul', 'SANTA ROSA DO SUL', 'M', 'SC', 'SL', 0),
(4215679, 'Santa Terezinha', 'SANTA TEREZINHA', 'M', 'SC', 'SL', 0),
(4215687, 'Santa Terezinha do Progresso', 'SANTA TEREZINHA DO PROGRESSO', 'M', 'SC', 'SL', 0),
(4215695, 'Santiago do Sul', 'SANTIAGO DO SUL', 'M', 'SC', 'SL', 0),
(4215703, 'Santo Amaro da Imperatriz', 'SANTO AMARO DA IMPERATRIZ', 'M', 'SC', 'SL', 0),
(4215752, 'São Bernardino', 'SAO BERNARDINO', 'M', 'SC', 'SL', 0),
(4215802, 'São Bento do Sul', 'SAO BENTO DO SUL', 'M', 'SC', 'SL', 0),
(4215901, 'São Bonifácio', 'SAO BONIFACIO', 'M', 'SC', 'SL', 0),
(4216008, 'São Carlos', 'SAO CARLOS', 'M', 'SC', 'SL', 0),
(4216057, 'São Cristovão do Sul', 'SAO CRISTOVAO DO SUL', 'M', 'SC', 'SL', 0),
(4216107, 'São Domingos', 'SAO DOMINGOS', 'M', 'SC', 'SL', 0),
(4216206, 'São Francisco do Sul', 'SAO FRANCISCO DO SUL', 'M', 'SC', 'SL', 0),
(4216255, 'São João', 'SAO JOAO', 'M', 'SC', 'SL', 0),
(4216305, 'São João Batista', 'SAO JOAO BATISTA', 'M', 'SC', 'SL', 0),
(4216354, 'São João do Itaperiu', 'SAO JOAO DO ITAPERIU', 'M', 'SC', 'SL', 0),
(4216404, 'São João do Sul', 'SAO JOAO DO SUL', 'M', 'SC', 'SL', 0),
(4216503, 'São Joaquim', 'SAO JOAQUIM', 'M', 'SC', 'SL', 0),
(4216602, 'São José', 'SAO JOSE', 'M', 'SC', 'SL', 0),
(4216701, 'São José do Cedro', 'SAO JOSE DO CEDRO', 'M', 'SC', 'SL', 0),
(4216800, 'São José do Cerrito', 'SAO JOSE DO CERRITO', 'M', 'SC', 'SL', 0),
(4216909, 'São Lourenço do Oeste', 'SAO LOURENCO DO OESTE', 'M', 'SC', 'SL', 0),
(4217006, 'São Ludgero', 'SAO LUDGERO', 'M', 'SC', 'SL', 0),
(4217105, 'São Martinho', 'SAO MARTINHO', 'M', 'SC', 'SL', 0),
(4217154, 'São Miguel da Boa Vista', 'SAO MIGUEL DA BOA VISTA', 'M', 'SC', 'SL', 0),
(4217204, 'São Miguel d´Oeste', 'SAO MIGUEL D´OESTE', 'M', 'SC', 'SL', 0),
(4217253, 'São Pedro de Alcântara', 'SAO PEDRO DE ALCANTARA', 'M', 'SC', 'SL', 0),
(4217303, 'Saudades', 'SAUDADES', 'M', 'SC', 'SL', 0),
(4217402, 'Schroeder', 'SCHROEDER', 'M', 'SC', 'SL', 0),
(4217501, 'Seara', 'SEARA', 'M', 'SC', 'SL', 0),
(4217550, 'Serra Alta', 'SERRA ALTA', 'M', 'SC', 'SL', 0),
(4217600, 'Siderópolis', 'SIDEROPOLIS', 'M', 'SC', 'SL', 0),
(4217709, 'Sombrio', 'SOMBRIO', 'M', 'SC', 'SL', 0),
(4217758, 'Sul Brasil', 'SUL BRASIL', 'M', 'SC', 'SL', 0),
(4217808, 'Taió', 'TAIO', 'M', 'SC', 'SL', 0),
(4217907, 'Tangará', 'TANGARA', 'M', 'SC', 'SL', 0),
(4217956, 'Tigrinhos', 'TIGRINHOS', 'M', 'SC', 'SL', 0),
(4218004, 'Tijucas', 'TIJUCAS', 'M', 'SC', 'SL', 0),
(4218103, 'Timbé do Sul', 'TIMBE DO SUL', 'M', 'SC', 'SL', 0),
(4218202, 'Timbó', 'TIMBO', 'M', 'SC', 'SL', 0),
(4218251, 'Timbó Grande', 'TIMBO GRANDE', 'M', 'SC', 'SL', 0),
(4218301, 'Três Barras', 'TRES BARRAS', 'M', 'SC', 'SL', 0),
(4218350, 'Treviso', 'TREVISO', 'M', 'SC', 'SL', 0),
(4218400, 'Treze de Maio', 'TREZE DE MAIO', 'M', 'SC', 'SL', 0),
(4218509, 'Treze Tilias', 'TREZE TILIAS', 'M', 'SC', 'SL', 0),
(4218608, 'Trombudo Central', 'TROMBUDO CENTRAL', 'M', 'SC', 'SL', 0),
(4218707, 'Tubarão', 'TUBARAO', 'M', 'SC', 'SL', 0),
(4218756, 'Tunápolis', 'TUNAPOLIS', 'M', 'SC', 'SL', 0),
(4218806, 'Turvo', 'TURVO', 'M', 'SC', 'SL', 0),
(4218855, 'União do Oeste', 'UNIAO DO OESTE', 'M', 'SC', 'SL', 0),
(4218905, 'Urubici', 'URUBICI', 'M', 'SC', 'SL', 0),
(4218954, 'Urupema', 'URUPEMA', 'M', 'SC', 'SL', 0),
(4219002, 'Urussanga', 'URUSSANGA', 'M', 'SC', 'SL', 0),
(4219101, 'Vargeão', 'VARGEAO', 'M', 'SC', 'SL', 0),
(4219150, 'Vargem', 'VARGEM', 'M', 'SC', 'SL', 0),
(4219176, 'Vargem Bonita', 'VARGEM BONITA', 'M', 'SC', 'SL', 0),
(4219200, 'Vidal Ramos', 'VIDAL RAMOS', 'M', 'SC', 'SL', 0),
(4219309, 'Videira', 'VIDEIRA', 'M', 'SC', 'SL', 0),
(4219358, 'Vitor Meireles', 'VITOR MEIRELES', 'M', 'SC', 'SL', 0),
(4219408, 'Witmarsum', 'WITMARSUM', 'M', 'SC', 'SL', 0),
(4219507, 'Xanxerê', 'XANXERE', 'M', 'SC', 'SL', 0),
(4219606, 'Xavantina', 'XAVANTINA', 'M', 'SC', 'SL', 0),
(4219705, 'Xaxim', 'XAXIM', 'M', 'SC', 'SL', 0),
(4219853, 'Zortéa', 'ZORTEA', 'M', 'SC', 'SL', 0),
(4300000, 'Rio Grande do Sul', 'RIO GRANDE DO SUL', 'U', 'RS', 'SL', 0),
(4300034, 'Aceguá', 'ACEGUA', 'M', 'RS', 'SL', 0),
(4300059, 'Água Santa', 'AGUA SANTA', 'M', 'RS', 'SL', 0),
(4300109, 'Agudo', 'AGUDO', 'M', 'RS', 'SL', 0),
(4300208, 'Ajuricaba', 'AJURICABA', 'M', 'RS', 'SL', 0),
(4300307, 'Alecrim', 'ALECRIM', 'M', 'RS', 'SL', 0),
(4300406, 'Alegrete', 'ALEGRETE', 'M', 'RS', 'SL', 0),
(4300455, 'Alegria', 'ALEGRIA', 'M', 'RS', 'SL', 0),
(4300471, 'Almirante Tamandaré do Sul', 'ALMIRANTE TAMANDARE DO SUL', 'M', 'RS', 'SL', 0),
(4300505, 'Alpestre', 'ALPESTRE', 'M', 'RS', 'SL', 0),
(4300554, 'Alto Alegre', 'ALTO ALEGRE', 'M', 'RS', 'SL', 0),
(4300570, 'Alto Feliz', 'ALTO FELIZ', 'M', 'RS', 'SL', 0),
(4300604, 'Alvorada', 'ALVORADA', 'M', 'RS', 'SL', 0),
(4300638, 'Amaral Ferrador', 'AMARAL FERRADOR', 'M', 'RS', 'SL', 0),
(4300646, 'Ametista do Sul', 'AMETISTA DO SUL', 'M', 'RS', 'SL', 0),
(4300661, 'André da Rocha', 'ANDRE DA ROCHA', 'M', 'RS', 'SL', 0),
(4300703, 'Anta Gorda', 'ANTA GORDA', 'M', 'RS', 'SL', 0),
(4300802, 'Antônio Prado', 'ANTONIO PRADO', 'M', 'RS', 'SL', 0),
(4300851, 'Arambare', 'ARAMBARE', 'M', 'RS', 'SL', 0),
(4300877, 'Araricá', 'ARARICA', 'M', 'RS', 'SL', 0),
(4300901, 'Aratiba', 'ARATIBA', 'M', 'RS', 'SL', 0),
(4301008, 'Arroio do Meio', 'ARROIO DO MEIO', 'M', 'RS', 'SL', 0),
(4301057, 'Arroio do Sal', 'ARROIO DO SAL', 'M', 'RS', 'SL', 0),
(4301073, 'Arroio do Padre', 'ARROIO DO PADRE', 'M', 'RS', 'SL', 0),
(4301107, 'Arroio dos Ratos', 'ARROIO DOS RATOS', 'M', 'RS', 'SL', 0),
(4301206, 'Arroio do Tigre', 'ARROIO DO TIGRE', 'M', 'RS', 'SL', 0),
(4301305, 'Arroio Grande', 'ARROIO GRANDE', 'M', 'RS', 'SL', 0),
(4301404, 'Arvorezinha', 'ARVOREZINHA', 'M', 'RS', 'SL', 0),
(4301503, 'Augusto Pestana', 'AUGUSTO PESTANA', 'M', 'RS', 'SL', 0),
(4301552, 'Áurea', 'AUREA', 'M', 'RS', 'SL', 0),
(4301602, 'Bagé', 'BAGE', 'M', 'RS', 'SL', 0),
(4301636, 'Balneario Pinhal', 'BALNEARIO PINHAL', 'M', 'RS', 'SL', 0),
(4301651, 'Barao', 'BARAO', 'M', 'RS', 'SL', 0),
(4301701, 'Barao de Cotegipe', 'BARAO DE COTEGIPE', 'M', 'RS', 'SL', 0),
(4301750, 'Barao do Triunfo', 'BARAO DO TRIUNFO', 'M', 'RS', 'SL', 0),
(4301800, 'Barracão', 'BARRACAO', 'M', 'RS', 'SL', 0),
(4301859, 'Barra do Guarita', 'BARRA DO GUARITA', 'M', 'RS', 'SL', 0),
(4301875, 'Barra do Quaraí', 'BARRA DO QUARAI', 'M', 'RS', 'SL', 0),
(4301909, 'Barra do Ribeiro', 'BARRA DO RIBEIRO', 'M', 'RS', 'SL', 0),
(4301925, 'Barra do Rio Azul', 'BARRA DO RIO AZUL', 'M', 'RS', 'SL', 0),
(4301958, 'Barra Funda', 'BARRA FUNDA', 'M', 'RS', 'SL', 0),
(4302006, 'Barros Cassal', 'BARROS CASSAL', 'M', 'RS', 'SL', 0),
(4302055, 'Benjamin Constant do Sul', 'BENJAMIN CONSTANT DO SUL', 'M', 'RS', 'SL', 0),
(4302105, 'Bento Gonçalves', 'BENTO GONCALVES', 'M', 'RS', 'SL', 0),
(4302154, 'Boa Vista das Missões', 'BOA VISTA DAS MISSOES', 'M', 'RS', 'SL', 0),
(4302204, 'Boa Vista do Buricá', 'BOA VISTA DO BURICA', 'M', 'RS', 'SL', 0),
(4302220, 'Boa Vista do Cadeado', 'BOA VISTA DO CADEADO', 'M', 'RS', 'SL', 0),
(4302238, 'Boa Vista do Incra', 'BOA VISTA DO INCRA', 'M', 'RS', 'SL', 0),
(4302253, 'Boa Vista do Sul', 'BOA VISTA DO SUL', 'M', 'RS', 'SL', 0),
(4302303, 'Bom Jesus', 'BOM JESUS', 'M', 'RS', 'SL', 0),
(4302352, 'Bom Princípio', 'BOM PRINCIPIO', 'M', 'RS', 'SL', 0),
(4302378, 'Bom Progresso', 'BOM PROGRESSO', 'M', 'RS', 'SL', 0),
(4302402, 'Bom Retiro do Sul', 'BOM RETIRO DO SUL', 'M', 'RS', 'SL', 0),
(4302451, 'Boqueirão do Leão', 'BOQUEIRAO DO LEAO', 'M', 'RS', 'SL', 0),
(4302501, 'Bossoroca', 'BOSSOROCA', 'M', 'RS', 'SL', 0),
(4302584, 'Bozano', 'BOZANO', 'M', 'RS', 'SL', 0),
(4302600, 'Braga', 'BRAGA', 'M', 'RS', 'SL', 0),
(4302659, 'Brochier do Marata', 'BROCHIER DO MARATA', 'M', 'RS', 'SL', 0),
(4302709, 'Butiá', 'BUTIA', 'M', 'RS', 'SL', 0),
(4302808, 'Cacapava do Sul', 'CACAPAVA DO SUL', 'M', 'RS', 'SL', 0),
(4302907, 'Cacequi', 'CACEQUI', 'M', 'RS', 'SL', 0),
(4303004, 'Cachoeira do Sul', 'CACHOEIRA DO SUL', 'M', 'RS', 'SL', 0),
(4303103, 'Cachoeirinha', 'CACHOEIRINHA', 'M', 'RS', 'SL', 0),
(4303202, 'Cacique Doble', 'CACIQUE DOBLE', 'M', 'RS', 'SL', 0),
(4303301, 'Caibaté', 'CAIBATE', 'M', 'RS', 'SL', 0),
(4303400, 'Caiçara', 'CAICARA', 'M', 'RS', 'SL', 0),
(4303509, 'Camaquã', 'CAMAQUA', 'M', 'RS', 'SL', 0),
(4303558, 'Camargo', 'CAMARGO', 'M', 'RS', 'SL', 0),
(4303608, 'Cambará do Sul', 'CAMBARA DO SUL', 'M', 'RS', 'SL', 0),
(4303673, 'Campestre da Serra', 'CAMPESTRE DA SERRA', 'M', 'RS', 'SL', 0),
(4303707, 'Campina das Missões', 'CAMPINA DAS MISSOES', 'M', 'RS', 'SL', 0),
(4303806, 'Campinas do Sul', 'CAMPINAS DO SUL', 'M', 'RS', 'SL', 0),
(4303905, 'Campo Bom', 'CAMPO BOM', 'M', 'RS', 'SL', 0),
(4304002, 'Campo Novo', 'CAMPO NOVO', 'M', 'RS', 'SL', 0),
(4304101, 'Campos Borges', 'CAMPOS BORGES', 'M', 'RS', 'SL', 0),
(4304200, 'Candelária', 'CANDELARIA', 'M', 'RS', 'SL', 0),
(4304309, 'Cândido Godói', 'CANDIDO GODOI', 'M', 'RS', 'SL', 0),
(4304358, 'Candiota', 'CANDIOTA', 'M', 'RS', 'SL', 0),
(4304408, 'Canela', 'CANELA', 'M', 'RS', 'SL', 0),
(4304507, 'Canguçu', 'CANGUCU', 'M', 'RS', 'SL', 0),
(4304606, 'Canoas', 'CANOAS', 'M', 'RS', 'SL', 0),
(4304614, 'Canudos do Vale', 'CANUDOS DO VALE', 'M', 'RS', 'SL', 0),
(4304622, 'Capão Bonito do Sul', 'CAPAO BONITO DO SUL', 'M', 'RS', 'SL', 0),
(4304630, 'Capão da Canoa', 'CAPAO DA CANOA', 'M', 'RS', 'SL', 0),
(4304655, 'Capão do Cipó', 'CAPAO DO CIPO', 'M', 'RS', 'SL', 0),
(4304663, 'Capão do Leão', 'CAPAO DO LEAO', 'M', 'RS', 'SL', 0),
(4304671, 'Capivari do Sul', 'CAPIVARI DO SUL', 'M', 'RS', 'SL', 0),
(4304689, 'Capela de Santana', 'CAPELA DE SANTANA', 'M', 'RS', 'SL', 0),
(4304697, 'Capitão', 'CAPITAO', 'M', 'RS', 'SL', 0),
(4304705, 'Carazinho', 'CARAZINHO', 'M', 'RS', 'SL', 0),
(4304713, 'Caraá', 'CARAA', 'M', 'RS', 'SL', 0),
(4304804, 'Carlos Barbosa', 'CARLOS BARBOSA', 'M', 'RS', 'SL', 0),
(4304853, 'Carlos Gomes', 'CARLOS GOMES', 'M', 'RS', 'SL', 0),
(4304903, 'Casca', 'CASCA', 'M', 'RS', 'SL', 0),
(4304952, 'Caseiros', 'CASEIROS', 'M', 'RS', 'SL', 0),
(4305009, 'Catuípe', 'CATUIPE', 'M', 'RS', 'SL', 0),
(4305108, 'Caxias do Sul', 'CAXIAS DO SUL', 'M', 'RS', 'SL', 0),
(4305116, 'Centenário', 'CENTENARIO', 'M', 'RS', 'SL', 0),
(4305124, 'Cerrito', 'CERRITO', 'M', 'RS', 'SL', 0),
(4305132, 'Cerro Branco', 'CERRO BRANCO', 'M', 'RS', 'SL', 0),
(4305157, 'Cerro Grande', 'CERRO GRANDE', 'M', 'RS', 'SL', 0),
(4305173, 'Cerro Grande do Sul', 'CERRO GRANDE DO SUL', 'M', 'RS', 'SL', 0),
(4305207, 'Cerro Largo', 'CERRO LARGO', 'M', 'RS', 'SL', 0),
(4305306, 'Chapada', 'CHAPADA', 'M', 'RS', 'SL', 0),
(4305355, 'Charqueadas', 'CHARQUEADAS', 'M', 'RS', 'SL', 0),
(4305371, 'Charrua', 'CHARRUA', 'M', 'RS', 'SL', 0),
(4305405, 'Chiapeta', 'CHIAPETA', 'M', 'RS', 'SL', 0),
(4305439, 'Chuí', 'CHUI', 'M', 'RS', 'SL', 0),
(4305447, 'Chuvisca', 'CHUVISCA', 'M', 'RS', 'SL', 0),
(4305454, 'Cidreira', 'CIDREIRA', 'M', 'RS', 'SL', 0),
(4305504, 'Ciriaco', 'CIRIACO', 'M', 'RS', 'SL', 0),
(4305587, 'Colinas', 'COLINAS', 'M', 'RS', 'SL', 0),
(4305603, 'Colorado', 'COLORADO', 'M', 'RS', 'SL', 0),
(4305702, 'Condor', 'CONDOR', 'M', 'RS', 'SL', 0),
(4305801, 'Constantina', 'CONSTANTINA', 'M', 'RS', 'SL', 0),
(4305835, 'Coqueiro Baixo', 'COQUEIRO BAIXO', 'M', 'RS', 'SL', 0),
(4305850, 'Coqueiros do Sul', 'COQUEIROS DO SUL', 'M', 'RS', 'SL', 0),
(4305871, 'Coronel Barros', 'CORONEL BARROS', 'M', 'RS', 'SL', 0),
(4305900, 'Coronel Bicaco', 'CORONEL BICACO', 'M', 'RS', 'SL', 0),
(4305934, 'Coronel Pilar', 'CORONEL PILAR', 'M', 'RS', 'SL', 0),
(4305959, 'Cotiporã', 'COTIPORA', 'M', 'RS', 'SL', 0),
(4305975, 'Coxilha', 'COXILHA', 'M', 'RS', 'SL', 0),
(4306007, 'Crissiumal', 'CRISSIUMAL', 'M', 'RS', 'SL', 0),
(4306056, 'Cristal', 'CRISTAL', 'M', 'RS', 'SL', 0),
(4306072, 'Cristal do Sul', 'CRISTAL DO SUL', 'M', 'RS', 'SL', 0),
(4306106, 'Cruz Alta', 'CRUZ ALTA', 'M', 'RS', 'SL', 0),
(4306130, 'Cruzaltense', 'CRUZALTENSE', 'M', 'RS', 'SL', 0),
(4306205, 'Cruzeiro do Sul', 'CRUZEIRO DO SUL', 'M', 'RS', 'SL', 0),
(4306304, 'David Canabarro', 'DAVID CANABARRO', 'M', 'RS', 'SL', 0),
(4306320, 'Derrubadas', 'DERRUBADAS', 'M', 'RS', 'SL', 0),
(4306353, 'Dezesseis de Novembro', 'DEZESSEIS DE NOVEMBRO', 'M', 'RS', 'SL', 0),
(4306379, 'Dilermando de Aguiar', 'DILERMANDO DE AGUIAR', 'M', 'RS', 'SL', 0),
(4306403, 'Dois Irmãos', 'DOIS IRMAOS', 'M', 'RS', 'SL', 0),
(4306429, 'Dois Irmãos das Missoes', 'DOIS IRMAOS DAS MISSOES', 'M', 'RS', 'SL', 0),
(4306452, 'Dois Lajeados', 'DOIS LAJEADOS', 'M', 'RS', 'SL', 0),
(4306502, 'Dom Feliciano', 'DOM FELICIANO', 'M', 'RS', 'SL', 0),
(4306551, 'Dom Pedro de Alcântara', 'DOM PEDRO DE ALCANTARA', 'M', 'RS', 'SL', 0),
(4306601, 'Dom Pedrito', 'DOM PEDRITO', 'M', 'RS', 'SL', 0),
(4306700, 'Dona Francisca', 'DONA FRANCISCA', 'M', 'RS', 'SL', 0),
(4306734, 'Doutor Maurício Cardoso', 'DOUTOR MAURICIO CARDOSO', 'M', 'RS', 'SL', 0),
(4306759, 'Doutor Ricardo', 'DOUTOR RICARDO', 'M', 'RS', 'SL', 0),
(4306767, 'Eldorado do Sul', 'ELDORADO DO SUL', 'M', 'RS', 'SL', 0),
(4306809, 'Encantado', 'ENCANTADO', 'M', 'RS', 'SL', 0),
(4306908, 'Encruzilhada do Sul', 'ENCRUZILHADA DO SUL', 'M', 'RS', 'SL', 0),
(4306924, 'Engenho Velho', 'ENGENHO VELHO', 'M', 'RS', 'SL', 0),
(4306932, 'Entre-Ijuís', 'ENTRE-IJUIS', 'M', 'RS', 'SL', 0),
(4306957, 'Entre Rios do Sul', 'ENTRE RIOS DO SUL', 'M', 'RS', 'SL', 0),
(4306973, 'Erebango', 'EREBANGO', 'M', 'RS', 'SL', 0),
(4307005, 'Erechim', 'ERECHIM', 'M', 'RS', 'SL', 0),
(4307054, 'Ernestina', 'ERNESTINA', 'M', 'RS', 'SL', 0),
(4307104, 'Herval', 'HERVAL', 'M', 'RS', 'SL', 0),
(4307203, 'Erval Grande', 'ERVAL GRANDE', 'M', 'RS', 'SL', 0),
(4307302, 'Erval Seco', 'ERVAL SECO', 'M', 'RS', 'SL', 0),
(4307401, 'Esmeralda', 'ESMERALDA', 'M', 'RS', 'SL', 0),
(4307450, 'Esperança do Sul', 'ESPERANCA DO SUL', 'M', 'RS', 'SL', 0),
(4307500, 'Espumoso', 'ESPUMOSO', 'M', 'RS', 'SL', 0),
(4307559, 'Estacao', 'ESTACAO', 'M', 'RS', 'SL', 0),
(4307609, 'Estância Velha', 'ESTANCIA VELHA', 'M', 'RS', 'SL', 0),
(4307708, 'Esteio', 'ESTEIO', 'M', 'RS', 'SL', 0),
(4307807, 'Estrela', 'ESTRELA', 'M', 'RS', 'SL', 0),
(4307815, 'Estrela Velha', 'ESTRELA VELHA', 'M', 'RS', 'SL', 0),
(4307831, 'Eugênio de Castro', 'EUGENIO DE CASTRO', 'M', 'RS', 'SL', 0),
(4307864, 'Fagundes Varela', 'FAGUNDES VARELA', 'M', 'RS', 'SL', 0),
(4307906, 'Farroupilha', 'FARROUPILHA', 'M', 'RS', 'SL', 0),
(4308003, 'Faxinal do Soturno', 'FAXINAL DO SOTURNO', 'M', 'RS', 'SL', 0),
(4308052, 'Faxinalzinho', 'FAXINALZINHO', 'M', 'RS', 'SL', 0),
(4308078, 'Fazenda Vilanova', 'FAZENDA VILANOVA', 'M', 'RS', 'SL', 0),
(4308102, 'Feliz', 'FELIZ', 'M', 'RS', 'SL', 0),
(4308201, 'Flores da Cunha', 'FLORES DA CUNHA', 'M', 'RS', 'SL', 0),
(4308250, 'Floriano Peixoto', 'FLORIANO PEIXOTO', 'M', 'RS', 'SL', 0),
(4308300, 'Fontoura Xavier', 'FONTOURA XAVIER', 'M', 'RS', 'SL', 0),
(4308409, 'Formigueiro', 'FORMIGUEIRO', 'M', 'RS', 'SL', 0),
(4308433, 'Forquetinha', 'FORQUETINHA', 'M', 'RS', 'SL', 0),
(4308458, 'Fortaleza dos Valos', 'FORTALEZA DOS VALOS', 'M', 'RS', 'SL', 0),
(4308508, 'Frederico Westphalen', 'FREDERICO WESTPHALEN', 'M', 'RS', 'SL', 0),
(4308607, 'Garibaldi', 'GARIBALDI', 'M', 'RS', 'SL', 0),
(4308656, 'Garruchos', 'GARRUCHOS', 'M', 'RS', 'SL', 0),
(4308706, 'Gaurama', 'GAURAMA', 'M', 'RS', 'SL', 0),
(4308805, 'General Câmara', 'GENERAL CAMARA', 'M', 'RS', 'SL', 0),
(4308854, 'Gentil', 'GENTIL', 'M', 'RS', 'SL', 0),
(4308904, 'Getúlio Vargas', 'GETULIO VARGAS', 'M', 'RS', 'SL', 0),
(4309001, 'Giruá', 'GIRUA', 'M', 'RS', 'SL', 0),
(4309050, 'Glorinha', 'GLORINHA', 'M', 'RS', 'SL', 0),
(4309100, 'Gramado', 'GRAMADO', 'M', 'RS', 'SL', 0),
(4309126, 'Gramado dos Loureiros', 'GRAMADO DOS LOUREIROS', 'M', 'RS', 'SL', 0),
(4309159, 'Gramado Xavier', 'GRAMADO XAVIER', 'M', 'RS', 'SL', 0),
(4309209, 'Gravataí', 'GRAVATAI', 'M', 'RS', 'SL', 0),
(4309258, 'Guabiju', 'GUABIJU', 'M', 'RS', 'SL', 0),
(4309308, 'Guaíba', 'GUAIBA', 'M', 'RS', 'SL', 0),
(4309407, 'Guaporé', 'GUAPORE', 'M', 'RS', 'SL', 0),
(4309506, 'Guarani das Missões', 'GUARANI DAS MISSOES', 'M', 'RS', 'SL', 0),
(4309555, 'Harmonia', 'HARMONIA', 'M', 'RS', 'SL', 0),
(4309571, 'Herveiras', 'HERVEIRAS', 'M', 'RS', 'SL', 0),
(4309605, 'Horizontina', 'HORIZONTINA', 'M', 'RS', 'SL', 0),
(4309654, 'Hulha Negra', 'HULHA NEGRA', 'M', 'RS', 'SL', 0),
(4309704, 'Humaitá', 'HUMAITA', 'M', 'RS', 'SL', 0),
(4309753, 'Ibarama', 'IBARAMA', 'M', 'RS', 'SL', 0),
(4309803, 'Ibiaçá', 'IBIACA', 'M', 'RS', 'SL', 0),
(4309902, 'Ibiraiaras', 'IBIRAIARAS', 'M', 'RS', 'SL', 0),
(4309951, 'Ibirapuitã', 'IBIRAPUITA', 'M', 'RS', 'SL', 0),
(4310009, 'Ibiruba', 'IBIRUBA', 'M', 'RS', 'SL', 0),
(4310108, 'Igrejinha', 'IGREJINHA', 'M', 'RS', 'SL', 0),
(4310207, 'Ijuí', 'IJUI', 'M', 'RS', 'SL', 0),
(4310306, 'Ilópolis', 'ILOPOLIS', 'M', 'RS', 'SL', 0),
(4310330, 'Imbé', 'IMBE', 'M', 'RS', 'SL', 0),
(4310363, 'Imigrante', 'IMIGRANTE', 'M', 'RS', 'SL', 0),
(4310405, 'Independência', 'INDEPENDENCIA', 'M', 'RS', 'SL', 0),
(4310413, 'Inhacorá', 'INHACORA', 'M', 'RS', 'SL', 0),
(4310439, 'Ipê', 'IPE', 'M', 'RS', 'SL', 0),
(4310462, 'Ipiranga do Sul', 'IPIRANGA DO SUL', 'M', 'RS', 'SL', 0),
(4310504, 'Iraí', 'IRAI', 'M', 'RS', 'SL', 0),
(4310538, 'Itaara', 'ITAARA', 'M', 'RS', 'SL', 0),
(4310553, 'Itacurubi', 'ITACURUBI', 'M', 'RS', 'SL', 0),
(4310579, 'Itapuca', 'ITAPUCA', 'M', 'RS', 'SL', 0),
(4310603, 'Itaqui', 'ITAQUI', 'M', 'RS', 'SL', 0),
(4310652, 'Itati', 'ITATI', 'M', 'RS', 'SL', 0),
(4310702, 'Itatiba do Sul', 'ITATIBA DO SUL', 'M', 'RS', 'SL', 0),
(4310751, 'Ivorá', 'IVORA', 'M', 'RS', 'SL', 0),
(4310801, 'Ivoti', 'IVOTI', 'M', 'RS', 'SL', 0),
(4310850, 'Jaboticaba', 'JABOTICABA', 'M', 'RS', 'SL', 0),
(4310876, 'Jacuizinho', 'JACUIZINHO', 'M', 'RS', 'SL', 0),
(4310900, 'Jacutinga', 'JACUTINGA', 'M', 'RS', 'SL', 0),
(4311007, 'Jaguarão', 'JAGUARAO', 'M', 'RS', 'SL', 0),
(4311106, 'Jaguari', 'JAGUARI', 'M', 'RS', 'SL', 0),
(4311122, 'Jaquirana', 'JAQUIRANA', 'M', 'RS', 'SL', 0),
(4311130, 'Jari', 'JARI', 'M', 'RS', 'SL', 0),
(4311155, 'Jóia', 'JOIA', 'M', 'RS', 'SL', 0),
(4311205, 'Júlio de Castilhos', 'JULIO DE CASTILHOS', 'M', 'RS', 'SL', 0),
(4311239, 'Lagoa Bonita do Sul', 'LAGOA BONITA DO SUL', 'M', 'RS', 'SL', 0),
(4311254, 'Lagoão', 'LAGOAO', 'M', 'RS', 'SL', 0),
(4311270, 'Lagoa dos Três Cantos', 'LAGOA DOS TRES CANTOS', 'M', 'RS', 'SL', 0),
(4311304, 'Lagoa Vermelha', 'LAGOA VERMELHA', 'M', 'RS', 'SL', 0),
(4311403, 'Lajeado', 'LAJEADO', 'M', 'RS', 'SL', 0),
(4311429, 'Lajeado do Bugre', 'LAJEADO DO BUGRE', 'M', 'RS', 'SL', 0),
(4311502, 'Lavras do Sul', 'LAVRAS DO SUL', 'M', 'RS', 'SL', 0),
(4311601, 'Liberato Salzano', 'LIBERATO SALZANO', 'M', 'RS', 'SL', 0),
(4311627, 'Lindolfo Collor', 'LINDOLFO COLLOR', 'M', 'RS', 'SL', 0),
(4311643, 'Linha Nova', 'LINHA NOVA', 'M', 'RS', 'SL', 0),
(4311700, 'Machadinho', 'MACHADINHO', 'M', 'RS', 'SL', 0),
(4311718, 'Macambara', 'MACAMBARA', 'M', 'RS', 'SL', 0),
(4311734, 'Mampituba', 'MAMPITUBA', 'M', 'RS', 'SL', 0),
(4311759, 'Manoel Viana', 'MANOEL VIANA', 'M', 'RS', 'SL', 0),
(4311775, 'Maquiné', 'MAQUINE', 'M', 'RS', 'SL', 0),
(4311791, 'Maratá', 'MARATA', 'M', 'RS', 'SL', 0),
(4311809, 'Maraú', 'MARAU', 'M', 'RS', 'SL', 0),
(4311908, 'Marcelino Ramos', 'MARCELINO RAMOS', 'M', 'RS', 'SL', 0),
(4311981, 'Mariana Pimentel', 'MARIANA PIMENTEL', 'M', 'RS', 'SL', 0),
(4312005, 'Mariano Moro', 'MARIANO MORO', 'M', 'RS', 'SL', 0),
(4312054, 'Marques de Souza', 'MARQUES DE SOUZA', 'M', 'RS', 'SL', 0),
(4312104, 'Mata', 'MATA', 'M', 'RS', 'SL', 0),
(4312138, 'Mato Castelhano', 'MATO CASTELHANO', 'M', 'RS', 'SL', 0),
(4312153, 'Mato Leitao', 'MATO LEITAO', 'M', 'RS', 'SL', 0),
(4312179, 'Mato Queimado', 'MATO QUEIMADO', 'M', 'RS', 'SL', 0),
(4312203, 'Maximiliano de Almeida', 'MAXIMILIANO DE ALMEIDA', 'M', 'RS', 'SL', 0),
(4312252, 'Minas do Leão', 'MINAS DO LEAO', 'M', 'RS', 'SL', 0),
(4312302, 'Miraguaí', 'MIRAGUAI', 'M', 'RS', 'SL', 0),
(4312351, 'Montauri', 'MONTAURI', 'M', 'RS', 'SL', 0),
(4312377, 'Monte Alegre dos Campos', 'MONTE ALEGRE DOS CAMPOS', 'M', 'RS', 'SL', 0),
(4312385, 'Monte Belo do Sul', 'MONTE BELO DO SUL', 'M', 'RS', 'SL', 0),
(4312401, 'Montenegro', 'MONTENEGRO', 'M', 'RS', 'SL', 0),
(4312427, 'Mormaço', 'MORMACO', 'M', 'RS', 'SL', 0),
(4312443, 'Morrinhos do Sul', 'MORRINHOS DO SUL', 'M', 'RS', 'SL', 0),
(4312450, 'Morro Redondo', 'MORRO REDONDO', 'M', 'RS', 'SL', 0),
(4312476, 'Morro Reuter', 'MORRO REUTER', 'M', 'RS', 'SL', 0),
(4312500, 'Mostardas', 'MOSTARDAS', 'M', 'RS', 'SL', 0),
(4312609, 'Muçum', 'MUCUM', 'M', 'RS', 'SL', 0),
(4312617, 'Muitos Capoes', 'MUITOS CAPOES', 'M', 'RS', 'SL', 0),
(4312625, 'Muliterno', 'MULITERNO', 'M', 'RS', 'SL', 0),
(4312658, 'Não-me-toque', 'NAO-ME-TOQUE', 'M', 'RS', 'SL', 0),
(4312674, 'Nicolau Vergueiro', 'NICOLAU VERGUEIRO', 'M', 'RS', 'SL', 0),
(4312708, 'Nonoai', 'NONOAI', 'M', 'RS', 'SL', 0),
(4312757, 'Nova Alvorada', 'NOVA ALVORADA', 'M', 'RS', 'SL', 0),
(4312807, 'Nova Araçá', 'NOVA ARACA', 'M', 'RS', 'SL', 0),
(4312906, 'Nova Bassano', 'NOVA BASSANO', 'M', 'RS', 'SL', 0),
(4312955, 'Nova Boa Vista', 'NOVA BOA VISTA', 'M', 'RS', 'SL', 0),
(4313003, 'Nova Brescia', 'NOVA BRESCIA', 'M', 'RS', 'SL', 0),
(4313011, 'Nova Candelária', 'NOVA CANDELARIA', 'M', 'RS', 'SL', 0),
(4313037, 'Nova Esperança do Sul', 'NOVA ESPERANCA DO SUL', 'M', 'RS', 'SL', 0),
(4313060, 'Nova Hartz', 'NOVA HARTZ', 'M', 'RS', 'SL', 0),
(4313086, 'Nova Pádua', 'NOVA PADUA', 'M', 'RS', 'SL', 0),
(4313102, 'Nova Palma', 'NOVA PALMA', 'M', 'RS', 'SL', 0),
(4313201, 'Nova Petrópolis', 'NOVA PETROPOLIS', 'M', 'RS', 'SL', 0),
(4313300, 'Nova Prata', 'NOVA PRATA', 'M', 'RS', 'SL', 0),
(4313334, 'Nova Ramada', 'NOVA RAMADA', 'M', 'RS', 'SL', 0),
(4313359, 'Nova Roma do Sul', 'NOVA ROMA DO SUL', 'M', 'RS', 'SL', 0),
(4313375, 'Nova Santa Rita', 'NOVA SANTA RITA', 'M', 'RS', 'SL', 0),
(4313391, 'Novo Cabrais', 'NOVO CABRAIS', 'M', 'RS', 'SL', 0),
(4313409, 'Novo Hamburgo', 'NOVO HAMBURGO', 'M', 'RS', 'SL', 0),
(4313425, 'Novo Machado', 'NOVO MACHADO', 'M', 'RS', 'SL', 0),
(4313441, 'Novo Tiradentes', 'NOVO TIRADENTES', 'M', 'RS', 'SL', 0),
(4313466, 'Novo Xingu', 'NOVO XINGU', 'M', 'RS', 'SL', 0),
(4313490, 'Novo Barreiro', 'NOVO BARREIRO', 'M', 'RS', 'SL', 0),
(4313508, 'Osório', 'OSORIO', 'M', 'RS', 'SL', 0),
(4313607, 'Paim Filho', 'PAIM FILHO', 'M', 'RS', 'SL', 0),
(4313656, 'Palmares do Sul', 'PALMARES DO SUL', 'M', 'RS', 'SL', 0),
(4313706, 'Palmeira das Missoes', 'PALMEIRA DAS MISSOES', 'M', 'RS', 'SL', 0),
(4313805, 'Palmitinho', 'PALMITINHO', 'M', 'RS', 'SL', 0),
(4313904, 'Panambi', 'PANAMBI', 'M', 'RS', 'SL', 0),
(4313953, 'Pantano Grande', 'PANTANO GRANDE', 'M', 'RS', 'SL', 0),
(4314001, 'Paraí', 'PARAI', 'M', 'RS', 'SL', 0),
(4314027, 'Paraíso do Sul', 'PARAISO DO SUL', 'M', 'RS', 'SL', 0),
(4314035, 'Pareci Novo', 'PARECI NOVO', 'M', 'RS', 'SL', 0),
(4314050, 'Parobé', 'PAROBE', 'M', 'RS', 'SL', 0),
(4314068, 'Passa Sete', 'PASSA SETE', 'M', 'RS', 'SL', 0),
(4314076, 'Passo do Sobrado', 'PASSO DO SOBRADO', 'M', 'RS', 'SL', 0),
(4314100, 'Passo Fundo', 'PASSO FUNDO', 'M', 'RS', 'SL', 0),
(4314134, 'Paulo Bento', 'PAULO BENTO', 'M', 'RS', 'SL', 0),
(4314159, 'Paverama', 'PAVERAMA', 'M', 'RS', 'SL', 0),
(4314175, 'Pedras Altas', 'PEDRAS ALTAS', 'M', 'RS', 'SL', 0),
(4314209, 'Pedro Osório', 'PEDRO OSORIO', 'M', 'RS', 'SL', 0),
(4314308, 'Pejuçara', 'PEJUCARA', 'M', 'RS', 'SL', 0),
(4314407, 'Pelotas', 'PELOTAS', 'M', 'RS', 'SL', 0),
(4314423, 'Picada Café', 'PICADA CAFE', 'M', 'RS', 'SL', 0),
(4314456, 'Pinhal', 'PINHAL', 'M', 'RS', 'SL', 0),
(4314464, 'Pinhal da Serra', 'PINHAL DA SERRA', 'M', 'RS', 'SL', 0),
(4314472, 'Pinhal Grande', 'PINHAL GRANDE', 'M', 'RS', 'SL', 0),
(4314498, 'Pinheirinho do Vale', 'PINHEIRINHO DO VALE', 'M', 'RS', 'SL', 0),
(4314506, 'Pinheiro Machado', 'PINHEIRO MACHADO', 'M', 'RS', 'SL', 0);
INSERT INTO `localidade` (`cod_localidade`, `nom_localidade`, `nom_localidade_pesq`, `tip_localidade`, `sgl_uf`, `sgl_regiao`, `ind_excluido`) VALUES
(4314530, 'Pinto Bandeira', 'PINTO BANDEIRA', 'M', 'RS', 'SL', 0),
(4314555, 'Pirapó', 'PIRAPO', 'M', 'RS', 'SL', 0),
(4314605, 'Piratini', 'PIRATINI', 'M', 'RS', 'SL', 0),
(4314704, 'Planalto', 'PLANALTO', 'M', 'RS', 'SL', 0),
(4314753, 'Poço das Antas', 'POCO DAS ANTAS', 'M', 'RS', 'SL', 0),
(4314779, 'Pontão', 'PONTAO', 'M', 'RS', 'SL', 0),
(4314787, 'Ponte Preta', 'PONTE PRETA', 'M', 'RS', 'SL', 0),
(4314803, 'Portão', 'PORTAO', 'M', 'RS', 'SL', 0),
(4314902, 'Porto Alegre', 'PORTO ALEGRE', 'M', 'RS', 'SL', 0),
(4315008, 'Porto Lucena', 'PORTO LUCENA', 'M', 'RS', 'SL', 0),
(4315057, 'Porto Mauá', 'PORTO MAUA', 'M', 'RS', 'SL', 0),
(4315073, 'Porto Vera Cruz', 'PORTO VERA CRUZ', 'M', 'RS', 'SL', 0),
(4315107, 'Porto Xavier', 'PORTO XAVIER', 'M', 'RS', 'SL', 0),
(4315131, 'Pouso Novo', 'POUSO NOVO', 'M', 'RS', 'SL', 0),
(4315149, 'Presidente Lucena', 'PRESIDENTE LUCENA', 'M', 'RS', 'SL', 0),
(4315156, 'Progresso', 'PROGRESSO', 'M', 'RS', 'SL', 0),
(4315172, 'Protásio Alves', 'PROTASIO ALVES', 'M', 'RS', 'SL', 0),
(4315206, 'Putinga', 'PUTINGA', 'M', 'RS', 'SL', 0),
(4315305, 'Quaraí', 'QUARAI', 'M', 'RS', 'SL', 0),
(4315313, 'Quatro Irmãos', 'QUATRO IRMAOS', 'M', 'RS', 'SL', 0),
(4315321, 'Quevedos', 'QUEVEDOS', 'M', 'RS', 'SL', 0),
(4315354, 'Quinze de Novembro', 'QUINZE DE NOVEMBRO', 'M', 'RS', 'SL', 0),
(4315404, 'Redentora', 'REDENTORA', 'M', 'RS', 'SL', 0),
(4315453, 'Relvado', 'RELVADO', 'M', 'RS', 'SL', 0),
(4315503, 'Restinga Seca', 'RESTINGA SECA', 'M', 'RS', 'SL', 0),
(4315552, 'Rio dos Índios', 'RIO DOS INDIOS', 'M', 'RS', 'SL', 0),
(4315602, 'Rio Grande', 'RIO GRANDE', 'M', 'RS', 'SL', 0),
(4315701, 'Rio Pardo', 'RIO PARDO', 'M', 'RS', 'SL', 0),
(4315750, 'Riozinho', 'RIOZINHO', 'M', 'RS', 'SL', 0),
(4315800, 'Roca Sales', 'ROCA SALES', 'M', 'RS', 'SL', 0),
(4315909, 'Rodeio Bonito', 'RODEIO BONITO', 'M', 'RS', 'SL', 0),
(4315958, 'Rolador', 'ROLADOR', 'M', 'RS', 'SL', 0),
(4316006, 'Rolante', 'ROLANTE', 'M', 'RS', 'SL', 0),
(4316105, 'Ronda Alta', 'RONDA ALTA', 'M', 'RS', 'SL', 0),
(4316204, 'Rondinha', 'RONDINHA', 'M', 'RS', 'SL', 0),
(4316303, 'Roque Gonzales', 'ROQUE GONZALES', 'M', 'RS', 'SL', 0),
(4316402, 'Rosário do Sul', 'ROSARIO DO SUL', 'M', 'RS', 'SL', 0),
(4316428, 'Sagrada Família', 'SAGRADA FAMILIA', 'M', 'RS', 'SL', 0),
(4316436, 'Saldanha Marinho', 'SALDANHA MARINHO', 'M', 'RS', 'SL', 0),
(4316451, 'Salto do Jacuí', 'SALTO DO JACUI', 'M', 'RS', 'SL', 0),
(4316477, 'Salvador das Missões', 'SALVADOR DAS MISSOES', 'M', 'RS', 'SL', 0),
(4316501, 'Salvador do Sul', 'SALVADOR DO SUL', 'M', 'RS', 'SL', 0),
(4316600, 'Sananduva', 'SANANDUVA', 'M', 'RS', 'SL', 0),
(4316709, 'Santa Bárbara do Sul', 'SANTA BARBARA DO SUL', 'M', 'RS', 'SL', 0),
(4316733, 'Santa Cecília do Sul', 'SANTA CECILIA DO SUL', 'M', 'RS', 'SL', 0),
(4316758, 'Santa Clara do Sul', 'SANTA CLARA DO SUL', 'M', 'RS', 'SL', 0),
(4316808, 'Santa Cruz do Sul', 'SANTA CRUZ DO SUL', 'M', 'RS', 'SL', 0),
(4316907, 'Santa Maria', 'SANTA MARIA', 'M', 'RS', 'SL', 0),
(4316956, 'Santa Maria do Herval', 'SANTA MARIA DO HERVAL', 'M', 'RS', 'SL', 0),
(4316972, 'Santa Margarida do Sul', 'SANTA MARGARIDA DO SUL', 'M', 'RS', 'SL', 0),
(4317004, 'Santana da Boa Vista', 'SANTANA DA BOA VISTA', 'M', 'RS', 'SL', 0),
(4317103, 'Santana do Livramento', 'SANTANA DO LIVRAMENTO', 'M', 'RS', 'SL', 0),
(4317202, 'Santa Rosa', 'SANTA ROSA', 'M', 'RS', 'SL', 0),
(4317251, 'Santa Tereza', 'SANTA TEREZA', 'M', 'RS', 'SL', 0),
(4317301, 'Santa Vitoria do Palmar', 'SANTA VITORIA DO PALMAR', 'M', 'RS', 'SL', 0),
(4317400, 'Santiago', 'SANTIAGO', 'M', 'RS', 'SL', 0),
(4317509, 'Santo Ângelo', 'SANTO ANGELO', 'M', 'RS', 'SL', 0),
(4317558, 'Santo Antônio do Palma', 'SANTO ANTONIO DO PALMA', 'M', 'RS', 'SL', 0),
(4317608, 'Santo Antônio da Patrulha', 'SANTO ANTONIO DA PATRULHA', 'M', 'RS', 'SL', 0),
(4317707, 'Santo Antônio das Missões', 'SANTO ANTONIO DAS MISSOES', 'M', 'RS', 'SL', 0),
(4317756, 'Santo Antônio do Planalto', 'SANTO ANTONIO DO PLANALTO', 'M', 'RS', 'SL', 0),
(4317806, 'Santo Augusto', 'SANTO AUGUSTO', 'M', 'RS', 'SL', 0),
(4317905, 'Santo Cristo', 'SANTO CRISTO', 'M', 'RS', 'SL', 0),
(4317954, 'Santo Expedito do Sul', 'SANTO EXPEDITO DO SUL', 'M', 'RS', 'SL', 0),
(4318002, 'São Borja', 'SAO BORJA', 'M', 'RS', 'SL', 0),
(4318051, 'São Domingos do Sul', 'SAO DOMINGOS DO SUL', 'M', 'RS', 'SL', 0),
(4318101, 'São Francisco de Assis', 'SAO FRANCISCO DE ASSIS', 'M', 'RS', 'SL', 0),
(4318200, 'São Francisco de Paula', 'SAO FRANCISCO DE PAULA', 'M', 'RS', 'SL', 0),
(4318309, 'São Gabriel', 'SAO GABRIEL', 'M', 'RS', 'SL', 0),
(4318408, 'São Jerônimo', 'SAO JERONIMO', 'M', 'RS', 'SL', 0),
(4318424, 'São João da Urtiga', 'SAO JOAO DA URTIGA', 'M', 'RS', 'SL', 0),
(4318432, 'São João do Polesine', 'SAO JOAO DO POLESINE', 'M', 'RS', 'SL', 0),
(4318440, 'São Jorge', 'SAO JORGE', 'M', 'RS', 'SL', 0),
(4318457, 'São José das Missões', 'SAO JOSE DAS MISSOES', 'M', 'RS', 'SL', 0),
(4318465, 'São José do Herval', 'SAO JOSE DO HERVAL', 'M', 'RS', 'SL', 0),
(4318481, 'São José do Hortêncio', 'SAO JOSE DO HORTENCIO', 'M', 'RS', 'SL', 0),
(4318499, 'São José do Inhacorá', 'SAO JOSE DO INHACORA', 'M', 'RS', 'SL', 0),
(4318507, 'São José do Norte', 'SAO JOSE DO NORTE', 'M', 'RS', 'SL', 0),
(4318606, 'São José do Ouro', 'SAO JOSE DO OURO', 'M', 'RS', 'SL', 0),
(4318614, 'São José do Sul', 'SAO JOSE DO SUL', 'M', 'RS', 'SL', 0),
(4318622, 'São José dos Ausentes', 'SAO JOSE DOS AUSENTES', 'M', 'RS', 'SL', 0),
(4318705, 'São Leopoldo', 'SAO LEOPOLDO', 'M', 'RS', 'SL', 0),
(4318804, 'São Lourenço do Sul', 'SAO LOURENCO DO SUL', 'M', 'RS', 'SL', 0),
(4318903, 'São Luiz Gonzaga', 'SAO LUIZ GONZAGA', 'M', 'RS', 'SL', 0),
(4319000, 'São Marcos', 'SAO MARCOS', 'M', 'RS', 'SL', 0),
(4319109, 'São Martinho', 'SAO MARTINHO', 'M', 'RS', 'SL', 0),
(4319125, 'São Martinho da Serra', 'SAO MARTINHO DA SERRA', 'M', 'RS', 'SL', 0),
(4319158, 'São Miguel das Missões', 'SAO MIGUEL DAS MISSOES', 'M', 'RS', 'SL', 0),
(4319208, 'São Nicolau', 'SAO NICOLAU', 'M', 'RS', 'SL', 0),
(4319307, 'São Paulo das Missões', 'SAO PAULO DAS MISSOES', 'M', 'RS', 'SL', 0),
(4319356, 'São Pedro da Serra', 'SAO PEDRO DA SERRA', 'M', 'RS', 'SL', 0),
(4319364, 'São Pedro das Missões', 'SAO PEDRO DAS MISSOES', 'M', 'RS', 'SL', 0),
(4319372, 'São Pedro do Butia', 'SAO PEDRO DO BUTIA', 'M', 'RS', 'SL', 0),
(4319406, 'São Pedro do Sul', 'SAO PEDRO DO SUL', 'M', 'RS', 'SL', 0),
(4319505, 'São Sebastião do Caí', 'SAO SEBASTIAO DO CAI', 'M', 'RS', 'SL', 0),
(4319604, 'São Sepé', 'SAO SEPE', 'M', 'RS', 'SL', 0),
(4319703, 'São Valentim', 'SAO VALENTIM', 'M', 'RS', 'SL', 0),
(4319711, 'São Valentim do Sul', 'SAO VALENTIM DO SUL', 'M', 'RS', 'SL', 0),
(4319737, 'São Valério do Sul', 'SAO VALERIO DO SUL', 'M', 'RS', 'SL', 0),
(4319752, 'São Vendelino', 'SAO VENDELINO', 'M', 'RS', 'SL', 0),
(4319802, 'São Vicente do Sul', 'SAO VICENTE DO SUL', 'M', 'RS', 'SL', 0),
(4319901, 'Sapiranga', 'SAPIRANGA', 'M', 'RS', 'SL', 0),
(4320008, 'Sapucaia do Sul', 'SAPUCAIA DO SUL', 'M', 'RS', 'SL', 0),
(4320107, 'Sarandi', 'SARANDI', 'M', 'RS', 'SL', 0),
(4320206, 'Seberi', 'SEBERI', 'M', 'RS', 'SL', 0),
(4320230, 'Sede Nova', 'SEDE NOVA', 'M', 'RS', 'SL', 0),
(4320263, 'Segredo', 'SEGREDO', 'M', 'RS', 'SL', 0),
(4320305, 'Selbach', 'SELBACH', 'M', 'RS', 'SL', 0),
(4320321, 'Senador Salgado Filho', 'SENADOR SALGADO FILHO', 'M', 'RS', 'SL', 0),
(4320354, 'Sentinela do Sul', 'SENTINELA DO SUL', 'M', 'RS', 'SL', 0),
(4320404, 'Serafina Correa', 'SERAFINA CORREA', 'M', 'RS', 'SL', 0),
(4320453, 'Sério', 'SERIO', 'M', 'RS', 'SL', 0),
(4320503, 'Sertão', 'SERTAO', 'M', 'RS', 'SL', 0),
(4320552, 'Sertão Santana', 'SERTAO SANTANA', 'M', 'RS', 'SL', 0),
(4320578, 'Sete de Setembro', 'SETE DE SETEMBRO', 'M', 'RS', 'SL', 0),
(4320602, 'Severiano de Almeida', 'SEVERIANO DE ALMEIDA', 'M', 'RS', 'SL', 0),
(4320651, 'Silveira Martins', 'SILVEIRA MARTINS', 'M', 'RS', 'SL', 0),
(4320677, 'Sinimbu', 'SINIMBU', 'M', 'RS', 'SL', 0),
(4320701, 'Sobradinho', 'SOBRADINHO', 'M', 'RS', 'SL', 0),
(4320800, 'Soledade', 'SOLEDADE', 'M', 'RS', 'SL', 0),
(4320859, 'Tabaí', 'TABAI', 'M', 'RS', 'SL', 0),
(4320909, 'Tapejara', 'TAPEJARA', 'M', 'RS', 'SL', 0),
(4321006, 'Tapera', 'TAPERA', 'M', 'RS', 'SL', 0),
(4321105, 'Tapes', 'TAPES', 'M', 'RS', 'SL', 0),
(4321204, 'Taquara', 'TAQUARA', 'M', 'RS', 'SL', 0),
(4321303, 'Taquari', 'TAQUARI', 'M', 'RS', 'SL', 0),
(4321329, 'Taquaruçu do Sul', 'TAQUARUCU DO SUL', 'M', 'RS', 'SL', 0),
(4321352, 'Tavares', 'TAVARES', 'M', 'RS', 'SL', 0),
(4321402, 'Tenente Portela', 'TENENTE PORTELA', 'M', 'RS', 'SL', 0),
(4321436, 'Terra de Areia', 'TERRA DE AREIA', 'M', 'RS', 'SL', 0),
(4321451, 'Teutonia', 'TEUTONIA', 'M', 'RS', 'SL', 0),
(4321469, 'Tio Hugo', 'TIO HUGO', 'M', 'RS', 'SL', 0),
(4321477, 'Tiradentes do Sul', 'TIRADENTES DO SUL', 'M', 'RS', 'SL', 0),
(4321493, 'Toropi', 'TOROPI', 'M', 'RS', 'SL', 0),
(4321501, 'Torres', 'TORRES', 'M', 'RS', 'SL', 0),
(4321600, 'Tramandaí', 'TRAMANDAI', 'M', 'RS', 'SL', 0),
(4321626, 'Travesseiro', 'TRAVESSEIRO', 'M', 'RS', 'SL', 0),
(4321634, 'Três Arroios', 'TRES ARROIOS', 'M', 'RS', 'SL', 0),
(4321667, 'Três Cachoeiras', 'TRES CACHOEIRAS', 'M', 'RS', 'SL', 0),
(4321709, 'Três Coroas', 'TRES COROAS', 'M', 'RS', 'SL', 0),
(4321808, 'Três de Maio', 'TRES DE MAIO', 'M', 'RS', 'SL', 0),
(4321832, 'Três Forquilhas', 'TRES FORQUILHAS', 'M', 'RS', 'SL', 0),
(4321857, 'Três Palmeiras', 'TRES PALMEIRAS', 'M', 'RS', 'SL', 0),
(4321907, 'Três Passos', 'TRES PASSOS', 'M', 'RS', 'SL', 0),
(4321956, 'Trindade do Sul', 'TRINDADE DO SUL', 'M', 'RS', 'SL', 0),
(4322004, 'Triunfo', 'TRIUNFO', 'M', 'RS', 'SL', 0),
(4322103, 'Tucunduva', 'TUCUNDUVA', 'M', 'RS', 'SL', 0),
(4322152, 'Tunas', 'TUNAS', 'M', 'RS', 'SL', 0),
(4322186, 'Tupanci do Sul', 'TUPANCI DO SUL', 'M', 'RS', 'SL', 0),
(4322202, 'Tupanciretã', 'TUPANCIRETA', 'M', 'RS', 'SL', 0),
(4322251, 'Tupandi', 'TUPANDI', 'M', 'RS', 'SL', 0),
(4322301, 'Tuparendi', 'TUPARENDI', 'M', 'RS', 'SL', 0),
(4322327, 'Turuçu', 'TURUCU', 'M', 'RS', 'SL', 0),
(4322343, 'Ubiretama', 'UBIRETAMA', 'M', 'RS', 'SL', 0),
(4322350, 'União da Serra', 'UNIAO DA SERRA', 'M', 'RS', 'SL', 0),
(4322376, 'Unistalda', 'UNISTALDA', 'M', 'RS', 'SL', 0),
(4322400, 'Uruguaiana', 'URUGUAIANA', 'M', 'RS', 'SL', 0),
(4322509, 'Vacaria', 'VACARIA', 'M', 'RS', 'SL', 0),
(4322525, 'Vale Verde', 'VALE VERDE', 'M', 'RS', 'SL', 0),
(4322533, 'Vale do Sol', 'VALE DO SOL', 'M', 'RS', 'SL', 0),
(4322541, 'Vale Real', 'VALE REAL', 'M', 'RS', 'SL', 0),
(4322558, 'Vanini', 'VANINI', 'M', 'RS', 'SL', 0),
(4322608, 'Venâncio Aires', 'VENANCIO AIRES', 'M', 'RS', 'SL', 0),
(4322707, 'Vera Cruz', 'VERA CRUZ', 'M', 'RS', 'SL', 0),
(4322806, 'Veranópolis', 'VERANOPOLIS', 'M', 'RS', 'SL', 0),
(4322855, 'Vespasiano Correa', 'VESPASIANO CORREA', 'M', 'RS', 'SL', 0),
(4322905, 'Viadutos', 'VIADUTOS', 'M', 'RS', 'SL', 0),
(4323002, 'Viamão', 'VIAMAO', 'M', 'RS', 'SL', 0),
(4323101, 'Vicente Dutra', 'VICENTE DUTRA', 'M', 'RS', 'SL', 0),
(4323200, 'Victor Graeff', 'VICTOR GRAEFF', 'M', 'RS', 'SL', 0),
(4323309, 'Vila Flores', 'VILA FLORES', 'M', 'RS', 'SL', 0),
(4323358, 'Vila Langaro', 'VILA LANGARO', 'M', 'RS', 'SL', 0),
(4323408, 'Vila Maria', 'VILA MARIA', 'M', 'RS', 'SL', 0),
(4323457, 'Vila Nova do Sul', 'VILA NOVA DO SUL', 'M', 'RS', 'SL', 0),
(4323507, 'Vista Alegre', 'VISTA ALEGRE', 'M', 'RS', 'SL', 0),
(4323606, 'Vista Alegre do Prata', 'VISTA ALEGRE DO PRATA', 'M', 'RS', 'SL', 0),
(4323705, 'Vista Gaúcha', 'VISTA GAUCHA', 'M', 'RS', 'SL', 0),
(4323754, 'Vitória das Missões', 'VITORIA DAS MISSOES', 'M', 'RS', 'SL', 0),
(4323770, 'Westfália', 'WESTFALIA', 'M', 'RS', 'SL', 0),
(4323804, 'Xangri-lá', 'XANGRI-LA', 'M', 'RS', 'SL', 0),
(5000000, 'Mato Grosso do Sul', 'MATO GROSSO DO SUL', 'U', 'MS', 'CO', 0),
(5000203, 'Água Clara', 'AGUA CLARA', 'M', 'MS', 'CO', 0),
(5000252, 'Alcinópolis', 'ALCINOPOLIS', 'M', 'MS', 'CO', 0),
(5000609, 'Amambaí', 'AMAMBAI', 'M', 'MS', 'CO', 0),
(5000708, 'Anastácio', 'ANASTACIO', 'M', 'MS', 'CO', 0),
(5000807, 'Anaurilândia', 'ANAURILANDIA', 'M', 'MS', 'CO', 0),
(5000856, 'Angélica', 'ANGELICA', 'M', 'MS', 'CO', 0),
(5000906, 'Antônio João', 'ANTONIO JOAO', 'M', 'MS', 'CO', 0),
(5001003, 'Aparecida do Taboado', 'APARECIDA DO TABOADO', 'M', 'MS', 'CO', 0),
(5001102, 'Aquidauana', 'AQUIDAUANA', 'M', 'MS', 'CO', 0),
(5001243, 'Aral Moreira', 'ARAL MOREIRA', 'M', 'MS', 'CO', 0),
(5001508, 'Bandeirantes', 'BANDEIRANTES', 'M', 'MS', 'CO', 0),
(5001904, 'Bataguassu', 'BATAGUASSU', 'M', 'MS', 'CO', 0),
(5002001, 'Bataiporã', 'BATAIPORA', 'M', 'MS', 'CO', 0),
(5002100, 'Bela Vista', 'BELA VISTA', 'M', 'MS', 'CO', 0),
(5002159, 'Bodoquena', 'BODOQUENA', 'M', 'MS', 'CO', 0),
(5002209, 'Bonito', 'BONITO', 'M', 'MS', 'CO', 0),
(5002308, 'Brasilândia', 'BRASILANDIA', 'M', 'MS', 'CO', 0),
(5002407, 'Caarapó', 'CAARAPO', 'M', 'MS', 'CO', 0),
(5002605, 'Camapuã', 'CAMAPUA', 'M', 'MS', 'CO', 0),
(5002704, 'Campo Grande', 'CAMPO GRANDE', 'M', 'MS', 'CO', 0),
(5002803, 'Caracol', 'CARACOL', 'M', 'MS', 'CO', 0),
(5002902, 'Cassilândia', 'CASSILANDIA', 'M', 'MS', 'CO', 0),
(5002951, 'Chapadão do Sul', 'CHAPADAO DO SUL', 'M', 'MS', 'CO', 0),
(5003108, 'Corguinho', 'CORGUINHO', 'M', 'MS', 'CO', 0),
(5003157, 'Coronel Sapucaia', 'CORONEL SAPUCAIA', 'M', 'MS', 'CO', 0),
(5003207, 'Corumbá', 'CORUMBA', 'M', 'MS', 'CO', 0),
(5003256, 'Costa Rica', 'COSTA RICA', 'M', 'MS', 'CO', 0),
(5003306, 'Coxim', 'COXIM', 'M', 'MS', 'CO', 0),
(5003454, 'Deodápolis', 'DEODAPOLIS', 'M', 'MS', 'CO', 0),
(5003488, 'Dois Irmãos do Buriti', 'DOIS IRMAOS DO BURITI', 'M', 'MS', 'CO', 0),
(5003504, 'Douradina', 'DOURADINA', 'M', 'MS', 'CO', 0),
(5003702, 'Dourados', 'DOURADOS', 'M', 'MS', 'CO', 0),
(5003751, 'Eldorado', 'ELDORADO', 'M', 'MS', 'CO', 0),
(5003801, 'Fátima do Sul', 'FATIMA DO SUL', 'M', 'MS', 'CO', 0),
(5004007, 'Glória de Dourados', 'GLORIA DE DOURADOS', 'M', 'MS', 'CO', 0),
(5004106, 'Guia Lopes da Laguna', 'GUIA LOPES DA LAGUNA', 'M', 'MS', 'CO', 0),
(5004304, 'Iguatemi', 'IGUATEMI', 'M', 'MS', 'CO', 0),
(5004403, 'Inocência', 'INOCENCIA', 'M', 'MS', 'CO', 0),
(5004502, 'Itaporã', 'ITAPORA', 'M', 'MS', 'CO', 0),
(5004601, 'Itaquiraí', 'ITAQUIRAI', 'M', 'MS', 'CO', 0),
(5004700, 'Ivinhema', 'IVINHEMA', 'M', 'MS', 'CO', 0),
(5004809, 'Japorã', 'JAPORA', 'M', 'MS', 'CO', 0),
(5004908, 'Jaraguari', 'JARAGUARI', 'M', 'MS', 'CO', 0),
(5005004, 'Jardim', 'JARDIM', 'M', 'MS', 'CO', 0),
(5005103, 'Jateí', 'JATEI', 'M', 'MS', 'CO', 0),
(5005152, 'Juti', 'JUTI', 'M', 'MS', 'CO', 0),
(5005202, 'Ladário', 'LADARIO', 'M', 'MS', 'CO', 0),
(5005251, 'Laguna Carapã', 'LAGUNA CARAPA', 'M', 'MS', 'CO', 0),
(5005400, 'Maracaju', 'MARACAJU', 'M', 'MS', 'CO', 0),
(5005608, 'Miranda', 'MIRANDA', 'M', 'MS', 'CO', 0),
(5005681, 'Mundo Novo', 'MUNDO NOVO', 'M', 'MS', 'CO', 0),
(5005707, 'Naviraí', 'NAVIRAI', 'M', 'MS', 'CO', 0),
(5005806, 'Nioaque', 'NIOAQUE', 'M', 'MS', 'CO', 0),
(5006002, 'Nova Alvorada do Sul', 'NOVA ALVORADA DO SUL', 'M', 'MS', 'CO', 0),
(5006200, 'Nova Andradina', 'NOVA ANDRADINA', 'M', 'MS', 'CO', 0),
(5006259, 'Novo Horizonte do Sul', 'NOVO HORIZONTE DO SUL', 'M', 'MS', 'CO', 0),
(5006309, 'Paranaíba', 'PARANAIBA', 'M', 'MS', 'CO', 0),
(5006358, 'Paranhos', 'PARANHOS', 'M', 'MS', 'CO', 0),
(5006408, 'Pedro Gomes', 'PEDRO GOMES', 'M', 'MS', 'CO', 0),
(5006606, 'Ponta Porã', 'PONTA PORA', 'M', 'MS', 'CO', 0),
(5006903, 'Porto Murtinho', 'PORTO MURTINHO', 'M', 'MS', 'CO', 0),
(5007109, 'Ribas do Rio Pardo', 'RIBAS DO RIO PARDO', 'M', 'MS', 'CO', 0),
(5007208, 'Rio Brilhante', 'RIO BRILHANTE', 'M', 'MS', 'CO', 0),
(5007307, 'Rio Negro', 'RIO NEGRO', 'M', 'MS', 'CO', 0),
(5007406, 'Rio Verde de Mato Grosso', 'RIO VERDE DE MATO GROSSO', 'M', 'MS', 'CO', 0),
(5007505, 'Rochedo', 'ROCHEDO', 'M', 'MS', 'CO', 0),
(5007554, 'Santa Rita do Pardo', 'SANTA RITA DO PARDO', 'M', 'MS', 'CO', 0),
(5007695, 'São Gabriel do Oeste', 'SAO GABRIEL DO OESTE', 'M', 'MS', 'CO', 0),
(5007703, 'Sete Quedas', 'SETE QUEDAS', 'M', 'MS', 'CO', 0),
(5007802, 'Selvíria', 'SELVIRIA', 'M', 'MS', 'CO', 0),
(5007901, 'Sidrolândia', 'SIDROLANDIA', 'M', 'MS', 'CO', 0),
(5007935, 'Sonora', 'SONORA', 'M', 'MS', 'CO', 0),
(5007950, 'Tacuru', 'TACURU', 'M', 'MS', 'CO', 0),
(5007976, 'Taquarussu', 'TAQUARUSSU', 'M', 'MS', 'CO', 0),
(5008008, 'Terenos', 'TERENOS', 'M', 'MS', 'CO', 0),
(5008305, 'Três Lagoas', 'TRES LAGOAS', 'M', 'MS', 'CO', 0),
(5008404, 'Vicentina', 'VICENTINA', 'M', 'MS', 'CO', 0),
(5100000, 'Mato Grosso', 'MATO GROSSO', 'U', 'MT', 'CO', 0),
(5100102, 'Acorizal', 'ACORIZAL', 'M', 'MT', 'CO', 0),
(5100201, 'Agua Boa', 'AGUA BOA', 'M', 'MT', 'CO', 0),
(5100250, 'Alta Floresta', 'ALTA FLORESTA', 'M', 'MT', 'CO', 0),
(5100300, 'Alto Araguaia', 'ALTO ARAGUAIA', 'M', 'MT', 'CO', 0),
(5100359, 'Alto Boa Vista', 'ALTO BOA VISTA', 'M', 'MT', 'CO', 0),
(5100409, 'Alto Garças', 'ALTO GARCAS', 'M', 'MT', 'CO', 0),
(5100508, 'Alto Paraguai', 'ALTO PARAGUAI', 'M', 'MT', 'CO', 0),
(5100607, 'Alto Taquari', 'ALTO TAQUARI', 'M', 'MT', 'CO', 0),
(5100805, 'Apiacás', 'APIACAS', 'M', 'MT', 'CO', 0),
(5101001, 'Araguaiana', 'ARAGUAIANA', 'M', 'MT', 'CO', 0),
(5101209, 'Araguainha', 'ARAGUAINHA', 'M', 'MT', 'CO', 0),
(5101258, 'Araputanga', 'ARAPUTANGA', 'M', 'MT', 'CO', 0),
(5101308, 'Arenápolis', 'ARENAPOLIS', 'M', 'MT', 'CO', 0),
(5101407, 'Aripuana', 'ARIPUANA', 'M', 'MT', 'CO', 0),
(5101605, 'Barão de Melgaço', 'BARAO DE MELGACO', 'M', 'MT', 'CO', 0),
(5101704, 'Barra do Bugres', 'BARRA DO BUGRES', 'M', 'MT', 'CO', 0),
(5101803, 'Barra do Garças', 'BARRA DO GARCAS', 'M', 'MT', 'CO', 0),
(5101852, 'Bom Jesus do Araguaia', 'BOM JESUS DO ARAGUAIA', 'M', 'MT', 'CO', 0),
(5101902, 'Brasnorte', 'BRASNORTE', 'M', 'MT', 'CO', 0),
(5102504, 'Cáceres', 'CACERES', 'M', 'MT', 'CO', 0),
(5102603, 'Campinápolis', 'CAMPINAPOLIS', 'M', 'MT', 'CO', 0),
(5102637, 'Campo Novo do Parecis', 'CAMPO NOVO DO PARECIS', 'M', 'MT', 'CO', 0),
(5102678, 'Campo Verde', 'CAMPO VERDE', 'M', 'MT', 'CO', 0),
(5102686, 'Campos de Júlio', 'CAMPOS DE JULIO', 'M', 'MT', 'CO', 0),
(5102694, 'Canabrava do Norte', 'CANABRAVA DO NORTE', 'M', 'MT', 'CO', 0),
(5102702, 'Canarana', 'CANARANA', 'M', 'MT', 'CO', 0),
(5102793, 'Carlinda', 'CARLINDA', 'M', 'MT', 'CO', 0),
(5102850, 'Castanheira', 'CASTANHEIRA', 'M', 'MT', 'CO', 0),
(5103007, 'Chapada dos Guimaraes', 'CHAPADA DOS GUIMARAES', 'M', 'MT', 'CO', 0),
(5103056, 'Cláudia', 'CLAUDIA', 'M', 'MT', 'CO', 0),
(5103106, 'Cocalinho', 'COCALINHO', 'M', 'MT', 'CO', 0),
(5103205, 'Colíder', 'COLIDER', 'M', 'MT', 'CO', 0),
(5103254, 'Colniza', 'COLNIZA', 'M', 'MT', 'CO', 0),
(5103304, 'Comodoro', 'COMODORO', 'M', 'MT', 'CO', 0),
(5103353, 'Confresa', 'CONFRESA', 'M', 'MT', 'CO', 0),
(5103361, 'Conquista D''Oeste', 'CONQUISTA D''OESTE', 'M', 'MT', 'CO', 0),
(5103379, 'Cotriguaçu', 'COTRIGUACU', 'M', 'MT', 'CO', 0),
(5103403, 'Cuiabá', 'CUIABA', 'M', 'MT', 'CO', 0),
(5103437, 'Curvelândia', 'CURVELANDIA', 'M', 'MT', 'CO', 0),
(5103452, 'Denise', 'DENISE', 'M', 'MT', 'CO', 0),
(5103502, 'Diamantino', 'DIAMANTINO', 'M', 'MT', 'CO', 0),
(5103601, 'Dom Aquino', 'DOM AQUINO', 'M', 'MT', 'CO', 0),
(5103700, 'Feliz Natal', 'FELIZ NATAL', 'M', 'MT', 'CO', 0),
(5103809, 'Figueirópolis D''Oeste', 'FIGUEIROPOLIS D''OESTE', 'M', 'MT', 'CO', 0),
(5103858, 'Gaúcha do Norte', 'GAUCHA DO NORTE', 'M', 'MT', 'CO', 0),
(5103908, 'General Carneiro', 'GENERAL CARNEIRO', 'M', 'MT', 'CO', 0),
(5103957, 'Glória D''Oeste', 'GLORIA D''OESTE', 'M', 'MT', 'CO', 0),
(5104104, 'Guarantã do Norte', 'GUARANTA DO NORTE', 'M', 'MT', 'CO', 0),
(5104203, 'Guiratinga', 'GUIRATINGA', 'M', 'MT', 'CO', 0),
(5104500, 'Indiavaí', 'INDIAVAI', 'M', 'MT', 'CO', 0),
(5104559, 'Itaúba', 'ITAUBA', 'M', 'MT', 'CO', 0),
(5104609, 'Itiquira', 'ITIQUIRA', 'M', 'MT', 'CO', 0),
(5104807, 'Jaciara', 'JACIARA', 'M', 'MT', 'CO', 0),
(5104906, 'Jangada', 'JANGADA', 'M', 'MT', 'CO', 0),
(5105002, 'Jauru', 'JAURU', 'M', 'MT', 'CO', 0),
(5105101, 'Juara', 'JUARA', 'M', 'MT', 'CO', 0),
(5105150, 'Juína', 'JUINA', 'M', 'MT', 'CO', 0),
(5105176, 'Juruena', 'JURUENA', 'M', 'MT', 'CO', 0),
(5105200, 'Juscimeira', 'JUSCIMEIRA', 'M', 'MT', 'CO', 0),
(5105234, 'Lambari D''Oeste', 'LAMBARI D''OESTE', 'M', 'MT', 'CO', 0),
(5105259, 'Lucas do Rio Verde', 'LUCAS DO RIO VERDE', 'M', 'MT', 'CO', 0),
(5105309, 'Luciara', 'LUCIARA', 'M', 'MT', 'CO', 0),
(5105507, 'Vila Bela da Santíssima Trindade', 'VILA BELA DA SANTISSIMA TRINDADE', 'M', 'MT', 'CO', 0),
(5105580, 'Marcelandia', 'MARCELANDIA', 'M', 'MT', 'CO', 0),
(5105606, 'Matupá', 'MATUPA', 'M', 'MT', 'CO', 0),
(5105622, 'Mirassol D''Oeste', 'MIRASSOL D''OESTE', 'M', 'MT', 'CO', 0),
(5105903, 'Nobres', 'NOBRES', 'M', 'MT', 'CO', 0),
(5106000, 'Nortelândia', 'NORTELANDIA', 'M', 'MT', 'CO', 0),
(5106109, 'Nossa Senhora do Livramento', 'NOSSA SENHORA DO LIVRAMENTO', 'M', 'MT', 'CO', 0),
(5106158, 'Nova Bandeirantes', 'NOVA BANDEIRANTES', 'M', 'MT', 'CO', 0),
(5106174, 'Nova Nazaré', 'NOVA NAZARE', 'M', 'MT', 'CO', 0),
(5106182, 'Nova Lacerda', 'NOVA LACERDA', 'M', 'MT', 'CO', 0),
(5106190, 'Nova Santa Helena', 'NOVA SANTA HELENA', 'M', 'MT', 'CO', 0),
(5106208, 'Nova Brasilândia', 'NOVA BRASILANDIA', 'M', 'MT', 'CO', 0),
(5106216, 'Nova Canaã do Norte', 'NOVA CANAA DO NORTE', 'M', 'MT', 'CO', 0),
(5106224, 'Nova Mutum', 'NOVA MUTUM', 'M', 'MT', 'CO', 0),
(5106232, 'Nova Olímpia', 'NOVA OLIMPIA', 'M', 'MT', 'CO', 0),
(5106240, 'Nova Ubiratã', 'NOVA UBIRATA', 'M', 'MT', 'CO', 0),
(5106257, 'Nova Xavantina', 'NOVA XAVANTINA', 'M', 'MT', 'CO', 0),
(5106265, 'Novo Mundo', 'NOVO MUNDO', 'M', 'MT', 'CO', 0),
(5106273, 'Novo Horizonte do Norte', 'NOVO HORIZONTE DO NORTE', 'M', 'MT', 'CO', 0),
(5106281, 'Novo São Joaquim', 'NOVO SAO JOAQUIM', 'M', 'MT', 'CO', 0),
(5106299, 'Paranaíta', 'PARANAITA', 'M', 'MT', 'CO', 0),
(5106307, 'Paranatinga', 'PARANATINGA', 'M', 'MT', 'CO', 0),
(5106315, 'Novo Santo Antônio', 'NOVO SANTO ANTONIO', 'M', 'MT', 'CO', 0),
(5106372, 'Pedra Preta', 'PEDRA PRETA', 'M', 'MT', 'CO', 0),
(5106422, 'Peixoto de Azevedo', 'PEIXOTO DE AZEVEDO', 'M', 'MT', 'CO', 0),
(5106455, 'Planalto da Serra', 'PLANALTO DA SERRA', 'M', 'MT', 'CO', 0),
(5106505, 'Poconé', 'POCONE', 'M', 'MT', 'CO', 0),
(5106653, 'Pontal do Araguaia', 'PONTAL DO ARAGUAIA', 'M', 'MT', 'CO', 0),
(5106703, 'Ponte Branca', 'PONTE BRANCA', 'M', 'MT', 'CO', 0),
(5106752, 'Pontes E Lacerda', 'PONTES E LACERDA', 'M', 'MT', 'CO', 0),
(5106778, 'Porto Alegre do Norte', 'PORTO ALEGRE DO NORTE', 'M', 'MT', 'CO', 0),
(5106802, 'Porto dos Gaúchos', 'PORTO DOS GAUCHOS', 'M', 'MT', 'CO', 0),
(5106828, 'Porto Esperidião', 'PORTO ESPERIDIAO', 'M', 'MT', 'CO', 0),
(5106851, 'Porto Estrela', 'PORTO ESTRELA', 'M', 'MT', 'CO', 0),
(5107008, 'Poxoréo', 'POXOREO', 'M', 'MT', 'CO', 0),
(5107040, 'Primavera do Leste', 'PRIMAVERA DO LESTE', 'M', 'MT', 'CO', 0),
(5107065, 'Querência', 'QUERENCIA', 'M', 'MT', 'CO', 0),
(5107107, 'São José dos Quatro Marcos', 'SAO JOSE DOS QUATRO MARCOS', 'M', 'MT', 'CO', 0),
(5107156, 'Reserva do Cabaçal', 'RESERVA DO CABACAL', 'M', 'MT', 'CO', 0),
(5107180, 'Ribeirão Cascalheira', 'RIBEIRAO CASCALHEIRA', 'M', 'MT', 'CO', 0),
(5107198, 'Ribeiraozinho', 'RIBEIRAOZINHO', 'M', 'MT', 'CO', 0),
(5107206, 'Rio Branco', 'RIO BRANCO', 'M', 'MT', 'CO', 0),
(5107248, 'Santa Carmem', 'SANTA CARMEM', 'M', 'MT', 'CO', 0),
(5107263, 'Santo Afonso', 'SANTO AFONSO', 'M', 'MT', 'CO', 0),
(5107297, 'São José do Povo', 'SAO JOSE DO POVO', 'M', 'MT', 'CO', 0),
(5107305, 'São José do Rio Claro', 'SAO JOSE DO RIO CLARO', 'M', 'MT', 'CO', 0),
(5107354, 'São José do Xingu', 'SAO JOSE DO XINGU', 'M', 'MT', 'CO', 0),
(5107404, 'São Pedro da Cipa', 'SAO PEDRO DA CIPA', 'M', 'MT', 'CO', 0),
(5107578, 'Rondolândia', 'RONDOLANDIA', 'M', 'MT', 'CO', 0),
(5107602, 'Rondonópolis', 'RONDONOPOLIS', 'M', 'MT', 'CO', 0),
(5107701, 'Rosário Oeste', 'ROSARIO OESTE', 'M', 'MT', 'CO', 0),
(5107743, 'Santa Cruz do Xingu', 'SANTA CRUZ DO XINGU', 'M', 'MT', 'CO', 0),
(5107750, 'Salto do Céu', 'SALTO DO CEU', 'M', 'MT', 'CO', 0),
(5107768, 'Santa Rita do Trivelato', 'SANTA RITA DO TRIVELATO', 'M', 'MT', 'CO', 0),
(5107776, 'Santa Terezinha', 'SANTA TEREZINHA', 'M', 'MT', 'CO', 0),
(5107792, 'Santo Antônio do Leste', 'SANTO ANTONIO DO LESTE', 'M', 'MT', 'CO', 0),
(5107800, 'Santo Antônio do Leverger', 'SANTO ANTONIO DO LEVERGER', 'M', 'MT', 'CO', 0),
(5107859, 'São Félix do Araguaia', 'SAO FELIX DO ARAGUAIA', 'M', 'MT', 'CO', 0),
(5107875, 'Sapezal', 'SAPEZAL', 'M', 'MT', 'CO', 0),
(5107883, 'Serra Nova Dourada', 'SERRA NOVA DOURADA', 'M', 'MT', 'CO', 0),
(5107909, 'Sinop', 'SINOP', 'M', 'MT', 'CO', 0),
(5107925, 'Sorriso', 'SORRISO', 'M', 'MT', 'CO', 0),
(5107941, 'Tabaporã', 'TABAPORA', 'M', 'MT', 'CO', 0),
(5107958, 'Tangara da Serra', 'TANGARA DA SERRA', 'M', 'MT', 'CO', 0),
(5108006, 'Tapurah', 'TAPURAH', 'M', 'MT', 'CO', 0),
(5108055, 'Terra Nova do Norte', 'TERRA NOVA DO NORTE', 'M', 'MT', 'CO', 0),
(5108105, 'Tesouro', 'TESOURO', 'M', 'MT', 'CO', 0),
(5108204, 'Torixoréu', 'TORIXOREU', 'M', 'MT', 'CO', 0),
(5108303, 'União do Sul', 'UNIAO DO SUL', 'M', 'MT', 'CO', 0),
(5108352, 'Vale de São Domingos', 'VALE DE SAO DOMINGOS', 'M', 'MT', 'CO', 0),
(5108402, 'Várzea Grande', 'VARZEA GRANDE', 'M', 'MT', 'CO', 0),
(5108501, 'Vera', 'VERA', 'M', 'MT', 'CO', 0),
(5108600, 'Vila Rica', 'VILA RICA', 'M', 'MT', 'CO', 0),
(5108808, 'Nova Guarita', 'NOVA GUARITA', 'M', 'MT', 'CO', 0),
(5108857, 'Nova Marilândia', 'NOVA MARILANDIA', 'M', 'MT', 'CO', 0),
(5108907, 'Nova Maringá', 'NOVA MARINGA', 'M', 'MT', 'CO', 0),
(5108956, 'Nova Monte Verde', 'NOVA MONTE VERDE', 'M', 'MT', 'CO', 0),
(5200000, 'Goiás', 'GOIAS', 'U', 'GO', 'CO', 0),
(5200050, 'Abadia de Goiás', 'ABADIA DE GOIAS', 'M', 'GO', 'CO', 0),
(5200100, 'Abadiânia', 'ABADIANIA', 'M', 'GO', 'CO', 0),
(5200134, 'Acreúna', 'ACREUNA', 'M', 'GO', 'CO', 0),
(5200159, 'Adelândia', 'ADELANDIA', 'M', 'GO', 'CO', 0),
(5200175, 'Água Fria de Goias', 'AGUA FRIA DE GOIAS', 'M', 'GO', 'CO', 0),
(5200209, 'Água Limpa', 'AGUA LIMPA', 'M', 'GO', 'CO', 0),
(5200258, 'Águas Lindas de Goiás', 'AGUAS LINDAS DE GOIAS', 'M', 'GO', 'CO', 0),
(5200308, 'Alexânia', 'ALEXANIA', 'M', 'GO', 'CO', 0),
(5200506, 'Aloândia', 'ALOANDIA', 'M', 'GO', 'CO', 0),
(5200555, 'Alto Horizonte', 'ALTO HORIZONTE', 'M', 'GO', 'CO', 0),
(5200605, 'Alto Paraíso de Goiás', 'ALTO PARAISO DE GOIAS', 'M', 'GO', 'CO', 0),
(5200803, 'Alvorada do Norte', 'ALVORADA DO NORTE', 'M', 'GO', 'CO', 0),
(5200829, 'Amaralina', 'AMARALINA', 'M', 'GO', 'CO', 0),
(5200852, 'Americano do Brasil', 'AMERICANO DO BRASIL', 'M', 'GO', 'CO', 0),
(5200902, 'Amorinópolis', 'AMORINOPOLIS', 'M', 'GO', 'CO', 0),
(5201108, 'Anápolis', 'ANAPOLIS', 'M', 'GO', 'CO', 0),
(5201207, 'Anhanguera', 'ANHANGUERA', 'M', 'GO', 'CO', 0),
(5201306, 'Anicuns', 'ANICUNS', 'M', 'GO', 'CO', 0),
(5201405, 'Aparecida de Goiânia', 'APARECIDA DE GOIANIA', 'M', 'GO', 'CO', 0),
(5201454, 'Aparecida do Rio Doce', 'APARECIDA DO RIO DOCE', 'M', 'GO', 'CO', 0),
(5201504, 'Aporé', 'APORE', 'M', 'GO', 'CO', 0),
(5201603, 'Araçu', 'ARACU', 'M', 'GO', 'CO', 0),
(5201702, 'Aragarças', 'ARAGARCAS', 'M', 'GO', 'CO', 0),
(5201801, 'Aragoiânia', 'ARAGOIANIA', 'M', 'GO', 'CO', 0),
(5202155, 'Araguapaz', 'ARAGUAPAZ', 'M', 'GO', 'CO', 0),
(5202353, 'Arenópolis', 'ARENOPOLIS', 'M', 'GO', 'CO', 0),
(5202502, 'Aruanã', 'ARUANA', 'M', 'GO', 'CO', 0),
(5202601, 'Aurilândia', 'AURILANDIA', 'M', 'GO', 'CO', 0),
(5202809, 'Avelinópolis', 'AVELINOPOLIS', 'M', 'GO', 'CO', 0),
(5203104, 'Baliza', 'BALIZA', 'M', 'GO', 'CO', 0),
(5203203, 'Barro Alto', 'BARRO ALTO', 'M', 'GO', 'CO', 0),
(5203302, 'Bela Vista de Goiás', 'BELA VISTA DE GOIAS', 'M', 'GO', 'CO', 0),
(5203401, 'Bom Jardim de Goiás', 'BOM JARDIM DE GOIAS', 'M', 'GO', 'CO', 0),
(5203500, 'Bom Jesus de Goiás', 'BOM JESUS DE GOIAS', 'M', 'GO', 'CO', 0),
(5203559, 'Bonfinópolis', 'BONFINOPOLIS', 'M', 'GO', 'CO', 0),
(5203575, 'Bonópolis', 'BONOPOLIS', 'M', 'GO', 'CO', 0),
(5203609, 'Brazabrantes', 'BRAZABRANTES', 'M', 'GO', 'CO', 0),
(5203807, 'Britania', 'BRITANIA', 'M', 'GO', 'CO', 0),
(5203906, 'Buriti Alegre', 'BURITI ALEGRE', 'M', 'GO', 'CO', 0),
(5203939, 'Buriti de Goiás', 'BURITI DE GOIAS', 'M', 'GO', 'CO', 0),
(5203962, 'Buritinopolis', 'BURITINOPOLIS', 'M', 'GO', 'CO', 0),
(5204003, 'Cabeceiras', 'CABECEIRAS', 'M', 'GO', 'CO', 0),
(5204102, 'Cachoeira Alta', 'CACHOEIRA ALTA', 'M', 'GO', 'CO', 0),
(5204201, 'Cachoeira de Goiás', 'CACHOEIRA DE GOIAS', 'M', 'GO', 'CO', 0),
(5204250, 'Cachoeira Dourada', 'CACHOEIRA DOURADA', 'M', 'GO', 'CO', 0),
(5204300, 'Caçu', 'CACU', 'M', 'GO', 'CO', 0),
(5204409, 'Caiapônia', 'CAIAPONIA', 'M', 'GO', 'CO', 0),
(5204508, 'Caldas Novas', 'CALDAS NOVAS', 'M', 'GO', 'CO', 0),
(5204557, 'Caldazinha', 'CALDAZINHA', 'M', 'GO', 'CO', 0),
(5204607, 'Campestre de Goiás', 'CAMPESTRE DE GOIAS', 'M', 'GO', 'CO', 0),
(5204656, 'Campinaçu', 'CAMPINACU', 'M', 'GO', 'CO', 0),
(5204706, 'Campinorte', 'CAMPINORTE', 'M', 'GO', 'CO', 0),
(5204805, 'Campo Alegre de Goiás', 'CAMPO ALEGRE DE GOIAS', 'M', 'GO', 'CO', 0),
(5204854, 'Campo Limpo de Goiás', 'CAMPO LIMPO DE GOIAS', 'M', 'GO', 'CO', 0),
(5204904, 'Campos Belos', 'CAMPOS BELOS', 'M', 'GO', 'CO', 0),
(5204953, 'Campos Verdes', 'CAMPOS VERDES', 'M', 'GO', 'CO', 0),
(5205000, 'Carmo do Rio Verde', 'CARMO DO RIO VERDE', 'M', 'GO', 'CO', 0),
(5205059, 'Castelândia', 'CASTELANDIA', 'M', 'GO', 'CO', 0),
(5205109, 'Catalão', 'CATALAO', 'M', 'GO', 'CO', 0),
(5205208, 'Caturaí', 'CATURAI', 'M', 'GO', 'CO', 0),
(5205307, 'Cavalcante', 'CAVALCANTE', 'M', 'GO', 'CO', 0),
(5205406, 'Ceres', 'CERES', 'M', 'GO', 'CO', 0),
(5205455, 'Cezarina', 'CEZARINA', 'M', 'GO', 'CO', 0),
(5205471, 'Chapadão do Céu', 'CHAPADAO DO CEU', 'M', 'GO', 'CO', 0),
(5205497, 'Cidade Ocidental', 'CIDADE OCIDENTAL', 'M', 'GO', 'CO', 0),
(5205513, 'Cocalzinho de Goiás', 'COCALZINHO DE GOIAS', 'M', 'GO', 'CO', 0),
(5205521, 'Colinas do Sul', 'COLINAS DO SUL', 'M', 'GO', 'CO', 0),
(5205703, 'Córrego do Ouro', 'CORREGO DO OURO', 'M', 'GO', 'CO', 0),
(5205802, 'Corumbá de Goiás', 'CORUMBA DE GOIAS', 'M', 'GO', 'CO', 0),
(5205901, 'Corumbaíba', 'CORUMBAIBA', 'M', 'GO', 'CO', 0),
(5206206, 'Cristalina', 'CRISTALINA', 'M', 'GO', 'CO', 0),
(5206305, 'Cristianópolis', 'CRISTIANOPOLIS', 'M', 'GO', 'CO', 0),
(5206404, 'Crixás', 'CRIXAS', 'M', 'GO', 'CO', 0),
(5206503, 'Cromínia', 'CROMINIA', 'M', 'GO', 'CO', 0),
(5206602, 'Cumari', 'CUMARI', 'M', 'GO', 'CO', 0),
(5206701, 'Damianópolis', 'DAMIANOPOLIS', 'M', 'GO', 'CO', 0),
(5206800, 'Damolândia', 'DAMOLANDIA', 'M', 'GO', 'CO', 0),
(5206909, 'Davinópolis', 'DAVINOPOLIS', 'M', 'GO', 'CO', 0),
(5207105, 'Diorama', 'DIORAMA', 'M', 'GO', 'CO', 0),
(5207253, 'Doverlândia', 'DOVERLANDIA', 'M', 'GO', 'CO', 0),
(5207352, 'Edealina', 'EDEALINA', 'M', 'GO', 'CO', 0),
(5207402, 'Edéia', 'EDEIA', 'M', 'GO', 'CO', 0),
(5207501, 'Estrela do Norte', 'ESTRELA DO NORTE', 'M', 'GO', 'CO', 0),
(5207535, 'Faina', 'FAINA', 'M', 'GO', 'CO', 0),
(5207600, 'Fazenda Nova', 'FAZENDA NOVA', 'M', 'GO', 'CO', 0),
(5207808, 'Firminópolis', 'FIRMINOPOLIS', 'M', 'GO', 'CO', 0),
(5207907, 'Flores de Goiás', 'FLORES DE GOIAS', 'M', 'GO', 'CO', 0),
(5208004, 'Formosa', 'FORMOSA', 'M', 'GO', 'CO', 0),
(5208103, 'Formoso', 'FORMOSO', 'M', 'GO', 'CO', 0),
(5208152, 'Gameleira de Goiás', 'GAMELEIRA DE GOIAS', 'M', 'GO', 'CO', 0),
(5208301, 'Divinópolis de Goiás', 'DIVINOPOLIS DE GOIAS', 'M', 'GO', 'CO', 0),
(5208400, 'Goianápolis', 'GOIANAPOLIS', 'M', 'GO', 'CO', 0),
(5208509, 'Goiandira', 'GOIANDIRA', 'M', 'GO', 'CO', 0),
(5208608, 'Goianésia', 'GOIANESIA', 'M', 'GO', 'CO', 0),
(5208707, 'Goiânia', 'GOIANIA', 'M', 'GO', 'CO', 0),
(5208806, 'Goianira', 'GOIANIRA', 'M', 'GO', 'CO', 0),
(5208905, 'Goiás', 'GOIAS', 'M', 'GO', 'CO', 0),
(5209101, 'Goiatuba', 'GOIATUBA', 'M', 'GO', 'CO', 0),
(5209150, 'Gouvelandia', 'GOUVELANDIA', 'M', 'GO', 'CO', 0),
(5209200, 'Guapó', 'GUAPO', 'M', 'GO', 'CO', 0),
(5209291, 'Guaraita', 'GUARAITA', 'M', 'GO', 'CO', 0),
(5209408, 'Guarani de Goiás', 'GUARANI DE GOIAS', 'M', 'GO', 'CO', 0),
(5209457, 'Guarinos', 'GUARINOS', 'M', 'GO', 'CO', 0),
(5209606, 'Heitorai', 'HEITORAI', 'M', 'GO', 'CO', 0),
(5209705, 'Hidrolândia', 'HIDROLANDIA', 'M', 'GO', 'CO', 0),
(5209804, 'Hidrolina', 'HIDROLINA', 'M', 'GO', 'CO', 0),
(5209903, 'Iaciara', 'IACIARA', 'M', 'GO', 'CO', 0),
(5209937, 'Inaciolândia', 'INACIOLANDIA', 'M', 'GO', 'CO', 0),
(5209952, 'Indiara', 'INDIARA', 'M', 'GO', 'CO', 0),
(5210000, 'Inhúmas', 'INHUMAS', 'M', 'GO', 'CO', 0),
(5210109, 'Ipameri', 'IPAMERI', 'M', 'GO', 'CO', 0),
(5210158, 'Ipiranga de Goiás', 'IPIRANGA DE GOIAS', 'M', 'GO', 'CO', 0),
(5210208, 'Iporã', 'IPORA', 'M', 'GO', 'CO', 0),
(5210307, 'Israelândia', 'ISRAELANDIA', 'M', 'GO', 'CO', 0),
(5210406, 'Itaberaí', 'ITABERAI', 'M', 'GO', 'CO', 0),
(5210562, 'Itaguari', 'ITAGUARI', 'M', 'GO', 'CO', 0),
(5210604, 'Itaguaru', 'ITAGUARU', 'M', 'GO', 'CO', 0),
(5210802, 'Itaja', 'ITAJA', 'M', 'GO', 'CO', 0),
(5210901, 'Itapaci', 'ITAPACI', 'M', 'GO', 'CO', 0),
(5211008, 'Itapirapuã', 'ITAPIRAPUA', 'M', 'GO', 'CO', 0),
(5211206, 'Itapuranga', 'ITAPURANGA', 'M', 'GO', 'CO', 0),
(5211305, 'Itaruma', 'ITARUMA', 'M', 'GO', 'CO', 0),
(5211404, 'Itauçu', 'ITAUCU', 'M', 'GO', 'CO', 0),
(5211503, 'Itumbiara', 'ITUMBIARA', 'M', 'GO', 'CO', 0),
(5211602, 'Ivolândia', 'IVOLANDIA', 'M', 'GO', 'CO', 0),
(5211701, 'Jandaia', 'JANDAIA', 'M', 'GO', 'CO', 0),
(5211800, 'Jaraguá', 'JARAGUA', 'M', 'GO', 'CO', 0),
(5211909, 'Jataí', 'JATAI', 'M', 'GO', 'CO', 0),
(5212006, 'Jaupaci', 'JAUPACI', 'M', 'GO', 'CO', 0),
(5212055, 'Jesúpolis', 'JESUPOLIS', 'M', 'GO', 'CO', 0),
(5212105, 'Joviânia', 'JOVIANIA', 'M', 'GO', 'CO', 0),
(5212204, 'Jussara', 'JUSSARA', 'M', 'GO', 'CO', 0),
(5212253, 'Lagoa Santa', 'LAGOA SANTA', 'M', 'GO', 'CO', 0),
(5212303, 'Leopoldo de Bulhoes', 'LEOPOLDO DE BULHOES', 'M', 'GO', 'CO', 0),
(5212501, 'Luziânia', 'LUZIANIA', 'M', 'GO', 'CO', 0),
(5212600, 'Mairipotaba', 'MAIRIPOTABA', 'M', 'GO', 'CO', 0),
(5212709, 'Mambaí', 'MAMBAI', 'M', 'GO', 'CO', 0),
(5212808, 'Mara Rosa', 'MARA ROSA', 'M', 'GO', 'CO', 0),
(5212907, 'Marzagão', 'MARZAGAO', 'M', 'GO', 'CO', 0),
(5212956, 'Matrinchã', 'MATRINCHA', 'M', 'GO', 'CO', 0),
(5213004, 'Maurilândia', 'MAURILANDIA', 'M', 'GO', 'CO', 0),
(5213053, 'Mimoso de Goiás', 'MIMOSO DE GOIAS', 'M', 'GO', 'CO', 0),
(5213087, 'Minaçu', 'MINACU', 'M', 'GO', 'CO', 0),
(5213103, 'Mineiros', 'MINEIROS', 'M', 'GO', 'CO', 0),
(5213400, 'Moiporá', 'MOIPORA', 'M', 'GO', 'CO', 0),
(5213509, 'Monte Alegre de Goiás', 'MONTE ALEGRE DE GOIAS', 'M', 'GO', 'CO', 0),
(5213707, 'Montes Claros de Goiás', 'MONTES CLAROS DE GOIAS', 'M', 'GO', 'CO', 0),
(5213756, 'Montividiu', 'MONTIVIDIU', 'M', 'GO', 'CO', 0),
(5213772, 'Montividiu do Norte', 'MONTIVIDIU DO NORTE', 'M', 'GO', 'CO', 0),
(5213806, 'Morrinhos', 'MORRINHOS', 'M', 'GO', 'CO', 0),
(5213855, 'Morro Agudo de Goiás', 'MORRO AGUDO DE GOIAS', 'M', 'GO', 'CO', 0),
(5213905, 'Mossâmedes', 'MOSSAMEDES', 'M', 'GO', 'CO', 0),
(5214002, 'Mozarlândia', 'MOZARLANDIA', 'M', 'GO', 'CO', 0),
(5214051, 'Mundo Novo', 'MUNDO NOVO', 'M', 'GO', 'CO', 0),
(5214101, 'Mutunópolis', 'MUTUNOPOLIS', 'M', 'GO', 'CO', 0),
(5214408, 'Nazário', 'NAZARIO', 'M', 'GO', 'CO', 0),
(5214507, 'Nerópolis', 'NEROPOLIS', 'M', 'GO', 'CO', 0),
(5214606, 'Niquelândia', 'NIQUELANDIA', 'M', 'GO', 'CO', 0),
(5214705, 'Nova América', 'NOVA AMERICA', 'M', 'GO', 'CO', 0),
(5214804, 'Nova Aurora', 'NOVA AURORA', 'M', 'GO', 'CO', 0),
(5214838, 'Nova Crixás', 'NOVA CRIXAS', 'M', 'GO', 'CO', 0),
(5214861, 'Nova Glória', 'NOVA GLORIA', 'M', 'GO', 'CO', 0),
(5214879, 'Nova Iguaçu de Goiás', 'NOVA IGUACU DE GOIAS', 'M', 'GO', 'CO', 0),
(5214903, 'Nova Roma', 'NOVA ROMA', 'M', 'GO', 'CO', 0),
(5215009, 'Nova Veneza', 'NOVA VENEZA', 'M', 'GO', 'CO', 0),
(5215207, 'Novo Brasil', 'NOVO BRASIL', 'M', 'GO', 'CO', 0),
(5215231, 'Novo Gama', 'NOVO GAMA', 'M', 'GO', 'CO', 0),
(5215256, 'Novo Planalto', 'NOVO PLANALTO', 'M', 'GO', 'CO', 0),
(5215306, 'Orizona', 'ORIZONA', 'M', 'GO', 'CO', 0),
(5215405, 'Ouro Verde de Goias', 'OURO VERDE DE GOIAS', 'M', 'GO', 'CO', 0),
(5215504, 'Ouvidor', 'OUVIDOR', 'M', 'GO', 'CO', 0),
(5215603, 'Padre Bernardo', 'PADRE BERNARDO', 'M', 'GO', 'CO', 0),
(5215652, 'Palestina de Goiás', 'PALESTINA DE GOIAS', 'M', 'GO', 'CO', 0),
(5215702, 'Palmeiras de Goiás', 'PALMEIRAS DE GOIAS', 'M', 'GO', 'CO', 0),
(5215801, 'Palmelo', 'PALMELO', 'M', 'GO', 'CO', 0),
(5215900, 'Palminópolis', 'PALMINOPOLIS', 'M', 'GO', 'CO', 0),
(5216007, 'Panamá', 'PANAMA', 'M', 'GO', 'CO', 0),
(5216304, 'Paranaiguara', 'PARANAIGUARA', 'M', 'GO', 'CO', 0),
(5216403, 'Paraúna', 'PARAUNA', 'M', 'GO', 'CO', 0),
(5216452, 'Perolândia', 'PEROLANDIA', 'M', 'GO', 'CO', 0),
(5216809, 'Petrolina de Goiás', 'PETROLINA DE GOIAS', 'M', 'GO', 'CO', 0),
(5216908, 'Pilar de Goiás', 'PILAR DE GOIAS', 'M', 'GO', 'CO', 0),
(5217104, 'Piracanjuba', 'PIRACANJUBA', 'M', 'GO', 'CO', 0),
(5217203, 'Piranhas', 'PIRANHAS', 'M', 'GO', 'CO', 0),
(5217302, 'Pirenópolis', 'PIRENOPOLIS', 'M', 'GO', 'CO', 0),
(5217401, 'Pires do Rio', 'PIRES DO RIO', 'M', 'GO', 'CO', 0),
(5217609, 'Planaltina', 'PLANALTINA', 'M', 'GO', 'CO', 0),
(5217708, 'Pontalina', 'PONTALINA', 'M', 'GO', 'CO', 0),
(5218003, 'Porangatu', 'PORANGATU', 'M', 'GO', 'CO', 0),
(5218052, 'Porteirao', 'PORTEIRAO', 'M', 'GO', 'CO', 0),
(5218102, 'Portelândia', 'PORTELANDIA', 'M', 'GO', 'CO', 0),
(5218300, 'Posse', 'POSSE', 'M', 'GO', 'CO', 0),
(5218391, 'Professor Jamil', 'PROFESSOR JAMIL', 'M', 'GO', 'CO', 0),
(5218508, 'Quirinopolis', 'QUIRINOPOLIS', 'M', 'GO', 'CO', 0),
(5218607, 'Rialma', 'RIALMA', 'M', 'GO', 'CO', 0),
(5218706, 'Rianápolis', 'RIANAPOLIS', 'M', 'GO', 'CO', 0),
(5218789, 'Rio Quente', 'RIO QUENTE', 'M', 'GO', 'CO', 0),
(5218805, 'Rio Verde', 'RIO VERDE', 'M', 'GO', 'CO', 0),
(5218904, 'Rubiataba', 'RUBIATABA', 'M', 'GO', 'CO', 0),
(5219001, 'Sanclerlândia', 'SANCLERLANDIA', 'M', 'GO', 'CO', 0),
(5219100, 'Santa Bárbara de Goiás', 'SANTA BARBARA DE GOIAS', 'M', 'GO', 'CO', 0),
(5219209, 'Santa Cruz de Goiás', 'SANTA CRUZ DE GOIAS', 'M', 'GO', 'CO', 0),
(5219258, 'Santa Fé de Goiás', 'SANTA FE DE GOIAS', 'M', 'GO', 'CO', 0),
(5219308, 'Santa Helena de Goiás', 'SANTA HELENA DE GOIAS', 'M', 'GO', 'CO', 0),
(5219357, 'Santa Isabel', 'SANTA ISABEL', 'M', 'GO', 'CO', 0),
(5219407, 'Santa Rita do Araguaia', 'SANTA RITA DO ARAGUAIA', 'M', 'GO', 'CO', 0),
(5219456, 'Santa Rita do Novo Destino', 'SANTA RITA DO NOVO DESTINO', 'M', 'GO', 'CO', 0),
(5219506, 'Santa Rosa de Goiás', 'SANTA ROSA DE GOIAS', 'M', 'GO', 'CO', 0),
(5219605, 'Santa Tereza de Goiás', 'SANTA TEREZA DE GOIAS', 'M', 'GO', 'CO', 0),
(5219704, 'Santa Terezinha de Goiás', 'SANTA TEREZINHA DE GOIAS', 'M', 'GO', 'CO', 0),
(5219712, 'Santo Antônio da Barra', 'SANTO ANTONIO DA BARRA', 'M', 'GO', 'CO', 0),
(5219738, 'Santo Antônio de Goiás', 'SANTO ANTONIO DE GOIAS', 'M', 'GO', 'CO', 0),
(5219753, 'Santo Antônio do Descoberto', 'SANTO ANTONIO DO DESCOBERTO', 'M', 'GO', 'CO', 0),
(5219803, 'São Domingos', 'SAO DOMINGOS', 'M', 'GO', 'CO', 0),
(5219902, 'São Francisco de Goiás', 'SAO FRANCISCO DE GOIAS', 'M', 'GO', 'CO', 0),
(5220009, 'São João D''Aliança', 'SAO JOAO D''ALIANCA', 'M', 'GO', 'CO', 0),
(5220058, 'São João da Paraúna', 'SAO JOAO DA PARAUNA', 'M', 'GO', 'CO', 0),
(5220108, 'São Luis de Montes Belos', 'SAO LUIS DE MONTES BELOS', 'M', 'GO', 'CO', 0),
(5220157, 'São Luiz do Norte', 'SAO LUIZ DO NORTE', 'M', 'GO', 'CO', 0),
(5220207, 'São Miguel do Araguaia', 'SAO MIGUEL DO ARAGUAIA', 'M', 'GO', 'CO', 0),
(5220264, 'São Miguel do Passa Quatro', 'SAO MIGUEL DO PASSA QUATRO', 'M', 'GO', 'CO', 0),
(5220280, 'São Patrício', 'SAO PATRICIO', 'M', 'GO', 'CO', 0),
(5220405, 'São Simão', 'SAO SIMAO', 'M', 'GO', 'CO', 0),
(5220454, 'Senador Canedo', 'SENADOR CANEDO', 'M', 'GO', 'CO', 0),
(5220504, 'Serranópolis', 'SERRANOPOLIS', 'M', 'GO', 'CO', 0),
(5220603, 'Silvânia', 'SILVANIA', 'M', 'GO', 'CO', 0),
(5220686, 'Simolândia', 'SIMOLANDIA', 'M', 'GO', 'CO', 0),
(5220702, 'Sítio D''Abadia', 'SITIO D''ABADIA', 'M', 'GO', 'CO', 0),
(5221007, 'Taquaral de Goiás', 'TAQUARAL DE GOIAS', 'M', 'GO', 'CO', 0),
(5221080, 'Teresina de Goiás', 'TERESINA DE GOIAS', 'M', 'GO', 'CO', 0),
(5221197, 'Terezópolis de Goiás', 'TEREZOPOLIS DE GOIAS', 'M', 'GO', 'CO', 0),
(5221304, 'Três Ranchos', 'TRES RANCHOS', 'M', 'GO', 'CO', 0),
(5221403, 'Trindade', 'TRINDADE', 'M', 'GO', 'CO', 0),
(5221452, 'Trombas', 'TROMBAS', 'M', 'GO', 'CO', 0),
(5221502, 'Turvânia', 'TURVANIA', 'M', 'GO', 'CO', 0),
(5221551, 'Turvelândia', 'TURVELANDIA', 'M', 'GO', 'CO', 0),
(5221577, 'Uirapuru', 'UIRAPURU', 'M', 'GO', 'CO', 0),
(5221601, 'Uruaçu', 'URUACU', 'M', 'GO', 'CO', 0),
(5221700, 'Uruana', 'URUANA', 'M', 'GO', 'CO', 0),
(5221809, 'Urutaí', 'URUTAI', 'M', 'GO', 'CO', 0),
(5221858, 'Valparaíso de Goiás', 'VALPARAISO DE GOIAS', 'M', 'GO', 'CO', 0),
(5221908, 'Varjão', 'VARJAO', 'M', 'GO', 'CO', 0),
(5222005, 'Vianópolis', 'VIANOPOLIS', 'M', 'GO', 'CO', 0),
(5222054, 'Vicentinópolis', 'VICENTINOPOLIS', 'M', 'GO', 'CO', 0),
(5222203, 'Vila Boa', 'VILA BOA', 'M', 'GO', 'CO', 0),
(5222302, 'Vila Propício', 'VILA PROPICIO', 'M', 'GO', 'CO', 0),
(5300000, 'Distrito Federal', 'DISTRITO FEDERAL', 'U', 'DF', 'CO', 0),
(5300108, 'Brasília', 'BRASILIA', 'M', 'DF', 'CO', 0),
(8000000, 'Exterior', 'EXTERIOR', 'R', 'EX', 'EX', 0),
(9000000, 'Nacional', 'NACIONAL', 'R', 'NA', 'NA', 0),
(9100000, 'Região Norte', 'REGIAO NORTE', 'R', 'NO', 'NO', 0),
(9200000, 'Região Nordeste', 'REGIAO NORDESTE', 'R', 'NE', 'NE', 0),
(9300000, 'Região Sudeste', 'REGIAO SUDESTE', 'R', 'SD', 'SD', 0),
(9400000, 'Região Sul', 'REGIAO SUL', 'R', 'SL', 'SL', 0),
(9500000, 'Região Centro Oeste', 'REGIAO CENTRO OESTE', 'R', 'CO', 'CO', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `mandato`
--

CREATE TABLE IF NOT EXISTS `mandato` (
  `cod_mandato` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_afastamento` tinyint(4) DEFAULT NULL,
  `num_legislatura` int(11) NOT NULL,
  `cod_coligacao` int(11) DEFAULT NULL,
  `tip_causa_fim_mandato` tinyint(4) DEFAULT NULL,
  `dat_inicio_mandato` date DEFAULT NULL,
  `dat_fim_mandato` date DEFAULT NULL,
  `num_votos_recebidos` int(11) DEFAULT NULL,
  `dat_expedicao_diploma` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_titular` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_mandato`),
  KEY `idx_coligacao` (`cod_coligacao`),
  KEY `idx_parlamentar` (`cod_parlamentar`),
  KEY `idx_afastamento` (`tip_afastamento`),
  KEY `idx_mandato_legislatura` (`num_legislatura`,`cod_parlamentar`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`),
  KEY `tip_causa_fim_mandato` (`tip_causa_fim_mandato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `mandato`:
--   `cod_coligacao`
--       `coligacao` -> `cod_coligacao`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_afastamento`
--       `tipo_afastamento` -> `tip_afastamento`
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `materia_apresentada_sessao`
--

CREATE TABLE IF NOT EXISTS `materia_apresentada_sessao` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) unsigned NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `fk_cod_materia` (`cod_materia`),
  KEY `idx_apres_datord` (`dat_ordem`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `materia_apresentada_sessao`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `materia_legislativa`
--

CREATE TABLE IF NOT EXISTS `materia_legislativa` (
  `cod_materia` int(11) NOT NULL AUTO_INCREMENT,
  `tip_id_basica` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `num_ident_basica` int(11) NOT NULL,
  `ano_ident_basica` smallint(6) NOT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_regime_tramitacao` tinyint(4) NOT NULL,
  `dat_publicacao` date DEFAULT NULL,
  `tip_origem_externa` int(11) DEFAULT NULL,
  `num_origem_externa` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ano_origem_externa` smallint(6) DEFAULT NULL,
  `dat_origem_externa` date DEFAULT NULL,
  `cod_local_origem_externa` int(11) DEFAULT NULL,
  `nom_apelido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL,
  `ind_polemica` tinyint(4) DEFAULT NULL,
  `des_objeto` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_complementar` tinyint(4) DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `cod_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`),
  KEY `idx_matleg_ident` (`ind_excluido`,`tip_id_basica`,`ano_ident_basica`,`num_ident_basica`),
  KEY `tip_id_basica` (`tip_id_basica`),
  KEY `cod_local_origem_externa` (`cod_local_origem_externa`),
  KEY `tip_origem_externa` (`tip_origem_externa`),
  KEY `cod_regime_tramitacao` (`cod_regime_tramitacao`),
  KEY `idx_dat_apresentacao` (`dat_apresentacao`,`tip_id_basica`,`ind_excluido`),
  KEY `idx_matleg_dat_publicacao` (`dat_publicacao`,`tip_id_basica`,`ind_excluido`),
  KEY `cod_situacao` (`cod_situacao`),
  FULLTEXT KEY `txt_indexacao` (`txt_indexacao`),
  FULLTEXT KEY `txt_ementa` (`txt_ementa`),
  FULLTEXT KEY `txt_observacao` (`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `materia_legislativa`:
--   `cod_situacao`
--       `tipo_situacao_materia` -> `tip_situacao_materia`
--   `tip_id_basica`
--       `tipo_materia_legislativa` -> `tip_materia`
--   `cod_regime_tramitacao`
--       `regime_tramitacao` -> `cod_regime_tramitacao`
--   `cod_local_origem_externa`
--       `origem` -> `cod_origem`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `mesa_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `mesa_sessao_plenaria` (
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_sessao_leg` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `ind_excluido` tinyint(4) unsigned DEFAULT NULL,
  PRIMARY KEY (`cod_cargo`,`cod_sessao_leg`,`cod_parlamentar`,`cod_sessao_plen`),
  KEY `cod_sessao_leg` (`cod_sessao_leg`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `mesa_sessao_plenaria`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `nivel_instrucao`
--

CREATE TABLE IF NOT EXISTS `nivel_instrucao` (
  `cod_nivel_instrucao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_nivel_instrucao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_nivel_instrucao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `nivel_instrucao`
--

INSERT INTO `nivel_instrucao` (`cod_nivel_instrucao`, `des_nivel_instrucao`, `ind_excluido`) VALUES
(1, 'Fundamental', 0),
(2, 'Médio', 0),
(3, 'Ensino Superior', 0),
(4, 'Mestrado', 0),
(5, 'Doutorado', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `norma_juridica`
--

CREATE TABLE IF NOT EXISTS `norma_juridica` (
  `cod_norma` int(11) NOT NULL AUTO_INCREMENT,
  `tip_norma` tinyint(4) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `num_norma` int(11) NOT NULL,
  `ano_norma` smallint(6) NOT NULL,
  `tip_esfera_federacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_norma` date DEFAULT NULL,
  `dat_publicacao` date DEFAULT NULL,
  `des_veiculo_publicacao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_pag_inicio_publ` int(11) DEFAULT NULL,
  `num_pag_fim_publ` int(11) DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_complemento` tinyint(4) DEFAULT NULL,
  `cod_assunto` char(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_situacao` int(11) DEFAULT NULL,
  `dat_vigencia` date DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_norma`),
  KEY `cod_assunto` (`cod_assunto`),
  KEY `tip_norma` (`tip_norma`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_ano_numero` (`ano_norma`,`num_norma`,`ind_excluido`),
  KEY `dat_norma` (`dat_norma`),
  KEY `cod_situacao` (`cod_situacao`),
  FULLTEXT KEY `txt_ementa` (`txt_ementa`),
  FULLTEXT KEY `txt_indexacao` (`txt_indexacao`),
  FULLTEXT KEY `txt_observacao` (`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `norma_juridica`:
--   `cod_situacao`
--       `tipo_situacao_norma` -> `tip_situacao_norma`
--   `tip_norma`
--       `tipo_norma_juridica` -> `tip_norma`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `numeracao`
--

CREATE TABLE IF NOT EXISTS `numeracao` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `tip_materia` int(11) NOT NULL,
  `num_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ano_materia` smallint(6) NOT NULL,
  `dat_materia` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`,`num_ordem`),
  KEY `cod_materia` (`cod_materia`),
  KEY `tip_materia` (`tip_materia`),
  KEY `idx_numer_identificacao` (`tip_materia`,`num_materia`,`ano_materia`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `numeracao`:
--   `tip_materia`
--       `tipo_materia_legislativa` -> `tip_materia`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `oradores`
--

CREATE TABLE IF NOT EXISTS `oradores` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `oradores`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `oradores_expediente`
--

CREATE TABLE IF NOT EXISTS `oradores_expediente` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `oradores_expediente`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `ordem_dia`
--

CREATE TABLE IF NOT EXISTS `ordem_dia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) unsigned NOT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_votacao` int(11) unsigned NOT NULL,
  `tip_quorum` int(11) DEFAULT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_dat_ordem` (`dat_ordem`,`ind_excluido`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `tip_quorum` (`tip_quorum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `ordem_dia`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `ordem_dia_presenca`
--

CREATE TABLE IF NOT EXISTS `ordem_dia_presenca` (
  `cod_presenca_ordem_dia` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_ordem_dia`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `dat_ordem` (`dat_ordem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `ordem_dia_presenca`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `orgao`
--

CREATE TABLE IF NOT EXISTS `orgao` (
  `cod_orgao` int(11) NOT NULL AUTO_INCREMENT,
  `nom_orgao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_orgao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `end_orgao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_orgao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_orgao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=8 ;

--
-- Fazendo dump de dados para tabela `orgao`
--

INSERT INTO `orgao` (`cod_orgao`, `nom_orgao`, `sgl_orgao`, `ind_unid_deliberativa`, `end_orgao`, `num_tel_orgao`, `ind_excluido`) VALUES
(1, 'Plenário', 'PLEN', 1, NULL, NULL, 0),
(2, 'Protocolo', 'PROT', 0, NULL, NULL, 0),
(3, 'Mesa Diretora', 'MESA', 0, NULL, NULL, 0),
(4, 'Externo - Executivo', 'PM', 0, NULL, NULL, 0),
(5, 'Externo - Outros', 'EXT', 0, NULL, NULL, 0),
(6, 'Departamento Legislativo', 'DL', 0, NULL, NULL, 0),
(7, 'Arquivo', 'ARQ', 0, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `origem`
--

CREATE TABLE IF NOT EXISTS `origem` (
  `cod_origem` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_origem` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_origem` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_origem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `parecer`
--

CREATE TABLE IF NOT EXISTS `parecer` (
  `cod_relatoria` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `tip_conclusao` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_relatoria`,`cod_materia`),
  KEY `idx_parecer_materia` (`cod_materia`,`ind_excluido`),
  KEY `cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `parecer`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `parlamentar`
--

CREATE TABLE IF NOT EXISTS `parlamentar` (
  `cod_parlamentar` int(11) NOT NULL AUTO_INCREMENT,
  `cod_nivel_instrucao` tinyint(4) DEFAULT NULL,
  `tip_situacao_militar` tinyint(4) DEFAULT NULL,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_parlamentar` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_casa` int(11) NOT NULL,
  `num_gab_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade_resid` int(11) DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_web` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_profissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_local_atuacao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_ativo` tinyint(4) NOT NULL DEFAULT '1',
  `txt_biografia` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_parlamentar`),
  KEY `cod_localidade_resid` (`cod_localidade_resid`),
  KEY `tip_situacao_militar` (`tip_situacao_militar`),
  KEY `cod_nivel_instrucao` (`cod_nivel_instrucao`),
  KEY `ind_parlamentar_ativo` (`ind_ativo`,`ind_excluido`),
  FULLTEXT KEY `nom_completo` (`nom_completo`),
  FULLTEXT KEY `nom_parlamentar` (`nom_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `parlamentar`:
--   `cod_localidade_resid`
--       `localidade` -> `cod_localidade`
--   `cod_nivel_instrucao`
--       `nivel_instrucao` -> `cod_nivel_instrucao`
--   `tip_situacao_militar`
--       `tipo_situacao_militar` -> `tip_situacao_militar`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `partido`
--

CREATE TABLE IF NOT EXISTS `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=44 ;

--
-- Fazendo dump de dados para tabela `partido`
--

INSERT INTO `partido` (`cod_partido`, `sgl_partido`, `nom_partido`, `dat_criacao`, `dat_extincao`, `ind_excluido`) VALUES
(1, 'PMDB', 'Partido do Movimento Democrático Brasileiro', '1981-06-30', NULL, 0),
(2, 'PTB', 'Partido Trabalhista Brasileiro', '1981-11-03', NULL, 0),
(3, 'PDT', 'Partido Democrático Trabalhista', '1981-11-10', NULL, 0),
(4, 'PT', 'Partido dos Trabalhadores', '1982-02-10', NULL, 0),
(5, 'DEM', 'Democratas', '2007-03-28', NULL, 0),
(6, 'PCdoB', 'Partido Comunista do Brasil', '1988-06-23', NULL, 0),
(7, 'PSB', 'Partido Socialista Brasileiro', '1988-07-01', NULL, 0),
(8, 'PSDB', 'Partido da Social Democracia Brasileira', '1989-08-24', NULL, 0),
(9, 'PTC', 'Partido Trabalhista Cristão', '1990-02-22', NULL, 0),
(10, 'PSC', 'Partido Social Cristão', '1990-03-29', NULL, 0),
(11, 'PMN', 'Partido da Mobilização Nacional', '1990-10-25', NULL, 0),
(12, 'PRP', 'Partido Republicano Progressista', '2005-08-25', NULL, 0),
(13, 'PPS', 'Partido Popular Socialista', '1992-03-19', NULL, 0),
(14, 'PV', 'Partido Verde', '1993-09-30', NULL, 0),
(15, 'PTdoB', 'Partido Trabalhista do Brasil', '1994-10-11', NULL, 0),
(16, 'PP', 'Partido Progressista', '1995-11-16', NULL, 0),
(17, 'PSTU', 'Partido Socialista dos Trabalhadores Unificado', '1995-12-19', NULL, 0),
(18, 'PCB', 'Partido Comunista Brasileiro', '1996-05-09', NULL, 0),
(19, 'PRTB', 'Partido Renovador Trabalhista Brasileiro', '1997-02-18', NULL, 0),
(20, 'PHS', 'Partido Humanista da Solidariedade', '1997-03-20', NULL, 0),
(21, 'PSDC', 'Partido Social Democrata Cristão', '1997-08-05', NULL, 0),
(22, 'PCO', 'Partido da Causa Operária', '1997-09-30', NULL, 0),
(23, 'PTN', 'Partido Trabalhista Nacional', '1997-10-02', NULL, 0),
(24, 'PSL', 'Partido Social Liberal', '1998-06-02', NULL, 0),
(25, 'PRB', 'Partido Republicano Brasileiro', '2005-08-25', NULL, 0),
(26, 'PSOL', 'Partido Socialismo e Liberdade', '2005-09-15', NULL, 0),
(27, 'PR', 'Partido da República', '2006-12-19', NULL, 0),
(28, 'PPB', 'Partido Progressista Brasileiro', '1993-01-31', '2003-04-04', 0),
(29, 'ARENA', 'Aliança Renovadora Nacional', '1966-04-04', '1979-12-20', 0),
(30, 'MDB', 'Movimento Democrático Brasileiro', '1966-03-24', '1979-11-27', 0),
(31, 'PDS', 'Partido Democrático Social', '1980-01-30', '1993-04-04', 0),
(32, 'PL', 'Partido Liberal', '1985-02-03', '2006-12-21', 0),
(33, 'PFL', 'Partido da Frente Liberal', '1985-01-24', '2007-03-28', 0),
(34, 'PSD', 'Partido Social Democrático', '2011-09-27', NULL, 0),
(35, 'PSP', 'Partido Social Progressista', '1945-11-08', '1946-11-19', 0),
(36, 'PDC', 'Partido Democrata Cristão', '1945-07-09', '1965-10-27', 0),
(37, 'UDN', 'União Democrática Nacional', '1945-04-07', '1965-10-27', 0),
(38, 'PRT', 'Partido Revolucionário dos Trabalhadores', '1969-01-13', '1971-02-05', 0),
(39, 'PPR', 'Partido Progressista Renovador', '1993-04-04', '1995-04-15', 0),
(40, 'PPL', 'Partido Pátria Livre', '2011-10-04', NULL, 0),
(41, 'PEN', 'Partido Ecológico Nacional', '2012-06-19', NULL, 0),
(42, 'PROS', 'Partido Republicano da Ordem Social', '2013-09-24', NULL, 0),
(43, 'SDD', 'Solidariedade', '2013-09-24', NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `periodo_comp_comissao`
--

CREATE TABLE IF NOT EXISTS `periodo_comp_comissao` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompcom_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `periodo_comp_mesa`
--

CREATE TABLE IF NOT EXISTS `periodo_comp_mesa` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompmesa_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `periodo_comp_mesa`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `proposicao`
--

CREATE TABLE IF NOT EXISTS `proposicao` (
  `cod_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `tip_proposicao` int(11) NOT NULL,
  `dat_envio` datetime NOT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `txt_descricao` varchar(400) COLLATE utf8_unicode_ci NOT NULL,
  `cod_mat_ou_doc` int(11) DEFAULT NULL,
  `dat_devolucao` datetime DEFAULT NULL,
  `txt_justif_devolucao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_proposicao`),
  KEY `tip_proposicao` (`tip_proposicao`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_autor` (`cod_autor`),
  KEY `idx_prop_autor` (`dat_envio`,`dat_recebimento`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `proposicao`:
--   `tip_proposicao`
--       `tipo_proposicao` -> `tip_proposicao`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `protocolo`
--

CREATE TABLE IF NOT EXISTS `protocolo` (
  `cod_protocolo` int(7) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `num_protocolo` int(7) unsigned zerofill DEFAULT NULL,
  `ano_protocolo` smallint(6) NOT NULL,
  `dat_protocolo` date NOT NULL,
  `hor_protocolo` time NOT NULL DEFAULT '00:00:00',
  `dat_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tip_protocolo` int(4) NOT NULL,
  `tip_processo` int(4) NOT NULL,
  `txt_interessado` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `txt_assunto_ementa` text COLLATE utf8_unicode_ci,
  `tip_documento` int(11) DEFAULT NULL,
  `tip_materia` int(11) DEFAULT NULL,
  `num_paginas` int(6) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_anulado` tinyint(4) NOT NULL DEFAULT '0',
  `txt_user_anulacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_anulacao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_just_anulacao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp_anulacao` datetime DEFAULT NULL,
  PRIMARY KEY (`cod_protocolo`),
  UNIQUE KEY `idx_num_protocolo` (`num_protocolo`,`ano_protocolo`),
  KEY `tip_protocolo` (`tip_protocolo`),
  KEY `cod_autor` (`cod_autor`),
  KEY `tip_materia` (`tip_materia`),
  KEY `tip_documento` (`tip_documento`),
  KEY `dat_protocolo` (`dat_protocolo`),
  FULLTEXT KEY `txt_assunto_ementa` (`txt_assunto_ementa`),
  FULLTEXT KEY `txt_interessado` (`txt_interessado`),
  FULLTEXT KEY `txt_observacao` (`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `protocolo`:
--   `tip_materia`
--       `tipo_materia_legislativa` -> `tip_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_documento`
--       `tipo_documento_administrativo` -> `tip_documento`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `regime_tramitacao`
--

CREATE TABLE IF NOT EXISTS `regime_tramitacao` (
  `cod_regime_tramitacao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_regime_tramitacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_regime_tramitacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `regime_tramitacao`
--

INSERT INTO `regime_tramitacao` (`cod_regime_tramitacao`, `des_regime_tramitacao`, `ind_excluido`) VALUES
(1, 'Ordinária', 0),
(2, 'Urgência', 0),
(3, 'Prioridade', 0),
(4, 'Especial - Veto', 0),
(5, 'Especial - Leis Orçamentárias', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `registro_votacao`
--

CREATE TABLE IF NOT EXISTS `registro_votacao` (
  `cod_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_resultado_votacao` int(10) unsigned NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `cod_ordem` int(11) NOT NULL,
  `cod_emenda` int(11) DEFAULT NULL,
  `cod_subemenda` int(11) DEFAULT NULL,
  `cod_substitutivo` int(11) DEFAULT NULL,
  `num_votos_sim` tinyint(4) unsigned NOT NULL,
  `num_votos_nao` tinyint(4) unsigned NOT NULL,
  `num_abstencao` tinyint(4) unsigned NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`cod_votacao`),
  KEY `cod_ordem` (`cod_ordem`),
  KEY `cod_materia` (`cod_materia`),
  KEY `tip_resultado_votacao` (`tip_resultado_votacao`),
  KEY `cod_emenda` (`cod_emenda`),
  KEY `cod_subemenda` (`cod_subemenda`),
  KEY `cod_substitutivo` (`cod_substitutivo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `registro_votacao`:
--   `cod_substitutivo`
--       `substitutivo` -> `cod_substitutivo`
--   `tip_resultado_votacao`
--       `tipo_resultado_votacao` -> `tip_resultado_votacao`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_emenda`
--       `emenda` -> `cod_emenda`
--   `cod_subemenda`
--       `subemenda` -> `cod_subemenda`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `registro_votacao_parlamentar`
--

CREATE TABLE IF NOT EXISTS `registro_votacao_parlamentar` (
  `cod_votacao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  `vot_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_votacao`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_votacao` (`cod_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA TABELAS `registro_votacao_parlamentar`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_votacao`
--       `registro_votacao` -> `cod_votacao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `relatoria`
--

CREATE TABLE IF NOT EXISTS `relatoria` (
  `cod_relatoria` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_fim_relatoria` tinyint(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `dat_desig_relator` date NOT NULL,
  `dat_destit_relator` date DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `tip_conclusao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_relatoria`),
  KEY `cod_comissao` (`cod_comissao`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `tip_fim_relatoria` (`tip_fim_relatoria`),
  KEY `idx_relat_materia` (`cod_materia`,`cod_parlamentar`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `relatoria`:
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_fim_relatoria`
--       `tipo_fim_relatoria` -> `tip_fim_relatoria`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `reuniao_comissao`
--

CREATE TABLE IF NOT EXISTS `reuniao_comissao` (
  `cod_reuniao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) NOT NULL,
  `num_reuniao` int(11) NOT NULL,
  `dat_inicio_reuniao` date NOT NULL,
  `hr_inicio_reuniao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_reuniao`),
  KEY `cod_comissao` (`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `reuniao_comissao`:
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `sessao_legislativa`
--

CREATE TABLE IF NOT EXISTS `sessao_legislativa` (
  `cod_sessao_leg` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `num_sessao_leg` tinyint(4) NOT NULL,
  `tip_sessao_leg` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_inicio_intervalo` date DEFAULT NULL,
  `dat_fim_intervalo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_leg`),
  KEY `idx_sessleg_datas` (`dat_inicio`,`ind_excluido`,`dat_fim`,`dat_inicio_intervalo`,`dat_fim_intervalo`),
  KEY `idx_sessleg_legislatura` (`num_legislatura`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `sessao_legislativa`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL AUTO_INCREMENT,
  `cod_andamento_sessao` int(11) DEFAULT NULL,
  `tip_sessao` tinyint(4) NOT NULL,
  `cod_sessao_leg` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `tip_expediente` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_inicio_sessao` date NOT NULL,
  `dia_sessao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hr_inicio_sessao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hr_fim_sessao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_sessao_plen` int(11) unsigned NOT NULL,
  `dat_fim_sessao` date DEFAULT NULL,
  `url_audio` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url_video` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_sessao_plen`),
  KEY `cod_sessao_leg` (`cod_sessao_leg`),
  KEY `tip_sessao` (`tip_sessao`),
  KEY `num_legislatura` (`num_legislatura`),
  KEY `dat_inicio_sessao` (`dat_inicio_sessao`),
  KEY `num_sessao_plen` (`num_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `sessao_plenaria`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--   `tip_sessao`
--       `tipo_sessao_plenaria` -> `tip_sessao`
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `sessao_plenaria_presenca`
--

CREATE TABLE IF NOT EXISTS `sessao_plenaria_presenca` (
  `cod_presenca_sessao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `dat_sessao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_sessao`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `dat_sessao` (`dat_sessao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `sessao_plenaria_presenca`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `status_tramitacao`
--

CREATE TABLE IF NOT EXISTS `status_tramitacao` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=53 ;

--
-- Fazendo dump de dados para tabela `status_tramitacao`
--

INSERT INTO `status_tramitacao` (`cod_status`, `sgl_status`, `des_status`, `ind_fim_tramitacao`, `ind_retorno_tramitacao`, `ind_excluido`) VALUES
(1, 'APRESPLEN', 'Proposição apresentada em Plenário', 1, 0, 1),
(2, 'AGPARECER', 'Aguardando emissão de parecer da comissão', 0, 1, 0),
(3, 'INCLORDIA', 'Proposição inclusa na ordem do dia', 0, 1, 0),
(4, 'RETAUTOR', 'Proposição retirada pelo autor', 1, 0, 0),
(5, 'AUTUAPAUTA', 'Proposição autuada e cumprindo prazo de pauta', 0, 1, 0),
(6, 'PARECERFAV', 'Parecer favorável da comissão', 0, 1, 0),
(7, 'PARECCONTR', 'Parecer contrário da comissão de mérito', 0, 1, 0),
(8, 'PARECERARQ', 'Parecer da CCJR ou da CFO pelo arquivamento da proposição', 1, 0, 0),
(9, 'APROVADA', 'Proposição aprovada', 1, 0, 0),
(10, 'REJEITADA', 'Proposição rejeitada pelo Plenário', 1, 0, 0),
(11, 'MAT', 'Matéria', 1, 0, 1),
(12, 'DISTRCOMIS', 'Proposição distribuída às comissões', 0, 1, 0),
(13, 'ORDDIA', 'Proposição inclusa na ordem do dia', 0, 1, 1),
(14, 'ARQUIVADA', 'Proposição arquivada', 1, 0, 0),
(15, 'DESARQUIV', 'Proposição desarquivada pelo Autor', 0, 1, 0),
(16, 'AGAUTOGR', 'Aguardando assinatura do autógrafo', 0, 1, 0),
(17, 'AGSANCAO', 'Aguardando sanção governamental', 1, 0, 0),
(18, 'TRANSFLEI', 'Proposição transformada em lei', 1, 0, 0),
(19, 'VETOLIDO', 'Veto sobre a proposição lido em sessão plenária', 0, 1, 0),
(20, 'VETOTOTAL', 'Proposição com veto total', 0, 1, 0),
(21, 'VETOREJEI', 'Veto sobre a proposição rejeitado', 1, 0, 0),
(22, 'VETOMANT', 'Veto sobre a proposição mantido', 1, 0, 0),
(23, 'AGPROMLEI', 'Aguardando promulgação da lei', 1, 0, 0),
(24, 'DESPCOMIS', 'Proposição despachada às Comissões', 0, 1, 1),
(25, 'AUTUADA', 'Proposição autuada', 0, 1, 1),
(26, 'VETOPAUTA', 'Veto autuado e incluso em pauta', 1, 0, 0),
(27, 'PREJUD', 'Proposição prejudicada', 1, 0, 0),
(28, 'APRESENT', 'Proposição apresentada em Plenário', 0, 1, 0),
(29, 'EMITEPAREC', 'Para emitir parecer sobre a proposição', 0, 1, 1),
(30, 'AGORDIA', 'Aguardando a inclusão na ordem do dia', 0, 1, 0),
(31, 'PARFAVCCJ', 'Parecer favorável da Comissão de Constituição e Justiça', 0, 1, 0),
(32, 'PARFAVCFO', 'Parecer favorável da Comissão de Finanças e Orçamento', 0, 1, 0),
(33, 'APROV1TUR', 'Proposição aprovada em 1º turno', 0, 1, 0),
(34, 'LEIVETPAR', 'Transformada em lei com veto parcial', 0, 1, 0),
(35, 'LEIPROMUL', 'Proposição transformada em lei por promulgação', 1, 0, 0),
(36, 'VETODISTR', 'Veto distribuido para emissão de parecer', 0, 1, 0),
(37, 'MANUTVETO', 'Parecer pelo manutenção do veto', 0, 1, 0),
(38, 'REJEIVETO', 'Parecer pela rejeição do veto', 0, 1, 0),
(39, 'VETOORDIA', 'Veto  incluso na ordem do dia', 1, 0, 0),
(40, 'AGMENSVET', 'Aguardando assinatura da mensagem sobre o veto', 0, 1, 0),
(41, 'ANEXADA', 'Proposição anexada à outra análoga ou conexa mais antiga.', 0, 1, 0),
(42, 'PROMULVETO', 'Veto total ou parcial promulgado', 1, 0, 0),
(43, 'AGPROMNOR', 'Aguardando promulgação da norma jurídica', 1, 0, 0),
(44, 'NORMPROMUL', 'Norma promulgada', 1, 0, 0),
(45, 'AGPROMVET', 'Aguardando promulgação de lei com veto rejeitado', 0, 1, 0),
(46, 'VETOPROMUL', 'Projeto com veto total ou parcial promulgado', 1, 0, 1),
(47, 'PARECPLEN', 'Parecer em Plenário pelas comissões pertinentes', 1, 0, 0),
(48, 'ADIADA', 'Adiada discussão e votação', 0, 1, 0),
(49, 'RETORDIA', 'Proposição retirada da Ordem do Dia.', 0, 1, 0),
(50, 'PAREUCONJ', 'Parecer em reunião conjunta das Comissões pertinentes', 0, 1, 0),
(51, 'INCLEXP', 'Incluído na pauta do expediente', 0, 1, 0),
(52, 'DESPACHADA', 'Indicação despachada ao Executivo', 1, 0, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `status_tramitacao_administrativo`
--

CREATE TABLE IF NOT EXISTS `status_tramitacao_administrativo` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `status_tramitacao_administrativo`
--

INSERT INTO `status_tramitacao_administrativo` (`cod_status`, `sgl_status`, `des_status`, `ind_fim_tramitacao`, `ind_retorno_tramitacao`, `ind_excluido`) VALUES
(1, 'DEF', 'Deferido', 1, 0, 0),
(2, 'IND', 'Indeferido', 1, 0, 0),
(3, 'AP', 'Aguardando Parecer', 0, 1, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `subemenda`
--

CREATE TABLE IF NOT EXISTS `subemenda` (
  `cod_subemenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_subemenda` int(11) NOT NULL,
  `num_subemenda` int(11) NOT NULL,
  `cod_emenda` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_subemenda`),
  UNIQUE KEY `numsub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_emenda` (`cod_emenda`),
  KEY `tip_subemenda` (`tip_subemenda`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `subemenda`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_subemenda`
--       `tipo_emenda` -> `tip_emenda`
--   `cod_emenda`
--       `emenda` -> `cod_emenda`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `substitutivo`
--

CREATE TABLE IF NOT EXISTS `substitutivo` (
  `cod_substitutivo` int(11) NOT NULL AUTO_INCREMENT,
  `num_substitutivo` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_substitutivo`),
  UNIQUE KEY `idx_numsub_materia` (`num_substitutivo`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_materia` (`cod_materia`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`),
  FULLTEXT KEY `txt_observacao` (`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `substitutivo`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_afastamento`
--

CREATE TABLE IF NOT EXISTS `tipo_afastamento` (
  `tip_afastamento` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_afastamento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_afastamento` tinyint(4) NOT NULL,
  `ind_fim_mandato` tinyint(4) NOT NULL,
  `des_dispositivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_afastamento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=5 ;

--
-- Fazendo dump de dados para tabela `tipo_afastamento`
--

INSERT INTO `tipo_afastamento` (`tip_afastamento`, `des_afastamento`, `ind_afastamento`, `ind_fim_mandato`, `des_dispositivo`, `ind_excluido`) VALUES
(1, 'Licença Saúde', 1, 0, NULL, 0),
(2, 'Missão Oficial', 1, 0, NULL, 0),
(3, 'Interesse particular', 1, 0, NULL, 0),
(4, 'Suspensão do mandato', 1, 0, NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_autor`
--

CREATE TABLE IF NOT EXISTS `tipo_autor` (
  `tip_autor` tinyint(4) NOT NULL,
  `des_tipo_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_autor`),
  KEY `des_tipo_autor` (`des_tipo_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Fazendo dump de dados para tabela `tipo_autor`
--

INSERT INTO `tipo_autor` (`tip_autor`, `des_tipo_autor`, `ind_excluido`) VALUES
(1, 'Parlamentar', 0),
(2, 'Comissao', 0),
(3, 'Bancada', 0),
(4, 'Externo', 0),
(5, 'Mesa Diretora', 0),
(6, 'Líderes', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_comissao`
--

CREATE TABLE IF NOT EXISTS `tipo_comissao` (
  `tip_comissao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_comissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_natureza_comissao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_dispositivo_regimental` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_comissao`),
  KEY `nom_tipo_comissao` (`nom_tipo_comissao`),
  KEY `sgl_natureza_comissao` (`sgl_natureza_comissao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `tipo_comissao`
--

INSERT INTO `tipo_comissao` (`tip_comissao`, `nom_tipo_comissao`, `sgl_natureza_comissao`, `sgl_tipo_comissao`, `des_dispositivo_regimental`, `ind_excluido`) VALUES
(1, 'Permanente', 'P', 'CP', NULL, 0),
(2, 'Especial de Inquérito', 'T', 'CEI', NULL, 0),
(3, 'Especial', 'T', 'CE', NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_dependente`
--

CREATE TABLE IF NOT EXISTS `tipo_dependente` (
  `tip_dependente` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_tipo_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_dependente`),
  KEY `des_tipo_dependente` (`des_tipo_dependente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=3 ;

--
-- Fazendo dump de dados para tabela `tipo_dependente`
--

INSERT INTO `tipo_dependente` (`tip_dependente`, `des_tipo_dependente`, `ind_excluido`) VALUES
(1, 'Esposa', 0),
(2, 'Filho', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_documento`
--

CREATE TABLE IF NOT EXISTS `tipo_documento` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=8 ;

--
-- Fazendo dump de dados para tabela `tipo_documento`
--

INSERT INTO `tipo_documento` (`tip_documento`, `des_tipo_documento`, `ind_excluido`) VALUES
(1, 'Parecer', 0),
(2, 'Ofício', 0),
(3, 'Relatório', 0),
(4, 'Autógrafo', 0),
(5, 'Despacho', 0),
(6, 'Ofício / Resposta', 0),
(7, 'Mensagem Aditiva', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_documento_administrativo`
--

CREATE TABLE IF NOT EXISTS `tipo_documento_administrativo` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_documento` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `tipo_documento_administrativo`
--

INSERT INTO `tipo_documento_administrativo` (`tip_documento`, `sgl_tipo_documento`, `des_tipo_documento`, `ind_excluido`) VALUES
(1, 'CNV', 'Convite', 0),
(2, 'OFC', 'Oficio', 0),
(3, 'REQ', 'Requerimento', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_emenda`
--

CREATE TABLE IF NOT EXISTS `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`),
  KEY `des_tipo_emenda` (`des_tipo_emenda`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `tipo_emenda`
--

INSERT INTO `tipo_emenda` (`tip_emenda`, `des_tipo_emenda`, `ind_excluido`) VALUES
(1, 'Aditiva', 0),
(2, 'Modificativa', 0),
(3, 'Substitutiva', 0),
(4, 'Supressiva', 0),
(5, 'Mensagem Aditiva', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_expediente`
--

CREATE TABLE IF NOT EXISTS `tipo_expediente` (
  `cod_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `nom_expediente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`cod_expediente`),
  KEY `nom_expediente` (`nom_expediente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=5 ;

--
-- Fazendo dump de dados para tabela `tipo_expediente`
--

INSERT INTO `tipo_expediente` (`cod_expediente`, `nom_expediente`, `ind_excluido`) VALUES
(1, 'Correspondências Recebidas', 0),
(2, 'Expedientes Diversos', 0),
(3, 'Tribuna Livre', 0),
(4, 'Expedientes do Executivo', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_fim_relatoria`
--

CREATE TABLE IF NOT EXISTS `tipo_fim_relatoria` (
  `tip_fim_relatoria` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_fim_relatoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_fim_relatoria`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=3 ;

--
-- Fazendo dump de dados para tabela `tipo_fim_relatoria`
--

INSERT INTO `tipo_fim_relatoria` (`tip_fim_relatoria`, `des_fim_relatoria`, `ind_excluido`) VALUES
(1, 'Aprovado', 0),
(2, 'Rejeitado', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_instituicao`
--

CREATE TABLE IF NOT EXISTS `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `tipo_instituicao`
--

INSERT INTO `tipo_instituicao` (`tip_instituicao`, `nom_tipo_instituicao`, `ind_excluido`) VALUES
(1, 'ESCOLAS MUNICIPAIS', 0),
(2, 'ESCOLAS PARTICULARES', 0),
(3, 'ENSINO SUPERIOR', 0),
(4, 'ENTIDADES DE CLASSE', 0),
(5, 'SECRETÁRIOS MUNICIPAIS', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_materia_legislativa`
--

CREATE TABLE IF NOT EXISTS `tipo_materia_legislativa` (
  `tip_materia` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_materia` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_num_automatica` tinyint(4) NOT NULL DEFAULT '0',
  `quorum_minimo_votacao` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_materia`),
  KEY `des_tipo_materia` (`des_tipo_materia`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=11 ;

--
-- Fazendo dump de dados para tabela `tipo_materia_legislativa`
--

INSERT INTO `tipo_materia_legislativa` (`tip_materia`, `sgl_tipo_materia`, `des_tipo_materia`, `ind_num_automatica`, `quorum_minimo_votacao`, `ind_excluido`) VALUES
(1, 'PL', 'Projeto de Lei', 0, 1, 0),
(2, 'PR', 'Projeto de Resolução', 0, 1, 0),
(3, 'REQ', 'Requerimento', 0, 1, 0),
(4, 'REC', 'Recurso', 0, 1, 0),
(5, 'PLC', 'Projeto de Lei Complementar', 0, 1, 0),
(6, 'PDL', 'Projeto de Decreto Legislativo', 0, 1, 0),
(7, 'MOC', 'Moção', 0, 1, 0),
(8, 'IND', 'Indicação', 0, 1, 0),
(9, 'PEL', 'Proposta de Emenda à Lei Orgânica', 0, 1, 0),
(10, 'VET', 'Veto', 0, 1, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_norma_juridica`
--

CREATE TABLE IF NOT EXISTS `tipo_norma_juridica` (
  `tip_norma` tinyint(4) NOT NULL AUTO_INCREMENT,
  `voc_lexml` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_norma` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_norma` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_norma`),
  KEY `des_tipo_norma` (`des_tipo_norma`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=9 ;

--
-- Fazendo dump de dados para tabela `tipo_norma_juridica`
--

INSERT INTO `tipo_norma_juridica` (`tip_norma`, `voc_lexml`, `sgl_tipo_norma`, `des_tipo_norma`, `ind_excluido`) VALUES
(1, 'lei', 'LEI', 'Lei', 0),
(2, 'lei.complementar', 'LC', 'Lei Complementar', 0),
(3, 'decreto.legislativo', 'DL', 'Decreto Legislativo', 0),
(4, 'resolucao', 'RE', 'Resolução', 0),
(5, 'emenda.lei.organica', 'EML', 'Emenda à Lei Orgânica', 0),
(6, '', 'AM', 'Ato da Mesa', 0),
(7, '', 'POR', 'Portaria', 0),
(8, 'decreto', 'DE', 'Decreto do Executivo', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_proposicao`
--

CREATE TABLE IF NOT EXISTS `tipo_proposicao` (
  `tip_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_proposicao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_mat_ou_doc` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_mat_ou_doc` int(11) NOT NULL,
  `nom_modelo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_proposicao`),
  KEY `des_tipo_proposicao` (`des_tipo_proposicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=12 ;

--
-- Fazendo dump de dados para tabela `tipo_proposicao`
--

INSERT INTO `tipo_proposicao` (`tip_proposicao`, `des_tipo_proposicao`, `ind_mat_ou_doc`, `tip_mat_ou_doc`, `nom_modelo`, `ind_excluido`) VALUES
(1, 'Requerimento', 'M', 3, '', 0),
(2, 'Projeto de Lei', 'M', 1, '', 0),
(3, 'Parecer', 'D', 1, '', 1),
(4, 'Indicação', 'M', 8, '', 0),
(5, 'Moção', 'M', 7, '', 0),
(6, 'Emenda', 'D', 1, '', 0),
(7, 'Substitutivo', 'D', 1, '', 0),
(8, 'Projeto de Lei Complementar', 'M', 5, '', 0),
(9, 'Projeto de Resolução', 'M', 2, '', 0),
(10, 'Projeto de Decreto Legislativo', 'M', 6, '', 0),
(11, 'Proposta de Emenda à Lei Orgânica', 'M', 9, '', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_resultado_votacao`
--

CREATE TABLE IF NOT EXISTS `tipo_resultado_votacao` (
  `tip_resultado_votacao` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom_resultado` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`tip_resultado_votacao`),
  KEY `nom_resultado` (`nom_resultado`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=7 ;

--
-- Fazendo dump de dados para tabela `tipo_resultado_votacao`
--

INSERT INTO `tipo_resultado_votacao` (`tip_resultado_votacao`, `nom_resultado`, `ind_excluido`) VALUES
(1, 'Aprovado', 0),
(2, 'Rejeitado', 0),
(3, 'Adiado', 0),
(4, 'Mantido', 0),
(5, 'Despachada', 0),
(6, 'Retirado', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `tipo_sessao_plenaria` (
  `tip_sessao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_sessao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_minimo` int(11) NOT NULL,
  PRIMARY KEY (`tip_sessao`),
  KEY `nom_sessao` (`nom_sessao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=6 ;

--
-- Fazendo dump de dados para tabela `tipo_sessao_plenaria`
--

INSERT INTO `tipo_sessao_plenaria` (`tip_sessao`, `nom_sessao`, `ind_excluido`, `num_minimo`) VALUES
(1, 'Ordinária', 0, 6),
(2, 'Extraordinária', 0, 6),
(3, 'Solene', 0, 6),
(4, 'Especial', 0, 6),
(5, 'Audiência Púbica', 0, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_situacao_materia`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_materia` (
  `tip_situacao_materia` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_materia`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=111 ;

--
-- Fazendo dump de dados para tabela `tipo_situacao_materia`
--

INSERT INTO `tipo_situacao_materia` (`tip_situacao_materia`, `des_tipo_situacao`, `ind_excluido`) VALUES
(1, 'VETADO', 0),
(2, 'APROVADO', 0),
(3, 'APROVADO EM URGÊNCIA', 0),
(4, 'PREJUDICADO', 0),
(5, 'RETIRADO', 0),
(6, 'REJEITADO', 0),
(7, 'ADIADO', 0),
(8, 'APROVADO EM 1º TURNO', 0),
(9, 'APROVADO EM 2º TURNO', 0),
(10, 'ARQUIVADO', 0),
(11, 'DECLARADA INCONSTITUCIONAL', 0),
(12, 'APTO P/ APRECIAÇÃO', 0),
(13, 'DEFERIDO', 0),
(14, 'CANCELADO', 0),
(15, 'DESPACHADO', 0),
(16, 'APRESENTADO', 0),
(17, 'RECUSADO', 0),
(18, 'SANÇÃO TÁCITA', 0),
(19, 'SUSTADO', 0),
(20, 'PARECER CONTRÁRIO CJR (APTO)', 0),
(21, 'APTO (VETO)', 0),
(22, 'PARECER REJEITADO', 0),
(23, 'PARECER CONTRÁRIO CJR APROVADO', 0),
(24, 'APROVADO EM PREFERÊNCIA', 0),
(25, 'TRAMITANDO', 0),
(26, 'AUTÓGRAFO', 0),
(27, 'VETO TOTAL REJEITADO', 0),
(28, 'VETO TOTAL MANTIDO', 0),
(29, 'DISCUSSÃO INTERROMPIDA', 0),
(30, 'PARECER CONTRÁRIO DA CJR (TRAMITANDO)', 0),
(31, 'VETO PARCIAL MANTIDO', 0),
(32, 'VETO PARCIAL REJEITADO', 0),
(33, 'NORMA', 0),
(34, 'VETO EM TRÂMITE', 0),
(35, 'ENVIANDO OFÍCIOS', 0),
(36, 'CONSULTORIA JURÍDICA', 0),
(37, 'AGUARDANDO INFORMAÇÕES', 0),
(38, 'EM PAUTA', 0),
(39, 'DIRETORIA JURÍDICA', 0),
(40, 'VETO PARCIAL MANTIDO PARCIALMENTE', 0),
(41, 'AGUARDANDO AUDIÊNCIA PÚBLICA', 0),
(42, 'AGUARDANDO INF/AUD. PÚBLICA', 0),
(43, 'INDEFERIDO', 0),
(44, 'AUDIÊNCIA PÚBLICA', 0),
(45, 'SUBSTITUTIVO TRAMITANDO', 0),
(46, 'MANTIDO', 0),
(47, 'SEM EFEITO', 0),
(48, 'ADIADO/DISCUSSÃO INTERROMPIDA', 0),
(49, 'CONVERTIDO EM PDL', 0),
(50, 'CONVERTIDO EM PL', 0),
(51, 'CONVERTIDO EM PLC', 0),
(52, 'SEM RESULTADO', 0),
(53, 'REJEITADA NA COMISSÃO MISTA', 0),
(54, 'PUBLICAR NA IMPRENSA OFICIAL', 0),
(55, 'APROVADO COM ALTERAÇÕES', 0),
(56, 'APROVADO SEM ALTERAÇÕES', 0),
(57, 'CONVERTIDO EM PR', 0),
(58, 'VETO PARCIAL EM TRÂMITE', 0),
(59, 'VETADO PARCIALMENTE', 0),
(60, 'REVOGADO', 0),
(61, 'NORMA (VETO PARCIAL MANTIDO)', 0),
(62, 'NORMA (VETO TOTAL REJEITADO)', 0),
(63, 'NORMA (SANÇÃO TÁCITA)', 0),
(64, 'ADIADO (PAR. CONTRÁRIO CJR)', 0),
(65, 'NORMA (VETO PARCIAL REJEITADO)', 0),
(66, 'APTO P/ APRECIAÇÃO (2º. TURNO)', 0),
(67, 'VETO ADIADO', 0),
(68, 'DEVOLVIDO À PREFEITURA', 0),
(69, 'CONVERTIDO EM INDICAÇÃO', 0),
(70, 'ANEXADO A PROJETO DE LEI', 0),
(71, 'ANEXADO A PROJETO DE RESOLUÇÃO', 0),
(72, 'CONVERTIDO EM REQUERIMENTO', 0),
(73, 'CONVERTIDO EM MOÇÃO', 0),
(74, 'CONVERTIDO EM JUSTIFICATIVA DE PL', 0),
(75, 'ADIADO - AGUARDA AUD. PÚBLICA', 0),
(76, 'APTO ILEGAL', 0),
(77, 'APTO ILEGAL/INCOSNTITUCIONAL', 0),
(78, 'APTO INCONSTITUCIONAL', 0),
(79, 'ADIADO ILEGAL', 0),
(80, 'ADIADO ILEGAL/INCONSTITUCIONAL', 0),
(81, 'ADIADO INCONSTITUCIONAL', 0),
(82, 'PAUTADO PARA EXTRAORDINÁRIA', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_situacao_militar`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_militar` (
  `tip_situacao_militar` tinyint(4) NOT NULL,
  `des_tipo_situacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_situacao_militar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Fazendo dump de dados para tabela `tipo_situacao_militar`
--

INSERT INTO `tipo_situacao_militar` (`tip_situacao_militar`, `des_tipo_situacao`, `ind_excluido`) VALUES
(1, 'Reservista', 0),
(2, 'Excesso de Contingente', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_situacao_norma`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=21 ;

--
-- Fazendo dump de dados para tabela `tipo_situacao_norma`
--

INSERT INTO `tipo_situacao_norma` (`tip_situacao_norma`, `des_tipo_situacao`, `ind_excluido`) VALUES
(1, 'Em vigor', 0),
(2, 'Revogada', 0),
(3, 'Revogada parcialmente', 0),
(4, 'Revogada tacitamente', 0),
(5, 'Execução suspensa', 0),
(6, 'Prejudicada', 0),
(7, 'Sub Judice', 0),
(8, 'Execução suspensa de dispositivos', 0),
(9, 'Nula', 0),
(10, 'Insubsistente', 0),
(11, 'Sub Judice (sem liminar)', 0),
(12, 'Em vigor, com revogação parcial', 0),
(13, 'Em vigor (sub judice parcial)', 0),
(14, 'Em vigor (execução suspensa parcial)', 0),
(15, 'Revogação sub judice', 0),
(16, 'Declarada inconstitucional pelo TJ', 0),
(17, 'Em vigor, parte declarada inconstitucional', 0),
(18, 'Em vigor 45 dias após a publicação', 0),
(19, 'Sem efeito', 0),
(20, 'Em vigor, com alterações posteriores', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tramitacao`
--

CREATE TABLE IF NOT EXISTS `tramitacao` (
  `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_status` int(11) DEFAULT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_tramitacao` date DEFAULT NULL,
  `cod_unid_tram_local` int(11) DEFAULT NULL,
  `dat_encaminha` date DEFAULT NULL,
  `cod_unid_tram_dest` int(11) DEFAULT NULL,
  `ind_ult_tramitacao` tinyint(4) NOT NULL,
  `ind_urgencia` tinyint(4) NOT NULL,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_tramitacao` text COLLATE utf8_unicode_ci,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tramitacao`),
  KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  KEY `cod_status` (`cod_status`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_tramit_ultmat` (`ind_ult_tramitacao`,`dat_tramitacao`,`cod_materia`,`ind_excluido`),
  KEY `sgl_turno` (`sgl_turno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `tramitacao`:
--   `cod_unid_tram_dest`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--   `cod_status`
--       `status_tramitacao` -> `cod_status`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_unid_tram_local`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `tramitacao_administrativo`
--

CREATE TABLE IF NOT EXISTS `tramitacao_administrativo` (
  `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL DEFAULT '0',
  `dat_tramitacao` date DEFAULT NULL,
  `cod_unid_tram_local` int(11) DEFAULT NULL,
  `dat_encaminha` date DEFAULT NULL,
  `cod_unid_tram_dest` int(11) DEFAULT NULL,
  `cod_status` int(11) DEFAULT NULL,
  `ind_ult_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_tramitacao` text COLLATE utf8_unicode_ci,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_tramitacao`),
  UNIQUE KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  KEY `tramitacao_ind1` (`ind_ult_tramitacao`),
  KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  KEY `cod_status` (`cod_status`),
  KEY `cod_documento` (`cod_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `tramitacao_administrativo`:
--   `cod_status`
--       `status_tramitacao_administrativo` -> `cod_status`
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--   `cod_unid_tram_local`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--   `cod_unid_tram_dest`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `unidade_tramitacao`
--

CREATE TABLE IF NOT EXISTS `unidade_tramitacao` (
  `cod_unid_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_orgao` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_unid_tramitacao`),
  KEY `idx_unidtramit_orgao` (`cod_orgao`,`ind_excluido`),
  KEY `idx_unidtramit_comissao` (`cod_comissao`,`ind_excluido`),
  KEY `cod_orgao` (`cod_orgao`),
  KEY `cod_comissao` (`cod_comissao`),
  KEY `idx_unidtramit_parlamentar` (`cod_parlamentar`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=8 ;

--
-- RELACIONAMENTOS PARA TABELAS `unidade_tramitacao`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_orgao`
--       `orgao` -> `cod_orgao`
--

--
-- Fazendo dump de dados para tabela `unidade_tramitacao`
--

INSERT INTO `unidade_tramitacao` (`cod_unid_tramitacao`, `cod_comissao`, `cod_orgao`, `cod_parlamentar`, `ind_excluido`) VALUES
(1, NULL, 1, NULL, 0),
(2, NULL, 2, NULL, 0),
(3, NULL, 3, NULL, 0),
(4, NULL, 4, NULL, 0),
(5, NULL, 5, NULL, 0),
(6, NULL, 6, NULL, 0),
(7, NULL, 7, NULL, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `vinculo_norma_juridica`
--

CREATE TABLE IF NOT EXISTS `vinculo_norma_juridica` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma_referente` int(11) NOT NULL,
  `cod_norma_referida` int(11) DEFAULT NULL,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `idx_vnj_norma_referente` (`cod_norma_referente`,`cod_norma_referida`,`ind_excluido`),
  KEY `idx_vnj_norma_referida` (`cod_norma_referida`,`cod_norma_referente`,`ind_excluido`),
  KEY `cod_norma_referente` (`cod_norma_referente`),
  KEY `cod_norma_referida` (`cod_norma_referida`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0 AUTO_INCREMENT=1 ;

--
-- RELACIONAMENTOS PARA TABELAS `vinculo_norma_juridica`:
--   `cod_norma_referida`
--       `norma_juridica` -> `cod_norma`
--   `cod_norma_referente`
--       `norma_juridica` -> `cod_norma`
--

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `acomp_materia`
--
ALTER TABLE `acomp_materia`
  ADD CONSTRAINT `acomp_materia_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `afastamento`
--
ALTER TABLE `afastamento`
  ADD CONSTRAINT `afastamento_ibfk_5` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `afastamento_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `afastamento_ibfk_2` FOREIGN KEY (`cod_mandato`) REFERENCES `mandato` (`cod_mandato`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `afastamento_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `afastamento_ibfk_4` FOREIGN KEY (`cod_parlamentar_suplente`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `anexada`
--
ALTER TABLE `anexada`
  ADD CONSTRAINT `anexada_ibfk_2` FOREIGN KEY (`cod_materia_anexada`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `anexada_ibfk_1` FOREIGN KEY (`cod_materia_principal`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Restrições para tabelas `assessor_parlamentar`
--
ALTER TABLE `assessor_parlamentar`
  ADD CONSTRAINT `assessor_parlamentar_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `autor`
--
ALTER TABLE `autor`
  ADD CONSTRAINT `autor_ibfk_5` FOREIGN KEY (`tip_autor`) REFERENCES `tipo_autor` (`tip_autor`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `autor_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `autor_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `autor_ibfk_3` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `autor_ibfk_4` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `autoria`
--
ALTER TABLE `autoria`
  ADD CONSTRAINT `autoria_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `autoria_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `coligacao`
--
ALTER TABLE `coligacao`
  ADD CONSTRAINT `coligacao_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `comissao`
--
ALTER TABLE `comissao`
  ADD CONSTRAINT `comissao_ibfk_1` FOREIGN KEY (`tip_comissao`) REFERENCES `tipo_comissao` (`tip_comissao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `composicao_bancada`
--
ALTER TABLE `composicao_bancada`
  ADD CONSTRAINT `composicao_bancada_ibfk_3` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_bancada` (`cod_cargo`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_bancada_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_bancada_ibfk_2` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `composicao_coligacao`
--
ALTER TABLE `composicao_coligacao`
  ADD CONSTRAINT `composicao_coligacao_ibfk_2` FOREIGN KEY (`cod_coligacao`) REFERENCES `coligacao` (`cod_coligacao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_coligacao_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `composicao_comissao`
--
ALTER TABLE `composicao_comissao`
  ADD CONSTRAINT `composicao_comissao_ibfk_4` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_comissao` (`cod_cargo`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_comissao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_comissao_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_comissao_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_comissao` (`cod_periodo_comp`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `composicao_mesa`
--
ALTER TABLE `composicao_mesa`
  ADD CONSTRAINT `composicao_mesa_ibfk_4` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_mesa_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_mesa_ibfk_2` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_mesa` (`cod_cargo`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `composicao_mesa_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_mesa` (`cod_periodo_comp`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `dependente`
--
ALTER TABLE `dependente`
  ADD CONSTRAINT `dependente_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `dependente_ibfk_1` FOREIGN KEY (`tip_dependente`) REFERENCES `tipo_dependente` (`tip_dependente`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `despacho_inicial`
--
ALTER TABLE `despacho_inicial`
  ADD CONSTRAINT `despacho_inicial_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `despacho_inicial_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `documento_acessorio`
--
ALTER TABLE `documento_acessorio`
  ADD CONSTRAINT `documento_acessorio_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento` (`tip_documento`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `documento_acessorio_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `documento_acessorio_administrativo`
--
ALTER TABLE `documento_acessorio_administrativo`
  ADD CONSTRAINT `documento_acessorio_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `documento_administrativo`
--
ALTER TABLE `documento_administrativo`
  ADD CONSTRAINT `documento_administrativo_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `documento_administrativo_ibfk_1` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `emenda`
--
ALTER TABLE `emenda`
  ADD CONSTRAINT `emenda_ibfk_3` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `emenda_ibfk_1` FOREIGN KEY (`tip_emenda`) REFERENCES `tipo_emenda` (`tip_emenda`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `emenda_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `encerramento_presenca`
--
ALTER TABLE `encerramento_presenca`
  ADD CONSTRAINT `encerramento_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `encerramento_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `expediente_materia`
--
ALTER TABLE `expediente_materia`
  ADD CONSTRAINT `expediente_materia_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `expediente_materia_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `expediente_presenca`
--
ALTER TABLE `expediente_presenca`
  ADD CONSTRAINT `expediente_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `expediente_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `expediente_sessao_plenaria`
--
ALTER TABLE `expediente_sessao_plenaria`
  ADD CONSTRAINT `expediente_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_expediente`) REFERENCES `tipo_expediente` (`cod_expediente`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `filiacao`
--
ALTER TABLE `filiacao`
  ADD CONSTRAINT `filiacao_ibfk_2` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `filiacao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `instituicao`
--
ALTER TABLE `instituicao`
  ADD CONSTRAINT `instituicao_ibfk_2` FOREIGN KEY (`cod_localidade`) REFERENCES `localidade` (`cod_localidade`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `instituicao_ibfk_1` FOREIGN KEY (`tip_instituicao`) REFERENCES `tipo_instituicao` (`tip_instituicao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `legislacao_citada`
--
ALTER TABLE `legislacao_citada`
  ADD CONSTRAINT `legislacao_citada_ibfk_2` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `legislacao_citada_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `mandato`
--
ALTER TABLE `mandato`
  ADD CONSTRAINT `mandato_ibfk_4` FOREIGN KEY (`cod_coligacao`) REFERENCES `coligacao` (`cod_coligacao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `mandato_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `mandato_ibfk_2` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `mandato_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `materia_apresentada_sessao`
--
ALTER TABLE `materia_apresentada_sessao`
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `materia_legislativa`
--
ALTER TABLE `materia_legislativa`
  ADD CONSTRAINT `materia_legislativa_ibfk_4` FOREIGN KEY (`cod_situacao`) REFERENCES `tipo_situacao_materia` (`tip_situacao_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `materia_legislativa_ibfk_1` FOREIGN KEY (`tip_id_basica`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `materia_legislativa_ibfk_2` FOREIGN KEY (`cod_regime_tramitacao`) REFERENCES `regime_tramitacao` (`cod_regime_tramitacao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `materia_legislativa_ibfk_3` FOREIGN KEY (`cod_local_origem_externa`) REFERENCES `origem` (`cod_origem`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `mesa_sessao_plenaria`
--
ALTER TABLE `mesa_sessao_plenaria`
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_3` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `norma_juridica`
--
ALTER TABLE `norma_juridica`
  ADD CONSTRAINT `norma_juridica_ibfk_3` FOREIGN KEY (`cod_situacao`) REFERENCES `tipo_situacao_norma` (`tip_situacao_norma`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `norma_juridica_ibfk_1` FOREIGN KEY (`tip_norma`) REFERENCES `tipo_norma_juridica` (`tip_norma`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `norma_juridica_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE SET NULL ON UPDATE NO ACTION;

--
-- Restrições para tabelas `numeracao`
--
ALTER TABLE `numeracao`
  ADD CONSTRAINT `numeracao_ibfk_2` FOREIGN KEY (`tip_materia`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `numeracao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `oradores`
--
ALTER TABLE `oradores`
  ADD CONSTRAINT `oradores_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `oradores_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `oradores_expediente`
--
ALTER TABLE `oradores_expediente`
  ADD CONSTRAINT `oradores_expediente_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `oradores_expediente_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `ordem_dia`
--
ALTER TABLE `ordem_dia`
  ADD CONSTRAINT `ordem_dia_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `ordem_dia_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `ordem_dia_presenca`
--
ALTER TABLE `ordem_dia_presenca`
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `parecer`
--
ALTER TABLE `parecer`
  ADD CONSTRAINT `parecer_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `parlamentar`
--
ALTER TABLE `parlamentar`
  ADD CONSTRAINT `parlamentar_ibfk_3` FOREIGN KEY (`cod_localidade_resid`) REFERENCES `localidade` (`cod_localidade`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `parlamentar_ibfk_1` FOREIGN KEY (`cod_nivel_instrucao`) REFERENCES `nivel_instrucao` (`cod_nivel_instrucao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `parlamentar_ibfk_2` FOREIGN KEY (`tip_situacao_militar`) REFERENCES `tipo_situacao_militar` (`tip_situacao_militar`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `periodo_comp_mesa`
--
ALTER TABLE `periodo_comp_mesa`
  ADD CONSTRAINT `periodo_comp_mesa_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `proposicao`
--
ALTER TABLE `proposicao`
  ADD CONSTRAINT `proposicao_ibfk_3` FOREIGN KEY (`tip_proposicao`) REFERENCES `tipo_proposicao` (`tip_proposicao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `proposicao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `proposicao_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `protocolo`
--
ALTER TABLE `protocolo`
  ADD CONSTRAINT `protocolo_ibfk_3` FOREIGN KEY (`tip_materia`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `protocolo_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `protocolo_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `registro_votacao`
--
ALTER TABLE `registro_votacao`
  ADD CONSTRAINT `registro_votacao_ibfk_5` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `registro_votacao_ibfk_1` FOREIGN KEY (`tip_resultado_votacao`) REFERENCES `tipo_resultado_votacao` (`tip_resultado_votacao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `registro_votacao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `registro_votacao_ibfk_3` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `registro_votacao_ibfk_4` FOREIGN KEY (`cod_subemenda`) REFERENCES `subemenda` (`cod_subemenda`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `registro_votacao_parlamentar`
--
ALTER TABLE `registro_votacao_parlamentar`
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_1` FOREIGN KEY (`cod_votacao`) REFERENCES `registro_votacao` (`cod_votacao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `relatoria`
--
ALTER TABLE `relatoria`
  ADD CONSTRAINT `relatoria_ibfk_4` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `relatoria_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `relatoria_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `relatoria_ibfk_3` FOREIGN KEY (`tip_fim_relatoria`) REFERENCES `tipo_fim_relatoria` (`tip_fim_relatoria`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `reuniao_comissao`
--
ALTER TABLE `reuniao_comissao`
  ADD CONSTRAINT `reuniao_comissao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `sessao_legislativa`
--
ALTER TABLE `sessao_legislativa`
  ADD CONSTRAINT `sessao_legislativa_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `sessao_plenaria`
--
ALTER TABLE `sessao_plenaria`
  ADD CONSTRAINT `sessao_plenaria_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `sessao_plenaria_ibfk_1` FOREIGN KEY (`tip_sessao`) REFERENCES `tipo_sessao_plenaria` (`tip_sessao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `sessao_plenaria_ibfk_2` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `sessao_plenaria_presenca`
--
ALTER TABLE `sessao_plenaria_presenca`
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `subemenda`
--
ALTER TABLE `subemenda`
  ADD CONSTRAINT `subemenda_ibfk_3` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `subemenda_ibfk_1` FOREIGN KEY (`tip_subemenda`) REFERENCES `tipo_emenda` (`tip_emenda`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `subemenda_ibfk_2` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `substitutivo`
--
ALTER TABLE `substitutivo`
  ADD CONSTRAINT `substitutivo_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `substitutivo_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `tramitacao`
--
ALTER TABLE `tramitacao`
  ADD CONSTRAINT `tramitacao_ibfk_4` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`),
  ADD CONSTRAINT `tramitacao_ibfk_1` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao` (`cod_status`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `tramitacao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `tramitacao_ibfk_3` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `tramitacao_administrativo`
--
ALTER TABLE `tramitacao_administrativo`
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_4` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao_administrativo` (`cod_status`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_2` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_3` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`);

--
-- Restrições para tabelas `unidade_tramitacao`
--
ALTER TABLE `unidade_tramitacao`
  ADD CONSTRAINT `unidade_tramitacao_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_2` FOREIGN KEY (`cod_orgao`) REFERENCES `orgao` (`cod_orgao`) ON UPDATE NO ACTION;

--
-- Restrições para tabelas `vinculo_norma_juridica`
--
ALTER TABLE `vinculo_norma_juridica`
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_2` FOREIGN KEY (`cod_norma_referida`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_1` FOREIGN KEY (`cod_norma_referente`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
