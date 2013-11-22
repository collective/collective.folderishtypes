from setuptools import setup, find_packages

version = '1.8'

setup(name='collective.folderishtypes',
      version=version,
      description="Provides folderish types as a replacement for some ATContentTypes",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      # Get more strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='ATContentTypes Archetypes Plone Folderish',
      author='Johannes Raggam',
      author_email='johannes@raggam.co.at',
      url='http://github.com/collective/collective.folderishtypes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
