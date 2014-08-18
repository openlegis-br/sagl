-- Versão do servidor: 5.6.19-0ubuntu0.14.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `acomp_materia`
--
ALTER TABLE `acomp_materia`
  ADD CONSTRAINT `acomp_materia_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `afastamento`
--
ALTER TABLE `afastamento`
  ADD CONSTRAINT `afastamento_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `afastamento_ibfk_2` FOREIGN KEY (`cod_mandato`) REFERENCES `mandato` (`cod_mandato`) ON UPDATE CASCADE,
  ADD CONSTRAINT `afastamento_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `afastamento_ibfk_4` FOREIGN KEY (`cod_parlamentar_suplente`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `afastamento_ibfk_5` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `anexada`
--
ALTER TABLE `anexada`
  ADD CONSTRAINT `anexada_ibfk_1` FOREIGN KEY (`cod_materia_principal`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `anexada_ibfk_2` FOREIGN KEY (`cod_materia_anexada`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `arquivo_armario`
--
ALTER TABLE `arquivo_armario`
  ADD CONSTRAINT `arquivo_armario_ibfk_1` FOREIGN KEY (`cod_corredor`) REFERENCES `arquivo_corredor` (`cod_corredor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_armario_ibfk_2` FOREIGN KEY (`cod_unidade`) REFERENCES `arquivo_unidade` (`cod_unidade`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `arquivo_corredor`
--
ALTER TABLE `arquivo_corredor`
  ADD CONSTRAINT `arquivo_corredor_ibfk_1` FOREIGN KEY (`cod_unidade`) REFERENCES `arquivo_unidade` (`cod_unidade`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `arquivo_item`
--
ALTER TABLE `arquivo_item`
  ADD CONSTRAINT `arquivo_item_ibfk_1` FOREIGN KEY (`cod_recipiente`) REFERENCES `arquivo_recipiente` (`cod_recipiente`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_item_ibfk_2` FOREIGN KEY (`tip_suporte`) REFERENCES `arquivo_tipo_suporte` (`tip_suporte`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_item_ibfk_3` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_item_ibfk_4` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_item_ibfk_5` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_item_ibfk_6` FOREIGN KEY (`cod_protocolo`) REFERENCES `protocolo` (`cod_protocolo`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `arquivo_prateleira`
--
ALTER TABLE `arquivo_prateleira`
  ADD CONSTRAINT `arquivo_prateleira_ibfk_1` FOREIGN KEY (`cod_armario`) REFERENCES `arquivo_armario` (`cod_armario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_prateleira_ibfk_2` FOREIGN KEY (`cod_corredor`) REFERENCES `arquivo_corredor` (`cod_corredor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_prateleira_ibfk_3` FOREIGN KEY (`cod_unidade`) REFERENCES `arquivo_unidade` (`cod_unidade`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `arquivo_recipiente`
--
ALTER TABLE `arquivo_recipiente`
  ADD CONSTRAINT `arquivo_recipiente_ibfk_1` FOREIGN KEY (`tip_recipiente`) REFERENCES `arquivo_tipo_recipiente` (`tip_recipiente`),
  ADD CONSTRAINT `arquivo_recipiente_ibfk_2` FOREIGN KEY (`tip_tit_documental`) REFERENCES `arquivo_tipo_tit_documental` (`tip_tit_documental`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_recipiente_ibfk_3` FOREIGN KEY (`cod_corredor`) REFERENCES `arquivo_corredor` (`cod_corredor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_recipiente_ibfk_4` FOREIGN KEY (`cod_armario`) REFERENCES `arquivo_armario` (`cod_armario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `arquivo_recipiente_ibfk_5` FOREIGN KEY (`cod_prateleira`) REFERENCES `arquivo_prateleira` (`cod_prateleira`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `assessor_parlamentar`
--
ALTER TABLE `assessor_parlamentar`
  ADD CONSTRAINT `assessor_parlamentar_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `autor`
--
ALTER TABLE `autor`
  ADD CONSTRAINT `autor_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE CASCADE,
  ADD CONSTRAINT `autor_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `autor_ibfk_3` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON UPDATE CASCADE,
  ADD CONSTRAINT `autor_ibfk_4` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `autor_ibfk_5` FOREIGN KEY (`tip_autor`) REFERENCES `tipo_autor` (`tip_autor`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `autoria`
--
ALTER TABLE `autoria`
  ADD CONSTRAINT `autoria_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `autoria_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `bancada`
--
ALTER TABLE `bancada`
  ADD CONSTRAINT `bancada_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `bancada_ibfk_2` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `coligacao`
--
ALTER TABLE `coligacao`
  ADD CONSTRAINT `coligacao_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `comissao`
--
ALTER TABLE `comissao`
  ADD CONSTRAINT `comissao_ibfk_1` FOREIGN KEY (`tip_comissao`) REFERENCES `tipo_comissao` (`tip_comissao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `composicao_bancada`
--
ALTER TABLE `composicao_bancada`
  ADD CONSTRAINT `composicao_bancada_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_bancada_ibfk_2` FOREIGN KEY (`cod_bancada`) REFERENCES `bancada` (`cod_bancada`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_bancada_ibfk_3` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_bancada` (`cod_cargo`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `composicao_coligacao`
--
ALTER TABLE `composicao_coligacao`
  ADD CONSTRAINT `composicao_coligacao_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_coligacao_ibfk_2` FOREIGN KEY (`cod_coligacao`) REFERENCES `coligacao` (`cod_coligacao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `composicao_comissao`
--
ALTER TABLE `composicao_comissao`
  ADD CONSTRAINT `composicao_comissao_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_comissao_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_comissao_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_comissao` (`cod_periodo_comp`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_comissao_ibfk_4` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_comissao` (`cod_cargo`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `composicao_mesa`
--
ALTER TABLE `composicao_mesa`
  ADD CONSTRAINT `composicao_mesa_ibfk_1` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_mesa_ibfk_2` FOREIGN KEY (`cod_cargo`) REFERENCES `cargo_mesa` (`cod_cargo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_mesa_ibfk_3` FOREIGN KEY (`cod_periodo_comp`) REFERENCES `periodo_comp_mesa` (`cod_periodo_comp`) ON UPDATE CASCADE,
  ADD CONSTRAINT `composicao_mesa_ibfk_4` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `dependente`
--
ALTER TABLE `dependente`
  ADD CONSTRAINT `dependente_ibfk_1` FOREIGN KEY (`tip_dependente`) REFERENCES `tipo_dependente` (`tip_dependente`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dependente_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `despacho_inicial`
--
ALTER TABLE `despacho_inicial`
  ADD CONSTRAINT `despacho_inicial_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `despacho_inicial_ibfk_2` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `documento_acessorio`
--
ALTER TABLE `documento_acessorio`
  ADD CONSTRAINT `documento_acessorio_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `documento_acessorio_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento` (`tip_documento`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `documento_acessorio_administrativo`
--
ALTER TABLE `documento_acessorio_administrativo`
  ADD CONSTRAINT `documento_acessorio_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `documento_administrativo`
--
ALTER TABLE `documento_administrativo`
  ADD CONSTRAINT `documento_administrativo_ibfk_1` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `documento_administrativo_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Restrições para tabelas `emenda`
--
ALTER TABLE `emenda`
  ADD CONSTRAINT `emenda_ibfk_1` FOREIGN KEY (`tip_emenda`) REFERENCES `tipo_emenda` (`tip_emenda`) ON UPDATE CASCADE,
  ADD CONSTRAINT `emenda_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `emenda_ibfk_3` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `encerramento_presenca`
--
ALTER TABLE `encerramento_presenca`
  ADD CONSTRAINT `encerramento_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `encerramento_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `expediente_materia`
--
ALTER TABLE `expediente_materia`
  ADD CONSTRAINT `expediente_materia_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `expediente_materia_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `expediente_presenca`
--
ALTER TABLE `expediente_presenca`
  ADD CONSTRAINT `expediente_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `expediente_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `expediente_sessao_plenaria`
--
ALTER TABLE `expediente_sessao_plenaria`
  ADD CONSTRAINT `expediente_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_expediente`) REFERENCES `tipo_expediente` (`cod_expediente`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `filiacao`
--
ALTER TABLE `filiacao`
  ADD CONSTRAINT `filiacao_ibfk_2` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`) ON UPDATE CASCADE,
  ADD CONSTRAINT `filiacao_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `instituicao`
--
ALTER TABLE `instituicao`
  ADD CONSTRAINT `instituicao_ibfk_1` FOREIGN KEY (`tip_instituicao`) REFERENCES `tipo_instituicao` (`tip_instituicao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `instituicao_ibfk_2` FOREIGN KEY (`cod_localidade`) REFERENCES `localidade` (`cod_localidade`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `legislacao_citada`
--
ALTER TABLE `legislacao_citada`
  ADD CONSTRAINT `legislacao_citada_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `legislacao_citada_ibfk_2` FOREIGN KEY (`cod_norma`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `mandato`
--
ALTER TABLE `mandato`
  ADD CONSTRAINT `mandato_ibfk_2` FOREIGN KEY (`tip_afastamento`) REFERENCES `tipo_afastamento` (`tip_afastamento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mandato_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mandato_ibfk_4` FOREIGN KEY (`cod_coligacao`) REFERENCES `coligacao` (`cod_coligacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mandato_ibfk_5` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `materia_apresentada_sessao`
--
ALTER TABLE `materia_apresentada_sessao`
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `materia_apresentada_sessao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `materia_legislativa`
--
ALTER TABLE `materia_legislativa`
  ADD CONSTRAINT `materia_legislativa_ibfk_1` FOREIGN KEY (`tip_id_basica`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `materia_legislativa_ibfk_2` FOREIGN KEY (`cod_regime_tramitacao`) REFERENCES `regime_tramitacao` (`cod_regime_tramitacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `materia_legislativa_ibfk_3` FOREIGN KEY (`cod_local_origem_externa`) REFERENCES `origem` (`cod_origem`) ON UPDATE CASCADE,
  ADD CONSTRAINT `materia_legislativa_ibfk_4` FOREIGN KEY (`cod_situacao`) REFERENCES `tipo_situacao_materia` (`tip_situacao_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `mesa_sessao_plenaria`
--
ALTER TABLE `mesa_sessao_plenaria`
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_1` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mesa_sessao_plenaria_ibfk_3` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `norma_juridica`
--
ALTER TABLE `norma_juridica`
  ADD CONSTRAINT `norma_juridica_ibfk_1` FOREIGN KEY (`tip_norma`) REFERENCES `tipo_norma_juridica` (`tip_norma`) ON UPDATE CASCADE,
  ADD CONSTRAINT `norma_juridica_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `norma_juridica_ibfk_3` FOREIGN KEY (`cod_situacao`) REFERENCES `tipo_situacao_norma` (`tip_situacao_norma`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `numeracao`
--
ALTER TABLE `numeracao`
  ADD CONSTRAINT `numeracao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `numeracao_ibfk_2` FOREIGN KEY (`tip_materia`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `oradores`
--
ALTER TABLE `oradores`
  ADD CONSTRAINT `oradores_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `oradores_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `oradores_expediente`
--
ALTER TABLE `oradores_expediente`
  ADD CONSTRAINT `oradores_expediente_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `oradores_expediente_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `ordem_dia`
--
ALTER TABLE `ordem_dia`
  ADD CONSTRAINT `ordem_dia_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `ordem_dia_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `ordem_dia_presenca`
--
ALTER TABLE `ordem_dia_presenca`
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `ordem_dia_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `parecer`
--
ALTER TABLE `parecer`
  ADD CONSTRAINT `parecer_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `parlamentar`
--
ALTER TABLE `parlamentar`
  ADD CONSTRAINT `parlamentar_ibfk_1` FOREIGN KEY (`cod_nivel_instrucao`) REFERENCES `nivel_instrucao` (`cod_nivel_instrucao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `parlamentar_ibfk_2` FOREIGN KEY (`tip_situacao_militar`) REFERENCES `tipo_situacao_militar` (`tip_situacao_militar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `parlamentar_ibfk_3` FOREIGN KEY (`cod_localidade_resid`) REFERENCES `localidade` (`cod_localidade`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `periodo_comp_mesa`
--
ALTER TABLE `periodo_comp_mesa`
  ADD CONSTRAINT `periodo_comp_mesa_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `proposicao`
--
ALTER TABLE `proposicao`
  ADD CONSTRAINT `proposicao_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `proposicao_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `proposicao_ibfk_3` FOREIGN KEY (`tip_proposicao`) REFERENCES `tipo_proposicao` (`tip_proposicao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `protocolo`
--
ALTER TABLE `protocolo`
  ADD CONSTRAINT `protocolo_ibfk_1` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `protocolo_ibfk_2` FOREIGN KEY (`tip_documento`) REFERENCES `tipo_documento_administrativo` (`tip_documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `protocolo_ibfk_3` FOREIGN KEY (`tip_materia`) REFERENCES `tipo_materia_legislativa` (`tip_materia`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `registro_votacao`
--
ALTER TABLE `registro_votacao`
  ADD CONSTRAINT `registro_votacao_ibfk_1` FOREIGN KEY (`tip_resultado_votacao`) REFERENCES `tipo_resultado_votacao` (`tip_resultado_votacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_votacao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_votacao_ibfk_3` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_votacao_ibfk_4` FOREIGN KEY (`cod_subemenda`) REFERENCES `subemenda` (`cod_subemenda`) ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_votacao_ibfk_5` FOREIGN KEY (`cod_substitutivo`) REFERENCES `substitutivo` (`cod_substitutivo`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `registro_votacao_parlamentar`
--
ALTER TABLE `registro_votacao_parlamentar`
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_1` FOREIGN KEY (`cod_votacao`) REFERENCES `registro_votacao` (`cod_votacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_votacao_parlamentar_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `relatoria`
--
ALTER TABLE `relatoria`
  ADD CONSTRAINT `relatoria_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `relatoria_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE,
  ADD CONSTRAINT `relatoria_ibfk_3` FOREIGN KEY (`tip_fim_relatoria`) REFERENCES `tipo_fim_relatoria` (`tip_fim_relatoria`) ON UPDATE CASCADE,
  ADD CONSTRAINT `relatoria_ibfk_4` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `reuniao_comissao`
--
ALTER TABLE `reuniao_comissao`
  ADD CONSTRAINT `reuniao_comissao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `sessao_legislativa`
--
ALTER TABLE `sessao_legislativa`
  ADD CONSTRAINT `sessao_legislativa_ibfk_1` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `sessao_plenaria`
--
ALTER TABLE `sessao_plenaria`
  ADD CONSTRAINT `sessao_plenaria_ibfk_1` FOREIGN KEY (`tip_sessao`) REFERENCES `tipo_sessao_plenaria` (`tip_sessao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sessao_plenaria_ibfk_2` FOREIGN KEY (`cod_sessao_leg`) REFERENCES `sessao_legislativa` (`cod_sessao_leg`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sessao_plenaria_ibfk_3` FOREIGN KEY (`num_legislatura`) REFERENCES `legislatura` (`num_legislatura`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `sessao_plenaria_presenca`
--
ALTER TABLE `sessao_plenaria_presenca`
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_1` FOREIGN KEY (`cod_sessao_plen`) REFERENCES `sessao_plenaria` (`cod_sessao_plen`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sessao_plenaria_presenca_ibfk_2` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `subemenda`
--
ALTER TABLE `subemenda`
  ADD CONSTRAINT `subemenda_ibfk_1` FOREIGN KEY (`tip_subemenda`) REFERENCES `tipo_emenda` (`tip_emenda`) ON UPDATE CASCADE,
  ADD CONSTRAINT `subemenda_ibfk_2` FOREIGN KEY (`cod_emenda`) REFERENCES `emenda` (`cod_emenda`) ON UPDATE CASCADE,
  ADD CONSTRAINT `subemenda_ibfk_3` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `substitutivo`
--
ALTER TABLE `substitutivo`
  ADD CONSTRAINT `substitutivo_ibfk_1` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `substitutivo_ibfk_2` FOREIGN KEY (`cod_autor`) REFERENCES `autor` (`cod_autor`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `tramitacao`
--
ALTER TABLE `tramitacao`
  ADD CONSTRAINT `tramitacao_ibfk_1` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao` (`cod_status`) ON UPDATE CASCADE,
  ADD CONSTRAINT `tramitacao_ibfk_2` FOREIGN KEY (`cod_materia`) REFERENCES `materia_legislativa` (`cod_materia`) ON UPDATE CASCADE,
  ADD CONSTRAINT `tramitacao_ibfk_3` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `tramitacao_ibfk_4` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`);

--
-- Restrições para tabelas `tramitacao_administrativo`
--
ALTER TABLE `tramitacao_administrativo`
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_1` FOREIGN KEY (`cod_documento`) REFERENCES `documento_administrativo` (`cod_documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_2` FOREIGN KEY (`cod_unid_tram_local`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_3` FOREIGN KEY (`cod_unid_tram_dest`) REFERENCES `unidade_tramitacao` (`cod_unid_tramitacao`),
  ADD CONSTRAINT `tramitacao_administrativo_ibfk_4` FOREIGN KEY (`cod_status`) REFERENCES `status_tramitacao_administrativo` (`cod_status`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `unidade_tramitacao`
--
ALTER TABLE `unidade_tramitacao`
  ADD CONSTRAINT `unidade_tramitacao_ibfk_1` FOREIGN KEY (`cod_comissao`) REFERENCES `comissao` (`cod_comissao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_2` FOREIGN KEY (`cod_orgao`) REFERENCES `orgao` (`cod_orgao`) ON UPDATE CASCADE,
  ADD CONSTRAINT `unidade_tramitacao_ibfk_3` FOREIGN KEY (`cod_parlamentar`) REFERENCES `parlamentar` (`cod_parlamentar`) ON UPDATE CASCADE;

--
-- Restrições para tabelas `vinculo_norma_juridica`
--
ALTER TABLE `vinculo_norma_juridica`
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_1` FOREIGN KEY (`cod_norma_referente`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vinculo_norma_juridica_ibfk_2` FOREIGN KEY (`cod_norma_referida`) REFERENCES `norma_juridica` (`cod_norma`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
