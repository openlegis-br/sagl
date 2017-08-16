-- Generation Time: 16-Ago-2017 às 19:36
-- Versão do servidor: 5.7.19-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `interlegis`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `acomp_materia`
--

CREATE TABLE IF NOT EXISTS `acomp_materia` (
  `cod_cadastro` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_hash` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cadastro`),
  UNIQUE KEY `idx_unique` (`cod_materia`,`end_email`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `afastamento`
--

CREATE TABLE IF NOT EXISTS `afastamento` (
  `cod_afastamento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_mandato` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `tip_afastamento` int(11) NOT NULL,
  `dat_inicio_afastamento` date NOT NULL,
  `dat_fim_afastamento` date DEFAULT NULL,
  `cod_parlamentar_suplente` int(11) NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_afastamento`),
  KEY `idx_parlamentar_mandato` (`cod_parlamentar`,`num_legislatura`),
  KEY `idx_afastamento_datas` (`cod_parlamentar`,`dat_inicio_afastamento`,`dat_fim_afastamento`),
  KEY `idx_tip_afastamento` (`tip_afastamento`),
  KEY `idx__parlamentar_suplente` (`cod_parlamentar_suplente`,`num_legislatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `anexada`
--

CREATE TABLE IF NOT EXISTS `anexada` (
  `cod_materia_principal` int(11) NOT NULL,
  `cod_materia_anexada` int(11) NOT NULL,
  `dat_anexacao` date NOT NULL,
  `dat_desanexacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia_principal`,`cod_materia_anexada`),
  KEY `idx_mat_anexada` (`cod_materia_anexada`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `anexo_norma`
--

CREATE TABLE IF NOT EXISTS `anexo_norma` (
  `cod_anexo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma` int(11) NOT NULL,
  `txt_descricao` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_anexo`),
  KEY `cod_norma` (`cod_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_armario`
--

CREATE TABLE IF NOT EXISTS `arquivo_armario` (
  `cod_armario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_armario` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_corredor`
--

CREATE TABLE IF NOT EXISTS `arquivo_corredor` (
  `cod_corredor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_unidade` int(11) NOT NULL,
  `nom_corredor` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_item`
--

CREATE TABLE IF NOT EXISTS `arquivo_item` (
  `cod_item` int(11) NOT NULL AUTO_INCREMENT,
  `cod_recipiente` int(11) NOT NULL,
  `tip_suporte` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_norma` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `cod_protocolo` int(7) UNSIGNED ZEROFILL DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_prateleira`
--

CREATE TABLE IF NOT EXISTS `arquivo_prateleira` (
  `cod_prateleira` int(11) NOT NULL AUTO_INCREMENT,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_prateleira` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_prateleira`),
  KEY `cod_armario` (`cod_armario`),
  KEY `cod_corredor` (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_recipiente`
--

CREATE TABLE IF NOT EXISTS `arquivo_recipiente` (
  `cod_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `tip_recipiente` int(11) NOT NULL,
  `num_recipiente` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_recipiente`
--

CREATE TABLE IF NOT EXISTS `arquivo_tipo_recipiente` (
  `tip_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_recipiente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_recipiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_suporte`
--

CREATE TABLE IF NOT EXISTS `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_suporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_tipo_tit_documental`
--

CREATE TABLE IF NOT EXISTS `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_tit_documental`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `arquivo_unidade`
--

CREATE TABLE IF NOT EXISTS `arquivo_unidade` (
  `cod_unidade` int(11) NOT NULL AUTO_INCREMENT,
  `tip_extensao_atuacao` int(11) NOT NULL,
  `tip_estagio_evolucao` int(11) NOT NULL,
  `nom_unidade` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_localizacao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `assessor_parlamentar`
--

CREATE TABLE IF NOT EXISTS `assessor_parlamentar` (
  `cod_assessor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_assessor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `assunto_norma`
--

CREATE TABLE IF NOT EXISTS `assunto_norma` (
  `cod_assunto` int(4) NOT NULL AUTO_INCREMENT,
  `des_assunto` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estendida` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_assunto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `autor`
--

CREATE TABLE IF NOT EXISTS `autor` (
  `cod_autor` int(11) NOT NULL AUTO_INCREMENT,
  `tip_autor` tinyint(4) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_bancada` int(11) DEFAULT NULL,
  `nom_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  `col_username` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `autoria`
--

CREATE TABLE IF NOT EXISTS `autoria` (
  `cod_autor` int(11) NOT NULL DEFAULT '0',
  `cod_materia` int(11) NOT NULL DEFAULT '0',
  `ind_primeiro_autor` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_autor`,`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estrutura da tabela `bancada`
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
  KEY `idx_cod_bancada` (`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_bancada`
--

CREATE TABLE IF NOT EXISTS `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_comissao`
--

CREATE TABLE IF NOT EXISTS `cargo_comissao` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_executivo`
--

CREATE TABLE IF NOT EXISTS `cargo_executivo` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo_mesa`
--

CREATE TABLE IF NOT EXISTS `cargo_mesa` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `coautoria_proposicao`
--

CREATE TABLE IF NOT EXISTS `coautoria_proposicao` (
  `cod_proposicao` int(11) NOT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_aderido` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_proposicao`,`cod_autor`),
  KEY `idx_proposicao` (`cod_proposicao`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `coligacao`
--

CREATE TABLE IF NOT EXISTS `coligacao` (
  `cod_coligacao` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `nom_coligacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_votos_coligacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_coligacao`),
  KEY `idx_coligacao_legislatura` (`ind_excluido`,`num_legislatura`),
  KEY `idx_legislatura` (`num_legislatura`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `comissao`
--

CREATE TABLE IF NOT EXISTS `comissao` (
  `cod_comissao` int(11) NOT NULL AUTO_INCREMENT,
  `nom_comissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_comissao` tinyint(4) NOT NULL DEFAULT '0',
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
  `ind_unid_deliberativa` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_bancada`
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
  KEY `idx_cargo` (`cod_cargo`) USING BTREE,
  KEY `idx_bancada` (`cod_bancada`) USING BTREE,
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_coligacao`
--

CREATE TABLE IF NOT EXISTS `composicao_coligacao` (
  `cod_partido` int(11) NOT NULL,
  `cod_coligacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_partido`,`cod_coligacao`),
  KEY `idx_coligacao` (`cod_coligacao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_comissao`
--

CREATE TABLE IF NOT EXISTS `composicao_comissao` (
  `cod_comp_comissao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_periodo_comp` int(11) NOT NULL DEFAULT '0',
  `cod_comissao` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL DEFAULT '0',
  `cod_cargo` tinyint(4) NOT NULL DEFAULT '0',
  `ind_titular` tinyint(4) NOT NULL DEFAULT '0',
  `dat_designacao` date DEFAULT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_comp_comissao`),
  KEY `cod_periodo_comp` (`cod_periodo_comp`),
  KEY `cod_comissao` (`cod_comissao`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_cargo` (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_executivo`
--

CREATE TABLE IF NOT EXISTS `composicao_executivo` (
  `cod_composicao` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` tinyint(4) NOT NULL,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `dat_inicio_mandato` date DEFAULT NULL,
  `dat_fim_mandato` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_composicao`),
  KEY `num_legislatura` (`num_legislatura`),
  KEY `cod_cargo` (`cod_cargo`),
  KEY `cod_partido` (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `composicao_mesa`
--

CREATE TABLE IF NOT EXISTS `composicao_mesa` (
  `cod_parlamentar` int(11) NOT NULL DEFAULT '0',
  `cod_sessao_leg` int(11) DEFAULT NULL,
  `cod_periodo_comp` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_parlamentar`,`cod_periodo_comp`,`cod_cargo`),
  KEY `idx_cod_periodo_comp` (`cod_periodo_comp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dependente`
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
  KEY `idx_dep_parlam` (`ind_excluido`,`cod_parlamentar`,`tip_dependente`),
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE,
  KEY `idx_tip_dependente` (`tip_dependente`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `despacho_inicial`
--

CREATE TABLE IF NOT EXISTS `despacho_inicial` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) UNSIGNED NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_materia`,`num_ordem`),
  KEY `idx_despinic_comissao` (`ind_excluido`,`cod_comissao`),
  KEY `fk_{24ED266E-2C4B-4C6C-84F0-57AFC228FACE}` (`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `destinatario_oficio`
--

CREATE TABLE IF NOT EXISTS `destinatario_oficio` (
  `cod_destinatario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_instituicao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_destinatario`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_instituicao` (`cod_instituicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_acessorio`
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
  KEY `idx_doc_materia` (`ind_excluido`),
  KEY `idx_doc_tipdoc_mat` (`ind_excluido`),
  KEY `fk_{F4F80AA5-442B-49CF-95C6-A5D400BFA666}` (`tip_documento`),
  KEY `fk_{E56B7D01-44A5-4AF1-8D14-EF5BA538BD00}` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_acessorio_administrativo`
--

CREATE TABLE IF NOT EXISTS `documento_acessorio_administrativo` (
  `cod_documento_acessorio` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL DEFAULT '0',
  `tip_documento` int(11) NOT NULL DEFAULT '0',
  `nom_documento` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_arquivo` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_documento` date DEFAULT NULL,
  `nom_autor_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_documento_acessorio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_administrativo`
--

CREATE TABLE IF NOT EXISTS `documento_administrativo` (
  `cod_documento` int(11) NOT NULL AUTO_INCREMENT,
  `tip_documento` tinyint(4) NOT NULL,
  `num_documento` int(8) NOT NULL,
  `ano_documento` smallint(6) NOT NULL DEFAULT '0',
  `dat_documento` date NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `txt_interessado` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_assunto` text CHARACTER SET latin1 NOT NULL,
  `txt_observacao` text CHARACTER SET latin1,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_documento`),
  KEY `idx_num_ano` (`num_documento`,`ano_documento`),
  KEY `idx_dat_documento` (`dat_documento`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_documento` (`tip_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `documento_administrativo_materia`
--

CREATE TABLE IF NOT EXISTS `documento_administrativo_materia` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `idx_cod_documento` (`cod_documento`),
  KEY `idx_cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `emenda`
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
  `exc_pauta` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_emenda`),
  UNIQUE KEY `idx_numemen_materia` (`num_emenda`,`cod_materia`,`ind_excluido`),
  UNIQUE KEY `idx_emen_materia` (`num_emenda`,`tip_emenda`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_materia` (`cod_materia`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_tip_emenda` (`tip_emenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `encerramento_presenca`
--

CREATE TABLE IF NOT EXISTS `encerramento_presenca` (
  `cod_presenca_encerramento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_encerramento`),
  UNIQUE KEY `idx_encpres_sessao_plenaria` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_materia`
--

CREATE TABLE IF NOT EXISTS `expediente_materia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) DEFAULT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_quorum` int(11) DEFAULT NULL,
  `tip_votacao` int(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `idx_exped_datord` (`dat_ordem`,`ind_excluido`),
  KEY `tip_quorum` (`tip_quorum`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `idx_materia` (`cod_materia`) USING BTREE,
  KEY `idx_materia_sessao` (`cod_materia`,`cod_sessao_plen`,`ind_excluido`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_presenca`
--

CREATE TABLE IF NOT EXISTS `expediente_presenca` (
  `cod_presenca_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_presenca_expediente`),
  UNIQUE KEY `idx_exppres_sessao_plenaria` (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `expediente_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `expediente_sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_expediente` int(11) NOT NULL,
  `txt_expediente` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_expediente`),
  KEY `idx_expediente` (`cod_expediente`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `filiacao`
--

CREATE TABLE IF NOT EXISTS `filiacao` (
  `dat_filiacao` date NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_partido` int(11) NOT NULL,
  `dat_desfiliacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`dat_filiacao`,`cod_parlamentar`,`cod_partido`),
  KEY `idx_partido` (`cod_partido`) USING BTREE,
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario`
--

CREATE TABLE IF NOT EXISTS `funcionario` (
  `cod_funcionario` int(11) NOT NULL AUTO_INCREMENT,
  `nom_funcionario` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cod_usuario` int(11) DEFAULT NULL,
  `des_cargo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_cadastro` date NOT NULL,
  `ind_ativo` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_funcionario`),
  KEY `cod_usuario` (`cod_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `instituicao`
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
  PRIMARY KEY (`cod_instituicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `legislacao_citada`
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
  KEY `fk_{7C4DDF94-DF67-4F33-90A0-06A770185844}` (`cod_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `legislatura`
--

CREATE TABLE IF NOT EXISTS `legislatura` (
  `num_legislatura` tinyint(4) NOT NULL DEFAULT '0',
  `dat_inicio` date DEFAULT NULL,
  `dat_fim` date DEFAULT NULL,
  `dat_eleicao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`num_legislatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lexml_registro_provedor`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lexml_registro_publicador`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `localidade`
--

CREATE TABLE IF NOT EXISTS `localidade` (
  `cod_localidade` int(11) NOT NULL DEFAULT '0',
  `nom_localidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_localidade_pesq` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_localidade` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_uf` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_regiao` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_localidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `logradouro`
--

CREATE TABLE IF NOT EXISTS `logradouro` (
  `cod_logradouro` int(11) NOT NULL AUTO_INCREMENT,
  `nom_logradouro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_logradouro`),
  KEY `num_cep` (`num_cep`),
  KEY `cod_localidade` (`cod_localidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mandato`
--

CREATE TABLE IF NOT EXISTS `mandato` (
  `cod_mandato` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL DEFAULT '0',
  `cod_coligacao` int(11) DEFAULT NULL,
  `dat_inicio_mandato` date DEFAULT NULL,
  `tip_causa_fim_mandato` tinyint(4) DEFAULT NULL,
  `dat_fim_mandato` date DEFAULT NULL,
  `num_votos_recebidos` int(11) DEFAULT NULL,
  `dat_expedicao_diploma` date DEFAULT NULL,
  `cod_parlamentar` int(11) NOT NULL DEFAULT '0',
  `tip_afastamento` tinyint(4) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_titular` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_mandato`),
  KEY `Codigo_LEGISLATURA` (`num_legislatura`),
  KEY `Codigo_POLITICO` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `materia_apresentada_sessao`
--

CREATE TABLE IF NOT EXISTS `materia_apresentada_sessao` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `fk_cod_materia` (`cod_materia`),
  KEY `idx_apresent_datord` (`dat_ordem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `materia_legislativa`
--

CREATE TABLE IF NOT EXISTS `materia_legislativa` (
  `cod_materia` int(11) NOT NULL AUTO_INCREMENT,
  `tip_id_basica` int(11) NOT NULL DEFAULT '0',
  `num_protocolo` int(11) DEFAULT NULL,
  `num_ident_basica` int(11) NOT NULL,
  `ano_ident_basica` smallint(6) NOT NULL DEFAULT '0',
  `dat_apresentacao` date DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_publicacao` date DEFAULT NULL,
  `tip_origem_externa` int(11) DEFAULT NULL,
  `num_origem_externa` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ano_origem_externa` smallint(6) DEFAULT NULL,
  `dat_origem_externa` date DEFAULT NULL,
  `cod_local_origem_externa` int(11) DEFAULT NULL,
  `nom_apelido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_polemica` tinyint(4) DEFAULT NULL,
  `des_objeto` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_complementar` tinyint(4) DEFAULT NULL,
  `cod_regime_tramitacao` tinyint(4) DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci NOT NULL,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `tip_quorum` int(11) DEFAULT NULL,
  `cod_situacao` int(11) DEFAULT NULL,
  `cod_materia_principal` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_materia`),
  KEY `idx_matleg_ident` (`ind_excluido`,`tip_id_basica`,`ano_ident_basica`,`num_ident_basica`),
  KEY `idx_dat_apresentacao` (`dat_apresentacao`,`ind_excluido`,`tip_id_basica`),
  KEY `idx_matleg_dat_publicacao` (`dat_publicacao`,`ind_excluido`,`tip_id_basica`),
  KEY `tip_id_basica` (`tip_id_basica`),
  KEY `cod_local_origem_externa` (`cod_local_origem_externa`),
  KEY `tip_quorum` (`tip_quorum`),
  KEY `idx_mat_principal` (`cod_materia_principal`),
  KEY `idx_regime_tram` (`cod_regime_tramitacao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mesa_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `mesa_sessao_plenaria` (
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_sessao_leg` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `ind_excluido` tinyint(4) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`cod_cargo`,`cod_sessao_leg`,`cod_parlamentar`,`cod_sessao_plen`),
  KEY `idx_sessao_leg` (`cod_sessao_leg`) USING BTREE,
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE,
  KEY `idx_sessao_plen` (`cod_sessao_plen`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `nivel_instrucao`
--

CREATE TABLE IF NOT EXISTS `nivel_instrucao` (
  `cod_nivel_instrucao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_nivel_instrucao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_nivel_instrucao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `norma_juridica`
--

CREATE TABLE IF NOT EXISTS `norma_juridica` (
  `cod_norma` int(11) NOT NULL AUTO_INCREMENT,
  `tip_norma` tinyint(4) NOT NULL DEFAULT '0',
  `num_norma` int(11) NOT NULL DEFAULT '0',
  `ano_norma` smallint(6) NOT NULL,
  `tip_esfera_federacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `dat_norma` date NOT NULL,
  `dat_publicacao` date DEFAULT NULL,
  `des_veiculo_publicacao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_pag_inicio_publ` int(11) DEFAULT NULL,
  `num_pag_fim_publ` int(11) DEFAULT NULL,
  `txt_ementa` text CHARACTER SET latin1 NOT NULL,
  `txt_indexacao` text CHARACTER SET latin1,
  `txt_observacao` text CHARACTER SET latin1,
  `ind_complemento` tinyint(4) DEFAULT NULL,
  `cod_assunto` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_situacao` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  `dat_vigencia` date DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cod_norma`),
  KEY `idx_nj_assnorm` (`cod_assunto`),
  KEY `cod_assunto` (`cod_assunto`),
  KEY `tip_norma` (`tip_norma`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_ano_numero` (`ano_norma`,`num_norma`,`ind_excluido`),
  KEY `cod_situacao` (`cod_situacao`),
  KEY `dat_norma` (`dat_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `numeracao`
--

CREATE TABLE IF NOT EXISTS `numeracao` (
  `cod_materia` int(11) NOT NULL DEFAULT '0',
  `num_ordem` tinyint(4) NOT NULL DEFAULT '0',
  `tip_materia` int(11) NOT NULL DEFAULT '0',
  `num_materia` varchar(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ano_materia` smallint(6) NOT NULL DEFAULT '0',
  `dat_materia` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_materia`,`num_ordem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `oradores`
--

CREATE TABLE IF NOT EXISTS `oradores` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_{A63E6611-A33C-4831-976E-64D1DCF51F7D}` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `oradores_expediente`
--

CREATE TABLE IF NOT EXISTS `oradores_expediente` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `fk_{A63E6611-A33C-4831-976E-64D1DCF51F7D}` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `ordem_dia`
--

CREATE TABLE IF NOT EXISTS `ordem_dia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) DEFAULT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_turno` int(11) DEFAULT NULL,
  `tip_votacao` int(11) UNSIGNED NOT NULL,
  `tip_quorum` int(11) DEFAULT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `idx_orddia_datord` (`dat_ordem`,`ind_excluido`),
  KEY `tip_quorum` (`tip_quorum`),
  KEY `tip_turno` (`tip_turno`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `idx_materia` (`cod_materia`) USING BTREE,
  KEY `idx_materia_sessao` (`cod_sessao_plen`,`cod_materia`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `ordem_dia_presenca`
--

CREATE TABLE IF NOT EXISTS `ordem_dia_presenca` (
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  `dat_ordem` date NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_presenca_ordem_dia` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`cod_presenca_ordem_dia`),
  KEY `idx_orddiapres_sessao_plenaria` (`cod_sessao_plen`),
  KEY `tip_frequencia` (`tip_frequencia`),
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `orgao`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `origem`
--

CREATE TABLE IF NOT EXISTS `origem` (
  `cod_origem` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_origem` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_origem` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_origem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `parecer`
--

CREATE TABLE IF NOT EXISTS `parecer` (
  `cod_relatoria` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `tip_conclusao` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_relatoria`,`cod_materia`),
  KEY `idx_parecer_materia` (`ind_excluido`,`cod_materia`),
  KEY `fk_{AFF28198-95BD-4AC4-AE37-E02F46C6EEF7}` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `parlamentar`
--

CREATE TABLE IF NOT EXISTS `parlamentar` (
  `cod_parlamentar` int(11) NOT NULL AUTO_INCREMENT,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_parlamentar` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_situacao_militar` tinyint(4) DEFAULT NULL,
  `cod_nivel_instrucao` tinyint(4) DEFAULT NULL,
  `cod_casa` int(11) NOT NULL DEFAULT '0',
  `num_gab_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax_parlamentar` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade_resid` int(11) DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_fax_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_web` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_profissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_local_atuacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_ativo` tinyint(4) NOT NULL DEFAULT '0',
  `ind_unid_deliberativa` tinyint(4) DEFAULT NULL,
  `txt_biografia` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `partido`
--

CREATE TABLE IF NOT EXISTS `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `periodo_comp_comissao`
--

CREATE TABLE IF NOT EXISTS `periodo_comp_comissao` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompcom_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `periodo_comp_mesa`
--

CREATE TABLE IF NOT EXISTS `periodo_comp_mesa` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompmesa_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoa`
--

CREATE TABLE IF NOT EXISTS `pessoa` (
  `cod_pessoa` int(11) NOT NULL AUTO_INCREMENT,
  `nom_pessoa` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `doc_identidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `sex_pessoa` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estado_civil` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_conjuge` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dependentes` tinytext COLLATE utf8_unicode_ci,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_logradouro` int(11) DEFAULT NULL,
  `end_residencial` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `num_imovel` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `num_cep` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nom_cidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_tempo_residencia` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_celular` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_local_trabalho` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `dat_atualizacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_pessoa`),
  KEY `num_cep` (`num_cep`),
  KEY `cod_logradouro` (`cod_logradouro`),
  KEY `nom_cidade` (`nom_cidade`),
  KEY `dat_nascimento` (`dat_nascimento`),
  KEY `des_profissao` (`des_profissao`),
  KEY `des_estado_civil` (`des_estado_civil`),
  KEY `sex_visitante` (`sex_pessoa`),
  KEY `nom_bairro` (`nom_bairro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `proposicao`
--

CREATE TABLE IF NOT EXISTS `proposicao` (
  `cod_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `tip_proposicao` int(11) NOT NULL,
  `dat_envio` datetime DEFAULT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `txt_descricao` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_mat_ou_doc` int(11) DEFAULT NULL,
  `cod_emenda` int(11) DEFAULT NULL,
  `cod_substitutivo` int(11) DEFAULT NULL,
  `dat_devolucao` datetime DEFAULT NULL,
  `txt_justif_devolucao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_proposicao`),
  KEY `idx_prop_autor` (`ind_excluido`,`dat_envio`,`dat_recebimento`),
  KEY `idx_materia` (`cod_materia`) USING BTREE,
  KEY `idx_autor` (`cod_autor`) USING BTREE,
  KEY `idx_tip_proposicao` (`tip_proposicao`) USING BTREE,
  KEY `idx_substitutivo` (`cod_substitutivo`) USING BTREE,
  KEY `idx_emenda` (`cod_emenda`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `protocolo`
--

CREATE TABLE IF NOT EXISTS `protocolo` (
  `cod_protocolo` int(7) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
  `num_protocolo` int(7) UNSIGNED ZEROFILL DEFAULT NULL,
  `ano_protocolo` smallint(6) NOT NULL,
  `dat_protocolo` date NOT NULL,
  `hor_protocolo` time NOT NULL DEFAULT '00:00:00',
  `dat_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tip_protocolo` int(4) NOT NULL,
  `tip_processo` int(4) DEFAULT NULL,
  `txt_interessado` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `txt_assunto_ementa` text COLLATE utf8_unicode_ci,
  `tip_documento` int(11) DEFAULT NULL,
  `tip_materia` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `num_paginas` int(6) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_anulado` tinyint(4) NOT NULL DEFAULT '0',
  `txt_user_anulacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_anulacao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_just_anulacao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp_anulacao` datetime DEFAULT NULL,
  PRIMARY KEY (`cod_protocolo`),
  KEY `idx_num_protocolo` (`cod_protocolo`,`ano_protocolo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `quorum_votacao`
--

CREATE TABLE IF NOT EXISTS `quorum_votacao` (
  `cod_quorum` int(11) NOT NULL AUTO_INCREMENT,
  `des_quorum` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_formula` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_quorum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `regime_tramitacao`
--

CREATE TABLE IF NOT EXISTS `regime_tramitacao` (
  `cod_regime_tramitacao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_regime_tramitacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_regime_tramitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_votacao`
--

CREATE TABLE IF NOT EXISTS `registro_votacao` (
  `cod_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `tip_resultado_votacao` int(10) UNSIGNED NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `cod_ordem` int(11) NOT NULL,
  `cod_emenda` int(11) DEFAULT NULL,
  `cod_subemenda` int(11) DEFAULT NULL,
  `cod_substitutivo` int(11) DEFAULT NULL,
  `num_votos_sim` tinyint(4) UNSIGNED NOT NULL,
  `num_votos_nao` tinyint(4) UNSIGNED NOT NULL,
  `num_abstencao` tinyint(4) UNSIGNED NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  PRIMARY KEY (`cod_votacao`),
  KEY `idx_ordem` (`cod_ordem`) USING BTREE,
  KEY `idx_materia` (`cod_materia`) USING BTREE,
  KEY `idx_tip_resultado` (`tip_resultado_votacao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_votacao_parlamentar`
--

CREATE TABLE IF NOT EXISTS `registro_votacao_parlamentar` (
  `cod_votacao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  `vot_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_votacao`,`cod_parlamentar`),
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatoria`
--

CREATE TABLE IF NOT EXISTS `relatoria` (
  `cod_relatoria` int(11) NOT NULL AUTO_INCREMENT,
  `cod_materia` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_fim_relatoria` tinyint(4) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `dat_desig_relator` date NOT NULL,
  `dat_destit_relator` date DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `tip_conclusao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_relatoria`),
  KEY `idx_relat_materia` (`ind_excluido`,`cod_materia`,`cod_parlamentar`),
  KEY `idx_comissao` (`cod_comissao`) USING BTREE,
  KEY `idx_fim_relatoria` (`tip_fim_relatoria`) USING BTREE,
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE,
  KEY `idx_materia` (`cod_materia`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `reuniao_comissao`
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
  KEY `fk_cod_comissao` (`cod_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_legislativa`
--

CREATE TABLE IF NOT EXISTS `sessao_legislativa` (
  `cod_sessao_leg` int(11) NOT NULL AUTO_INCREMENT,
  `num_sessao_leg` tinyint(4) NOT NULL DEFAULT '0',
  `num_legislatura` tinyint(4) NOT NULL DEFAULT '0',
  `tip_sessao_leg` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_inicio_intervalo` date DEFAULT NULL,
  `dat_fim_intervalo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_sessao_leg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_plenaria`
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
  `num_sessao_plen` int(11) UNSIGNED NOT NULL,
  `dat_fim_sessao` date DEFAULT NULL,
  `url_audio` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url_video` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_sessao_plen`),
  KEY `idx_sessao_leg` (`cod_sessao_leg`) USING BTREE,
  KEY `idx_tip_sessao` (`tip_sessao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessao_plenaria_presenca`
--

CREATE TABLE IF NOT EXISTS `sessao_plenaria_presenca` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE,
  KEY `idx_tip_frequencia` (`tip_frequencia`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `status_tramitacao`
--

CREATE TABLE IF NOT EXISTS `status_tramitacao` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `status_tramitacao_administrativo`
--

CREATE TABLE IF NOT EXISTS `status_tramitacao_administrativo` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subemenda`
--

CREATE TABLE IF NOT EXISTS `subemenda` (
  `cod_subemenda` int(11) NOT NULL AUTO_INCREMENT,
  `tip_subemenda` int(11) NOT NULL,
  `num_subemenda` int(11) NOT NULL,
  `cod_emenda` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_subemenda`),
  UNIQUE KEY `idx_numsub_emenda` (`num_subemenda`,`cod_emenda`,`ind_excluido`),
  UNIQUE KEY `idx_sub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_emenda` (`cod_emenda`),
  KEY `idx_tip_subemenda` (`tip_subemenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `substitutivo`
--

CREATE TABLE IF NOT EXISTS `substitutivo` (
  `cod_substitutivo` int(11) NOT NULL AUTO_INCREMENT,
  `num_substitutivo` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_substitutivo`),
  UNIQUE KEY `idx_numsub_materia` (`num_substitutivo`,`cod_materia`,`ind_excluido`),
  KEY `idx_cod_autor` (`cod_autor`),
  KEY `idx_cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_afastamento`
--

CREATE TABLE IF NOT EXISTS `tipo_afastamento` (
  `tip_afastamento` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_afastamento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_afastamento` tinyint(4) NOT NULL,
  `ind_fim_mandato` tinyint(4) NOT NULL,
  `des_dispositivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_afastamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_autor`
--

CREATE TABLE IF NOT EXISTS `tipo_autor` (
  `tip_autor` tinyint(4) NOT NULL,
  `des_tipo_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_proposicao` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_comissao`
--

CREATE TABLE IF NOT EXISTS `tipo_comissao` (
  `tip_comissao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_comissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_natureza_comissao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_dispositivo_regimental` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_dependente`
--

CREATE TABLE IF NOT EXISTS `tipo_dependente` (
  `tip_dependente` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_tipo_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_dependente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_documento`
--

CREATE TABLE IF NOT EXISTS `tipo_documento` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_documento_administrativo`
--

CREATE TABLE IF NOT EXISTS `tipo_documento_administrativo` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_documento` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_publico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_emenda`
--

CREATE TABLE IF NOT EXISTS `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_expediente`
--

CREATE TABLE IF NOT EXISTS `tipo_expediente` (
  `cod_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `nom_expediente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  PRIMARY KEY (`cod_expediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_fim_relatoria`
--

CREATE TABLE IF NOT EXISTS `tipo_fim_relatoria` (
  `tip_fim_relatoria` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_fim_relatoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_fim_relatoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_instituicao`
--

CREATE TABLE IF NOT EXISTS `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_materia_legislativa`
--

CREATE TABLE IF NOT EXISTS `tipo_materia_legislativa` (
  `tip_materia` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_materia` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_natureza` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_norma_juridica`
--

CREATE TABLE IF NOT EXISTS `tipo_norma_juridica` (
  `tip_norma` tinyint(4) NOT NULL AUTO_INCREMENT,
  `voc_lexml` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_norma` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_norma` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_proposicao`
--

CREATE TABLE IF NOT EXISTS `tipo_proposicao` (
  `tip_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_proposicao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_mat_ou_doc` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_mat_ou_doc` int(11) NOT NULL,
  `nom_modelo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_proposicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_resultado_votacao`
--

CREATE TABLE IF NOT EXISTS `tipo_resultado_votacao` (
  `tip_resultado_votacao` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom_resultado` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  PRIMARY KEY (`tip_resultado_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_sessao_plenaria`
--

CREATE TABLE IF NOT EXISTS `tipo_sessao_plenaria` (
  `tip_sessao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_sessao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_minimo` int(11) NOT NULL,
  PRIMARY KEY (`tip_sessao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_materia`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_materia` (
  `tip_situacao_materia` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_militar`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_militar` (
  `tip_situacao_militar` tinyint(4) NOT NULL,
  `des_tipo_situacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_situacao_militar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_situacao_norma`
--

CREATE TABLE IF NOT EXISTS `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_vinculo_norma`
--

CREATE TABLE IF NOT EXISTS `tipo_vinculo_norma` (
  `cod_tip_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tip_vinculo`),
  UNIQUE KEY `tip_vinculo` (`tipo_vinculo`),
  UNIQUE KEY `idx_vinculo` (`tipo_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`),
  KEY `tip_situacao` (`tip_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_votacao`
--

CREATE TABLE IF NOT EXISTS `tipo_votacao` (
  `tip_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_votacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tramitacao`
--

CREATE TABLE IF NOT EXISTS `tramitacao` (
  `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_status` int(11) DEFAULT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_tramitacao` date DEFAULT NULL,
  `cod_unid_tram_local` int(11) DEFAULT NULL,
  `cod_usuario_local` int(11) DEFAULT NULL,
  `dat_encaminha` datetime DEFAULT NULL,
  `cod_unid_tram_dest` int(11) DEFAULT NULL,
  `cod_usuario_dest` int(11) DEFAULT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `ind_ult_tramitacao` tinyint(4) NOT NULL,
  `ind_urgencia` tinyint(4) NOT NULL,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_tramitacao` text COLLATE utf8_unicode_ci,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tramitacao`),
  KEY `idx_tramit_ultmat` (`ind_excluido`,`ind_ult_tramitacao`,`dat_tramitacao`,`cod_materia`),
  KEY `cod_usuario_local` (`cod_usuario_local`),
  KEY `cod_usuario_dest` (`cod_usuario_dest`),
  KEY `idx_unid_tram_local` (`cod_unid_tram_local`) USING BTREE,
  KEY `idx_status` (`cod_status`) USING BTREE,
  KEY `idx_materia` (`cod_materia`) USING BTREE,
  KEY `idx_unid_tram_dest` (`cod_unid_tram_dest`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tramitacao_administrativo`
--

CREATE TABLE IF NOT EXISTS `tramitacao_administrativo` (
  `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL DEFAULT '0',
  `dat_tramitacao` date DEFAULT NULL,
  `cod_unid_tram_local` int(11) DEFAULT NULL,
  `cod_usuario_local` int(11) DEFAULT NULL,
  `dat_encaminha` datetime DEFAULT NULL,
  `cod_unid_tram_dest` int(11) DEFAULT NULL,
  `cod_usuario_dest` int(11) DEFAULT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `cod_status` int(11) DEFAULT NULL,
  `ind_ult_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_tramitacao` text COLLATE utf8_unicode_ci,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_tramitacao`),
  KEY `tramitacao_ind1` (`ind_ult_tramitacao`),
  KEY `cod_usuario_local` (`cod_usuario_local`),
  KEY `cod_usuario_dest` (`cod_usuario_dest`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `turno_discussao`
--

CREATE TABLE IF NOT EXISTS `turno_discussao` (
  `cod_turno` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_turno` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_turno`),
  UNIQUE KEY `idx_unique_key` (`cod_turno`,`sgl_turno`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `unidade_tramitacao`
--

CREATE TABLE IF NOT EXISTS `unidade_tramitacao` (
  `cod_unid_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_orgao` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `unid_dest_permitidas` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status_permitidos` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_unid_tramitacao`),
  KEY `idx_unidtramit_orgao` (`ind_excluido`,`cod_orgao`),
  KEY `idx_unidtramit_comissao` (`ind_excluido`,`cod_comissao`),
  KEY `idx_unidtramit_parlamentar` (`ind_excluido`,`cod_parlamentar`),
  KEY `idx_cod_ordao` (`cod_orgao`) USING BTREE,
  KEY `idx_cod_comissao` (`cod_comissao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `cod_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `col_username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci NOT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade_resid` int(11) DEFAULT NULL,
  `num_cep_resid` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_resid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_celular` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nom_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_comercial` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_ramal` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_usuario`),
  KEY `idx_col_username` (`col_username`),
  KEY `idx_cod_localidade` (`cod_localidade_resid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario_unid_tram`
--

CREATE TABLE IF NOT EXISTS `usuario_unid_tram` (
  `cod_usuario` int(11) NOT NULL,
  `cod_unid_tramitacao` int(11) NOT NULL,
  `ind_responsavel` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  UNIQUE KEY `PRIMARY_KEY` (`cod_usuario`,`cod_unid_tramitacao`),
  KEY `idx_usuario` (`cod_usuario`),
  KEY `idx_unid_tramitacao` (`cod_unid_tramitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `vinculo_norma_juridica`
--

CREATE TABLE IF NOT EXISTS `vinculo_norma_juridica` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma_referente` int(11) NOT NULL,
  `cod_norma_referida` int(11) NOT NULL,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao_vinculo` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `idx_vnj_norma_referente` (`cod_norma_referente`,`ind_excluido`,`cod_norma_referida`),
  KEY `idx_vnj_norma_referida` (`cod_norma_referida`,`ind_excluido`,`cod_norma_referente`),
  KEY `tip_vinculo` (`tip_vinculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Estrutura da tabela `visita`
--

CREATE TABLE IF NOT EXISTS `visita` (
  `cod_visita` int(11) NOT NULL AUTO_INCREMENT,
  `cod_pessoa` int(11) NOT NULL,
  `dat_entrada` datetime NOT NULL,
  `cod_funcionario` int(11) NOT NULL,
  `num_cracha` int(11) DEFAULT NULL,
  `dat_saida` datetime DEFAULT NULL,
  `txt_atendimento` text COLLATE utf8_unicode_ci,
  `des_situacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_solucao` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_visita`),
  KEY `cod_funcionario` (`cod_funcionario`),
  KEY `cod_pessoa` (`cod_pessoa`) USING BTREE,
  KEY `dat_entrada` (`dat_entrada`),
  KEY `des_situacao` (`des_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `autor`
--
ALTER TABLE `autor` ADD FULLTEXT KEY `nom_autor` (`nom_autor`);

--
-- Indexes for table `bancada`
--
ALTER TABLE `bancada` ADD FULLTEXT KEY `nom_bancada` (`nom_bancada`);

--
-- Indexes for table `comissao`
--
ALTER TABLE `comissao` ADD FULLTEXT KEY `nom_comissao` (`nom_comissao`);

--
-- Indexes for table `documento_acessorio`
--
ALTER TABLE `documento_acessorio` ADD FULLTEXT KEY `txt_indexacao` (`txt_indexacao`);

--
-- Indexes for table `documento_acessorio_administrativo`
--
ALTER TABLE `documento_acessorio_administrativo` ADD FULLTEXT KEY `txt_indexacao` (`txt_indexacao`);

--
-- Indexes for table `documento_administrativo`
--
ALTER TABLE `documento_administrativo` ADD FULLTEXT KEY `idx_busca_documento` (`txt_assunto`,`txt_observacao`);
ALTER TABLE `documento_administrativo` ADD FULLTEXT KEY `idx_txt_interessado` (`txt_interessado`);

--
-- Indexes for table `emenda`
--
ALTER TABLE `emenda` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);

--
-- Indexes for table `instituicao`
--
ALTER TABLE `instituicao` ADD FULLTEXT KEY `idx_nom_instituicao` (`nom_instituicao`);
ALTER TABLE `instituicao` ADD FULLTEXT KEY `idx_nom_responsavel` (`nom_responsavel`);

--
-- Indexes for table `logradouro`
--
ALTER TABLE `logradouro` ADD FULLTEXT KEY `nom_logradouro` (`nom_logradouro`);

--
-- Indexes for table `materia_legislativa`
--
ALTER TABLE `materia_legislativa` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_indexacao`,`txt_observacao`);

--
-- Indexes for table `norma_juridica`
--
ALTER TABLE `norma_juridica` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`);

--
-- Indexes for table `parlamentar`
--
ALTER TABLE `parlamentar` ADD FULLTEXT KEY `nom_completo` (`nom_completo`);
ALTER TABLE `parlamentar` ADD FULLTEXT KEY `nom_parlamentar` (`nom_parlamentar`);

--
-- Indexes for table `pessoa`
--
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_pessoa` (`nom_pessoa`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_conjuge` (`nom_conjuge`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `idx_busca` (`doc_identidade`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `end_residencial` (`end_residencial`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `doc_identidade` (`doc_identidade`);

--
-- Indexes for table `protocolo`
--
ALTER TABLE `protocolo` ADD FULLTEXT KEY `txt_interessado` (`txt_interessado`);
ALTER TABLE `protocolo` ADD FULLTEXT KEY `idx_busca_protocolo` (`txt_assunto_ementa`,`txt_observacao`);

--
-- Indexes for table `subemenda`
--
ALTER TABLE `subemenda` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);

--
-- Indexes for table `substitutivo`
--
ALTER TABLE `substitutivo` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
