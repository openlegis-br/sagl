SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `acomp_materia` (
  `cod_cadastro` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_hash` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `afastamento` (
  `cod_afastamento` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_mandato` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `tip_afastamento` tinyint(4) NOT NULL,
  `dat_inicio_afastamento` date NOT NULL,
  `dat_fim_afastamento` date DEFAULT NULL,
  `cod_parlamentar_suplente` int(11) NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `anexada` (
  `cod_materia_principal` int(11) NOT NULL,
  `cod_materia_anexada` int(11) NOT NULL,
  `dat_anexacao` date NOT NULL,
  `dat_desanexacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `anexo_norma` (
  `cod_anexo` int(11) NOT NULL,
  `cod_norma` int(11) NOT NULL,
  `txt_descricao` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_armario` (
  `cod_armario` int(11) NOT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_armario` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_corredor` (
  `cod_corredor` int(11) NOT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_corredor` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_item` (
  `cod_item` int(11) NOT NULL,
  `cod_recipiente` int(11) NOT NULL,
  `tip_suporte` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_norma` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `cod_protocolo` int(7) UNSIGNED ZEROFILL DEFAULT NULL,
  `des_item` text COLLATE utf8_unicode_ci,
  `dat_arquivamento` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_prateleira` (
  `cod_prateleira` int(11) NOT NULL,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_unidade` int(11) NOT NULL,
  `nom_prateleira` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_recipiente` (
  `cod_recipiente` int(11) NOT NULL,
  `tip_recipiente` int(11) NOT NULL,
  `num_recipiente` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `tip_tit_documental` int(11) NOT NULL,
  `ano_recipiente` smallint(6) NOT NULL,
  `dat_recipiente` date NOT NULL,
  `cod_corredor` int(11) DEFAULT NULL,
  `cod_armario` int(11) DEFAULT NULL,
  `cod_prateleira` int(11) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_tipo_recipiente` (
  `tip_recipiente` int(11) NOT NULL,
  `des_tipo_recipiente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `arquivo_unidade` (
  `cod_unidade` int(11) NOT NULL,
  `tip_extensao_atuacao` int(11) NOT NULL,
  `tip_estagio_evolucao` int(11) NOT NULL,
  `nom_unidade` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `txt_localizacao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `assessor_parlamentar` (
  `cod_assessor` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `assunto_norma` (
  `cod_assunto` int(4) NOT NULL,
  `des_assunto` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estendida` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `autor` (
  `cod_autor` int(11) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_bancada` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `tip_autor` tinyint(4) NOT NULL,
  `nom_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `col_username` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `autoria` (
  `cod_autor` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_primeiro_autor` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `bancada` (
  `cod_bancada` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `nom_bancada` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `cargo_comissao` (
  `cod_cargo` tinyint(4) NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `cargo_executivo` (
  `cod_cargo` tinyint(4) NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `cargo_mesa` (
  `cod_cargo` tinyint(4) NOT NULL,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `categoria_instituicao` (
  `tip_instituicao` int(11) NOT NULL,
  `cod_categoria` int(11) NOT NULL,
  `des_categoria` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `coautoria_proposicao` (
  `cod_proposicao` int(11) NOT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_aderido` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `coligacao` (
  `cod_coligacao` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `nom_coligacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_votos_coligacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `comissao` (
  `cod_comissao` int(11) NOT NULL,
  `tip_comissao` tinyint(4) NOT NULL,
  `nom_comissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `composicao_bancada` (
  `cod_comp_bancada` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_bancada` int(11) NOT NULL,
  `cod_periodo_comp` int(11) DEFAULT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `composicao_coligacao` (
  `cod_partido` int(11) NOT NULL,
  `cod_coligacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `composicao_comissao` (
  `cod_comp_comissao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `cod_periodo_comp` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_titular` tinyint(4) NOT NULL,
  `dat_designacao` date NOT NULL,
  `dat_desligamento` date DEFAULT NULL,
  `des_motivo_desligamento` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `obs_composicao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `composicao_executivo` (
  `cod_composicao` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `nom_completo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_partido` int(11) DEFAULT NULL,
  `dat_inicio_mandato` date DEFAULT NULL,
  `dat_fim_mandato` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `composicao_mesa` (
  `cod_parlamentar` int(11) NOT NULL,
  `cod_sessao_leg` int(11) DEFAULT NULL,
  `cod_periodo_comp` int(11) NOT NULL,
  `cod_cargo` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `dependente` (
  `cod_dependente` int(11) NOT NULL,
  `tip_dependente` tinyint(4) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `nom_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_dependente` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `num_cpf` varchar(14) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_rg` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `despacho_inicial` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) UNSIGNED NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `destinatario_oficio` (
  `cod_destinatario` int(11) NOT NULL,
  `cod_documento` int(11) NOT NULL,
  `cod_instituicao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `documento_acessorio` (
  `cod_documento` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `tip_documento` int(11) NOT NULL,
  `nom_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_documento` date DEFAULT NULL,
  `nom_autor_documento` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `documento_acessorio_administrativo` (
  `cod_documento_acessorio` int(11) NOT NULL,
  `cod_documento` int(11) NOT NULL DEFAULT '0',
  `tip_documento` int(11) NOT NULL DEFAULT '0',
  `nom_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_arquivo` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_documento` date DEFAULT NULL,
  `nom_autor_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_indexacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `documento_administrativo` (
  `cod_documento` int(11) NOT NULL,
  `tip_documento` int(11) NOT NULL,
  `num_documento` int(11) NOT NULL,
  `ano_documento` smallint(6) NOT NULL DEFAULT '0',
  `dat_documento` date NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `txt_interessado` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `cod_entidade` int(11) DEFAULT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `dat_fim_prazo` date DEFAULT NULL,
  `ind_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `txt_assunto` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `cod_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `documento_administrativo_materia` (
  `cod_vinculo` int(11) NOT NULL,
  `cod_documento` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `documento_administrativo_vinculado` (
  `cod_vinculo` int(11) NOT NULL,
  `cod_documento_vinculante` int(11) NOT NULL,
  `cod_documento_vinculado` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `documento_comissao` (
  `cod_documento` int(11) NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `dat_documento` date NOT NULL,
  `txt_descricao` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `emenda` (
  `cod_emenda` int(11) NOT NULL,
  `tip_emenda` int(11) NOT NULL,
  `num_emenda` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `exc_pauta` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `encerramento_presenca` (
  `cod_presenca_encerramento` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `expediente_discussao` (
  `cod_ordem` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `expediente_materia` (
  `cod_ordem` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) DEFAULT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_votacao` int(11) NOT NULL,
  `tip_quorum` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `expediente_presenca` (
  `cod_presenca_expediente` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `expediente_sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_expediente` int(11) NOT NULL,
  `txt_expediente` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `filiacao` (
  `dat_filiacao` date NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_partido` int(11) NOT NULL,
  `dat_desfiliacao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `funcionario` (
  `cod_funcionario` int(11) NOT NULL,
  `nom_funcionario` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cod_usuario` int(11) DEFAULT NULL,
  `des_cargo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_cadastro` date NOT NULL,
  `ind_ativo` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `gabinete_atendimento` (
  `cod_atendimento` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_eleitor` int(11) NOT NULL,
  `dat_atendimento` date NOT NULL,
  `txt_assunto` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `dat_resultado` date DEFAULT NULL,
  `txt_resultado` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_atendente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_status` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `gabinete_eleitor` (
  `cod_eleitor` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `dat_cadastro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nom_eleitor` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_eleitor` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `des_estado_civil` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `doc_identidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cpf` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_classe` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_escolaridade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tit_eleitor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_residencial` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_bairro` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_localidade` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_uf` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_celular` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_conjuge` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_dependentes` tinytext COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `des_local_trabalho` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_atualizacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `instituicao` (
  `cod_instituicao` int(11) NOT NULL,
  `tip_instituicao` int(11) NOT NULL,
  `cod_categoria` int(11) NOT NULL,
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
  `txt_ip_alteracao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `legislatura` (
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_eleicao` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `lexml_registro_provedor` (
  `cod_provedor` int(11) NOT NULL,
  `id_provedor` int(11) NOT NULL,
  `nom_provedor` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_provedor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adm_email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_responsavel` int(11) DEFAULT NULL,
  `xml_provedor` longtext COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `lexml_registro_publicador` (
  `cod_publicador` int(11) NOT NULL,
  `id_publicador` int(11) NOT NULL,
  `nom_publicador` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adm_email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sigla` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_responsavel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_responsavel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `liderancas_partidarias` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_partido` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `localidade` (
  `cod_localidade` int(11) NOT NULL DEFAULT '0',
  `nom_localidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_localidade_pesq` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_localidade` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_uf` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_regiao` char(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `logradouro` (
  `cod_logradouro` int(11) NOT NULL,
  `nom_logradouro` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `cod_norma` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `mandato` (
  `cod_mandato` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `materia_apresentada_sessao` (
  `cod_ordem` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_documento` int(11) DEFAULT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `materia_legislativa` (
  `cod_materia` int(11) NOT NULL,
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
  `cod_materia_principal` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `mesa_sessao_plenaria` (
  `cod_cargo` tinyint(4) NOT NULL,
  `cod_sessao_leg` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `ind_excluido` tinyint(4) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `nivel_instrucao` (
  `cod_nivel_instrucao` tinyint(4) NOT NULL,
  `des_nivel_instrucao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `norma_juridica` (
  `cod_norma` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `numeracao` (
  `cod_materia` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `tip_materia` int(11) NOT NULL,
  `num_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ano_materia` smallint(6) NOT NULL,
  `dat_materia` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `oradores` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `oradores_expediente` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `ordem_dia` (
  `cod_ordem` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) DEFAULT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_turno` int(11) DEFAULT NULL,
  `tip_votacao` int(11) NOT NULL,
  `tip_quorum` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `ordem_dia_discussao` (
  `cod_ordem` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `ordem_dia_presenca` (
  `cod_presenca_ordem_dia` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL DEFAULT '0',
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'P',
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_ordem` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `orgao` (
  `cod_orgao` int(11) NOT NULL,
  `nom_orgao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_orgao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `end_orgao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_orgao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `origem` (
  `cod_origem` int(11) NOT NULL,
  `sgl_origem` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_origem` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `parecer` (
  `cod_relatoria` int(11) NOT NULL,
  `num_parecer` smallint(6) DEFAULT NULL,
  `ano_parecer` smallint(6) DEFAULT NULL,
  `cod_materia` int(11) NOT NULL,
  `tip_conclusao` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `parlamentar` (
  `cod_parlamentar` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `partido` (
  `cod_partido` int(11) NOT NULL,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `periodo_comp_bancada` (
  `cod_periodo_comp` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `periodo_comp_comissao` (
  `cod_periodo_comp` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `periodo_comp_mesa` (
  `cod_periodo_comp` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `pessoa` (
  `cod_pessoa` int(11) NOT NULL,
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
  `txt_complemento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `num_cep` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nom_cidade` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sgl_uf` varchar(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tempo_residencia` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_telefone` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_celular` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_local_trabalho` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `dat_atualizacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `proposicao` (
  `cod_proposicao` int(11) NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `tip_proposicao` int(11) NOT NULL,
  `dat_envio` datetime DEFAULT NULL,
  `dat_recebimento` datetime DEFAULT NULL,
  `txt_descricao` varchar(400) COLLATE utf8_unicode_ci NOT NULL,
  `cod_mat_ou_doc` int(11) DEFAULT NULL,
  `cod_emenda` int(11) DEFAULT NULL,
  `cod_substitutivo` int(11) DEFAULT NULL,
  `dat_devolucao` datetime DEFAULT NULL,
  `txt_justif_devolucao` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `protocolo` (
  `cod_protocolo` int(7) UNSIGNED ZEROFILL NOT NULL,
  `num_protocolo` int(7) UNSIGNED ZEROFILL DEFAULT NULL,
  `ano_protocolo` smallint(6) NOT NULL,
  `dat_protocolo` date NOT NULL,
  `hor_protocolo` time NOT NULL DEFAULT '00:00:00',
  `dat_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tip_protocolo` int(4) NOT NULL,
  `tip_processo` int(4) DEFAULT NULL,
  `txt_interessado` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) DEFAULT NULL,
  `cod_entidade` int(11) DEFAULT NULL,
  `txt_assunto_ementa` text COLLATE utf8_unicode_ci,
  `tip_documento` int(11) DEFAULT NULL,
  `tip_materia` int(11) DEFAULT NULL,
  `num_paginas` int(6) DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_anulado` tinyint(4) NOT NULL DEFAULT '0',
  `txt_user_protocolo` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_user_anulacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_ip_anulacao` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_just_anulacao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp_anulacao` datetime DEFAULT NULL,
  `codigo_acesso` varchar(18) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `quorum_votacao` (
  `cod_quorum` int(11) NOT NULL,
  `des_quorum` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `txt_formula` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `regime_tramitacao` (
  `cod_regime_tramitacao` tinyint(4) NOT NULL,
  `des_regime_tramitacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `registro_votacao` (
  `cod_votacao` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `registro_votacao_parlamentar` (
  `cod_votacao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL,
  `vot_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `relatoria` (
  `cod_relatoria` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_fim_relatoria` tinyint(11) DEFAULT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `dat_desig_relator` date NOT NULL,
  `dat_destit_relator` date DEFAULT NULL,
  `tip_apresentacao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_parecer` int(6) DEFAULT NULL,
  `ano_parecer` smallint(6) DEFAULT NULL,
  `txt_parecer` text COLLATE utf8_unicode_ci,
  `tip_conclusao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `reuniao_comissao` (
  `cod_reuniao` int(11) NOT NULL,
  `cod_comissao` int(11) NOT NULL,
  `num_reuniao` int(11) NOT NULL,
  `dat_inicio_reuniao` date NOT NULL,
  `hr_inicio_reuniao` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `sessao_legislativa` (
  `cod_sessao_leg` int(11) NOT NULL,
  `num_legislatura` int(11) NOT NULL,
  `num_sessao_leg` tinyint(4) NOT NULL,
  `tip_sessao_leg` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_inicio_intervalo` date DEFAULT NULL,
  `dat_fim_intervalo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
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
  `url_fotos` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url_audio` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url_video` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `sessao_plenaria_painel` (
  `cod_item` int(11) NOT NULL,
  `tip_item` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `nom_fase` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_ordem` int(11) NOT NULL,
  `txt_exibicao` text COLLATE utf8_unicode_ci NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `txt_autoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_turno` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_extrapauta` tinyint(4) DEFAULT '0',
  `ind_exibicao` tinyint(4) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `sessao_plenaria_presenca` (
  `cod_presenca_sessao` int(11) NOT NULL,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `tip_frequencia` char(1) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'P',
  `txt_justif_ausencia` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_sessao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `status_tramitacao` (
  `cod_status` int(11) NOT NULL,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `status_tramitacao_administrativo` (
  `cod_status` int(11) NOT NULL,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `subemenda` (
  `cod_subemenda` int(11) NOT NULL,
  `tip_subemenda` int(11) NOT NULL,
  `num_subemenda` int(11) NOT NULL,
  `cod_emenda` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `substitutivo` (
  `cod_substitutivo` int(11) NOT NULL,
  `num_substitutivo` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `dat_apresentacao` date DEFAULT NULL,
  `txt_ementa` text COLLATE utf8_unicode_ci,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `cod_autor` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_afastamento` (
  `tip_afastamento` tinyint(4) NOT NULL,
  `des_afastamento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_afastamento` tinyint(4) NOT NULL,
  `ind_fim_mandato` tinyint(4) NOT NULL,
  `des_dispositivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_autor` (
  `tip_autor` tinyint(4) NOT NULL,
  `des_tipo_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_proposicao` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_comissao` (
  `tip_comissao` tinyint(4) NOT NULL,
  `nom_tipo_comissao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_natureza_comissao` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_comissao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_dispositivo_regimental` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_dependente` (
  `tip_dependente` tinyint(4) NOT NULL,
  `des_tipo_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_documento` (
  `tip_documento` int(11) NOT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_documento_administrativo` (
  `tip_documento` int(11) NOT NULL,
  `sgl_tipo_documento` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_publico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_expediente` (
  `cod_expediente` int(11) NOT NULL,
  `nom_expediente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_fim_relatoria` (
  `tip_fim_relatoria` tinyint(4) NOT NULL,
  `des_fim_relatoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_instituicao` (
  `tip_instituicao` int(11) NOT NULL,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_materia_legislativa` (
  `tip_materia` int(11) NOT NULL,
  `sgl_tipo_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_materia` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_natureza` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_num_automatica` tinyint(4) NOT NULL DEFAULT '0',
  `quorum_minimo_votacao` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_norma_juridica` (
  `tip_norma` tinyint(4) NOT NULL,
  `voc_lexml` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_norma` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_norma` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_proposicao` (
  `tip_proposicao` int(11) NOT NULL,
  `des_tipo_proposicao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_mat_ou_doc` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_mat_ou_doc` int(11) NOT NULL,
  `nom_modelo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_resultado_votacao` (
  `tip_resultado_votacao` int(10) UNSIGNED NOT NULL,
  `nom_resultado` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_sessao_plenaria` (
  `tip_sessao` tinyint(4) NOT NULL,
  `nom_sessao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_minimo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tipo_situacao_materia` (
  `tip_situacao_materia` int(11) NOT NULL,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_situacao_militar` (
  `tip_situacao_militar` tinyint(4) NOT NULL,
  `des_tipo_situacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_vinculo_norma` (
  `cod_tip_vinculo` int(11) NOT NULL,
  `tipo_vinculo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tip_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tipo_votacao` (
  `tip_votacao` int(11) NOT NULL,
  `des_tipo_votacao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tramitacao` (
  `cod_tramitacao` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `tramitacao_administrativo` (
  `cod_tramitacao` int(11) NOT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

CREATE TABLE `turno_discussao` (
  `cod_turno` int(11) NOT NULL,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_turno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `unidade_tramitacao` (
  `cod_unid_tramitacao` int(11) NOT NULL,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_orgao` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `ind_leg` tinyint(4) DEFAULT '1',
  `unid_dest_permitidas` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status_permitidos` varchar(400) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_adm` tinyint(4) DEFAULT '0',
  `status_adm_permitidos` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `usuario` (
  `cod_usuario` int(11) NOT NULL,
  `col_username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `roles` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `usuario_unid_tram` (
  `cod_usuario` int(11) NOT NULL,
  `cod_unid_tramitacao` int(11) NOT NULL,
  `ind_responsavel` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `vinculo_norma_juridica` (
  `cod_vinculo` int(11) NOT NULL,
  `cod_norma_referente` int(11) NOT NULL,
  `cod_norma_referida` int(11) DEFAULT NULL,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao_vinculo` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` char(1) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;

CREATE TABLE `visita` (
  `cod_visita` int(11) NOT NULL,
  `cod_pessoa` int(11) NOT NULL,
  `dat_entrada` datetime NOT NULL,
  `cod_funcionario` int(11) NOT NULL,
  `num_cracha` int(11) DEFAULT NULL,
  `dat_saida` datetime DEFAULT NULL,
  `txt_atendimento` text COLLATE utf8_unicode_ci,
  `des_situacao` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_solucao` date DEFAULT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


ALTER TABLE `acomp_materia`
  ADD PRIMARY KEY (`cod_cadastro`),
  ADD UNIQUE KEY `fk_{CCECA63D-5992-437B-BCD3-D7C98DA3E926}` (`cod_materia`,`end_email`),
  ADD KEY `cod_materia` (`cod_materia`);

ALTER TABLE `afastamento`
  ADD PRIMARY KEY (`cod_afastamento`),
  ADD KEY `idx_parlamentar_mandato` (`cod_parlamentar`,`num_legislatura`),
  ADD KEY `idx_afastamento_datas` (`cod_parlamentar`,`dat_inicio_afastamento`,`dat_fim_afastamento`),
  ADD KEY `idx_tip_afastamento` (`tip_afastamento`),
  ADD KEY `idx__parlamentar_suplente` (`cod_parlamentar_suplente`,`num_legislatura`),
  ADD KEY `cod_mandato` (`cod_mandato`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `num_legislatura` (`num_legislatura`),
  ADD KEY `cod_parlamentar_suplente` (`cod_parlamentar_suplente`);

ALTER TABLE `anexada`
  ADD PRIMARY KEY (`cod_materia_principal`,`cod_materia_anexada`),
  ADD KEY `idx_materia_anexada` (`cod_materia_anexada`),
  ADD KEY `idx_materia_principal` (`cod_materia_principal`);

ALTER TABLE `anexo_norma`
  ADD PRIMARY KEY (`cod_anexo`),
  ADD KEY `cod_norma` (`cod_norma`);

ALTER TABLE `arquivo_armario`
  ADD PRIMARY KEY (`cod_armario`),
  ADD KEY `cod_corredor` (`cod_corredor`),
  ADD KEY `cod_unidade` (`cod_unidade`);

ALTER TABLE `arquivo_corredor`
  ADD PRIMARY KEY (`cod_corredor`),
  ADD KEY `cod_unidade` (`cod_unidade`);

ALTER TABLE `arquivo_item`
  ADD PRIMARY KEY (`cod_item`),
  ADD KEY `cod_recipiente` (`cod_recipiente`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `cod_norma` (`cod_norma`),
  ADD KEY `cod_documento` (`cod_documento`),
  ADD KEY `cod_protocolo` (`cod_protocolo`),
  ADD KEY `tip_suporte` (`tip_suporte`);

ALTER TABLE `arquivo_prateleira`
  ADD PRIMARY KEY (`cod_prateleira`),
  ADD KEY `cod_armario` (`cod_armario`),
  ADD KEY `cod_corredor` (`cod_corredor`),
  ADD KEY `cod_unidade` (`cod_unidade`);

ALTER TABLE `arquivo_recipiente`
  ADD PRIMARY KEY (`cod_recipiente`),
  ADD UNIQUE KEY `num_tipo_recipiente` (`num_recipiente`,`tip_recipiente`,`ano_recipiente`,`ind_excluido`),
  ADD KEY `tip_recipiente` (`tip_recipiente`),
  ADD KEY `tip_tit_documental` (`tip_tit_documental`),
  ADD KEY `cod_armario` (`cod_armario`),
  ADD KEY `cod_corredor` (`cod_corredor`),
  ADD KEY `cod_prateleira` (`cod_prateleira`);

ALTER TABLE `arquivo_tipo_recipiente`
  ADD PRIMARY KEY (`tip_recipiente`);

ALTER TABLE `arquivo_tipo_suporte`
  ADD PRIMARY KEY (`tip_suporte`);

ALTER TABLE `arquivo_tipo_tit_documental`
  ADD PRIMARY KEY (`tip_tit_documental`);

ALTER TABLE `arquivo_unidade`
  ADD PRIMARY KEY (`cod_unidade`);

ALTER TABLE `assessor_parlamentar`
  ADD PRIMARY KEY (`cod_assessor`),
  ADD UNIQUE KEY `assessor_parlamentar` (`cod_assessor`,`cod_parlamentar`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `col_username` (`col_username`);

ALTER TABLE `assunto_norma`
  ADD PRIMARY KEY (`cod_assunto`);

ALTER TABLE `autor`
  ADD PRIMARY KEY (`cod_autor`),
  ADD KEY `idx_tip_autor` (`tip_autor`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`),
  ADD KEY `idx_comissao` (`cod_comissao`),
  ADD KEY `idx_partido` (`cod_partido`),
  ADD KEY `idx_bancada` (`cod_bancada`),
  ADD KEY `col_username` (`col_username`);
ALTER TABLE `autor` ADD FULLTEXT KEY `nom_autor` (`nom_autor`);

ALTER TABLE `autoria`
  ADD PRIMARY KEY (`cod_autor`,`cod_materia`),
  ADD KEY `idx_materia` (`cod_materia`),
  ADD KEY `idx_autor` (`cod_autor`);

ALTER TABLE `bancada`
  ADD PRIMARY KEY (`cod_bancada`),
  ADD KEY `idt_nom_bancada` (`nom_bancada`),
  ADD KEY `num_legislatura` (`num_legislatura`),
  ADD KEY `cod_partido` (`cod_partido`);
ALTER TABLE `bancada` ADD FULLTEXT KEY `nom_bancada` (`nom_bancada`);

ALTER TABLE `cargo_bancada`
  ADD PRIMARY KEY (`cod_cargo`);

ALTER TABLE `cargo_comissao`
  ADD PRIMARY KEY (`cod_cargo`);

ALTER TABLE `cargo_executivo`
  ADD PRIMARY KEY (`cod_cargo`);

ALTER TABLE `cargo_mesa`
  ADD PRIMARY KEY (`cod_cargo`);

ALTER TABLE `categoria_instituicao`
  ADD PRIMARY KEY (`cod_categoria`,`tip_instituicao`) USING BTREE,
  ADD KEY `tip_instituicao` (`tip_instituicao`) USING BTREE;

ALTER TABLE `coautoria_proposicao`
  ADD PRIMARY KEY (`cod_proposicao`,`cod_autor`),
  ADD KEY `idx_proposicao` (`cod_proposicao`),
  ADD KEY `idx_autor` (`cod_autor`);

ALTER TABLE `coligacao`
  ADD PRIMARY KEY (`cod_coligacao`),
  ADD KEY `idx_legislatura` (`num_legislatura`),
  ADD KEY `idx_coligacao_legislatura` (`num_legislatura`,`ind_excluido`);

ALTER TABLE `comissao`
  ADD PRIMARY KEY (`cod_comissao`),
  ADD KEY `idx_comissao_tipo` (`tip_comissao`),
  ADD KEY `idx_comissao_nome` (`nom_comissao`);
ALTER TABLE `comissao` ADD FULLTEXT KEY `nom_comissao` (`nom_comissao`);

ALTER TABLE `composicao_bancada`
  ADD PRIMARY KEY (`cod_comp_bancada`),
  ADD KEY `idx_cargo` (`cod_cargo`),
  ADD KEY `idx_bancada` (`cod_bancada`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_periodo_comp` (`cod_periodo_comp`);

ALTER TABLE `composicao_coligacao`
  ADD PRIMARY KEY (`cod_partido`,`cod_coligacao`),
  ADD KEY `idx_coligacao` (`cod_coligacao`),
  ADD KEY `idx_partido` (`cod_partido`);

ALTER TABLE `composicao_comissao`
  ADD PRIMARY KEY (`cod_comp_comissao`),
  ADD KEY `idx_cargo` (`cod_cargo`),
  ADD KEY `idx_periodo_comp` (`cod_periodo_comp`),
  ADD KEY `idx_comissao` (`cod_comissao`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`);

ALTER TABLE `composicao_executivo`
  ADD PRIMARY KEY (`cod_composicao`),
  ADD KEY `num_legislatura` (`num_legislatura`),
  ADD KEY `cod_cargo` (`cod_cargo`),
  ADD KEY `cod_partido` (`cod_partido`);

ALTER TABLE `composicao_mesa`
  ADD PRIMARY KEY (`cod_parlamentar`,`cod_periodo_comp`,`cod_cargo`),
  ADD KEY `idx_cargo` (`cod_cargo`),
  ADD KEY `idx_periodo_comp` (`cod_periodo_comp`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_sessao_leg` (`cod_sessao_leg`);

ALTER TABLE `dependente`
  ADD PRIMARY KEY (`cod_dependente`),
  ADD KEY `idx_dep_parlam` (`tip_dependente`,`cod_parlamentar`,`ind_excluido`),
  ADD KEY `idx_dependente` (`tip_dependente`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`);

ALTER TABLE `despacho_inicial`
  ADD UNIQUE KEY `idx_unique` (`cod_materia`,`num_ordem`),
  ADD KEY `idx_comissao` (`cod_comissao`),
  ADD KEY `idx_materia` (`cod_materia`),
  ADD KEY `idx_despinic_comissao` (`cod_materia`,`num_ordem`,`cod_comissao`);

ALTER TABLE `destinatario_oficio`
  ADD PRIMARY KEY (`cod_destinatario`),
  ADD KEY `cod_documento` (`cod_documento`),
  ADD KEY `cod_instituicao` (`cod_instituicao`);

ALTER TABLE `documento_acessorio`
  ADD PRIMARY KEY (`cod_documento`),
  ADD KEY `idx_tip_documento` (`tip_documento`),
  ADD KEY `idx_materia` (`cod_materia`);
ALTER TABLE `documento_acessorio` ADD FULLTEXT KEY `idx_ementa` (`txt_ementa`);

ALTER TABLE `documento_acessorio_administrativo`
  ADD PRIMARY KEY (`cod_documento_acessorio`),
  ADD KEY `idx_tip_documento` (`tip_documento`),
  ADD KEY `idx_documento` (`cod_documento`),
  ADD KEY `idx_autor_documento` (`nom_autor_documento`),
  ADD KEY `idx_dat_documento` (`dat_documento`);
ALTER TABLE `documento_acessorio_administrativo` ADD FULLTEXT KEY `idx_assunto` (`txt_assunto`);

ALTER TABLE `documento_administrativo`
  ADD PRIMARY KEY (`cod_documento`),
  ADD KEY `tip_documento` (`tip_documento`,`num_documento`,`ano_documento`),
  ADD KEY `cod_situacao` (`cod_situacao`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `cod_entidade` (`cod_entidade`),
  ADD KEY `cod_autor` (`cod_autor`),
  ADD KEY `ano_documento` (`ano_documento`),
  ADD KEY `dat_documento` (`dat_documento`),
  ADD KEY `num_protocolo` (`num_protocolo`);
ALTER TABLE `documento_administrativo` ADD FULLTEXT KEY `idx_busca_documento` (`txt_assunto`,`txt_observacao`);
ALTER TABLE `documento_administrativo` ADD FULLTEXT KEY `txt_interessado` (`txt_interessado`);

ALTER TABLE `documento_administrativo_materia`
  ADD PRIMARY KEY (`cod_vinculo`),
  ADD KEY `idx_cod_documento` (`cod_documento`),
  ADD KEY `idx_cod_materia` (`cod_materia`);

ALTER TABLE `documento_administrativo_vinculado`
  ADD PRIMARY KEY (`cod_vinculo`),
  ADD UNIQUE KEY `idx_doc_vinculo` (`cod_documento_vinculante`,`cod_documento_vinculado`),
  ADD KEY `idx_doc_vinculado` (`cod_documento_vinculado`) USING BTREE,
  ADD KEY `idx_cod_documento` (`cod_documento_vinculante`) USING BTREE;

ALTER TABLE `documento_comissao`
  ADD PRIMARY KEY (`cod_documento`),
  ADD KEY `cod_comissao` (`cod_comissao`);
ALTER TABLE `documento_comissao` ADD FULLTEXT KEY `txt_descricao` (`txt_descricao`);

ALTER TABLE `emenda`
  ADD PRIMARY KEY (`cod_emenda`),
  ADD KEY `idx_cod_materia` (`cod_materia`),
  ADD KEY `idx_cod_autor` (`cod_autor`),
  ADD KEY `idx_tip_emenda` (`tip_emenda`),
  ADD KEY `idx_emenda` (`cod_emenda`,`tip_emenda`,`cod_materia`) USING BTREE;
ALTER TABLE `emenda` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);

ALTER TABLE `encerramento_presenca`
  ADD PRIMARY KEY (`cod_presenca_encerramento`),
  ADD UNIQUE KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `dat_ordem` (`dat_ordem`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`);

ALTER TABLE `expediente_discussao`
  ADD PRIMARY KEY (`cod_ordem`,`cod_parlamentar`) USING BTREE,
  ADD KEY `cod_ordem` (`cod_ordem`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`);

ALTER TABLE `expediente_materia`
  ADD PRIMARY KEY (`cod_ordem`),
  ADD KEY `idx_exped_datord` (`dat_ordem`,`ind_excluido`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `tip_votacao` (`tip_votacao`),
  ADD KEY `tip_quorum` (`tip_quorum`);

ALTER TABLE `expediente_presenca`
  ADD PRIMARY KEY (`cod_presenca_expediente`),
  ADD UNIQUE KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `dat_ordem` (`dat_ordem`,`ind_excluido`);

ALTER TABLE `expediente_sessao_plenaria`
  ADD PRIMARY KEY (`cod_sessao_plen`,`cod_expediente`),
  ADD KEY `cod_expediente` (`cod_expediente`);

ALTER TABLE `filiacao`
  ADD PRIMARY KEY (`dat_filiacao`,`cod_parlamentar`,`cod_partido`),
  ADD KEY `idx_partido` (`cod_partido`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`);

ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`cod_funcionario`),
  ADD KEY `cod_usuario` (`cod_usuario`);

ALTER TABLE `gabinete_atendimento`
  ADD PRIMARY KEY (`cod_atendimento`),
  ADD KEY `idx_resultado` (`txt_resultado`) USING BTREE,
  ADD KEY `idx_eleitor` (`cod_eleitor`) USING BTREE,
  ADD KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE;
ALTER TABLE `gabinete_atendimento` ADD FULLTEXT KEY `idx_assunto` (`txt_assunto`);

ALTER TABLE `gabinete_eleitor`
  ADD PRIMARY KEY (`cod_eleitor`),
  ADD KEY `sex_eleitor` (`sex_eleitor`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_eleitor` (`nom_eleitor`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `des_profissao` (`des_profissao`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `end_residencial` (`end_residencial`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_localidade` (`nom_localidade`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `des_local_trabalho` (`des_local_trabalho`);
ALTER TABLE `gabinete_eleitor` ADD FULLTEXT KEY `nom_bairro` (`nom_bairro`);

ALTER TABLE `instituicao`
  ADD PRIMARY KEY (`cod_instituicao`),
  ADD KEY `tip_instituicao` (`tip_instituicao`),
  ADD KEY `cod_categoria` (`cod_categoria`),
  ADD KEY `cod_localidade` (`cod_localidade`),
  ADD KEY `dat_insercao` (`dat_insercao`),
  ADD KEY `ind_excluido` (`ind_excluido`),
  ADD KEY `idx_cod_cat` (`tip_instituicao`,`cod_categoria`);
ALTER TABLE `instituicao` ADD FULLTEXT KEY `idx_nom_instituicao` (`nom_instituicao`);
ALTER TABLE `instituicao` ADD FULLTEXT KEY `idx_nom_responsavel` (`nom_responsavel`);

ALTER TABLE `legislacao_citada`
  ADD PRIMARY KEY (`cod_materia`,`cod_norma`),
  ADD KEY `cod_norma` (`cod_norma`),
  ADD KEY `cod_materia` (`cod_materia`);

ALTER TABLE `legislatura`
  ADD PRIMARY KEY (`num_legislatura`),
  ADD KEY `idx_legislatura_datas` (`dat_inicio`,`dat_fim`,`dat_eleicao`,`ind_excluido`);

ALTER TABLE `lexml_registro_provedor`
  ADD PRIMARY KEY (`cod_provedor`);

ALTER TABLE `lexml_registro_publicador`
  ADD PRIMARY KEY (`cod_publicador`);

ALTER TABLE `liderancas_partidarias`
  ADD PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  ADD UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_partido` (`cod_partido`);

ALTER TABLE `localidade`
  ADD PRIMARY KEY (`cod_localidade`),
  ADD KEY `nom_localidade` (`nom_localidade`),
  ADD KEY `sgl_uf` (`sgl_uf`),
  ADD KEY `tip_localidade` (`tip_localidade`);
ALTER TABLE `localidade` ADD FULLTEXT KEY `nom_localidade_pesq` (`nom_localidade_pesq`);

ALTER TABLE `logradouro`
  ADD PRIMARY KEY (`cod_logradouro`),
  ADD KEY `num_cep` (`num_cep`),
  ADD KEY `cod_localidade` (`cod_localidade`),
  ADD KEY `cod_norma` (`cod_norma`);
ALTER TABLE `logradouro` ADD FULLTEXT KEY `nom_logradouro` (`nom_logradouro`);

ALTER TABLE `mandato`
  ADD PRIMARY KEY (`cod_mandato`),
  ADD KEY `idx_coligacao` (`cod_coligacao`),
  ADD KEY `idx_parlamentar` (`cod_parlamentar`),
  ADD KEY `idx_afastamento` (`tip_afastamento`),
  ADD KEY `idx_mandato_legislatura` (`num_legislatura`,`cod_parlamentar`,`ind_excluido`),
  ADD KEY `idx_legislatura` (`num_legislatura`),
  ADD KEY `tip_causa_fim_mandato` (`tip_causa_fim_mandato`);

ALTER TABLE `materia_apresentada_sessao`
  ADD PRIMARY KEY (`cod_ordem`),
  ADD KEY `fk_cod_materia` (`cod_materia`),
  ADD KEY `idx_apres_datord` (`dat_ordem`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_documento` (`cod_documento`),
  ADD KEY `cod_materia` (`cod_materia`);

ALTER TABLE `materia_legislativa`
  ADD PRIMARY KEY (`cod_materia`),
  ADD KEY `cod_local_origem_externa` (`cod_local_origem_externa`),
  ADD KEY `tip_origem_externa` (`tip_origem_externa`),
  ADD KEY `cod_regime_tramitacao` (`cod_regime_tramitacao`),
  ADD KEY `idx_dat_apresentacao` (`dat_apresentacao`,`tip_id_basica`,`ind_excluido`),
  ADD KEY `idx_matleg_dat_publicacao` (`dat_publicacao`,`tip_id_basica`,`ind_excluido`),
  ADD KEY `cod_situacao` (`cod_situacao`),
  ADD KEY `idx_mat_principal` (`cod_materia_principal`),
  ADD KEY `tip_quorum` (`tip_quorum`),
  ADD KEY `tip_id_basica` (`tip_id_basica`) USING BTREE,
  ADD KEY `idx_matleg_ident` (`ind_excluido`,`tip_id_basica`,`ano_ident_basica`,`num_ident_basica`) USING BTREE,
  ADD KEY `idx_tramitacao` (`ind_tramitacao`);
ALTER TABLE `materia_legislativa` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`);

ALTER TABLE `mesa_sessao_plenaria`
  ADD PRIMARY KEY (`cod_cargo`,`cod_sessao_leg`,`cod_parlamentar`,`cod_sessao_plen`),
  ADD KEY `cod_sessao_leg` (`cod_sessao_leg`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`);

ALTER TABLE `nivel_instrucao`
  ADD PRIMARY KEY (`cod_nivel_instrucao`);

ALTER TABLE `norma_juridica`
  ADD PRIMARY KEY (`cod_norma`),
  ADD KEY `cod_assunto` (`cod_assunto`),
  ADD KEY `tip_norma` (`tip_norma`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `idx_ano_numero` (`ano_norma`,`num_norma`,`ind_excluido`),
  ADD KEY `dat_norma` (`dat_norma`),
  ADD KEY `cod_situacao` (`cod_situacao`);
ALTER TABLE `norma_juridica` ADD FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`);

ALTER TABLE `numeracao`
  ADD PRIMARY KEY (`cod_materia`,`num_ordem`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `tip_materia` (`tip_materia`),
  ADD KEY `idx_numer_identificacao` (`tip_materia`,`num_materia`,`ano_materia`,`ind_excluido`);

ALTER TABLE `oradores`
  ADD PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  ADD UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`);

ALTER TABLE `oradores_expediente`
  ADD PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  ADD UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`);

ALTER TABLE `ordem_dia`
  ADD PRIMARY KEY (`cod_ordem`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `idx_dat_ordem` (`dat_ordem`),
  ADD KEY `tip_votacao` (`tip_votacao`),
  ADD KEY `tip_quorum` (`tip_quorum`),
  ADD KEY `tip_turno` (`tip_turno`),
  ADD KEY `num_ordem` (`num_ordem`);

ALTER TABLE `ordem_dia_discussao`
  ADD PRIMARY KEY (`cod_ordem`,`cod_parlamentar`) USING BTREE,
  ADD KEY `cod_ordem` (`cod_ordem`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`);

ALTER TABLE `ordem_dia_presenca`
  ADD PRIMARY KEY (`cod_presenca_ordem_dia`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `dat_ordem` (`dat_ordem`),
  ADD KEY `tip_frequencia` (`tip_frequencia`);

ALTER TABLE `orgao`
  ADD PRIMARY KEY (`cod_orgao`);

ALTER TABLE `origem`
  ADD PRIMARY KEY (`cod_origem`);

ALTER TABLE `parecer`
  ADD PRIMARY KEY (`cod_relatoria`,`cod_materia`),
  ADD KEY `idx_parecer_materia` (`cod_materia`,`ind_excluido`),
  ADD KEY `cod_materia` (`cod_materia`);

ALTER TABLE `parlamentar`
  ADD PRIMARY KEY (`cod_parlamentar`),
  ADD KEY `cod_localidade_resid` (`cod_localidade_resid`),
  ADD KEY `tip_situacao_militar` (`tip_situacao_militar`),
  ADD KEY `cod_nivel_instrucao` (`cod_nivel_instrucao`),
  ADD KEY `ind_parlamentar_ativo` (`ind_ativo`,`ind_excluido`);
ALTER TABLE `parlamentar` ADD FULLTEXT KEY `nom_completo` (`nom_completo`);
ALTER TABLE `parlamentar` ADD FULLTEXT KEY `nom_parlamentar` (`nom_parlamentar`);

ALTER TABLE `partido`
  ADD PRIMARY KEY (`cod_partido`);

ALTER TABLE `periodo_comp_bancada`
  ADD PRIMARY KEY (`cod_periodo_comp`),
  ADD KEY `ind_percompbancada_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  ADD KEY `idx_legislatura` (`num_legislatura`);

ALTER TABLE `periodo_comp_comissao`
  ADD PRIMARY KEY (`cod_periodo_comp`),
  ADD KEY `ind_percompcom_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`);

ALTER TABLE `periodo_comp_mesa`
  ADD PRIMARY KEY (`cod_periodo_comp`),
  ADD KEY `ind_percompmesa_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  ADD KEY `idx_legislatura` (`num_legislatura`);

ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`cod_pessoa`),
  ADD KEY `num_cep` (`num_cep`),
  ADD KEY `cod_logradouro` (`cod_logradouro`),
  ADD KEY `nom_cidade` (`nom_cidade`),
  ADD KEY `dat_nascimento` (`dat_nascimento`),
  ADD KEY `des_profissao` (`des_profissao`),
  ADD KEY `des_estado_civil` (`des_estado_civil`),
  ADD KEY `sex_visitante` (`sex_pessoa`),
  ADD KEY `nom_bairro` (`nom_bairro`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_pessoa` (`nom_pessoa`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `nom_conjuge` (`nom_conjuge`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `idx_busca` (`doc_identidade`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `end_residencial` (`end_residencial`);
ALTER TABLE `pessoa` ADD FULLTEXT KEY `doc_identidade` (`doc_identidade`);

ALTER TABLE `proposicao`
  ADD PRIMARY KEY (`cod_proposicao`),
  ADD KEY `tip_proposicao` (`tip_proposicao`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `cod_emenda` (`cod_emenda`),
  ADD KEY `cod_substitutivo` (`cod_substitutivo`),
  ADD KEY `cod_autor` (`cod_autor`),
  ADD KEY `idx_prop_autor` (`dat_envio`,`dat_recebimento`,`ind_excluido`);

ALTER TABLE `protocolo`
  ADD PRIMARY KEY (`cod_protocolo`),
  ADD UNIQUE KEY `idx_num_protocolo` (`num_protocolo`,`ano_protocolo`),
  ADD KEY `tip_protocolo` (`tip_protocolo`),
  ADD KEY `cod_autor` (`cod_autor`),
  ADD KEY `tip_materia` (`tip_materia`),
  ADD KEY `tip_documento` (`tip_documento`),
  ADD KEY `dat_protocolo` (`dat_protocolo`),
  ADD KEY `tip_processo` (`tip_processo`),
  ADD KEY `ano_protocolo` (`ano_protocolo`),
  ADD KEY `codigo_acesso` (`codigo_acesso`),
  ADD KEY `cod_entidade` (`cod_entidade`);
ALTER TABLE `protocolo` ADD FULLTEXT KEY `idx_busca_protocolo` (`txt_assunto_ementa`,`txt_observacao`);
ALTER TABLE `protocolo` ADD FULLTEXT KEY `txt_interessado` (`txt_interessado`);

ALTER TABLE `quorum_votacao`
  ADD PRIMARY KEY (`cod_quorum`);

ALTER TABLE `regime_tramitacao`
  ADD PRIMARY KEY (`cod_regime_tramitacao`);

ALTER TABLE `registro_votacao`
  ADD PRIMARY KEY (`cod_votacao`),
  ADD KEY `cod_ordem` (`cod_ordem`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `tip_resultado_votacao` (`tip_resultado_votacao`),
  ADD KEY `cod_emenda` (`cod_emenda`),
  ADD KEY `cod_subemenda` (`cod_subemenda`),
  ADD KEY `cod_substitutivo` (`cod_substitutivo`);

ALTER TABLE `registro_votacao_parlamentar`
  ADD PRIMARY KEY (`cod_votacao`,`cod_parlamentar`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `cod_votacao` (`cod_votacao`);

ALTER TABLE `relatoria`
  ADD PRIMARY KEY (`cod_relatoria`),
  ADD KEY `cod_comissao` (`cod_comissao`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `tip_fim_relatoria` (`tip_fim_relatoria`),
  ADD KEY `idx_relat_materia` (`cod_materia`,`cod_parlamentar`,`ind_excluido`);

ALTER TABLE `reuniao_comissao`
  ADD PRIMARY KEY (`cod_reuniao`),
  ADD KEY `cod_comissao` (`cod_comissao`);

ALTER TABLE `sessao_legislativa`
  ADD PRIMARY KEY (`cod_sessao_leg`),
  ADD KEY `idx_sessleg_datas` (`dat_inicio`,`ind_excluido`,`dat_fim`,`dat_inicio_intervalo`,`dat_fim_intervalo`),
  ADD KEY `idx_sessleg_legislatura` (`num_legislatura`,`ind_excluido`),
  ADD KEY `idx_legislatura` (`num_legislatura`);

ALTER TABLE `sessao_plenaria`
  ADD PRIMARY KEY (`cod_sessao_plen`),
  ADD KEY `cod_sessao_leg` (`cod_sessao_leg`),
  ADD KEY `tip_sessao` (`tip_sessao`),
  ADD KEY `num_legislatura` (`num_legislatura`),
  ADD KEY `dat_inicio_sessao` (`dat_inicio_sessao`),
  ADD KEY `num_sessao_plen` (`num_sessao_plen`);

ALTER TABLE `sessao_plenaria_painel`
  ADD PRIMARY KEY (`cod_item`),
  ADD UNIQUE KEY `ind_cod_materia` (`cod_materia`);

ALTER TABLE `sessao_plenaria_presenca`
  ADD PRIMARY KEY (`cod_presenca_sessao`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `idx_sessao_parlamentar` (`cod_sessao_plen`,`cod_parlamentar`),
  ADD KEY `cod_sessao_plen` (`cod_sessao_plen`),
  ADD KEY `dat_sessao` (`dat_sessao`),
  ADD KEY `tip_frequencia` (`tip_frequencia`);

ALTER TABLE `status_tramitacao`
  ADD PRIMARY KEY (`cod_status`),
  ADD KEY `sgl_status` (`sgl_status`);
ALTER TABLE `status_tramitacao` ADD FULLTEXT KEY `des_status` (`des_status`);

ALTER TABLE `status_tramitacao_administrativo`
  ADD PRIMARY KEY (`cod_status`),
  ADD KEY `sgl_status` (`sgl_status`);
ALTER TABLE `status_tramitacao_administrativo` ADD FULLTEXT KEY `des_status` (`des_status`);

ALTER TABLE `subemenda`
  ADD PRIMARY KEY (`cod_subemenda`),
  ADD UNIQUE KEY `numsub_emenda` (`num_subemenda`,`tip_subemenda`,`cod_emenda`,`ind_excluido`),
  ADD KEY `idx_cod_autor` (`cod_autor`),
  ADD KEY `idx_cod_emenda` (`cod_emenda`),
  ADD KEY `tip_subemenda` (`tip_subemenda`);
ALTER TABLE `subemenda` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);

ALTER TABLE `substitutivo`
  ADD PRIMARY KEY (`cod_substitutivo`),
  ADD UNIQUE KEY `idx_substitutivo` (`cod_substitutivo`,`cod_materia`),
  ADD KEY `idx_cod_autor` (`cod_autor`),
  ADD KEY `idx_cod_materia` (`cod_materia`);
ALTER TABLE `substitutivo` ADD FULLTEXT KEY `idx_txt_ementa` (`txt_ementa`);
ALTER TABLE `substitutivo` ADD FULLTEXT KEY `txt_observacao` (`txt_observacao`);

ALTER TABLE `tipo_afastamento`
  ADD PRIMARY KEY (`tip_afastamento`);

ALTER TABLE `tipo_autor`
  ADD PRIMARY KEY (`tip_autor`),
  ADD KEY `des_tipo_autor` (`des_tipo_autor`);

ALTER TABLE `tipo_comissao`
  ADD PRIMARY KEY (`tip_comissao`),
  ADD KEY `nom_tipo_comissao` (`nom_tipo_comissao`),
  ADD KEY `sgl_natureza_comissao` (`sgl_natureza_comissao`);

ALTER TABLE `tipo_dependente`
  ADD PRIMARY KEY (`tip_dependente`),
  ADD KEY `des_tipo_dependente` (`des_tipo_dependente`);

ALTER TABLE `tipo_documento`
  ADD PRIMARY KEY (`tip_documento`),
  ADD KEY `des_tipo_documento` (`des_tipo_documento`);

ALTER TABLE `tipo_documento_administrativo`
  ADD PRIMARY KEY (`tip_documento`),
  ADD KEY `des_tipo_documento` (`des_tipo_documento`);

ALTER TABLE `tipo_emenda`
  ADD PRIMARY KEY (`tip_emenda`),
  ADD KEY `des_tipo_emenda` (`des_tipo_emenda`);

ALTER TABLE `tipo_expediente`
  ADD PRIMARY KEY (`cod_expediente`),
  ADD KEY `nom_expediente` (`nom_expediente`);

ALTER TABLE `tipo_fim_relatoria`
  ADD PRIMARY KEY (`tip_fim_relatoria`);

ALTER TABLE `tipo_instituicao`
  ADD PRIMARY KEY (`tip_instituicao`);

ALTER TABLE `tipo_materia_legislativa`
  ADD PRIMARY KEY (`tip_materia`),
  ADD KEY `des_tipo_materia` (`des_tipo_materia`);

ALTER TABLE `tipo_norma_juridica`
  ADD PRIMARY KEY (`tip_norma`),
  ADD KEY `des_tipo_norma` (`des_tipo_norma`);

ALTER TABLE `tipo_proposicao`
  ADD PRIMARY KEY (`tip_proposicao`),
  ADD KEY `des_tipo_proposicao` (`des_tipo_proposicao`);

ALTER TABLE `tipo_resultado_votacao`
  ADD PRIMARY KEY (`tip_resultado_votacao`),
  ADD KEY `nom_resultado` (`nom_resultado`);

ALTER TABLE `tipo_sessao_plenaria`
  ADD PRIMARY KEY (`tip_sessao`),
  ADD KEY `nom_sessao` (`nom_sessao`);

ALTER TABLE `tipo_situacao_materia`
  ADD PRIMARY KEY (`tip_situacao_materia`),
  ADD KEY `des_tipo_situacao` (`des_tipo_situacao`);

ALTER TABLE `tipo_situacao_militar`
  ADD PRIMARY KEY (`tip_situacao_militar`);

ALTER TABLE `tipo_situacao_norma`
  ADD PRIMARY KEY (`tip_situacao_norma`),
  ADD KEY `des_tipo_situacao` (`des_tipo_situacao`);

ALTER TABLE `tipo_vinculo_norma`
  ADD PRIMARY KEY (`cod_tip_vinculo`),
  ADD UNIQUE KEY `tipo_vinculo` (`tipo_vinculo`),
  ADD UNIQUE KEY `idx_vinculo` (`tipo_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`),
  ADD KEY `tip_situacao` (`tip_situacao`);

ALTER TABLE `tipo_votacao`
  ADD PRIMARY KEY (`tip_votacao`);

ALTER TABLE `tramitacao`
  ADD PRIMARY KEY (`cod_tramitacao`),
  ADD KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  ADD KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  ADD KEY `cod_status` (`cod_status`),
  ADD KEY `cod_materia` (`cod_materia`),
  ADD KEY `idx_tramit_ultmat` (`ind_ult_tramitacao`,`dat_tramitacao`,`cod_materia`,`ind_excluido`),
  ADD KEY `sgl_turno` (`sgl_turno`),
  ADD KEY `cod_usuario_local` (`cod_usuario_local`),
  ADD KEY `cod_usuario_dest` (`cod_usuario_dest`);

ALTER TABLE `tramitacao_administrativo`
  ADD PRIMARY KEY (`cod_tramitacao`),
  ADD KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  ADD KEY `tramitacao_ind1` (`ind_ult_tramitacao`),
  ADD KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  ADD KEY `cod_status` (`cod_status`),
  ADD KEY `cod_documento` (`cod_documento`),
  ADD KEY `cod_usuario_local` (`cod_usuario_local`),
  ADD KEY `cod_usuario_dest` (`cod_usuario_dest`);

ALTER TABLE `turno_discussao`
  ADD PRIMARY KEY (`cod_turno`),
  ADD UNIQUE KEY `idx_unique_key` (`cod_turno`,`sgl_turno`,`ind_excluido`);

ALTER TABLE `unidade_tramitacao`
  ADD PRIMARY KEY (`cod_unid_tramitacao`),
  ADD KEY `idx_unidtramit_orgao` (`cod_orgao`,`ind_excluido`),
  ADD KEY `idx_unidtramit_comissao` (`cod_comissao`,`ind_excluido`),
  ADD KEY `cod_orgao` (`cod_orgao`),
  ADD KEY `cod_comissao` (`cod_comissao`),
  ADD KEY `idx_unidtramit_parlamentar` (`cod_parlamentar`,`ind_excluido`),
  ADD KEY `cod_parlamentar` (`cod_parlamentar`),
  ADD KEY `ind_leg` (`ind_leg`),
  ADD KEY `ind_adm` (`ind_adm`);

ALTER TABLE `usuario`
  ADD PRIMARY KEY (`cod_usuario`),
  ADD KEY `idx_col_username` (`col_username`),
  ADD KEY `idx_cod_localidade` (`cod_localidade_resid`);

ALTER TABLE `usuario_unid_tram`
  ADD UNIQUE KEY `PRIMARY_KEY` (`cod_usuario`,`cod_unid_tramitacao`),
  ADD KEY `idx_usuario` (`cod_usuario`),
  ADD KEY `idx_unid_tramitacao` (`cod_unid_tramitacao`);

ALTER TABLE `vinculo_norma_juridica`
  ADD PRIMARY KEY (`cod_vinculo`),
  ADD KEY `tip_vinculo` (`tip_vinculo`),
  ADD KEY `idx_vnj_norma_referente` (`cod_norma_referente`,`cod_norma_referida`,`ind_excluido`),
  ADD KEY `idx_vnj_norma_referida` (`cod_norma_referida`,`cod_norma_referente`,`ind_excluido`),
  ADD KEY `cod_norma_referente` (`cod_norma_referente`),
  ADD KEY `cod_norma_referida` (`cod_norma_referida`);

ALTER TABLE `visita`
  ADD PRIMARY KEY (`cod_visita`),
  ADD KEY `cod_funcionario` (`cod_funcionario`),
  ADD KEY `cod_pessoa` (`cod_pessoa`) USING BTREE,
  ADD KEY `dat_entrada` (`dat_entrada`),
  ADD KEY `des_situacao` (`des_situacao`);


ALTER TABLE `acomp_materia`
  MODIFY `cod_cadastro` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `afastamento`
  MODIFY `cod_afastamento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `anexo_norma`
  MODIFY `cod_anexo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_armario`
  MODIFY `cod_armario` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_corredor`
  MODIFY `cod_corredor` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_item`
  MODIFY `cod_item` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_prateleira`
  MODIFY `cod_prateleira` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_recipiente`
  MODIFY `cod_recipiente` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_tipo_recipiente`
  MODIFY `tip_recipiente` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_tipo_suporte`
  MODIFY `tip_suporte` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_tipo_tit_documental`
  MODIFY `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `arquivo_unidade`
  MODIFY `cod_unidade` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `assessor_parlamentar`
  MODIFY `cod_assessor` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `assunto_norma`
  MODIFY `cod_assunto` int(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `autor`
  MODIFY `cod_autor` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `bancada`
  MODIFY `cod_bancada` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `cargo_bancada`
  MODIFY `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `cargo_comissao`
  MODIFY `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `cargo_executivo`
  MODIFY `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `cargo_mesa`
  MODIFY `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `coligacao`
  MODIFY `cod_coligacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `comissao`
  MODIFY `cod_comissao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `composicao_bancada`
  MODIFY `cod_comp_bancada` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `composicao_comissao`
  MODIFY `cod_comp_comissao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `composicao_executivo`
  MODIFY `cod_composicao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `dependente`
  MODIFY `cod_dependente` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `destinatario_oficio`
  MODIFY `cod_destinatario` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_acessorio`
  MODIFY `cod_documento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_acessorio_administrativo`
  MODIFY `cod_documento_acessorio` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_administrativo`
  MODIFY `cod_documento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_administrativo_materia`
  MODIFY `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_administrativo_vinculado`
  MODIFY `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `documento_comissao`
  MODIFY `cod_documento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `emenda`
  MODIFY `cod_emenda` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `encerramento_presenca`
  MODIFY `cod_presenca_encerramento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `expediente_materia`
  MODIFY `cod_ordem` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `expediente_presenca`
  MODIFY `cod_presenca_expediente` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `funcionario`
  MODIFY `cod_funcionario` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `gabinete_atendimento`
  MODIFY `cod_atendimento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `gabinete_eleitor`
  MODIFY `cod_eleitor` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `instituicao`
  MODIFY `cod_instituicao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `lexml_registro_provedor`
  MODIFY `cod_provedor` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `lexml_registro_publicador`
  MODIFY `cod_publicador` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `logradouro`
  MODIFY `cod_logradouro` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `mandato`
  MODIFY `cod_mandato` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `materia_apresentada_sessao`
  MODIFY `cod_ordem` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `materia_legislativa`
  MODIFY `cod_materia` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `nivel_instrucao`
  MODIFY `cod_nivel_instrucao` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `norma_juridica`
  MODIFY `cod_norma` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `ordem_dia`
  MODIFY `cod_ordem` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `ordem_dia_presenca`
  MODIFY `cod_presenca_ordem_dia` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `orgao`
  MODIFY `cod_orgao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `origem`
  MODIFY `cod_origem` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `parlamentar`
  MODIFY `cod_parlamentar` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `partido`
  MODIFY `cod_partido` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `periodo_comp_bancada`
  MODIFY `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `periodo_comp_comissao`
  MODIFY `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `periodo_comp_mesa`
  MODIFY `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `pessoa`
  MODIFY `cod_pessoa` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `proposicao`
  MODIFY `cod_proposicao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `protocolo`
  MODIFY `cod_protocolo` int(7) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT;

ALTER TABLE `quorum_votacao`
  MODIFY `cod_quorum` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `regime_tramitacao`
  MODIFY `cod_regime_tramitacao` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `registro_votacao`
  MODIFY `cod_votacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `relatoria`
  MODIFY `cod_relatoria` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `reuniao_comissao`
  MODIFY `cod_reuniao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `sessao_legislativa`
  MODIFY `cod_sessao_leg` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `sessao_plenaria`
  MODIFY `cod_sessao_plen` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `sessao_plenaria_painel`
  MODIFY `cod_item` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `sessao_plenaria_presenca`
  MODIFY `cod_presenca_sessao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `status_tramitacao`
  MODIFY `cod_status` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `status_tramitacao_administrativo`
  MODIFY `cod_status` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `subemenda`
  MODIFY `cod_subemenda` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `substitutivo`
  MODIFY `cod_substitutivo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_afastamento`
  MODIFY `tip_afastamento` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_comissao`
  MODIFY `tip_comissao` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_dependente`
  MODIFY `tip_dependente` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_documento`
  MODIFY `tip_documento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_documento_administrativo`
  MODIFY `tip_documento` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_emenda`
  MODIFY `tip_emenda` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_expediente`
  MODIFY `cod_expediente` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_fim_relatoria`
  MODIFY `tip_fim_relatoria` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_instituicao`
  MODIFY `tip_instituicao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_materia_legislativa`
  MODIFY `tip_materia` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_norma_juridica`
  MODIFY `tip_norma` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_proposicao`
  MODIFY `tip_proposicao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_resultado_votacao`
  MODIFY `tip_resultado_votacao` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_sessao_plenaria`
  MODIFY `tip_sessao` tinyint(4) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_situacao_materia`
  MODIFY `tip_situacao_materia` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_situacao_norma`
  MODIFY `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_vinculo_norma`
  MODIFY `cod_tip_vinculo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tipo_votacao`
  MODIFY `tip_votacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tramitacao`
  MODIFY `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tramitacao_administrativo`
  MODIFY `cod_tramitacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `turno_discussao`
  MODIFY `cod_turno` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `unidade_tramitacao`
  MODIFY `cod_unid_tramitacao` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `usuario`
  MODIFY `cod_usuario` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `vinculo_norma_juridica`
  MODIFY `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `visita`
  MODIFY `cod_visita` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
