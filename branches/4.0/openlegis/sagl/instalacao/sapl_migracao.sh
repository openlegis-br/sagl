#!/bin/sh
###################################################################################################
### Preparação
### Script para migracao dos dados do SAPL 2.3 para o SAPL 2.4

NEW_INST="/var/interlegis/SAPL-2.4/instances/sapl24"
PYTHON_EGG_CACHE="$NEW_INST/var/.python-eggs"

export PYTHON_EGG_CACHE

if [ -d /var/interlegis/SAPL-2.3-beta/instances/sapl23 ]; then
    INST_PATH="/var/interlegis/SAPL-2.3-beta/instances/sapl23"
elif [ -d /var/interlegis/SAPL-2.3/instances/sapl23 ]; then
    INST_PATH="/var/interlegis/SAPL-2.3/instances/sapl23"
else
    echo "********* ERRO **********";
    echo "Não foi encontrada nenhuma instalação antiga do SAPL";
    echo "*************************";
    exit 1;
fi

if [ -d $path ]; then
    INST_PATH=$path
else
    echo "********* ERRO **********";
    echo "*  O diretório informado não existe.   *"
    echo "*  Reinicie o script de migração e informe o caminho corretamente.   *"
    echo "*************************";
   exit 1;
fi

if [ ! "$USER" = 'root' ]; then
   echo "********* ERRO **********";
   echo "*   Este script deve ser executado pelo usuário 'root'.";
   echo "*   Chame-o com o comando 'sudo ./sapl_migracao.sh'.";
   echo "*************************";
   exit 1;
fi

if [ ! -f "$NEW_INST/old/sapl_old.sql" ]; then
   echo "********* ERRO **********";
   echo "*   O arquivo de backup do MySQL da versão anterior do SAPL não está no diretório correto.";
   echo "*   Grave-o em '$NEW_INST/old', com o nome 'sapl_old.sql', e tente novamente.";
   echo "*************************";
   exit 1;
fi
echo "ok... Encontrado o arquivo sapl_old.sql"

# Pára o SAPL, se estiver em execução
INST_PATH/bin/shutdownsapl.sh
echo "ok... SAPL antigo parado."

$NEW_INST/bin/shutdownsapl.sh
echo "ok... SAPL 2.4 parado"

###################################################################################################
### Importação dos dados do banco relacional (MySQL)

ok=0
while [ $ok = 0 ]; do

    echo "Digite o nome do usuário MySQL: "
    read usuario

    if [ -z $usuario ]; then
        echo -e "\033[1;31mO usuário não pode ser em branco!\033[m";
    else
        ok=1
    fi

done

echo "Digite a senha do usuário admin (root) do MySQL: "
read senha

# Fazer a importacao dos dados antigos, inclusive com a substituicao das novas tabelas
# Depois, realizar a insercao das novas tabelas e colunas nas tabelas existentes

if [ -z $senha ]; then
    mysql -h 127.0.0.1 -u $usuario interlegis < $NEW_INST/old/sapl_old.sql
    mysql -h 127.0.0.1 -u $usuario interlegis < $NEW_INST/src/il.sapl/il/sapl/instalacao/sapl_migracao_banco.sql
else
    mysql -h 127.0.0.1 -u $usuario interlegis --password=$senha < $NEW_INST/old/sapl_old.sql
    mysql -h 127.0.0.1 -u $usuario interlegis --password=$senha < $NEW_INST/src/il.sapl/il/sapl/instalacao/sapl_migracao_banco.sql
fi
if [ $? -gt 0 ]; then
    echo ""
    echo -e "\033[1;31mErro na importação da estrutura da base de dados!\033[m";
    echo -e "\033[1;31mVerifique o usuário e senha e refaça a instalação!\033[m";
    echo -e "\033[1;31mInstalação abortada!\033[m";
    echo ""
    exit 1
else
    echo "ok... Importado o arquivo do backup do MySQL"
    echo "ok... Atualizado o banco para a nova estrutura do SAPL 2.4"
fi