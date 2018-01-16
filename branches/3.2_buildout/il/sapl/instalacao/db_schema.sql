-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: interlegis
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acomp_materia`
--

DROP TABLE IF EXISTS `acomp_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acomp_materia`
--

LOCK TABLES `acomp_materia` WRITE;
/*!40000 ALTER TABLE `acomp_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `acomp_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `afastamento`
--

DROP TABLE IF EXISTS `afastamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `afastamento`
--

LOCK TABLES `afastamento` WRITE;
/*!40000 ALTER TABLE `afastamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `afastamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anexada`
--

DROP TABLE IF EXISTS `anexada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anexada`
--

LOCK TABLES `anexada` WRITE;
/*!40000 ALTER TABLE `anexada` DISABLE KEYS */;
/*!40000 ALTER TABLE `anexada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anexo_norma`
--

DROP TABLE IF EXISTS `anexo_norma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anexo_norma` (
  `cod_anexo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma` int(11) NOT NULL,
  `txt_descricao` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_anexo`),
  KEY `cod_norma` (`cod_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anexo_norma`
--

LOCK TABLES `anexo_norma` WRITE;
/*!40000 ALTER TABLE `anexo_norma` DISABLE KEYS */;
/*!40000 ALTER TABLE `anexo_norma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_armario`
--

DROP TABLE IF EXISTS `arquivo_armario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_armario`
--

LOCK TABLES `arquivo_armario` WRITE;
/*!40000 ALTER TABLE `arquivo_armario` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_armario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_corredor`
--

DROP TABLE IF EXISTS `arquivo_corredor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arquivo_corredor` (
  `cod_corredor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_unidade` int(11) NOT NULL,
  `nom_corredor` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_corredor`),
  KEY `cod_unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_corredor`
--

LOCK TABLES `arquivo_corredor` WRITE;
/*!40000 ALTER TABLE `arquivo_corredor` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_corredor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_item`
--

DROP TABLE IF EXISTS `arquivo_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_item`
--

LOCK TABLES `arquivo_item` WRITE;
/*!40000 ALTER TABLE `arquivo_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_prateleira`
--

DROP TABLE IF EXISTS `arquivo_prateleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_prateleira`
--

LOCK TABLES `arquivo_prateleira` WRITE;
/*!40000 ALTER TABLE `arquivo_prateleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_prateleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_recipiente`
--

DROP TABLE IF EXISTS `arquivo_recipiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_recipiente`
--

LOCK TABLES `arquivo_recipiente` WRITE;
/*!40000 ALTER TABLE `arquivo_recipiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_recipiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_tipo_recipiente`
--

DROP TABLE IF EXISTS `arquivo_tipo_recipiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arquivo_tipo_recipiente` (
  `tip_recipiente` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_recipiente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_recipiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_tipo_recipiente`
--

LOCK TABLES `arquivo_tipo_recipiente` WRITE;
/*!40000 ALTER TABLE `arquivo_tipo_recipiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_tipo_recipiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_tipo_suporte`
--

DROP TABLE IF EXISTS `arquivo_tipo_suporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arquivo_tipo_suporte` (
  `tip_suporte` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_suporte` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_suporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_tipo_suporte`
--

LOCK TABLES `arquivo_tipo_suporte` WRITE;
/*!40000 ALTER TABLE `arquivo_tipo_suporte` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_tipo_suporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_tipo_tit_documental`
--

DROP TABLE IF EXISTS `arquivo_tipo_tit_documental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arquivo_tipo_tit_documental` (
  `tip_tit_documental` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tip_tit_documental` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `des_tipo_tit_documental` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_tit_documental`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_tipo_tit_documental`
--

LOCK TABLES `arquivo_tipo_tit_documental` WRITE;
/*!40000 ALTER TABLE `arquivo_tipo_tit_documental` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_tipo_tit_documental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arquivo_unidade`
--

DROP TABLE IF EXISTS `arquivo_unidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arquivo_unidade`
--

LOCK TABLES `arquivo_unidade` WRITE;
/*!40000 ALTER TABLE `arquivo_unidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `arquivo_unidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assessor_parlamentar`
--

DROP TABLE IF EXISTS `assessor_parlamentar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessor_parlamentar`
--

LOCK TABLES `assessor_parlamentar` WRITE;
/*!40000 ALTER TABLE `assessor_parlamentar` DISABLE KEYS */;
/*!40000 ALTER TABLE `assessor_parlamentar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assunto_norma`
--

DROP TABLE IF EXISTS `assunto_norma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assunto_norma` (
  `cod_assunto` int(4) NOT NULL AUTO_INCREMENT,
  `des_assunto` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_estendida` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_assunto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assunto_norma`
--

LOCK TABLES `assunto_norma` WRITE;
/*!40000 ALTER TABLE `assunto_norma` DISABLE KEYS */;
/*!40000 ALTER TABLE `assunto_norma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autor`
--

DROP TABLE IF EXISTS `autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  `end_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`),
  KEY `idx_tip_autor` (`tip_autor`),
  KEY `idx_parlamentar` (`cod_parlamentar`),
  KEY `idx_comissao` (`cod_comissao`),
  KEY `idx_partido` (`cod_partido`),
  KEY `idx_bancada` (`cod_bancada`),
  FULLTEXT KEY `nom_autor` (`nom_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autor`
--

LOCK TABLES `autor` WRITE;
/*!40000 ALTER TABLE `autor` DISABLE KEYS */;
/*!40000 ALTER TABLE `autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autoria`
--

DROP TABLE IF EXISTS `autoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autoria` (
  `cod_autor` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_primeiro_autor` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_autor`,`cod_materia`),
  KEY `idx_materia` (`cod_materia`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autoria`
--

LOCK TABLES `autoria` WRITE;
/*!40000 ALTER TABLE `autoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `autoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bancada`
--

DROP TABLE IF EXISTS `bancada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bancada`
--

LOCK TABLES `bancada` WRITE;
/*!40000 ALTER TABLE `bancada` DISABLE KEYS */;
/*!40000 ALTER TABLE `bancada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo_bancada`
--

DROP TABLE IF EXISTS `cargo_bancada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargo_bancada` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo_bancada`
--

LOCK TABLES `cargo_bancada` WRITE;
/*!40000 ALTER TABLE `cargo_bancada` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo_bancada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo_comissao`
--

DROP TABLE IF EXISTS `cargo_comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargo_comissao` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo_comissao`
--

LOCK TABLES `cargo_comissao` WRITE;
/*!40000 ALTER TABLE `cargo_comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo_comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo_executivo`
--

DROP TABLE IF EXISTS `cargo_executivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargo_executivo` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo_executivo`
--

LOCK TABLES `cargo_executivo` WRITE;
/*!40000 ALTER TABLE `cargo_executivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo_executivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo_mesa`
--

DROP TABLE IF EXISTS `cargo_mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargo_mesa` (
  `cod_cargo` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_cargo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo_mesa`
--

LOCK TABLES `cargo_mesa` WRITE;
/*!40000 ALTER TABLE `cargo_mesa` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo_mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coautoria_proposicao`
--

DROP TABLE IF EXISTS `coautoria_proposicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coautoria_proposicao` (
  `cod_proposicao` int(11) NOT NULL,
  `cod_autor` int(11) NOT NULL,
  `ind_aderido` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_proposicao`,`cod_autor`),
  KEY `idx_proposicao` (`cod_proposicao`),
  KEY `idx_autor` (`cod_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coautoria_proposicao`
--

LOCK TABLES `coautoria_proposicao` WRITE;
/*!40000 ALTER TABLE `coautoria_proposicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `coautoria_proposicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coligacao`
--

DROP TABLE IF EXISTS `coligacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coligacao`
--

LOCK TABLES `coligacao` WRITE;
/*!40000 ALTER TABLE `coligacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `coligacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comissao`
--

DROP TABLE IF EXISTS `comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comissao` (
  `cod_comissao` int(11) NOT NULL AUTO_INCREMENT,
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
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_comissao`),
  KEY `idx_comissao_tipo` (`tip_comissao`),
  KEY `idx_comissao_nome` (`nom_comissao`),
  FULLTEXT KEY `nom_comissao` (`nom_comissao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comissao`
--

LOCK TABLES `comissao` WRITE;
/*!40000 ALTER TABLE `comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composicao_bancada`
--

DROP TABLE IF EXISTS `composicao_bancada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composicao_bancada`
--

LOCK TABLES `composicao_bancada` WRITE;
/*!40000 ALTER TABLE `composicao_bancada` DISABLE KEYS */;
/*!40000 ALTER TABLE `composicao_bancada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composicao_coligacao`
--

DROP TABLE IF EXISTS `composicao_coligacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `composicao_coligacao` (
  `cod_partido` int(11) NOT NULL,
  `cod_coligacao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_partido`,`cod_coligacao`),
  KEY `idx_coligacao` (`cod_coligacao`),
  KEY `idx_partido` (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composicao_coligacao`
--

LOCK TABLES `composicao_coligacao` WRITE;
/*!40000 ALTER TABLE `composicao_coligacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `composicao_coligacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composicao_comissao`
--

DROP TABLE IF EXISTS `composicao_comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composicao_comissao`
--

LOCK TABLES `composicao_comissao` WRITE;
/*!40000 ALTER TABLE `composicao_comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `composicao_comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composicao_executivo`
--

DROP TABLE IF EXISTS `composicao_executivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `composicao_executivo` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composicao_executivo`
--

LOCK TABLES `composicao_executivo` WRITE;
/*!40000 ALTER TABLE `composicao_executivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `composicao_executivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composicao_mesa`
--

DROP TABLE IF EXISTS `composicao_mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composicao_mesa`
--

LOCK TABLES `composicao_mesa` WRITE;
/*!40000 ALTER TABLE `composicao_mesa` DISABLE KEYS */;
/*!40000 ALTER TABLE `composicao_mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependente`
--

DROP TABLE IF EXISTS `dependente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependente`
--

LOCK TABLES `dependente` WRITE;
/*!40000 ALTER TABLE `dependente` DISABLE KEYS */;
/*!40000 ALTER TABLE `dependente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `despacho_inicial`
--

DROP TABLE IF EXISTS `despacho_inicial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `despacho_inicial`
--

LOCK TABLES `despacho_inicial` WRITE;
/*!40000 ALTER TABLE `despacho_inicial` DISABLE KEYS */;
/*!40000 ALTER TABLE `despacho_inicial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destinatario_oficio`
--

DROP TABLE IF EXISTS `destinatario_oficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `destinatario_oficio` (
  `cod_destinatario` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_instituicao` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_destinatario`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_instituicao` (`cod_instituicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destinatario_oficio`
--

LOCK TABLES `destinatario_oficio` WRITE;
/*!40000 ALTER TABLE `destinatario_oficio` DISABLE KEYS */;
/*!40000 ALTER TABLE `destinatario_oficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_acessorio`
--

DROP TABLE IF EXISTS `documento_acessorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_acessorio`
--

LOCK TABLES `documento_acessorio` WRITE;
/*!40000 ALTER TABLE `documento_acessorio` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_acessorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_acessorio_administrativo`
--

DROP TABLE IF EXISTS `documento_acessorio_administrativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_acessorio_administrativo`
--

LOCK TABLES `documento_acessorio_administrativo` WRITE;
/*!40000 ALTER TABLE `documento_acessorio_administrativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_acessorio_administrativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_administrativo`
--

DROP TABLE IF EXISTS `documento_administrativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documento_administrativo` (
  `cod_documento` int(11) NOT NULL AUTO_INCREMENT,
  `tip_documento` int(11) NOT NULL,
  `num_documento` int(11) NOT NULL,
  `ano_documento` smallint(6) NOT NULL DEFAULT '0',
  `dat_documento` date NOT NULL,
  `num_protocolo` int(11) DEFAULT NULL,
  `txt_interessado` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_administrativo`
--

LOCK TABLES `documento_administrativo` WRITE;
/*!40000 ALTER TABLE `documento_administrativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_administrativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_administrativo_materia`
--

DROP TABLE IF EXISTS `documento_administrativo_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documento_administrativo_materia` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `idx_cod_documento` (`cod_documento`),
  KEY `idx_cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_administrativo_materia`
--

LOCK TABLES `documento_administrativo_materia` WRITE;
/*!40000 ALTER TABLE `documento_administrativo_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_administrativo_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_administrativo_vinculado`
--

DROP TABLE IF EXISTS `documento_administrativo_vinculado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documento_administrativo_vinculado` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_documento_vinculante` int(11) NOT NULL,
  `cod_documento_vinculado` int(11) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_vinculo`),
  UNIQUE KEY `idx_doc_vinculo` (`cod_documento_vinculante`,`cod_documento_vinculado`),
  KEY `idx_doc_vinculado` (`cod_documento_vinculado`) USING BTREE,
  KEY `idx_cod_documento` (`cod_documento_vinculante`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_administrativo_vinculado`
--

LOCK TABLES `documento_administrativo_vinculado` WRITE;
/*!40000 ALTER TABLE `documento_administrativo_vinculado` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_administrativo_vinculado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emenda`
--

DROP TABLE IF EXISTS `emenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emenda`
--

LOCK TABLES `emenda` WRITE;
/*!40000 ALTER TABLE `emenda` DISABLE KEYS */;
/*!40000 ALTER TABLE `emenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encerramento_presenca`
--

DROP TABLE IF EXISTS `encerramento_presenca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encerramento_presenca`
--

LOCK TABLES `encerramento_presenca` WRITE;
/*!40000 ALTER TABLE `encerramento_presenca` DISABLE KEYS */;
/*!40000 ALTER TABLE `encerramento_presenca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expediente_materia`
--

DROP TABLE IF EXISTS `expediente_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expediente_materia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_ordem` int(10) DEFAULT NULL,
  `txt_resultado` text COLLATE utf8_unicode_ci,
  `tip_votacao` int(11) NOT NULL,
  `tip_quorum` int(11) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `idx_exped_datord` (`dat_ordem`,`ind_excluido`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`),
  KEY `cod_materia` (`cod_materia`),
  KEY `tip_votacao` (`tip_votacao`),
  KEY `tip_quorum` (`tip_quorum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expediente_materia`
--

LOCK TABLES `expediente_materia` WRITE;
/*!40000 ALTER TABLE `expediente_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `expediente_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expediente_presenca`
--

DROP TABLE IF EXISTS `expediente_presenca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expediente_presenca`
--

LOCK TABLES `expediente_presenca` WRITE;
/*!40000 ALTER TABLE `expediente_presenca` DISABLE KEYS */;
/*!40000 ALTER TABLE `expediente_presenca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expediente_sessao_plenaria`
--

DROP TABLE IF EXISTS `expediente_sessao_plenaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expediente_sessao_plenaria` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_expediente` int(11) NOT NULL,
  `txt_expediente` text COLLATE utf8_unicode_ci,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_expediente`),
  KEY `cod_expediente` (`cod_expediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expediente_sessao_plenaria`
--

LOCK TABLES `expediente_sessao_plenaria` WRITE;
/*!40000 ALTER TABLE `expediente_sessao_plenaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `expediente_sessao_plenaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filiacao`
--

DROP TABLE IF EXISTS `filiacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filiacao`
--

LOCK TABLES `filiacao` WRITE;
/*!40000 ALTER TABLE `filiacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `filiacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcionario` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gabinete_atendimento`
--

DROP TABLE IF EXISTS `gabinete_atendimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gabinete_atendimento` (
  `cod_atendimento` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `cod_eleitor` int(11) NOT NULL,
  `dat_atendimento` date NOT NULL,
  `txt_assunto` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `dat_resultado` date DEFAULT NULL,
  `txt_resultado` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_atendente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_status` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_atendimento`),
  KEY `idx_resultado` (`txt_resultado`) USING BTREE,
  KEY `idx_eleitor` (`cod_eleitor`) USING BTREE,
  KEY `idx_parlamentar` (`cod_parlamentar`) USING BTREE,
  FULLTEXT KEY `idx_assunto` (`txt_assunto`),
  CONSTRAINT `gabinete_atendimento_ibfk_1` FOREIGN KEY (`cod_eleitor`) REFERENCES `gabinete_eleitor` (`cod_eleitor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `gabinete_atendimento_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gabinete_atendimento`
--

LOCK TABLES `gabinete_atendimento` WRITE;
/*!40000 ALTER TABLE `gabinete_atendimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `gabinete_atendimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gabinete_eleitor`
--

DROP TABLE IF EXISTS `gabinete_eleitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gabinete_eleitor` (
  `cod_eleitor` int(11) NOT NULL AUTO_INCREMENT,
  `cod_parlamentar` int(11) NOT NULL,
  `dat_cadastro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nom_eleitor` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex_eleitor` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_nascimento` date DEFAULT NULL,
  `des_estado_civil` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `doc_identidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cpf` varchar(50) CHARACTER SET utf32 COLLATE utf32_unicode_ci DEFAULT NULL,
  `txt_classe` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_profissao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_escolaridade` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_eleitor`),
  KEY `sex_eleitor` (`sex_eleitor`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  FULLTEXT KEY `nom_eleitor` (`nom_eleitor`),
  FULLTEXT KEY `des_profissao` (`des_profissao`),
  FULLTEXT KEY `end_residencial` (`end_residencial`),
  FULLTEXT KEY `nom_localidade` (`nom_localidade`),
  FULLTEXT KEY `des_local_trabalho` (`des_local_trabalho`),
  FULLTEXT KEY `nom_bairro` (`nom_bairro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gabinete_eleitor`
--

LOCK TABLES `gabinete_eleitor` WRITE;
/*!40000 ALTER TABLE `gabinete_eleitor` DISABLE KEYS */;
/*!40000 ALTER TABLE `gabinete_eleitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instituicao`
--

DROP TABLE IF EXISTS `instituicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instituicao`
--

LOCK TABLES `instituicao` WRITE;
/*!40000 ALTER TABLE `instituicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `instituicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `legislacao_citada`
--

DROP TABLE IF EXISTS `legislacao_citada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legislacao_citada`
--

LOCK TABLES `legislacao_citada` WRITE;
/*!40000 ALTER TABLE `legislacao_citada` DISABLE KEYS */;
/*!40000 ALTER TABLE `legislacao_citada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `legislatura`
--

DROP TABLE IF EXISTS `legislatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `legislatura` (
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio` date NOT NULL,
  `dat_fim` date NOT NULL,
  `dat_eleicao` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`num_legislatura`),
  KEY `idx_legislatura_datas` (`dat_inicio`,`dat_fim`,`dat_eleicao`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legislatura`
--

LOCK TABLES `legislatura` WRITE;
/*!40000 ALTER TABLE `legislatura` DISABLE KEYS */;
/*!40000 ALTER TABLE `legislatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lexml_registro_provedor`
--

DROP TABLE IF EXISTS `lexml_registro_provedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lexml_registro_provedor`
--

LOCK TABLES `lexml_registro_provedor` WRITE;
/*!40000 ALTER TABLE `lexml_registro_provedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `lexml_registro_provedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lexml_registro_publicador`
--

DROP TABLE IF EXISTS `lexml_registro_publicador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lexml_registro_publicador`
--

LOCK TABLES `lexml_registro_publicador` WRITE;
/*!40000 ALTER TABLE `lexml_registro_publicador` DISABLE KEYS */;
/*!40000 ALTER TABLE `lexml_registro_publicador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localidade`
--

DROP TABLE IF EXISTS `localidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localidade`
--

LOCK TABLES `localidade` WRITE;
/*!40000 ALTER TABLE `localidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `localidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logradouro`
--

DROP TABLE IF EXISTS `logradouro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logradouro` (
  `cod_logradouro` int(11) NOT NULL AUTO_INCREMENT,
  `nom_logradouro` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nom_bairro` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_cep` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_localidade` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_logradouro`),
  KEY `num_cep` (`num_cep`),
  KEY `cod_localidade` (`cod_localidade`),
  FULLTEXT KEY `nom_logradouro` (`nom_logradouro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logradouro`
--

LOCK TABLES `logradouro` WRITE;
/*!40000 ALTER TABLE `logradouro` DISABLE KEYS */;
/*!40000 ALTER TABLE `logradouro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mandato`
--

DROP TABLE IF EXISTS `mandato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mandato` (
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
  KEY `idx_coligacao` (`cod_coligacao`),
  KEY `idx_parlamentar` (`cod_parlamentar`),
  KEY `idx_afastamento` (`tip_afastamento`),
  KEY `idx_mandato_legislatura` (`num_legislatura`,`cod_parlamentar`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`),
  KEY `tip_causa_fim_mandato` (`tip_causa_fim_mandato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mandato`
--

LOCK TABLES `mandato` WRITE;
/*!40000 ALTER TABLE `mandato` DISABLE KEYS */;
/*!40000 ALTER TABLE `mandato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia_apresentada_sessao`
--

DROP TABLE IF EXISTS `materia_apresentada_sessao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materia_apresentada_sessao` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_ordem`),
  KEY `fk_cod_materia` (`cod_materia`),
  KEY `idx_apres_datord` (`dat_ordem`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_apresentada_sessao`
--

LOCK TABLES `materia_apresentada_sessao` WRITE;
/*!40000 ALTER TABLE `materia_apresentada_sessao` DISABLE KEYS */;
/*!40000 ALTER TABLE `materia_apresentada_sessao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia_legislativa`
--

DROP TABLE IF EXISTS `materia_legislativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  `cod_materia_principal` int(11) DEFAULT NULL,
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
  KEY `idx_mat_principal` (`cod_materia_principal`),
  KEY `tip_quorum` (`tip_quorum`),
  FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_legislativa`
--

LOCK TABLES `materia_legislativa` WRITE;
/*!40000 ALTER TABLE `materia_legislativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `materia_legislativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mesa_sessao_plenaria`
--

DROP TABLE IF EXISTS `mesa_sessao_plenaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesa_sessao_plenaria`
--

LOCK TABLES `mesa_sessao_plenaria` WRITE;
/*!40000 ALTER TABLE `mesa_sessao_plenaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `mesa_sessao_plenaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivel_instrucao`
--

DROP TABLE IF EXISTS `nivel_instrucao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nivel_instrucao` (
  `cod_nivel_instrucao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_nivel_instrucao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_nivel_instrucao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivel_instrucao`
--

LOCK TABLES `nivel_instrucao` WRITE;
/*!40000 ALTER TABLE `nivel_instrucao` DISABLE KEYS */;
/*!40000 ALTER TABLE `nivel_instrucao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `norma_juridica`
--

DROP TABLE IF EXISTS `norma_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  FULLTEXT KEY `idx_busca` (`txt_ementa`,`txt_observacao`,`txt_indexacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `norma_juridica`
--

LOCK TABLES `norma_juridica` WRITE;
/*!40000 ALTER TABLE `norma_juridica` DISABLE KEYS */;
/*!40000 ALTER TABLE `norma_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `numeracao`
--

DROP TABLE IF EXISTS `numeracao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `numeracao`
--

LOCK TABLES `numeracao` WRITE;
/*!40000 ALTER TABLE `numeracao` DISABLE KEYS */;
/*!40000 ALTER TABLE `numeracao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oradores`
--

DROP TABLE IF EXISTS `oradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oradores` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oradores`
--

LOCK TABLES `oradores` WRITE;
/*!40000 ALTER TABLE `oradores` DISABLE KEYS */;
/*!40000 ALTER TABLE `oradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oradores_expediente`
--

DROP TABLE IF EXISTS `oradores_expediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oradores_expediente` (
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `num_ordem` tinyint(4) NOT NULL,
  `url_discurso` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_sessao_plen`,`cod_parlamentar`),
  UNIQUE KEY `idx_num_ordem` (`cod_sessao_plen`,`num_ordem`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_sessao_plen` (`cod_sessao_plen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oradores_expediente`
--

LOCK TABLES `oradores_expediente` WRITE;
/*!40000 ALTER TABLE `oradores_expediente` DISABLE KEYS */;
/*!40000 ALTER TABLE `oradores_expediente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem_dia`
--

DROP TABLE IF EXISTS `ordem_dia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ordem_dia` (
  `cod_ordem` int(11) NOT NULL AUTO_INCREMENT,
  `cod_sessao_plen` int(11) NOT NULL,
  `cod_materia` int(11) NOT NULL,
  `dat_ordem` date NOT NULL,
  `txt_observacao` text COLLATE utf8_unicode_ci,
  `num_ordem` int(10) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem_dia`
--

LOCK TABLES `ordem_dia` WRITE;
/*!40000 ALTER TABLE `ordem_dia` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordem_dia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem_dia_presenca`
--

DROP TABLE IF EXISTS `ordem_dia_presenca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem_dia_presenca`
--

LOCK TABLES `ordem_dia_presenca` WRITE;
/*!40000 ALTER TABLE `ordem_dia_presenca` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordem_dia_presenca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgao`
--

DROP TABLE IF EXISTS `orgao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orgao` (
  `cod_orgao` int(11) NOT NULL AUTO_INCREMENT,
  `nom_orgao` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_orgao` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_unid_deliberativa` tinyint(4) NOT NULL,
  `end_orgao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_tel_orgao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_orgao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgao`
--

LOCK TABLES `orgao` WRITE;
/*!40000 ALTER TABLE `orgao` DISABLE KEYS */;
/*!40000 ALTER TABLE `orgao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `origem`
--

DROP TABLE IF EXISTS `origem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `origem` (
  `cod_origem` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_origem` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_origem` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_origem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `origem`
--

LOCK TABLES `origem` WRITE;
/*!40000 ALTER TABLE `origem` DISABLE KEYS */;
/*!40000 ALTER TABLE `origem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parecer`
--

DROP TABLE IF EXISTS `parecer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parecer`
--

LOCK TABLES `parecer` WRITE;
/*!40000 ALTER TABLE `parecer` DISABLE KEYS */;
/*!40000 ALTER TABLE `parecer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parlamentar`
--

DROP TABLE IF EXISTS `parlamentar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parlamentar` (
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
  PRIMARY KEY (`cod_parlamentar`),
  KEY `cod_localidade_resid` (`cod_localidade_resid`),
  KEY `tip_situacao_militar` (`tip_situacao_militar`),
  KEY `cod_nivel_instrucao` (`cod_nivel_instrucao`),
  KEY `ind_parlamentar_ativo` (`ind_ativo`,`ind_excluido`),
  FULLTEXT KEY `nom_completo` (`nom_completo`),
  FULLTEXT KEY `nom_parlamentar` (`nom_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parlamentar`
--

LOCK TABLES `parlamentar` WRITE;
/*!40000 ALTER TABLE `parlamentar` DISABLE KEYS */;
/*!40000 ALTER TABLE `parlamentar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partido`
--

DROP TABLE IF EXISTS `partido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partido` (
  `cod_partido` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_partido` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nom_partido` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dat_criacao` date DEFAULT NULL,
  `dat_extincao` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_partido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partido`
--

LOCK TABLES `partido` WRITE;
/*!40000 ALTER TABLE `partido` DISABLE KEYS */;
/*!40000 ALTER TABLE `partido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `periodo_comp_comissao`
--

DROP TABLE IF EXISTS `periodo_comp_comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `periodo_comp_comissao` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompcom_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodo_comp_comissao`
--

LOCK TABLES `periodo_comp_comissao` WRITE;
/*!40000 ALTER TABLE `periodo_comp_comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `periodo_comp_comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `periodo_comp_mesa`
--

DROP TABLE IF EXISTS `periodo_comp_mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `periodo_comp_mesa` (
  `cod_periodo_comp` int(11) NOT NULL AUTO_INCREMENT,
  `num_legislatura` int(11) NOT NULL,
  `dat_inicio_periodo` date NOT NULL,
  `dat_fim_periodo` date NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_periodo_comp`),
  KEY `ind_percompmesa_datas` (`dat_inicio_periodo`,`dat_fim_periodo`,`ind_excluido`),
  KEY `idx_legislatura` (`num_legislatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodo_comp_mesa`
--

LOCK TABLES `periodo_comp_mesa` WRITE;
/*!40000 ALTER TABLE `periodo_comp_mesa` DISABLE KEYS */;
/*!40000 ALTER TABLE `periodo_comp_mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa`
--

DROP TABLE IF EXISTS `pessoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pessoa` (
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
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_pessoa`),
  KEY `num_cep` (`num_cep`),
  KEY `cod_logradouro` (`cod_logradouro`),
  KEY `nom_cidade` (`nom_cidade`),
  KEY `dat_nascimento` (`dat_nascimento`),
  KEY `des_profissao` (`des_profissao`),
  KEY `des_estado_civil` (`des_estado_civil`),
  KEY `sex_visitante` (`sex_pessoa`),
  KEY `nom_bairro` (`nom_bairro`),
  FULLTEXT KEY `nom_pessoa` (`nom_pessoa`),
  FULLTEXT KEY `nom_conjuge` (`nom_conjuge`),
  FULLTEXT KEY `idx_busca` (`doc_identidade`),
  FULLTEXT KEY `end_residencial` (`end_residencial`),
  FULLTEXT KEY `doc_identidade` (`doc_identidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa`
--

LOCK TABLES `pessoa` WRITE;
/*!40000 ALTER TABLE `pessoa` DISABLE KEYS */;
/*!40000 ALTER TABLE `pessoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proposicao`
--

DROP TABLE IF EXISTS `proposicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proposicao` (
  `cod_proposicao` int(11) NOT NULL AUTO_INCREMENT,
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
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_proposicao`),
  KEY `tip_proposicao` (`tip_proposicao`),
  KEY `cod_materia` (`cod_materia`),
  KEY `cod_emenda` (`cod_emenda`),
  KEY `cod_substitutivo` (`cod_substitutivo`),
  KEY `cod_autor` (`cod_autor`),
  KEY `idx_prop_autor` (`dat_envio`,`dat_recebimento`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proposicao`
--

LOCK TABLES `proposicao` WRITE;
/*!40000 ALTER TABLE `proposicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `proposicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `protocolo`
--

DROP TABLE IF EXISTS `protocolo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `protocolo` (
  `cod_protocolo` int(7) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `num_protocolo` int(7) unsigned zerofill DEFAULT NULL,
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
  FULLTEXT KEY `idx_busca_protocolo` (`txt_assunto_ementa`,`txt_observacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `protocolo`
--

LOCK TABLES `protocolo` WRITE;
/*!40000 ALTER TABLE `protocolo` DISABLE KEYS */;
/*!40000 ALTER TABLE `protocolo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quorum_votacao`
--

DROP TABLE IF EXISTS `quorum_votacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quorum_votacao` (
  `cod_quorum` int(11) NOT NULL AUTO_INCREMENT,
  `des_quorum` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `txt_formula` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_quorum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quorum_votacao`
--

LOCK TABLES `quorum_votacao` WRITE;
/*!40000 ALTER TABLE `quorum_votacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `quorum_votacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regime_tramitacao`
--

DROP TABLE IF EXISTS `regime_tramitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regime_tramitacao` (
  `cod_regime_tramitacao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_regime_tramitacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_regime_tramitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regime_tramitacao`
--

LOCK TABLES `regime_tramitacao` WRITE;
/*!40000 ALTER TABLE `regime_tramitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `regime_tramitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_votacao`
--

DROP TABLE IF EXISTS `registro_votacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_votacao`
--

LOCK TABLES `registro_votacao` WRITE;
/*!40000 ALTER TABLE `registro_votacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_votacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_votacao_parlamentar`
--

DROP TABLE IF EXISTS `registro_votacao_parlamentar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_votacao_parlamentar` (
  `cod_votacao` int(11) NOT NULL,
  `cod_parlamentar` int(11) NOT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  `vot_parlamentar` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_votacao`,`cod_parlamentar`),
  KEY `cod_parlamentar` (`cod_parlamentar`),
  KEY `cod_votacao` (`cod_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_votacao_parlamentar`
--

LOCK TABLES `registro_votacao_parlamentar` WRITE;
/*!40000 ALTER TABLE `registro_votacao_parlamentar` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_votacao_parlamentar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relatoria`
--

DROP TABLE IF EXISTS `relatoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relatoria`
--

LOCK TABLES `relatoria` WRITE;
/*!40000 ALTER TABLE `relatoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `relatoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reuniao_comissao`
--

DROP TABLE IF EXISTS `reuniao_comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reuniao_comissao`
--

LOCK TABLES `reuniao_comissao` WRITE;
/*!40000 ALTER TABLE `reuniao_comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `reuniao_comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessao_legislativa`
--

DROP TABLE IF EXISTS `sessao_legislativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessao_legislativa`
--

LOCK TABLES `sessao_legislativa` WRITE;
/*!40000 ALTER TABLE `sessao_legislativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessao_legislativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessao_plenaria`
--

DROP TABLE IF EXISTS `sessao_plenaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessao_plenaria`
--

LOCK TABLES `sessao_plenaria` WRITE;
/*!40000 ALTER TABLE `sessao_plenaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessao_plenaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessao_plenaria_painel`
--

DROP TABLE IF EXISTS `sessao_plenaria_painel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sessao_plenaria_painel` (
  `cod_item` int(11) NOT NULL AUTO_INCREMENT,
  `tip_item` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `nom_fase` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num_ordem` int(11) NOT NULL,
  `txt_exibicao` text COLLATE utf8_unicode_ci NOT NULL,
  `cod_materia` int(11) DEFAULT NULL,
  `txt_autoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_turno` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_extrapauta` tinyint(4) DEFAULT '0',
  `ind_exibicao` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`cod_item`),
  UNIQUE KEY `ind_cod_materia` (`cod_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessao_plenaria_painel`
--

LOCK TABLES `sessao_plenaria_painel` WRITE;
/*!40000 ALTER TABLE `sessao_plenaria_painel` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessao_plenaria_painel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessao_plenaria_presenca`
--

DROP TABLE IF EXISTS `sessao_plenaria_presenca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessao_plenaria_presenca`
--

LOCK TABLES `sessao_plenaria_presenca` WRITE;
/*!40000 ALTER TABLE `sessao_plenaria_presenca` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessao_plenaria_presenca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_tramitacao`
--

DROP TABLE IF EXISTS `status_tramitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status_tramitacao` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_tramitacao`
--

LOCK TABLES `status_tramitacao` WRITE;
/*!40000 ALTER TABLE `status_tramitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `status_tramitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_tramitacao_administrativo`
--

DROP TABLE IF EXISTS `status_tramitacao_administrativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status_tramitacao_administrativo` (
  `cod_status` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_status` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_status` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_fim_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `ind_retorno_tramitacao` tinyint(4) NOT NULL DEFAULT '0',
  `num_dias_prazo` tinyint(4) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cod_status`),
  KEY `sgl_status` (`sgl_status`),
  FULLTEXT KEY `des_status` (`des_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_tramitacao_administrativo`
--

LOCK TABLES `status_tramitacao_administrativo` WRITE;
/*!40000 ALTER TABLE `status_tramitacao_administrativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `status_tramitacao_administrativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subemenda`
--

DROP TABLE IF EXISTS `subemenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subemenda`
--

LOCK TABLES `subemenda` WRITE;
/*!40000 ALTER TABLE `subemenda` DISABLE KEYS */;
/*!40000 ALTER TABLE `subemenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `substitutivo`
--

DROP TABLE IF EXISTS `substitutivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `substitutivo`
--

LOCK TABLES `substitutivo` WRITE;
/*!40000 ALTER TABLE `substitutivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `substitutivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_afastamento`
--

DROP TABLE IF EXISTS `tipo_afastamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_afastamento` (
  `tip_afastamento` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_afastamento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_afastamento` tinyint(4) NOT NULL,
  `ind_fim_mandato` tinyint(4) NOT NULL,
  `des_dispositivo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_afastamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_afastamento`
--

LOCK TABLES `tipo_afastamento` WRITE;
/*!40000 ALTER TABLE `tipo_afastamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_afastamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_autor`
--

DROP TABLE IF EXISTS `tipo_autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_autor` (
  `tip_autor` tinyint(4) NOT NULL,
  `des_tipo_autor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_proposicao` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_autor`),
  KEY `des_tipo_autor` (`des_tipo_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_autor`
--

LOCK TABLES `tipo_autor` WRITE;
/*!40000 ALTER TABLE `tipo_autor` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_comissao`
--

DROP TABLE IF EXISTS `tipo_comissao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_comissao`
--

LOCK TABLES `tipo_comissao` WRITE;
/*!40000 ALTER TABLE `tipo_comissao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_comissao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_dependente`
--

DROP TABLE IF EXISTS `tipo_dependente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_dependente` (
  `tip_dependente` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_tipo_dependente` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_dependente`),
  KEY `des_tipo_dependente` (`des_tipo_dependente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_dependente`
--

LOCK TABLES `tipo_dependente` WRITE;
/*!40000 ALTER TABLE `tipo_dependente` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_dependente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_documento`
--

DROP TABLE IF EXISTS `tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_documento` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_documento`
--

LOCK TABLES `tipo_documento` WRITE;
/*!40000 ALTER TABLE `tipo_documento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_documento_administrativo`
--

DROP TABLE IF EXISTS `tipo_documento_administrativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_documento_administrativo` (
  `tip_documento` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_documento` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_documento` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_publico` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_documento`),
  KEY `des_tipo_documento` (`des_tipo_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_documento_administrativo`
--

LOCK TABLES `tipo_documento_administrativo` WRITE;
/*!40000 ALTER TABLE `tipo_documento_administrativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_documento_administrativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_emenda`
--

DROP TABLE IF EXISTS `tipo_emenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_emenda` (
  `tip_emenda` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_emenda` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_emenda`),
  KEY `des_tipo_emenda` (`des_tipo_emenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_emenda`
--

LOCK TABLES `tipo_emenda` WRITE;
/*!40000 ALTER TABLE `tipo_emenda` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_emenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_expediente`
--

DROP TABLE IF EXISTS `tipo_expediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_expediente` (
  `cod_expediente` int(11) NOT NULL AUTO_INCREMENT,
  `nom_expediente` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`cod_expediente`),
  KEY `nom_expediente` (`nom_expediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_expediente`
--

LOCK TABLES `tipo_expediente` WRITE;
/*!40000 ALTER TABLE `tipo_expediente` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_expediente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_fim_relatoria`
--

DROP TABLE IF EXISTS `tipo_fim_relatoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_fim_relatoria` (
  `tip_fim_relatoria` tinyint(4) NOT NULL AUTO_INCREMENT,
  `des_fim_relatoria` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_fim_relatoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_fim_relatoria`
--

LOCK TABLES `tipo_fim_relatoria` WRITE;
/*!40000 ALTER TABLE `tipo_fim_relatoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_fim_relatoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_instituicao`
--

DROP TABLE IF EXISTS `tipo_instituicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_instituicao` (
  `tip_instituicao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_tipo_instituicao` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_instituicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_instituicao`
--

LOCK TABLES `tipo_instituicao` WRITE;
/*!40000 ALTER TABLE `tipo_instituicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_instituicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_materia_legislativa`
--

DROP TABLE IF EXISTS `tipo_materia_legislativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_materia_legislativa` (
  `tip_materia` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_tipo_materia` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_materia` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_natureza` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_num_automatica` tinyint(4) NOT NULL DEFAULT '0',
  `quorum_minimo_votacao` tinyint(4) NOT NULL DEFAULT '1',
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_materia`),
  KEY `des_tipo_materia` (`des_tipo_materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_materia_legislativa`
--

LOCK TABLES `tipo_materia_legislativa` WRITE;
/*!40000 ALTER TABLE `tipo_materia_legislativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_materia_legislativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_norma_juridica`
--

DROP TABLE IF EXISTS `tipo_norma_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_norma_juridica` (
  `tip_norma` tinyint(4) NOT NULL AUTO_INCREMENT,
  `voc_lexml` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sgl_tipo_norma` char(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `des_tipo_norma` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_norma`),
  KEY `des_tipo_norma` (`des_tipo_norma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_norma_juridica`
--

LOCK TABLES `tipo_norma_juridica` WRITE;
/*!40000 ALTER TABLE `tipo_norma_juridica` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_norma_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_proposicao`
--

DROP TABLE IF EXISTS `tipo_proposicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_proposicao` (
  `tip_proposicao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_proposicao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_mat_ou_doc` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tip_mat_ou_doc` int(11) NOT NULL,
  `nom_modelo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_proposicao`),
  KEY `des_tipo_proposicao` (`des_tipo_proposicao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_proposicao`
--

LOCK TABLES `tipo_proposicao` WRITE;
/*!40000 ALTER TABLE `tipo_proposicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_proposicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_resultado_votacao`
--

DROP TABLE IF EXISTS `tipo_resultado_votacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_resultado_votacao` (
  `tip_resultado_votacao` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom_resultado` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`tip_resultado_votacao`),
  KEY `nom_resultado` (`nom_resultado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_resultado_votacao`
--

LOCK TABLES `tipo_resultado_votacao` WRITE;
/*!40000 ALTER TABLE `tipo_resultado_votacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_resultado_votacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_sessao_plenaria`
--

DROP TABLE IF EXISTS `tipo_sessao_plenaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_sessao_plenaria` (
  `tip_sessao` tinyint(4) NOT NULL AUTO_INCREMENT,
  `nom_sessao` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  `num_minimo` int(11) NOT NULL,
  PRIMARY KEY (`tip_sessao`),
  KEY `nom_sessao` (`nom_sessao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_sessao_plenaria`
--

LOCK TABLES `tipo_sessao_plenaria` WRITE;
/*!40000 ALTER TABLE `tipo_sessao_plenaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_sessao_plenaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_situacao_materia`
--

DROP TABLE IF EXISTS `tipo_situacao_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_situacao_materia` (
  `tip_situacao_materia` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_materia`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_situacao_materia`
--

LOCK TABLES `tipo_situacao_materia` WRITE;
/*!40000 ALTER TABLE `tipo_situacao_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_situacao_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_situacao_militar`
--

DROP TABLE IF EXISTS `tipo_situacao_militar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_situacao_militar` (
  `tip_situacao_militar` tinyint(4) NOT NULL,
  `des_tipo_situacao` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_situacao_militar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_situacao_militar`
--

LOCK TABLES `tipo_situacao_militar` WRITE;
/*!40000 ALTER TABLE `tipo_situacao_militar` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_situacao_militar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_situacao_norma`
--

DROP TABLE IF EXISTS `tipo_situacao_norma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_situacao_norma` (
  `tip_situacao_norma` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_situacao` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tip_situacao_norma`),
  KEY `des_tipo_situacao` (`des_tipo_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_situacao_norma`
--

LOCK TABLES `tipo_situacao_norma` WRITE;
/*!40000 ALTER TABLE `tipo_situacao_norma` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_situacao_norma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_vinculo_norma`
--

DROP TABLE IF EXISTS `tipo_vinculo_norma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_vinculo_norma` (
  `cod_tip_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_vinculo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `des_vinculo_passivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tip_situacao` int(11) DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_tip_vinculo`),
  UNIQUE KEY `tipo_vinculo` (`tipo_vinculo`),
  UNIQUE KEY `idx_vinculo` (`tipo_vinculo`,`des_vinculo`,`des_vinculo_passivo`,`ind_excluido`),
  KEY `tip_situacao` (`tip_situacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_vinculo_norma`
--

LOCK TABLES `tipo_vinculo_norma` WRITE;
/*!40000 ALTER TABLE `tipo_vinculo_norma` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_vinculo_norma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_votacao`
--

DROP TABLE IF EXISTS `tipo_votacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_votacao` (
  `tip_votacao` int(11) NOT NULL AUTO_INCREMENT,
  `des_tipo_votacao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`tip_votacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_votacao`
--

LOCK TABLES `tipo_votacao` WRITE;
/*!40000 ALTER TABLE `tipo_votacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_votacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tramitacao`
--

DROP TABLE IF EXISTS `tramitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tramitacao` (
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
  KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  KEY `cod_status` (`cod_status`),
  KEY `cod_materia` (`cod_materia`),
  KEY `idx_tramit_ultmat` (`ind_ult_tramitacao`,`dat_tramitacao`,`cod_materia`,`ind_excluido`),
  KEY `sgl_turno` (`sgl_turno`),
  KEY `cod_usuario_local` (`cod_usuario_local`),
  KEY `cod_usuario_dest` (`cod_usuario_dest`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tramitacao`
--

LOCK TABLES `tramitacao` WRITE;
/*!40000 ALTER TABLE `tramitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tramitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tramitacao_administrativo`
--

DROP TABLE IF EXISTS `tramitacao_administrativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tramitacao_administrativo` (
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
  KEY `cod_unid_tram_dest` (`cod_unid_tram_dest`),
  KEY `tramitacao_ind1` (`ind_ult_tramitacao`),
  KEY `cod_unid_tram_local` (`cod_unid_tram_local`),
  KEY `cod_status` (`cod_status`),
  KEY `cod_documento` (`cod_documento`),
  KEY `cod_usuario_local` (`cod_usuario_local`),
  KEY `cod_usuario_dest` (`cod_usuario_dest`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tramitacao_administrativo`
--

LOCK TABLES `tramitacao_administrativo` WRITE;
/*!40000 ALTER TABLE `tramitacao_administrativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tramitacao_administrativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turno_discussao`
--

DROP TABLE IF EXISTS `turno_discussao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `turno_discussao` (
  `cod_turno` int(11) NOT NULL AUTO_INCREMENT,
  `sgl_turno` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `des_turno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_turno`),
  UNIQUE KEY `idx_unique_key` (`cod_turno`,`sgl_turno`,`ind_excluido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turno_discussao`
--

LOCK TABLES `turno_discussao` WRITE;
/*!40000 ALTER TABLE `turno_discussao` DISABLE KEYS */;
/*!40000 ALTER TABLE `turno_discussao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidade_tramitacao`
--

DROP TABLE IF EXISTS `unidade_tramitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unidade_tramitacao` (
  `cod_unid_tramitacao` int(11) NOT NULL AUTO_INCREMENT,
  `cod_comissao` int(11) DEFAULT NULL,
  `cod_orgao` int(11) DEFAULT NULL,
  `cod_parlamentar` int(11) DEFAULT NULL,
  `unid_dest_permitidas` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status_permitidos` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` tinyint(4) NOT NULL,
  PRIMARY KEY (`cod_unid_tramitacao`),
  KEY `idx_unidtramit_orgao` (`cod_orgao`,`ind_excluido`),
  KEY `idx_unidtramit_comissao` (`cod_comissao`,`ind_excluido`),
  KEY `cod_orgao` (`cod_orgao`),
  KEY `cod_comissao` (`cod_comissao`),
  KEY `idx_unidtramit_parlamentar` (`cod_parlamentar`,`ind_excluido`),
  KEY `cod_parlamentar` (`cod_parlamentar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidade_tramitacao`
--

LOCK TABLES `unidade_tramitacao` WRITE;
/*!40000 ALTER TABLE `unidade_tramitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `unidade_tramitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_unid_tram`
--

DROP TABLE IF EXISTS `usuario_unid_tram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario_unid_tram` (
  `cod_usuario` int(11) NOT NULL,
  `cod_unid_tramitacao` int(11) NOT NULL,
  `ind_responsavel` tinyint(4) NOT NULL DEFAULT '0',
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0',
  UNIQUE KEY `PRIMARY_KEY` (`cod_usuario`,`cod_unid_tramitacao`),
  KEY `idx_usuario` (`cod_usuario`),
  KEY `idx_unid_tramitacao` (`cod_unid_tramitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_unid_tram`
--

LOCK TABLES `usuario_unid_tram` WRITE;
/*!40000 ALTER TABLE `usuario_unid_tram` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_unid_tram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vinculo_norma_juridica`
--

DROP TABLE IF EXISTS `vinculo_norma_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vinculo_norma_juridica` (
  `cod_vinculo` int(11) NOT NULL AUTO_INCREMENT,
  `cod_norma_referente` int(11) NOT NULL,
  `cod_norma_referida` int(11) DEFAULT NULL,
  `tip_vinculo` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `txt_observacao_vinculo` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ind_excluido` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cod_vinculo`),
  KEY `tip_vinculo` (`tip_vinculo`),
  KEY `idx_vnj_norma_referente` (`cod_norma_referente`,`cod_norma_referida`,`ind_excluido`),
  KEY `idx_vnj_norma_referida` (`cod_norma_referida`,`cod_norma_referente`,`ind_excluido`),
  KEY `cod_norma_referente` (`cod_norma_referente`),
  KEY `cod_norma_referida` (`cod_norma_referida`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=0;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vinculo_norma_juridica`
--

LOCK TABLES `vinculo_norma_juridica` WRITE;
/*!40000 ALTER TABLE `vinculo_norma_juridica` DISABLE KEYS */;
/*!40000 ALTER TABLE `vinculo_norma_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visita`
--

DROP TABLE IF EXISTS `visita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `visita` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visita`
--

LOCK TABLES `visita` WRITE;
/*!40000 ALTER TABLE `visita` DISABLE KEYS */;
/*!40000 ALTER TABLE `visita` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-10 13:34:26
