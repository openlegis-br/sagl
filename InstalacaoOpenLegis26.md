# ROTEIRO DE INSTALAÇÃO NO UBUNTU 12.04/14.04 SERVER LTS (32 ou 64 bits) #

## 1) Habilitar uso de repositórios PPA ##
```
$ sudo apt-get install python-software-properties
```

## 2) Instalação de todas as dependências no Sistema Operacional ##

```
$ sudo add-apt-repository ppa:libreoffice/ppa && \
sudo add-apt-repository ppa:webupd8team/java && \
sudo apt-get update 
```

```
$ sudo apt-get install libjpeg62 libjpeg62-dev zlib1g-dev \
libfreetype6 libfreetype6-dev \
libssl-dev \
mysql-server libmysqlclient-dev \
subversion \
build-essential \
libreadline6 libreadline6-dev readline-common \
poppler-utils wv \
libbsd-dev libcurl4-openssl-dev libgdbm-dev libidn11-dev \
libncursesw5-dev libreadline-dev librtmp-dev \
python-dev libxml2-dev libxslt1-dev \
python-software-properties ttf-mscorefonts-installer \
libreoffice-common libreoffice-calc libreoffice-writer \
oracle-java7-installer
```


## 3) Baixando o instalador do repositório GoogleCode: ##
```
$ svn checkout http://openlegis.googlecode.com/svn/install/2.6/ install_openlegis
```

## 4) Execução do Script de Instalação: ##
```
$ cd install_openlegis
```
```
$ sudo bash install.sh 
```

## 5) O OpenLegis é inicializado automaticamente após a instalação. ##

Teste de funcionamento do sistema: Abra um navegador e digite URL:  http://127.0.0.1:8080/sapl. O endereço citado é o IP da máquina local. Para acessar a partir de outro computador, utilize  http://[ip_do_servidor]:8080/sapl