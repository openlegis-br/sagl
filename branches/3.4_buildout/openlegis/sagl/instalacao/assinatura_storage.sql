SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;

-- --------------------------------------------------------

--
-- Estrutura da tabela `assinatura_storage`
--

CREATE TABLE `assinatura_storage` (
  `tip_documento` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `pdf_location` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `storage_path` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pdf_file` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pdf_signed` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dados da tabela `assinatura_storage`
--

INSERT INTO `assinatura_storage` (`tip_documento`, `pdf_location`, `storage_path`, `pdf_file`, `pdf_signed`) VALUES
('ata', 'sapl_documentos/ata_sessao/', 'sapl_documentos.ata_sessao', '_ata_sessao.pdf', '_ata_sessao_signed.pdf'),
('doc_acessorio', 'sapl_documentos/materia/', 'sapl_documentos.materia', '.pdf', '_signed.pdf'),
('doc_acessorio_adm', 'sapl_documentos/administrativo/', 'sapl_documentos.administrativo', '.pdf', '_signed.pdf'),
('documento', 'sapl_documentos/administrativo/', 'sapl_documentos.administrativo', '_texto_integral.pdf', '_texto_integral_signed.pdf'),
('emenda', 'sapl_documentos/emenda/', 'sapl_documentos.emenda', '_emenda.pdf', '_emenda_signed.pdf'),
('materia', 'sapl_documentos/materia/', 'sapl_documentos.materia', '_texto_integral.pdf', '_texto_integral_signed.pdf'),
('norma', 'sapl_documentos/norma_juridica/', 'sapl_documentos.norma_juridica', '_texto_integral.pdf', '_texto_integral_signed.pdf'),
('parecer_comissao', 'sapl_documentos/parecer_comissao/', 'sapl_documentos.parecer_comissao', '_parecer.pdf', '_parecer_signed.pdf'),
('pauta', 'sapl_documentos/pauta_sessao/', 'sapl_documentos.pauta_sessao', '_pauta_sessao.pdf', '_pauta_sessao_signed.pdf'),
('proposicao', 'sapl_documentos/proposicao/', 'sapl_documentos.proposicao', '.pdf', '_signed.pdf'),
('protocolo', 'sapl_documentos/protocolo/', 'sapl_documentos.protocolo', '_protocolo.pdf', '_protocolo_signed.pdf'),
('redacao_final', 'sapl_documentos/materia/', 'sapl_documentos.materia', '_redacao_final.pdf', '_redacao_final_signed.pdf'),
('substitutivo', 'sapl_documentos/substitutivo/', 'sapl_documentos.substitutivo', '_substitutivo.pdf', '_substitutivo_signed.pdf'),
('tramitacao', 'sapl_documentos/materia/tramitacao/', 'sapl_documentos.materia.tramitacao', '_tram.pdf', '_tram_signed.pdf'),
('tramitacao_adm', 'sapl_documentos/administrativo/tramitacao/', 'sapl_documentos.administrativo.tramitacao', '_tram.pdf', '_tram_signed.pdf');

--
-- Indexes for table `assinatura_storage`
--
ALTER TABLE `assinatura_storage`
  ADD PRIMARY KEY (`tip_documento`);

--
-- Estrutura da tabela `assinatura_documento`
--

CREATE TABLE `assinatura_documento` (
  `cod_assinatura_doc` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `codigo` int(11) NOT NULL,
  `tipo_doc` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `dat_solicitacao` datetime NOT NULL,
  `cod_usuario` int(11) NOT NULL,
  `dat_assinatura` datetime DEFAULT NULL,
  `ind_assinado` tinyint(4) NOT NULL DEFAULT '0',
  `ind_prim_assinatura` tinyint(4) NOT NULL,
  `ind_excluido` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for table `assinatura_documento`
--
ALTER TABLE `assinatura_documento`
  ADD UNIQUE KEY `cod_assinatura_doc_2` (`cod_assinatura_doc`,`codigo`,`tipo_doc`,`cod_usuario`);

COMMIT;

