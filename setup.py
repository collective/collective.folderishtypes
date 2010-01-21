# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.folderishtypes',
      version=version,
      description="Provides folderish types as a replacement for some ATContentTypes",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='ATContentTypes Archetypes Plone Folderish',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='http://github.com/thet/collective.folderishtypes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      )
