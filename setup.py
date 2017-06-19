# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '1.0'

setup(name='trt13.embed',
      version=version,
      description="Provê tipo para conteúdos embarcados",
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
      namespace_packages=['trt13'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Pillow',
          'Products.CMFPlone',
          'collective.js.jqueryui',
          'plone.api',
          'plone.app.dexterity [grok]',
          'plone.app.contenttypes',
          'plone.formwidget.namedfile',
          'plone.namedfile [blobs]',
      ],
      extras_require={
          'test': [
              'plone.app.testing [robot]',
              'plone.app.robotframework',
          ]
      },
      entry_points="""
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
