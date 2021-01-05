from setuptools import setup, find_packages
import os

version = '1.5dev'

form_requires = [
    'grokcore.formlib',
    'five.formlib',
    'zope.formlib',
    ]
layout_requires = [
    'grokcore.layout',
    ]
test_requires = form_requires + layout_requires + [
    ]

setup(name='five.grok',
      version=version,
      description="Grok-like layer for Zope",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Zope4",
        ],
      keywords='zope4 grok',
      author='OpenLegis',
      author_email='contato@openlegis.com.br',
      url='https://github.com/openlegis-br',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['five'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'martian',
        'Zope2',
        'five.localsitemanager',
        'grokcore.annotation',
        'grokcore.component',
        'grokcore.security',
        'grokcore.site',
        'grokcore.view',
        'grokcore.viewlet',
        'zope.annotation',
        'zope.component',
        'zope.container',
        'zope.contentprovider',
        'zope.interface',
        'zope.location',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.traversing',
        ],
      extras_require={
        'form': form_requires,
        'layout': layout_requires,
        'test': form_requires},
      )
