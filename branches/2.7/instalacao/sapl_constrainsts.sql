-- Tempo de Geração: 28/07/2014 às 11:48
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
  ADD CONSTRAINT `unidade_trami--
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
--tacao_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE NO ACTION,
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
