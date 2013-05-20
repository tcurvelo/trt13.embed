# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='trt13.portal.embedvideo',
      version=version,
      description="Provê conteúdo para vídeos embarcados (ex: mms://)",
      long_description=open("README.rst").read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")
      ).read(),
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.2",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='python plone zope trt13',
      author='Thiago Curvelo',
      author_email='tcurvelo@gmail.com',
      url='http://www.trt13.jus.br',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['trt13', 'trt13.portal'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Pillow',
          'Plone>=4.2',
          'plone.api',
          'plone.app.dexterity[grok]',
          'plone.namedfile[blobs]',
          'plone.formwidget.namedfile',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.app.robotframework',
          ]
      },
      entry_points="""
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
