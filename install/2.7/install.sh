#!/bin/sh
#
# Unified OpenLegis installer build script
# Maintainer: OpenLegis (contato at openlegis.com.br)
#
# Note: this script must be run as root
#

# Export libraries
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

# Configure OpenLegis installation options
INSTALL_HOME=/var/interlegis/SAPL-2.7
EFFECTIVE_USER=zope
LOCAL_HOME=$INSTALL_HOME
PY_HOME=$INSTALL_HOME/Python-2.4
SITECUSTOMIZE_FILE=$PY_HOME/lib/python2.4/sitecustomize.py
PY=$PY_HOME/bin/python2.4
EASY_INSTALL=$PY_HOME/bin/easy_install
PIP=$PY_HOME/bin/pip
ZOPE_HOME=$INSTALL_HOME/Zope-2.9
SITE_PACKAGES=$PY_HOME/lib/python2.4/site-packages
INSTANCE_HOME=$INSTALL_HOME/instances
SAPL_HOME=$INSTANCE_HOME/sapl27
PRODUCTS_HOME=$SAPL_HOME/Products
PWFILE=$INSTALL_HOME/adminPassword.txt
SAPL_STARTUP_SCRIPT=$SAPL_HOME/bin/startsapl.sh
SAPL_SHUTDOWN_SCRIPT=$SAPL_HOME/bin/shutdownsapl.sh
SAPL_RESTART_SCRIPT=$SAPL_HOME/bin/restartsapl.sh
RECEIPTS_HOME=$INSTALL_HOME/receipts

# Include the following tarballs in the packages/ directory in the bundle
PYTHON_TB=Python-2.4.6.tar.bz2
PYTHON_DIR=Python-2.4.6
PYXML_TB=PyXML-0.8.4.tar.bz2
PYXML_DIR=PyXML-0.8.4
REPLAB_TB=reportlab_2_5.tar.bz2
REPLAB_DIR=reportlab-2.5
JPEG_TB=jpeg-6b.tar.bz2
JPEG_DIR=jpeg-6b
ZLIB_TB=zlib-1.2.3.tar.bz2
ZLIB_DIR=zlib-1.2.3
PIL_TB=Imaging-1.1.7.tar.bz2
PIL_DIR=Imaging-1.1.7
ZOPE_TB=Zope-2.9.12-final.tar.bz2
ZOPE_DIR=Zope-2.9.12-final
SAPL_TB=SAPL.tar.bz2
SAPL_DIR=ILSAPL
CMF_TB=CMF-1.6.4-final.tar.bz2
CMF_DIR=CMF-1.6.4-final
TXNG2_TB=TextIndexNG-2.2.0.tar.bz2
TXNG2_DIR=TextIndexNG2
HSCRIPTS_TB=HelperScripts.tar.bz2
HSCRIPTS_DIR=HelperScripts
ETREE_TB=elementtree-1.2.7-20070827-preview.tar.bz2
ETREE_DIR=elementtree-1.2.7-20070827-preview
DISTRIBUTE_TB=distribute-0.6.49.tar.bz2
DISTRIBUTE_DIR=distribute-0.6.49
ADVANCEDQUERY_TB=AdvancedQuery-2.2.tar.bz2
ADVANCEDQUERY_DIR=AdvancedQuery
MYSQLPYTHON_TB=MySQL-python-1.2.4.tar.bz2
MYSQLPYTHON_DIR=MySQL-python-1.2.4
TRML2PDF_TB=trml2pdf-1.2.tar.bz2
TRML2PDF_DIR=trml2pdf
SDE_TB=StructuredDoc.tar.bz2
SDE_DIR=StructuredDoc
EXTFILE_TB=ExtFile-2.0.2.tar.bz2
EXTFILE_DIR=ExtFile
EXTEDIT_TB=ExternalEditor-0.9.3-src.bz2
EXTEDIT_DIR=ExternalEditor
MAILDHOST_TB=MaildropHost.tar.bz2
MAILDHOST_DIR=MaildropHost
ZMYSQLDA_TB=ZMySQLDA-3.1.1.tar.bz2
ZMYSQLDA_DIR=ZMySQLDA
PYOAI_TB=pyoai-2.4.3.tar.bz2
PYOAI_DIR=pyoai-2.4.3

# Capture current working directory for build script
PWD=`pwd`

PACKAGES_DIR=packages
PKG=$PWD/$PACKAGES_DIR

GNU_TAR=`which tar`
GCC=`which gcc`
GPP=`which g++`
GNU_MAKE=`which make`
TAR_BZIP2_FLAG="--bzip2"
#TAR_BZIP2_FLAG="-j"

# The Unified Installer requires root privileges to install
ROOT_INSTALL=1

#####
# Verifica se existe uma instalacao do OpenLegis 2.6
if [ -d /var/interlegis/SAPL-2.6/ ]; then
    INST_PATH="/var/interlegis/SAPL-2.6"
else
    INST_PATH="/var/interlegis/SAPL-2.6"
fi

if [ -e $INST_PATH ]; then
    echo ""
    echo -e "\033[1;31mUma instalação do OpenLegis 2.6 foi detectada\033[m"
    echo -e "\033[1;31mRemova a versão instalada e execute o procedimento descrito em:\033[m"
    echo -e "\033[1;31mhttp://openlegis.googlecode.com/wiki/InstalacaoOpenLegis27\033[m"
    echo -e "\033[1;31mInstalação abortada\033[m"
    echo ""
    exit 1
fi

#################################################################
# Exit if potential conflict with existing install at $INSTALL_HOME
if [ -e $INSTALL_HOME ]
then
    echo ""
    echo -e "\033[1;31mUma instalação do OpenLegis foi detectada em $INSTALL_HOME.\033[m"
    echo -e "\033[1;31mInstalação abortada\033[m"
    echo ""
    exit 1
fi

# Verifica se existe o mysql server e se o serviço está sendo executado

mysql_pid=`ps ax | grep mysqld_safe  | grep \/bin\/ | cut -d " " -f1`
mysql_port=`netstat -ant | grep 3306 | cut -d ':' -f 2 | cut -d ' ' -f 1`


if [ ! $mysql_pid ] && [ ! $mysql_port ]; then

    echo ""
    echo -e "\033[1;31mO Mysql Server não está em execução\033[m"
    echo -e "\033[1;31mPara continuar a instalação, o MySQL deve estar em execução.\033[m"
    echo -e "\033[1;31mInstalação abortada\033[m"
    echo ""
    exit 1
fi

# Caso esteja sendo executado, pergunta o usuário e senha

ok=0
while [ $ok = 0 ]; do

    echo "Digite o nome do usuário MySQL: "
    read usuario

    if [ -z $usuario ]; then
        echo -e "\033[1;31mO nome do usuário não pode estar em branco!\033[m";
    else
        ok=1
    fi
    
done

echo "Digite a senha do usuário root do MySQL: "
read senha

echo "Verificando usuário e senha: "

if [ -z $senha ]; then
    mysqladmin status -u $usuario > /dev/null 2>&1
else
    mysqladmin status -u $usuario --password=$senha > /dev/null 2>&1
fi

if [ $? -gt 0 ]; then

    echo ""
    echo -e "\033[1;31mO usuário e/ou senha estão incorretos!\033[m";
    echo -e "\033[1;31mInstalação abortada\033[m"
    echo ""
    exit 1
fi

# Verifica se existe o banco 'interlegis'
if [ -z $senha ]; then
    mysqlcheck interlegis -u $usuario > /dev/null 2>&1
else
    mysqlcheck interlegis -u $usuario --password=$senha > /dev/null 2>&1
fi

if [ "$?" = "0" ]; then

    echo ""
    echo -e "\033[1;31mUma instalação do OpenLegis foi detectada\033[m"
    echo -e "\033[1;31mO instalador encontrou o banco de dados 'interlegis' no servidor MySQL\033[m"
    echo -e "\033[1;31mExecute a instalação descrita em:\033[m"
    echo -e "\033[1;31mhttp://openlegis.googlecode.com/wiki/InstalacaoOpenLegis27\033[m"
    echo -e "\033[1;31mInstalação abortada\033[m"
    echo ""
    exit 1
fi

############################
# Configure zlib and libjpeg
#
# This install requires the zlib and libjpeg libraries, which are
# usually installed as system libraries.
# Set the options below to
#   auto -   to have this program determine whether or not you need the
#            library installed, and where.
#   global - to force install to /usr/local/ (requires root)
#   local  - to force install to $INSTALL_HOME (or $LOCAL_HOME) for static link
#   no     - to force no install
INSTALL_ZLIB=auto
INSTALL_JPEG=auto

# library need determination
if [ $INSTALL_ZLIB = "auto" ]
then
    # check for zconf.h, zlib.h, libz.[so|a]
    if [ -e /usr/include/zconf.h ] || [ -e /usr/local/include/zconf.h ]
    then
        HAVE_ZCONF=1
        #echo have zconf
    else
        HAVE_ZCONF=0
        #echo no zconf
    fi
        if [ -e /usr/include/zlib.h ] || [ -e /usr/local/include/zlib.h ]
        then
                HAVE_ZLIB=1
                #echo have zlib
        else
                HAVE_ZLIB=0
                #echo no zlib
        fi
        if [ -e /usr/lib/libz.so ] || [ -e /usr/local/lib/libz.so ] || \
       [ -e /usr/lib/libz.dylib ] || [ -e /usr/local/lib/libz.dylib ] || \
       [ -e /usr/lib/libz.a ] || [ -e /usr/local/lib/libz.a ]
        then
                HAVE_LIBZ=1
                #echo have libz
        else
                HAVE_LIBZ=0
                #echo no libz
        fi
    if [ $HAVE_ZCONF -eq 1 ] && [ $HAVE_ZLIB -eq 1 ] && [ $HAVE_LIBZ -eq 1 ]
    then
        INSTALL_ZLIB=no
        #echo do not install zlib
    fi
    if [ $INSTALL_ZLIB = "auto" ] && [ $ROOT_INSTALL -eq 1 ]
    then
        INSTALL_ZLIB="global"
    fi
    if [ $INSTALL_ZLIB = "auto" ]
    then
        INSTALL_ZLIB="local"
    fi
    echo -e "\033[32mzlib installation: $INSTALL_ZLIB\033[m"
fi

if [ $INSTALL_JPEG = "auto" ]
then
    # check for jpeglib.h and libjpeg.[so|a]
    if [ -e /usr/include/jpeglib.h ] || [ -e /usr/local/include/jpeglib.h ]
    then
        HAVE_JPEGH=1
    else
        HAVE_JPEGH=0
    fi
    if [ -e /usr/lib/libjpeg.so ] || [ -e /usr/local/lib/libjpeg.so ] || \
       [ -e /usr/lib/libjpeg.dylib ] || [ -e /usr/local/lib/libjpeg.dylib ] || \
       [ -e /usr/lib/libjpeg.a ] || [ -e /usr/local/lib/libjpeg.a ]
    then
        HAVE_LIBJPEG=1
    else
        HAVE_LIBJPEG=0
    fi
    if [ $HAVE_JPEGH -eq 1 ] && [ $HAVE_LIBJPEG -eq 1 ]
    then
        INSTALL_JPEG="no"
    fi
    if [ $INSTALL_JPEG = "auto" ] && [ $ROOT_INSTALL -eq 1 ]
    then
        INSTALL_JPEG="global"
    fi
    if [ $INSTALL_JPEG = "auto" ]
    then
        INSTALL_JPEG="local"
    fi
    echo -e "\033[32mlibjpeg installation: $INSTALL_JPEG\033[m"
fi


#############################
# Preflight dependency checks
#
# Abort install if not running as root
if [ `whoami` != root ] && [ $ROOT_INSTALL -eq 1 ]
then
    echo "Este script precisa ser executado como root.  Uso: sudo ./install.sh  ( or su ; ./install.sh )."
    exit 1
fi

# Abort install if no gcc
if [ ! -e /usr/bin/gcc ]
then
    echo "Importante: gcc é necessário para a instalação. Saindo agora."
    exit 1
fi

# Abort install if no g++
if [ ! -e /usr/bin/g++ ]
then
    echo "Importante: g++ é necessário para a instalação. Saindo agora."
    exit 1
fi

# Abort install if no make
if [ ! -e /usr/bin/make ]
then
    echo "Importante: make é necessário para a instalação. Saindo agora."
    exit 1
fi

# Abort install if this script is not run from within it's parent folder
if [ ! -e $PACKAGES_DIR ]
then
    echo "Importante: Este script precisa ser executado dentro de um diretório.  Uso: sudo ./install.sh  (or su ; ./install.sh)"
    exit 1
fi


#################################
# Install will begin in 3 seconds
echo ""
echo -e "\033[32mInstalando OpenLegis 2.7 em $INSTALL_HOME\033[m"
sleep 3
echo ""


##################
# build zlib 1.2.3
# Note that, even though we're building static libraries, python
# is going to try to build a shared library for it's own use.
# The "-fPIC" flag is thus required for some platforms.
if [ "X$INSTALL_ZLIB" = "Xglobal" ]
then
    echo "Compilando e instalando zlib ..."
    cd $PKG
    $GNU_TAR $TAR_BZIP2_FLAG -xf $ZLIB_TB
    chmod -R 775 $ZLIB_DIR
    cd $ZLIB_DIR
    CFLAGS="-fPIC" ./configure
    $GNU_MAKE test
    $GNU_MAKE install
    cd $PKG
    if [ -d $ZLIB_DIR ]
    then
        rm -rf $ZLIB_DIR
    fi
elif [ "X$INSTALL_ZLIB" = "Xlocal" ]
then
    echo "Compilando e instalando zlib local ..."
    cd $PKG
    $GNU_TAR $TAR_BZIP2_FLAG -xf $ZLIB_TB
    chmod -R 775 $ZLIB_DIR
    cd $ZLIB_DIR
    CFLAGS="-fPIC" ./configure --prefix=$LOCAL_HOME
    $GNU_MAKE test
    $GNU_MAKE install
    cd $PKG
    if [ -d $ZLIB_DIR ]
    then
        rm -rf $ZLIB_DIR
    fi
    if [ ! -e "$LOCAL_HOME/lib/libz.a" ]
    then
        echo "Instalação local da zlib falhou"
        exit 1
    fi
else
    echo "Pulando compilação e instalação da zlib"
fi


###################
# build libjpeg v6b
if [ "X$INSTALL_JPEG" = "Xglobal" ]
then
    echo "Compilando e instalando bibliotecas jpeg no sistema ..."

    # It's not impossible that the /usr/local hierarchy doesn't
    # exist. The libjpeg install will not create it itself.
    # (The zlib install will, but we can't count on it having
    # run, since we've made it an option.)
    if [ ! -e /usr/local ]
    then
        mkdir /usr/local
    fi
    if [ ! -e /usr/local/bin ]
    then
        mkdir /usr/local/bin
    fi
    if [ ! -e /usr/local/include ]
    then
        mkdir /usr/local/include
    fi
    if [ ! -e /usr/local/lib ]
    then
        mkdir /usr/local/lib
    fi
    if [ ! -e /usr/local/man ]
    then
        mkdir /usr/local/man
    fi
    if [ ! -e /usr/local/man/man1 ]
    then
        mkdir /usr/local/man/man1
    fi

    cd $PKG
    $GNU_TAR $TAR_BZIP2_FLAG -xf $JPEG_TB
    chmod -R 775 $JPEG_DIR
    cd $JPEG_DIR
    # Oddities to workaround: on Mac OS X, using the "--enable-static"
    # flag will cause the make to fail. So, we need to manually
    # create and place the static library.
    ./configure CFLAGS='-fPIC'
    $GNU_MAKE
    $GNU_MAKE install
    ranlib libjpeg.a
    cp libjpeg.a /usr/local/lib
    cp *.h /usr/local/include
    cd $PKG
    if [ -d $JPEG_DIR ]
    then
            rm -rf $JPEG_DIR
    fi
elif [ "X$INSTALL_JPEG" = "Xlocal" ]
then
    echo "Compilando e instalando bibliotecas jpeg locais ..."

    mkdir $LOCAL_HOME/lib
    mkdir $LOCAL_HOME/bin
    mkdir $LOCAL_HOME/include
    mkdir $LOCAL_HOME/man
    mkdir $LOCAL_HOME/man/man1

    cd $PKG
    $GNU_TAR $TAR_BZIP2_FLAG -xf $JPEG_TB
    chmod -R 775 $JPEG_DIR
    cd $JPEG_DIR
    # Oddities to workaround: on Mac OS X, using the "--enable-static"
    # flag will cause the make to fail. So, we need to manually
    # create and place the static library.
    ./configure CFLAGS='-fPIC' --prefix=$LOCAL_HOME
    $GNU_MAKE
    $GNU_MAKE install
    # --enable-static flag doesn't work on OS X, make sure
    # we get an install anyway
    if [ ! -e "$LOCAL_HOME/lib/libjpeg.a" ]
    then
        ranlib libjpeg.a
        cp libjpeg.a $LOCAL_HOME/lib
        cp *.h $LOCAL_HOME/include
    fi

    if [ ! -e "$LOCAL_HOME/lib/libjpeg.a" ]
    then
        echo "Instalação local da libjpeg falhou"
        exit 1
    fi

    cd $PKG
    if [ -d $JPEG_DIR ]
    then
            rm -rf $JPEG_DIR
    fi
else
    echo "Pulando compilação e instalação da libjpeg"
fi

######################################
# Build Python (with ssl and readline support)
# note: Install readline before running this script
echo -e "\033[32mInstalando Python 2.4.6...\033[m"
cd $PKG
$GNU_TAR -jxf $PYTHON_TB
chmod -R 775 $PYTHON_DIR
cd $PYTHON_DIR
# Look for Leopard
uname -v | grep "Darwin Kernel Version 9" > /dev/null
if [ "$?" = "0" ]; then
    # patch for Leopard setpgrp
    sed -E -e "s|(CPPFLAGS=.+)|\\1 -D__DARWIN_UNIX03|" -i.bak Makefile.pre.in
    # if /opt/local is available, make sure it's included in the component
    # build so that we can get fixed readline lib
    if [ -d /opt/local/include ] && [ -d /opt/local/lib ]; then
        sed -E -e "s|#(add_dir_to_list\(self\.compiler\..+_dirs, '/opt/local/)|\\1|" -i.bak setup.py
    fi
fi
./configure \
    --prefix=$PY_HOME \
    --with-readline \
    --with-zlib \
    --with-ssl \
    --disable-tk \
    --with-gcc="$GCC"
make
make install
# make sistecustomize.py file
touch $SITECUSTOMIZE_FILE
echo "import sys" >> "$SITECUSTOMIZE_FILE"
echo "sys.setdefaultencoding('utf-8')" >> "$SITECUSTOMIZE_FILE"

cd $PKG
if [ -d $PYTHON_DIR ]
then
    rm -rf $PYTHON_DIR
fi

#########################
# install ReportLab 2.5
echo -e "\033[32mInstalando ReportLab...\033[m"
cd $PKG
$GNU_TAR -jxf $REPLAB_TB
mv $REPLAB_DIR/reportlab $SITE_PACKAGES/reportlab
cd $PKG
if [ -d $REPLAB_DIR ]
then
    rm -rf $REPLAB_DIR
fi

########################
# install trml2pdf 1.2
echo -e "\033[32mInstalando trml2pdf...\033[m"
cd $PKG
$GNU_TAR -jxf $TRML2PDF_TB
mv $TRML2PDF_DIR $SITE_PACKAGES/$TRML2PDF_DIR
cd $PKG
if [ -d $TRML2PDF_DIR ]
then
    rm -rf $TRML2PDF_DIR
fi

###################
# build PyXML 0.8.4
echo -e "\033[32mCompilando e instalando PyXML ...\033[m"
cd $PKG
$GNU_TAR -jxf $PYXML_TB
chmod -R 775 $PYXML_DIR
cd $PYXML_DIR
$PY ./setup.py build
$PY ./setup.py install
cd $PKG
if [ -d $PYXML_DIR ]
then
    rm -rf $PYXML_DIR
fi

###################
# build distribute 0.6.49
echo -e "\033[32mCompilando e instalando distribute ...\033[m"
cd $PKG
$GNU_TAR -jxf $DISTRIBUTE_TB
chmod -R 775 $DISTRIBUTE_DIR
cd $DISTRIBUTE_DIR
$PY ./setup.py build
$PY ./setup.py install
cd $PKG
if [ -d $DISTRIBUTE_DIR ]
then
    rm -rf $DISTRIBUTE_DIR
fi

###################
# install pip 
echo -e "\033[32mInstalando pip via distribute ...\033[m"
$PY $EASY_INSTALL pip==1.1

#################
# build PIL 1.1.7
echo -e "\033[32mCompilando e instalando PIL ...\033[m"
cd $PKG
$GNU_TAR -jxf $PIL_TB
chmod -R 775 $PIL_DIR
cd $PIL_DIR
$PY ./setup.py build_ext -i
$PY ./selftest.py
$PY ./setup.py install
cd $PKG
if [ -d $PIL_DIR ]
then
    rm -rf $PIL_DIR
fi

#####################
# install ElementTree
echo -e "\033[32mInstalando ElementTree ...\033[m"
cd $PKG
$GNU_TAR -jxf $ETREE_TB
chmod -R 775 $ETREE_DIR
cd $ETREE_DIR
$PY ./setup.py build
$PY ./setup.py install
cd $PKG
if [ -d $ETREE_DIR ]
then
        rm -rf $ETREE_DIR
fi

#################
# install lxml
echo -e "\033[32mBaixando e instalando lxml e suas dependências ...\033[m"
$PIP install lxml==2.3.1

#################
# install libxml2-python
echo -e "\033[32mInstalando libxml2-python ...\033[m"
$PIP install ftp://xmlsoft.org/libxml2/python/libxml2-python-2.6.21.tar.gz

##########################
# install PyOAI 2.4.3
echo -e "\033[32mCompilando e instalando PyOAI (OAI-PMH)...\033[m"
cd $PKG
$GNU_TAR -jxf $PYOAI_TB
chmod -R 775 $PYOAI_DIR
cd $PYOAI_DIR
$PY ./setup.py build
$PY ./setup.py install
cd $PKG
if [ -d $PYOAI_DIR ]
then
    rm -rf $PYOAI_DIR
fi

#################
# install appy.pod
echo -e "\033[32mBaixando e instalando appy.pod e suas dependências ...\033[m"
$PIP install appy

#################
# install uuid
echo -e "\033[32mBaixando e instalando uuid ...\033[m"
$PIP install uuid

###################
# build Zope 2.9.12
echo -e "\033[32mCompilando e instalando Zope 2.9.12 ...\033[m"
cd $PKG
$GNU_TAR -jxf $ZOPE_TB
chmod -R 775 $ZOPE_DIR
cd $ZOPE_DIR
./configure --with-python=$PY --prefix=$ZOPE_HOME
make
make install
cd $PKG
if [ -d $ZOPE_DIR ]
then
    rm -rf $ZOPE_DIR
fi

###################
# install MySQL-python
echo -e "\033[32mCompilando e instalando MySQL-python ...\033[m"
cd $PKG
$GNU_TAR -jxf $MYSQLPYTHON_TB
cd $MYSQLPYTHON_DIR
$PY setup.py build
$PY setup.py install
if [ $? -gt 0 ]; then
    echo ""
    echo -e "\033[1;31mErro na compilação do MySQL-python!\033[m";
    echo -e "\033[1;31mInstalação abortada!\033[m";
    echo ""
    exit 1
fi
cd $PKG
if [ -d $MYSQLPYTHON_DIR ]
then
    rm -rf $MYSQLPYTHON_DIR
fi

######################
# Postinstall steps
######################

##########################
# Generate random password
echo -e "\033[32mGerando senha aleatória ...\033[m"
cd $PKG
$GNU_TAR -jxf $HSCRIPTS_TB
chmod -R 775 $HSCRIPTS_DIR
cd $HSCRIPTS_DIR
PASSWORD_SCRIPT=./generateRandomPassword.py
PASSWORD=`$PY $PASSWORD_SCRIPT`
cd $PKG

######################
# Create OpenLegis instance
echo -e "\033[32mCriando instancia OpenLegis ...\033[m"
$ZOPE_HOME/bin/mkzopeinstance.py --dir=$SAPL_HOME --user=admin:$PASSWORD

#########################################
# Configura ponto de montagem
echo "<zodb_db documentos>
    # Zodb para armazenar documentos 
    <filestorage>
      path $SAPL_HOME/var/DocumentosSapl.fs
    </filestorage>
    mount-point /sapl/sapl_documentos
</zodb_db>

locale pt_BR.UTF-8

default-zpublisher-encoding utf-8

rest-input-encoding utf-8

rest-output-encoding utf-8" >> $SAPL_HOME/etc/zope.conf

#####################################
# Set effective-user in etc/zope.conf
# set user in ZEO server
mv $SAPL_HOME/etc/zope.conf $SAPL_HOME/etc/zope.conf.tmp
cat $SAPL_HOME/etc/zope.conf.tmp | sed 's/^.*#.*effective-user.*chrism.*$/effective-user zope/g'> $SAPL_HOME/etc/zope.conf
rm $SAPL_HOME/etc/zope.conf.tmp

###############################################################
# Extract and move ExtFile tarball to Products folder of Instance
echo -e "\033[32mExtraindo ExtFile tarball ...\033[m"
cp $PKG/$EXTFILE_TB $INSTALL_HOME/$EXTFILE_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$EXTFILE_TB
rm $INSTALL_HOME/$EXTFILE_TB
cp $INSTALL_HOME/$EXTFILE_DIR/extfile.ini $SAPL_HOME/etc/extfile.ini
mv $INSTALL_HOME/$EXTFILE_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move ExternalEditor tarball to Products folder of Instance
echo -e "\033[32mExtraindo ExternalEditor tarball ...\033[m"
cp $PKG/$EXTEDIT_TB $INSTALL_HOME/$EXTEDIT_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$EXTEDIT_TB
rm $INSTALL_HOME/$EXTEDIT_TB
mv $INSTALL_HOME/$EXTEDIT_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move SDE tarball to Products folder of Instance
echo -e "\033[32mExtraindo SDE tarball ...\033[m"
cp $PKG/$SDE_TB $INSTALL_HOME/$SDE_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$SDE_TB
rm $INSTALL_HOME/$SDE_TB
mv $INSTALL_HOME/$SDE_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move ZMySQLDA tarball to Products folder of Instance
echo -e "\033[32mExtraindo ZMySQLDA tarball ...\033[m"
cp $PKG/$ZMYSQLDA_TB $INSTALL_HOME/$ZMYSQLDA_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$ZMYSQLDA_TB
rm $INSTALL_HOME/$ZMYSQLDA_TB
mv $INSTALL_HOME/$ZMYSQLDA_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move CMF tarball to Products folder of Instance
echo -e "\033[32mExtraindo CMF tarball ...\033[m"
cp $PKG/$CMF_TB $INSTALL_HOME/$CMF_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$CMF_TB
rm $INSTALL_HOME/$CMF_TB
mv $INSTALL_HOME/$CMF_DIR/* $PRODUCTS_HOME
if [ -d $CMF_DIR ]
then
    rm -rf $CMF_DIR
fi
chmod -R 775 $PRODUCTS_HOME
cd $PKG

######################
# Install TextIndexNG2
echo -e "\033[32mInstalando TextIndexNG2\033[m"
cp $PKG/$TXNG2_TB $PRODUCTS_HOME
cd $PRODUCTS_HOME
$GNU_TAR -jxf ./$TXNG2_TB
chmod -R 775 ./$TXNG2_DIR
rm $PRODUCTS_HOME/$TXNG2_TB
cd $PRODUCTS_HOME/$TXNG2_DIR
$PY ./setup.py install
cd $PKG

###############################################################
# Extract and move AdvancedQuery tarball to Products folder of Instance
echo -e "\033[32mInstalando o AdvancedQuery ...\033[m"
$GNU_TAR -jxf ./$ADVANCEDQUERY_TB
mv $ADVANCEDQUERY_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move MailDropHost tarball to Products folder of Instance
echo -e "\033[32mInstalando o MailDropHost ...\033[m"
$GNU_TAR -jxf ./$MAILDHOST_TB
mv $MAILDHOST_DIR $PRODUCTS_HOME
chmod -R 775 $PRODUCTS_HOME
cd $PKG

###############################################################
# Extract and move SAPL tarball to Products folder of Instance
echo -e "\033[32mExtraindo o OpenLegis tarball ...\033[m"
cp $PKG/$SAPL_TB $INSTALL_HOME/$SAPL_TB
cd $INSTALL_HOME
$GNU_TAR -jxf ./$SAPL_TB
svn up $SAPL_DIR
mv $SAPL_DIR $PRODUCTS_HOME
mv $PRODUCTS_HOME/$SAPL_DIR/Products/PythonModules $PRODUCTS_HOME
rm $INSTALL_HOME/$SAPL_TB
chmod -R 775 $PRODUCTS_HOME
cd $PKG

########################
# Write password to file
echo -e "\033[32mCriando arquivo com senha aleatória ...\033[m"
touch $PWFILE
# Write admin password and startup/shutdown info to password file
echo "Use as informações da conta a seguir para logar na Zope Management Interface" >> "$PWFILE"
echo "A conta possui privilégios de 'Manager'." >> "$PWFILE"
echo " " >> "$PWFILE"
echo "  Username: admin" >> "$PWFILE"
echo "  Senha: $PASSWORD" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "Antes de iniciar o OpenLegis, você deverá rever as configurações em:" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "  $SAPL_HOME/etc/zope.conf" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "Ajuste as portas do OpenLegis antes de inicar seu uso, caso necessário" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "Para iniciar o OpenLegis, execute o seguinte comando no terminal:" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "  sudo $SAPL_STARTUP_SCRIPT" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "Para parar o OpenLegis, execute o seguinte comando no terminal:" >> "$PWFILE"
echo " " >> "$PWFILE"
echo "  sudo $SAPL_SHUTDOWN_SCRIPT" >> "$PWFILE"
echo " " >> "$PWFILE"

####################################################
# Write OpenLegis startup/shutdown/restart scripts to file

# Write startup script
echo -e "\033[32mEscrevendo o script de inicialização ...\033[m"
touch $SAPL_STARTUP_SCRIPT
echo "#!/bin/sh" >> "$SAPL_STARTUP_SCRIPT"
echo "#" >> "$SAPL_STARTUP_SCRIPT"
echo "# SAPL startup script" >> "$SAPL_STARTUP_SCRIPT"
echo "#" >> "$SAPL_STARTUP_SCRIPT"
echo "echo 'Iniciando OpenLegis server...'" >> "$SAPL_STARTUP_SCRIPT"
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >> "$SAPL_STARTUP_SCRIPT"
echo "$SAPL_HOME/bin/zopectl start" >> "$SAPL_STARTUP_SCRIPT"

# Configuring the system startup during boot
echo -e "\033[32mConfigurando script de inicialização durante o boot...\033[m"
echo "#" >> /etc/init.d/rc.local
echo "#Inicialização do OpenLegis 2.7" >> /etc/init.d/rc.local
echo "$SAPL_STARTUP_SCRIPT" >> /etc/init.d/rc.local

# Write shutdown script
echo -e "\033[32mEscrevendo o script de desligamento ...\033[m"
touch $SAPL_SHUTDOWN_SCRIPT
echo "#!/bin/sh" >> "$SAPL_SHUTDOWN_SCRIPT"
echo "#" >> "$SAPL_SHUTDOWN_SCRIPT"
echo "# OpenLegis shutdown script" >> "$SAPL_SHUTDOWN_SCRIPT"
echo "#" >> "$SAPL_SHUTDOWN_SCRIPT"
echo "echo 'Parando OpenLegis server...'" >> "$SAPL_SHUTDOWN_SCRIPT"
echo "$SAPL_HOME/bin/zopectl stop" >> "$SAPL_SHUTDOWN_SCRIPT"

# Write restart script
echo -e "\033[32mEscrevendo o script de reinicialização ...\033[m"
touch $SAPL_RESTART_SCRIPT
echo "#!/bin/sh" >> "$SAPL_RESTART_SCRIPT"
echo "#" >> "$SAPL_RESTART_SCRIPT"
echo "# SAPL restart script" >> "$SAPL_RESTART_SCRIPT"
echo "#" >> "$SAPL_RESTART_SCRIPT"
echo "echo 'Reiniciando OpenLegis server...'" >> "$SAPL_RESTART_SCRIPT"
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >> "$SAPL_RESTART_SCRIPT"
echo "$SAPL_HOME/bin/zopectl restart" >> "$SAPL_RESTART_SCRIPT"

#########################################################
# Fix path for Zope command line utils (repozo.py et.al.)
echo -e "\033[32mEscrevendo o arquivo de script restart ...\033[m"
echo "$INSTALL_HOME/lib/python" > "$SITE_PACKAGES/zope.pth"

#####################################
# Clean up any .DS_Store files (OS X)
find $INSTALL_HOME -name '.DS_Store' -delete

################################################
# Add system user account
echo -e "\033[32mAdicionando usuario 'zope' ao sistema ...\033[m"
# Add unprivileged user account via 'useradd', if exists (Linux)
if [ -e /usr/sbin/useradd ]
then
    /usr/sbin/useradd $EFFECTIVE_USER
# Add unprivileged user account via 'adduser', if exists (*BSD)
elif [ -e /usr/sbin/adduser ]
then
    /usr/sbin/adduser -f $PKG/$HSCRIPTS_DIR/adduser.txt
fi

###########################################
# Clean up helper scripts directory
cd $PKG
if [ -d $HSCRIPTS_DIR ]
then
    rm -rf $HSCRIPTS_DIR
fi

###########################################
# Set appropriate ownership and permissions
echo -e "\033[32mAjustando as propriedades e permissões apropriadas nos arquivos ...\033[m"
chmod -R 775 $INSTALL_HOME
chmod 660 "$PWFILE"
if [ `whoami` = root ]
then
    chown -R $EFFECTIVE_USER $INSTALL_HOME
fi

######################
# Import sql script to database
echo -e "\033[32mCriando o banco de dados MySQL e importando estrutura de tabelas\033[m"
if [ -z $senha ]; then
    mysql -h 127.0.0.1 -u $usuario < $PRODUCTS_HOME/$SAPL_DIR/instalacao/sapl_create.sql
    mysql -h 127.0.0.1 -u $usuario interlegis < $PRODUCTS_HOME/$SAPL_DIR/instalacao/sapl.sql
else
    mysql -h 127.0.0.1 -u $usuario --password=$senha < $PRODUCTS_HOME/$SAPL_DIR/instalacao/sapl_create.sql
    mysql -h 127.0.0.1 -u $usuario interlegis --password=$senha < $PRODUCTS_HOME/$SAPL_DIR/instalacao/sapl.sql
fi
if [ $? -gt 0 ]; then
    echo ""
    echo -e "\033[1;31mErro na importação da estrutura da base de dados!\033[m";
    echo -e "\033[1;31mVerifique o usuário e senha e repita o procedimento de instalação!\033[m";
    echo -e "\033[1;31mInstalação abortada!\033[m";
    echo ""
    exit 1
fi

#######################
# Building the OpenLegis instance
echo -e "\033[32mConfigurando a instância OpenLegis\033[m"
$SAPL_SHUTDOWN_SCRIPT
sleep 1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
ln -s $PRODUCTS_HOME/$SAPL_DIR/import/* $SAPL_HOME/import/
ln -s $PRODUCTS_HOME/$SAPL_DIR/Extensions/* $SAPL_HOME/Extensions/
cp $PRODUCTS_HOME/$SAPL_DIR/instalacao/libreoffice-server /etc/init.d/
chmod 0755 /etc/init.d/libreoffice-server
update-rc.d libreoffice-server defaults
service libreoffice-server start
$GNU_TAR -jxf $PRODUCTS_HOME/$SAPL_DIR/instalacao/modelos.tar.bz2 -C $SAPL_HOME/
chown -R $EFFECTIVE_USER:$EFFECTIVE_USER $SAPL_HOME/static
$SAPL_HOME/bin/zopectl run $PRODUCTS_HOME/$SAPL_DIR/instalacao/sapl_configurador.py
$SAPL_STARTUP_SCRIPT
sleep 1

#######################
# Conclude installation
if [ -d $INSTALL_HOME ]
    then
    mkdir $RECEIPTS_HOME
    echo "Instalação do OpenLegis 2.7 finalizada em" `date` > $RECEIPTS_HOME/installReceipt.txt
    echo " "
    echo "#####################################################################"
    echo "######################  Instalação Concluída ########################"
    echo " "
    cat $INSTALL_HOME/adminPassword.txt
    echo " "
    echo "O sistema OpenLegis foi instalado com sucesso em $INSTALL_HOME"
    echo "Consulte o arquivo $INSTALL_HOME/adminPassword.txt para verificar a senha e conhecer as instruções para inicialização"
    echo " "
    echo "Este instalador é mantido por OpenLegis (contato@openlegis.com.br)"
    echo " "
else
    echo "Ocorreram erros durante a instalação. Por favor leia o LEIAME.txt e tente novamente."
fi
