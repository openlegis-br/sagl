from setuptools import setup, find_packages
import os

version = '3.1'

setup(name='il.sapl',
      version=version,
      description="",
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
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['il'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Pillow',
          'Products.SecureMailHost',
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
          'uuid',
          'zope.globalrequest==1.0',
          'simplejson',
          'five.grok == 1.3.2',
          'five.formlib == 1.0.4',
          'five.localsitemanager == 2.0.5',
          'grokcore.annotation == 1.3',
          'grokcore.component == 2.5',
          'grokcore.formlib == 1.9',
          'grokcore.layout == 1.5.1',
          'grokcore.security == 1.6.1',
          'grokcore.site == 1.6.1',
          'grokcore.view == 2.7',
          'grokcore.viewlet == 1.10.1',
          'martian == 0.14',
          'reportlab',
          'trml2pdf==1.2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
