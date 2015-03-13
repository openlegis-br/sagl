# Edição direta de arquivos ODT no sistema OpenLegis (Ubuntu Desktop) #

### 1. Instalar os pacotes e dependências: ###

sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get update

sudo apt-get install python2.6 python2.6-dev python-tk

sudo dpkg -i collective.zopeedit\_1.0.0\_all.deb

(Download do pacote disponível no menu "Sistema" do OpenLegis)

### 2. Editar o arquivo /usr/bin/zopeedit ###

Ajuste a primeira linha.

De:

#!/usr/bin/env python

Para:

#!/usr/bin/env python2.6

### 3. Configurar editor padrão para arquivos ODT ###

Execute o comando $ zopeedit e na linha 139, adicione o editor padrão:

editor = /usr/bin/libreoffice

### 4. Configurar seu navegador para abrir os arquivos do tipo "application/x-zope-edit" com o aplicativo "/usr/bin/zopeedit" ###