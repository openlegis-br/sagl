from setuptools import setup, find_packages
import os

version = '4.0'

setup(name='openlegis.sagl',
      version=version,
      description="SAGL-OpenLegis",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='OpenLegis',
      author_email='contato@openlegis.com.br',
      url='https://github.com/openlegis-br/sagl/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openlegis'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.zrs',
          'Pillow',
          'Products.CMFActionIcons',
          'Products.CMFCalendar',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFFormController',
          'Products.CMFTopic',
          'Products.CMFUid',
          'Products.DCWorkflow',
          'Products.ExternalEditor',
          'Products.GenericSetup',
          'Products.ZMySQLDA',
          'Products.AdvancedQuery',
          'Products.TextIndexNG3',
          'Products.ExtendedPathIndex',
          'Zope2',
          'z3c.autoinclude',
          'pyoai',
          'appy',
          'lxml',
          'zope.globalrequest',
          'simplejson',
          'five.grok',
          'five.formlib',
          'five.localsitemanager',
          'grokcore.annotation',
          'grokcore.component',
          'grokcore.formlib',
          'grokcore.layout',
          'grokcore.security',
          'grokcore.site',
          'grokcore.view',
          'grokcore.viewlet',
          'martian',
          'reportlab',
          'trml2pdf==1.2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
