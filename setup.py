from setuptools import setup
from setuptools import find_packages

version = '2.0dev'
title = 'collective.folderishtypes'
description = "Folderish News Item, Document and Event as replacement for default types."  # noqa
long_desc = open("README.rst").read() + "\n" + open("CHANGES.rst").read()

setup(
    name=title,
    version=version,
    description=description,
    long_description=long_desc,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='content types plone folderish',
    author='Johannes Raggam',
    author_email='johannes@raggam.co.at',
    url='http://github.com/collective/collective.folderishtypes',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'dexterity': ['plone.app.contenttypes', ],
        'migration': ['Products.contentmigration', ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
