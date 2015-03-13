# OpenLegis - Sistema Aberto de Gestão Legislativa #

## Sobre o projeto ##
O projeto OpenLegis tem como objetivo disponibilizar às Casas Legislativas (Câmaras Municipais e Assembleias Legislativas) uma alternativa livre e de código aberto capaz de substituir sistemas comerciais (softwares proprietários), geralmente contratados em regime de locação mensal, para informatização de seu processo legislativo, possibilitando autonomia e independência tecnológica, com funcionalidades e rotinas desenvolvidas em consonância com padrão jurídico e legal do Processo Legislativo Brasileiro.

## Principais recursos ##

### Suporte a dispositivos móveis ###
Interface web (para consulta e operação) elaborada com tecnologias HTML5 / CSS3 / UTF-8 para fornecer uma ótima experiência de visualização, fácil leitura e navegação com um mínimo de redimensionamento e visionamento, para uma ampla gama de dispositivos (de monitores de computador a telefones celulares).

| **Computador** | **Smartphone** |
|:---------------|:---------------|
| ![https://openlegis.googlecode.com/svn/laptop.png](https://openlegis.googlecode.com/svn/laptop.png) | ![https://openlegis.googlecode.com/svn/mobile.png](https://openlegis.googlecode.com/svn/mobile.png) |

**Vantagens**
  * Acessível para todo tipo de dispositivo (celular, tablet netbook, desktop, TV)
  * Uma única interface que se adapta automaticamente
  * Possibilidade de redimensionar textos e fotos para facilitar a leitura em telas pequenas
  * Evita conteúdo duplicado que prejudica os mecanismos de busca, podendo gerar penalizações
  * Proporciona ótima experiência para todos os usuários do sistema

### Integridade de Dados ###
A integridade referencial preserva as relações definidas entre tabelas quando linhas são digitadas ou excluídas, assegurando que os registros permaneçam consistentes em todas as tabelas do sistema OpenLegis. Esse recurso visa a garantir a integridade dos dados, de modo a não haver como existir um registro "filho" sem um registro "pai".

### Geração de documentos em formato aberto ###
Geração nativa de documentos em formato ODF (Open Document Format), com uso do aplicativo LibreOffice-headless instalado no próprio servidor, disponível nos diversos módulos do sistema (proposições eletrônicas, matérias legislativas e documentos acessórios, normas jurídicas, documentos administrativos, atas e pautas das sessões, resumos e ofícios), a partir de modelos editáveis e personalizáveis via web.

A partir dos documentos ODF (com visualização e edição somente a usuários autenticados), o sistema possibilita conversão automática para o formato PDF, para disponibilização pública, como alternativa ao procedimento de digitalização em papel.

### Processo Legislativo Eletrônico com Certificação Digital ###
[Assinatura digital nos documentos ODF](https://help.libreoffice.org/Common/About_Digital_Signatures/pt-BR), incluindo elaboração de proposições em meio eletrônico, com uso de certificados digitais válidos emitidos por Autoridades Certificadoras, por exemplo os emitidos no âmbito da Infra-Estrutura de Chaves Públicas - ICP - Brasil. Alternativamente, o projeto de código aberto [CAcert](https://www.cacert.org/) emite certificados sem custos.

![https://openlegis.googlecode.com/svn/assinatura_digital.jpg](https://openlegis.googlecode.com/svn/assinatura_digital.jpg)

### Edição via web de documentos ODF ###
Edição, alteração e gravação de arquivos ODF via web, dispensando a necessidade de compartilhamentos de rede local (Redes Windows / Active Directory) para acesso dos operadores aos documentos do sistema, e abolindo a rotina de download / edição/ upload de arquivos.

Com recursos avançados de segurança providos pela linguagem Python, o sistema também conta com auditoria, versionamento de arquivos e níveis de acesso por perfis de usuários.

### Visualizador web de documentos ODF ###
Visualização de arquivos ODT diretamente no navegador, proporcionando ao operador a facilidade de consulta ao conteúdo de um arquivo pela própria interface do sistema.

## Casas Legislativas Usuárias ##

CasasLegislativasUsuarias

## Lista estendida de funcionalidades ##

ListaFuncionalidades

## Screenshots ##

Em elaboração

## Demonstração do sistema ##
http://demo.openlegis.com.br

Credenciais de acesso:

Usuário: saploper / Senha: saploper