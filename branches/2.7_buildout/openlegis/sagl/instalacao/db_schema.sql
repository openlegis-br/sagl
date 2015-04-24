-- Versão do servidor: 5.6.19-0ubuntu0.14.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de Dados: `interlegis`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `acomp_materia`
--

CREATE TABLE `acomp_materia` (
  `cod_cadastro` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_hash` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cadastro`),
  UNIQUE KEY `fk_{CCECA63D-5992-437B-BCD3-D7C98DA3E926}` (`cod_materia`,`end_email`),
  KEY `cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `acomp_materia`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `afastamento`
--

CREATE TABLE `afastamento` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `afastamento`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_mandato`
--       `mandato` -> `cod_mandato`
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--   `cod_parlamentar_suplente`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_afastamento`
--       `tipo_afastamento` -> `tip_afastamento`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `anexada`
--

CREATE TABLE `anexada` (
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
-- RELACIONAMENTOS PARA A TABELA `anexada`:
--   `cod_materia_principal`
--       `materia_legislativa` -> `cod_materia`
--   `cod_materia_anexada`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_armario`
--

CREATE TABLE `arquivo_armario` (
  `cod_armario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_armario` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `arquivo_armario`:
--   `cod_corredor`
--       `arquivo_corredor` -> `cod_corredor`
--   `cod_unidade`
--       `arquivo_unidade` -> `cod_unidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_corredor`
--

CREATE TABLE `arquivo_corredor` (
  `cod_corredor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_unidade` int(11) NOT NULL,
  `nom_corredor` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `arquivo_corredor`:
--   `cod_unidade`
--       `arquivo_unidade` -> `cod_unidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_item`
--

CREATE TABLE `arquivo_item` (
  `cod_item` int(11) NOT NULL AUTO_INCREMENT,
  `cod_recipiente` int(11) NOT NULL,
  `tip_suporte` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_norma` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `cod_protocolo` int(7) unsigned zerofill DEFAULT NULL,
  `des_item` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_arquivamento` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_item`),
  KEY `cod_recipiente` (`cod_recipiente`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_norma` (`cod_norma`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_protocolo` (`cod_protocolo`),
  KEY `tip_suporte` (`tip_suporte`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `arquivo_item`:
--   `cod_recipiente`
--       `arquivo_recipiente` -> `cod_recipiente`
--   `tip_suporte`
--       `arquivo_tipo_suporte` -> `tip_suporte`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_norma`
--       `norma_juridica` -> `cod_norma`
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--   `cod_protocolo`
--       `protocolo` -> `cod_protocolo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_prateleira`
--

CREATE TABLE `arquivo_prateleira` (
  `cod_prateleira` int(11) NOT NULL AUTO_INCREMENT,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_prateleira` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_prateleira`),
  KEY `cod_armario` (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `arquivo_prateleira`:
--   `cod_armario`
--       `arquivo_armario` -> `cod_armario`
--   `cod_corredor`
--       `arquivo_corredor` -> `cod_corredor`
--   `cod_unidade`
--       `arquivo_unidade` -> `cod_unidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_recipiente`
--

CREATE TABLE `arquivo_recipiente` (
  `cod_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `tip_recipiente` int(11) NOT NULL,
  `num_recipiente` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `tip_tit_documental` int(11) NOT NULL,
  `ano_recipiente` smallint(6) NOT NULL,
  `dat_recipiente` date NOT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_prateleira` int(11) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_recipiente`),
  UNIQUE KEY `num_tipo_recipiente` (`num_recipiente`,`tip_recipiente`,`ano_recipiente`,`ind_excluido`),
  KEY `tip_recipiente` (`tip_recipiente`),
  KEY `tip_tit_documental` (`tip_tit_documental`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `arquivo_recipiente`:
--   `tip_recipiente`
--       `arquivo_tipo_recipiente` -> `tip_recipiente`
--   `tip_tit_documental`
--       `arquivo_tipo_tit_documental` -> `tip_tit_documental`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_recipiente`
--

CREATE TABLE `arquivo_tipo_recipiente` (
  `tip_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_recipiente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_recipiente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_suporte`
--

CREATE TABLE `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_suporte`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_tit_documental`
--

CREATE TABLE `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_tit_documental`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_unidade`
--

CREATE TABLE `arquivo_unidade` (
  `cod_unidade` int(11) NOT NULL AUTO_INCREMENT,
  `tip_extensao_atuacao` int(11) NOT NULL,
  `tip_estagio_evolucao` int(11) NOT NULL,
  `nom_unidade` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `txt_localizacao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `assessor_parlamentar`
--

CREATE TABLE `assessor_parlamentar` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `assessor_parlamentar`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `assunto_norma`
--

CREATE TABLE `assunto_norma` (
  `cod_assunto` int(4) NOT NULL AUTO_INCREMENT,
  `des_assunto` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estendida` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_assunto`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `autor`
--

CREATE TABLE `autor` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `autor`:
--   `cod_partido`
--       `partido` -> `cod_partido`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_bancada`
--       `bancada` -> `cod_bancada`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_autor`
--       `tipo_autor` -> `tip_autor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `autoria`
--

CREATE TABLE `autoria` (
  `cod_autor` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_primeiro_autor` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`,`cod_materia`),
  KEY `idx_materia` (`cod_materia`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `autoria`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `bancada`
--

CREATE TABLE `bancada` (
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
  KEY `num_legislatura` (`num_legislatura`),
  KEY `cod_partido` (`cod_partido`),
  FULLTEXT KEY `nom_bancada` (`nom_bancada`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `bancada`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--   `cod_partido`
--       `partido` -> `cod_partido`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_bancada`
--

CREATE TABLE `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_comissao`
--

CREATE TABLE `cargo_comissao` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_mesa`
--

CREATE TABLE `cargo_mesa` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `coligacao`
--

CREATE TABLE `coligacao` (
  `cod_coligacao` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `nom_coligacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_votos_coligacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_coligacao`),
  KEY `idx_legislatura` (`num_legislatura`),
  KEY `idx_coligacao_legislatura` (`num_legislatura`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `coligacao`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `comissao`
--

CREATE TABLE `comissao` (
  `cod_comissao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_comissao` tinyint(4) NOT NULL,
  `nom_comissao` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `comissao`:
--   `tip_comissao`
--       `tipo_comissao` -> `tip_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_bancada`
--

CREATE TABLE `composicao_bancada` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `composicao_bancada`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_bancada`
--       `bancada` -> `cod_bancada`
--   `cod_cargo`
--       `cargo_bancada` -> `cod_cargo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_coligacao`
--

CREATE TABLE `composicao_coligacao` (
  `cod_partido` int(11) NOT NULL,
  `cod_coligacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_partido`,`cod_coligacao`),
  KEY `idx_coligacao` (`cod_coligacao`),
  KEY `idx_partido` (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `composicao_coligacao`:
--   `cod_partido`
--       `partido` -> `cod_partido`
--   `cod_coligacao`
--       `coligacao` -> `cod_coligacao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_comissao`
--

CREATE TABLE `composicao_comissao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `composicao_comissao`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_periodo_comp`
--       `periodo_comp_comissao` -> `cod_periodo_comp`
--   `cod_cargo`
--       `cargo_comissao` -> `cod_cargo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_mesa`
--

CREATE TABLE `composicao_mesa` (
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
-- RELACIONAMENTOS PARA A TABELA `composicao_mesa`:
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_cargo`
--       `cargo_mesa` -> `cod_cargo`
--   `cod_periodo_comp`
--       `periodo_comp_mesa` -> `cod_periodo_comp`
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `dependente`
--

CREATE TABLE `dependente` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `dependente`:
--   `tip_dependente`
--       `tipo_dependente` -> `tip_dependente`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `despacho_inicial`
--

CREATE TABLE `despacho_inicial` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) unsigned NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`,`num_ordem`),
  KEY `idx_comissao` (`cod_comissao`),
  KEY `idx_materia` (`cod_materia`),
  KEY `idx_despinic_comissao` (`cod_materia`,`num_ordem`,`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `despacho_inicial`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `destinatario_oficio`
--

CREATE TABLE `destinatario_oficio` (
  `cod_destinatario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_instituicao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_destinatario`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_instituicao` (`cod_instituicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `destinatario_oficio`:
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--   `cod_instituicao`
--       `instituicao` -> `cod_instituicao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_acessorio`
--

CREATE TABLE `documento_acessorio` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `documento_acessorio`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `tip_documento`
--       `tipo_documento` -> `tip_documento`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_acessorio_administrativo`
--

CREATE TABLE `documento_acessorio_administrativo` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `documento_acessorio_administrativo`:
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_administrativo`
--

CREATE TABLE `documento_administrativo` (
  `cod_documento` int(11) NOT NULL AUTO_INCREMENT,
  `tip_documento` int(11) NOT NULL,
  `num_documento` int(11) NOT NULL,
  `ano_documento` smallint(6) NOT NULL DEFAULT '0',
  `dat_documento` date NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `txt_interessado` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `cod_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_documento`),
  KEY `idx_num_ano` (`num_documento`,`ano_documento`),
  KEY `idx_dat_documento` (`dat_documento`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_documento` (`tip_documento`),
  FULLTEXT KEY `idx_busca_documento` (`txt_assunto`,`txt_observacao`),
  FULLTEXT KEY `idx_txt_interessado` (`txt_interessado`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `documento_administrativo`:
--   `tip_documento`
--       `tipo_documento_administrativo` -> `tip_documento`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `emenda`
--

CREATE TABLE `emenda` (
  `cod_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_emenda` int(11) NOT NULL,
  `num_emenda` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `exc_pauta` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_emenda`),
  UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_materia` (`cod_materia`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_emenda` (`tip_emenda`),
  FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `emenda`:
--   `tip_emenda`
--       `tipo_emenda` -> `tip_emenda`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `encerramento_presenca`
--

CREATE TABLE `encerramento_presenca` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `encerramento_presenca`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_materia`
--

CREATE TABLE `expediente_materia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) unsigned NOT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_votacao` int(11) NOT NULL,
  `tip_quorum` int(11) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `idx_exped_datord` (`dat_ordem`,`ind_excluido`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_materia` (`cod_materia`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `tip_quorum` (`tip_quorum`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `expediente_materia`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `tip_votacao`
--       `tipo_votacao` -> `tip_votacao`
--   `tip_quorum`
--       `quorum_votacao` -> `cod_quorum`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_presenca`
--

CREATE TABLE `expediente_presenca` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `expediente_presenca`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_sessao_plenaria`
--

CREATE TABLE `expediente_sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_expediente` int(11) NOT NULL,
  `txt_expediente` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_expediente`),
  KEY `cod_expediente` (`cod_expediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `expediente_sessao_plenaria`:
--   `cod_expediente`
--       `tipo_expediente` -> `cod_expediente`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `filiacao`
--

CREATE TABLE `filiacao` (
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
-- RELACIONAMENTOS PARA A TABELA `filiacao`:
--   `cod_partido`
--       `partido` -> `cod_partido`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `instituicao`
--

CREATE TABLE `instituicao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `instituicao`:
--   `tip_instituicao`
--       `tipo_instituicao` -> `tip_instituicao`
--   `cod_localidade`
--       `localidade` -> `cod_localidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `legislacao_citada`
--

CREATE TABLE `legislacao_citada` (
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
-- RELACIONAMENTOS PARA A TABELA `legislacao_citada`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_norma`
--       `norma_juridica` -> `cod_norma`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `legislatura`
--

CREATE TABLE `legislatura` (
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
-- Estrutura da tabela `lexml_registro_provedor`
--

CREATE TABLE `lexml_registro_provedor` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lexml_registro_publicador`
--

CREATE TABLE `lexml_registro_publicador` (
  `cod_publicador` int(11) NOT NULL AUTO_INCREMENT,
  `id_publicador` int(11) NOT NULL,
  `nom_publicador` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adm_email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sigla` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_responsavel` int(11) NOT NULL,
  PRIMARY KEY (`cod_publicador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `localidade`
--

CREATE TABLE `localidade` (
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

-- --------------------------------------------------------

--
-- Estrutura da tabela `mandato`
--

CREATE TABLE `mandato` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `mandato`:
--   `tip_afastamento`
--       `tipo_afastamento` -> `tip_afastamento`
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--   `cod_coligacao`
--       `coligacao` -> `cod_coligacao`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `materia_apresentada_sessao`
--

CREATE TABLE `materia_apresentada_sessao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `materia_apresentada_sessao`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `materia_legislativa`
--

CREATE TABLE `materia_legislativa` (
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
  `tip_quorum` int(11) DEFAULT NULL,
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
  FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `materia_legislativa`:
--   `tip_id_basica`
--       `tipo_materia_legislativa` -> `tip_materia`
--   `cod_regime_tramitacao`
--       `regime_tramitacao` -> `cod_regime_tramitacao`
--   `cod_local_origem_externa`
--       `origem` -> `cod_origem`
--   `cod_situacao`
--       `tipo_situacao_materia` -> `tip_situacao_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `mesa_sessao_plenaria`
--

CREATE TABLE `mesa_sessao_plenaria` (
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
-- RELACIONAMENTOS PARA A TABELA `mesa_sessao_plenaria`:
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `nivel_instrucao`
--

CREATE TABLE `nivel_instrucao` (
  `cod_nivel_instrucao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_nivel_instrucao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_nivel_instrucao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `norma_juridica`
--

CREATE TABLE `norma_juridica` (
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
  FULLTEXT KEY `idx_busca_norma` (`txt_ementa`,`txt_indexacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `norma_juridica`:
--   `cod_assunto`
--       `assunto_norma` -> `cod_assunto`
--   `tip_norma`
--       `tipo_norma_juridica` -> `tip_norma`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_situacao`
--       `tipo_situacao_norma` -> `tip_situacao_norma`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `numeracao`
--

CREATE TABLE `numeracao` (
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
-- RELACIONAMENTOS PARA A TABELA `numeracao`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `tip_materia`
--       `tipo_materia_legislativa` -> `tip_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `oradores`
--

CREATE TABLE `oradores` (
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
-- RELACIONAMENTOS PARA A TABELA `oradores`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `oradores_expediente`
--

CREATE TABLE `oradores_expediente` (
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
-- RELACIONAMENTOS PARA A TABELA `oradores_expediente`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `ordem_dia`
--

CREATE TABLE `ordem_dia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) unsigned NOT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_turno` int(11) DEFAULT NULL,
  `tip_votacao` int(11) NOT NULL,
  `tip_quorum` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_dat_ordem` (`dat_ordem`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `tip_quorum` (`tip_quorum`),
  KEY `tip_turno` (`tip_turno`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `ordem_dia`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `tip_turno`
--       `turno_discussao` -> `cod_turno`
--   `tip_quorum`
--       `quorum_votacao` -> `cod_quorum`
--   `tip_votacao`
--       `tipo_votacao` -> `tip_votacao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `ordem_dia_presenca`
--

CREATE TABLE `ordem_dia_presenca` (
  `cod_presenca_ordem_dia` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'P',
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_ordem_dia`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `dat_ordem` (`dat_ordem`),
  KEY `tip_frequencia` (`tip_frequencia`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `ordem_dia_presenca`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `orgao`
--

CREATE TABLE `orgao` (
  `cod_orgao` int(11) NOT NULL AUTO_INCREMENT,
  `nom_orgao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_orgao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `end_orgao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_orgao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_orgao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `origem`
--

CREATE TABLE `origem` (
  `cod_origem` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_origem` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_origem` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_origem`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `parecer`
--

CREATE TABLE `parecer` (
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
-- RELACIONAMENTOS PARA A TABELA `parecer`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `parlamentar`
--

CREATE TABLE `parlamentar` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `parlamentar`:
--   `cod_nivel_instrucao`
--       `nivel_instrucao` -> `cod_nivel_instrucao`
--   `tip_situacao_militar`
--       `tipo_situacao_militar` -> `tip_situacao_militar`
--   `cod_localidade_resid`
--       `localidade` -> `cod_localidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `partido`
--

CREATE TABLE `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `periodo_comp_comissao`
--

CREATE TABLE `periodo_comp_comissao` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompcom_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `periodo_comp_mesa`
--

CREATE TABLE `periodo_comp_mesa` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompmesa_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `periodo_comp_mesa`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `proposicao`
--

CREATE TABLE `proposicao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `proposicao`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_proposicao`
--       `tipo_proposicao` -> `tip_proposicao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `protocolo`
--

CREATE TABLE `protocolo` (
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
  FULLTEXT KEY `idx_busca_protocolo` (`txt_interessado`,`txt_assunto_ementa`,`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

--
-- RELACIONAMENTOS PARA A TABELA `protocolo`:
--   `cod_autor`
--       `autor` -> `cod_autor`
--   `tip_documento`
--       `tipo_documento_administrativo` -> `tip_documento`
--   `tip_materia`
--       `tipo_materia_legislativa` -> `tip_materia`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `quorum_votacao`
--

CREATE TABLE `quorum_votacao` (
  `cod_quorum` int(11) NOT NULL AUTO_INCREMENT,
  `des_quorum` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `txt_formula` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_quorum`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `regime_tramitacao`
--

CREATE TABLE `regime_tramitacao` (
  `cod_regime_tramitacao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_regime_tramitacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_regime_tramitacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_votacao`
--

CREATE TABLE `registro_votacao` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `registro_votacao`:
--   `tip_resultado_votacao`
--       `tipo_resultado_votacao` -> `tip_resultado_votacao`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_emenda`
--       `emenda` -> `cod_emenda`
--   `cod_subemenda`
--       `subemenda` -> `cod_subemenda`
--   `cod_substitutivo`
--       `substitutivo` -> `cod_substitutivo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_votacao_parlamentar`
--

CREATE TABLE `registro_votacao_parlamentar` (
  `cod_votacao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  `vot_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_votacao`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_votacao` (`cod_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `registro_votacao_parlamentar`:
--   `cod_votacao`
--       `registro_votacao` -> `cod_votacao`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatoria`
--

CREATE TABLE `relatoria` (
  `cod_relatoria` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_fim_relatoria` tinyint(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `num_ordem` tinyint(4) NOT NULL,
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `relatoria`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--   `tip_fim_relatoria`
--       `tipo_fim_relatoria` -> `tip_fim_relatoria`
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `reuniao_comissao`
--

CREATE TABLE `reuniao_comissao` (
  `cod_reuniao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) NOT NULL,
  `num_reuniao` int(11) NOT NULL,
  `dat_inicio_reuniao` date NOT NULL,
  `hr_inicio_reuniao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_reuniao`),
  KEY `cod_comissao` (`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `reuniao_comissao`:
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_legislativa`
--

CREATE TABLE `sessao_legislativa` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `sessao_legislativa`:
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_plenaria`
--

CREATE TABLE `sessao_plenaria` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `sessao_plenaria`:
--   `tip_sessao`
--       `tipo_sessao_plenaria` -> `tip_sessao`
--   `cod_sessao_leg`
--       `sessao_legislativa` -> `cod_sessao_leg`
--   `num_legislatura`
--       `legislatura` -> `num_legislatura`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_plenaria_presenca`
--

CREATE TABLE `sessao_plenaria_presenca` (
  `cod_presenca_sessao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'P',
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_sessao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_sessao`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `dat_sessao` (`dat_sessao`),
  KEY `tip_frequencia` (`tip_frequencia`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `sessao_plenaria_presenca`:
--   `cod_sessao_plen`
--       `sessao_plenaria` -> `cod_sessao_plen`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `status_tramitacao`
--

CREATE TABLE `status_tramitacao` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `status_tramitacao_administrativo`
--

CREATE TABLE `status_tramitacao_administrativo` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subemenda`
--

CREATE TABLE `subemenda` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `subemenda`:
--   `tip_subemenda`
--       `tipo_emenda` -> `tip_emenda`
--   `cod_emenda`
--       `emenda` -> `cod_emenda`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `substitutivo`
--

CREATE TABLE `substitutivo` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- RELACIONAMENTOS PARA A TABELA `substitutivo`:
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_autor`
--       `autor` -> `cod_autor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_afastamento`
--

CREATE TABLE `tipo_afastamento` (
  `tip_afastamento` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_afastamento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_afastamento` tinyint(4) NOT NULL,
  `ind_fim_mandato` tinyint(4) NOT NULL,
  `des_dispositivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_afastamento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_autor`
--

CREATE TABLE `tipo_autor` (
  `tip_autor` tinyint(4) NOT NULL,
  `des_tipo_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_autor`),
  KEY `des_tipo_autor` (`des_tipo_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_comissao`
--

CREATE TABLE `tipo_comissao` (
  `tip_comissao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_comissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_natureza_comissao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_dispositivo_regimental` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_comissao`),
  KEY `nom_tipo_comissao` (`nom_tipo_comissao`),
  KEY `sgl_natureza_comissao` (`sgl_natureza_comissao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_dependente`
--

CREATE TABLE `tipo_dependente` (
  `tip_dependente` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_tipo_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_dependente`),
  KEY `des_tipo_dependente` (`des_tipo_dependente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_documento`
--

CREATE TABLE `tipo_documento` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_documento_administrativo`
--

CREATE TABLE `tipo_documento_administrativo` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_documento` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_emenda`
--

CREATE TABLE `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`),
  KEY `des_tipo_emenda` (`des_tipo_emenda`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_expediente`
--

CREATE TABLE `tipo_expediente` (
  `cod_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `nom_expediente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`cod_expediente`),
  KEY `nom_expediente` (`nom_expediente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_fim_relatoria`
--

CREATE TABLE `tipo_fim_relatoria` (
  `tip_fim_relatoria` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_fim_relatoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_fim_relatoria`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_instituicao`
--

CREATE TABLE `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_materia_legislativa`
--

CREATE TABLE `tipo_materia_legislativa` (
  `tip_materia` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_materia` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_num_automatica` tinyint(4) NOT NULL DEFAULT '0',
  `quorum_minimo_votacao` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_materia`),
  KEY `des_tipo_materia` (`des_tipo_materia`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_norma_juridica`
--

CREATE TABLE `tipo_norma_juridica` (
  `tip_norma` tinyint(4) NOT NULL AUTO_INCREMENT,
  `voc_lexml` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_norma` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_norma` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_norma`),
  KEY `des_tipo_norma` (`des_tipo_norma`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_proposicao`
--

CREATE TABLE `tipo_proposicao` (
  `tip_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_proposicao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_mat_ou_doc` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_mat_ou_doc` int(11) NOT NULL,
  `nom_modelo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_proposicao`),
  KEY `des_tipo_proposicao` (`des_tipo_proposicao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_resultado_votacao`
--

CREATE TABLE `tipo_resultado_votacao` (
  `tip_resultado_votacao` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom_resultado` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`tip_resultado_votacao`),
  KEY `nom_resultado` (`nom_resultado`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_sessao_plenaria`
--

CREATE TABLE `tipo_sessao_plenaria` (
  `tip_sessao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_sessao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_minimo` int(11) NOT NULL,
  PRIMARY KEY (`tip_sessao`),
  KEY `nom_sessao` (`nom_sessao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_materia`
--

CREATE TABLE `tipo_situacao_materia` (
  `tip_situacao_materia` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_materia`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_militar`
--

CREATE TABLE `tipo_situacao_militar` (
  `tip_situacao_militar` tinyint(4) NOT NULL,
  `des_tipo_situacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_situacao_militar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_norma`
--

CREATE TABLE `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_vinculo_norma`
--

CREATE TABLE `tipo_vinculo_norma` (
  `cod_tip_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tip_vinculo`),
  UNIQUE KEY `tip_vinculo` (`tip_vinculo`),
  UNIQUE KEY `idx_vinculo` (`tip_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_votacao`
--

CREATE TABLE `tipo_votacao` (
  `tip_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_votacao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tramitacao`
--

CREATE TABLE `tramitacao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `tramitacao`:
--   `cod_status`
--       `status_tramitacao` -> `cod_status`
--   `cod_materia`
--       `materia_legislativa` -> `cod_materia`
--   `cod_unid_tram_local`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--   `cod_unid_tram_dest`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tramitacao_administrativo`
--

CREATE TABLE `tramitacao_administrativo` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

--
-- RELACIONAMENTOS PARA A TABELA `tramitacao_administrativo`:
--   `cod_documento`
--       `documento_administrativo` -> `cod_documento`
--   `cod_unid_tram_local`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--   `cod_unid_tram_dest`
--       `unidade_tramitacao` -> `cod_unid_tramitacao`
--   `cod_status`
--       `status_tramitacao_administrativo` -> `cod_status`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `turno_discussao`
--

CREATE TABLE `turno_discussao` (
  `cod_turno` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_turno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_turno`),
  UNIQUE KEY `idx_unique_key` (`cod_turno`,`sgl_turno`,`ind_excluido`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `unidade_tramitacao`
--

CREATE TABLE `unidade_tramitacao` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `unidade_tramitacao`:
--   `cod_comissao`
--       `comissao` -> `cod_comissao`
--   `cod_orgao`
--       `orgao` -> `cod_orgao`
--   `cod_parlamentar`
--       `parlamentar` -> `cod_parlamentar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `vinculo_norma_juridica`
--

CREATE TABLE `vinculo_norma_juridica` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma_referente` int(11) NOT NULL,
  `cod_norma_referida` int(11) DEFAULT NULL,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `tip_vinculo` (`tip_vinculo`),
  KEY `idx_vnj_norma_referente` (`cod_norma_referente`,`cod_norma_referida`,`ind_excluido`),
  KEY `idx_vnj_norma_referida` (`cod_norma_referida`,`cod_norma_referente`,`ind_excluido`),
  KEY `cod_norma_referente` (`cod_norma_referente`),
  KEY `cod_norma_referida` (`cod_norma_referida`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

--
-- RELACIONAMENTOS PARA A TABELA `vinculo_norma_juridica`:
--   `cod_norma_referente`
--       `norma_juridica` -> `cod_norma`
--   `cod_norma_referida`
--       `norma_juridica` -> `cod_norma`
--

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
