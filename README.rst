Introduction
============

Provides the types "Folderish Event", "Folderish News Item" and
"Folderish Document" as replacements for their `Plone`_ ATContentTypes equivalents.
Those types are able to hold any other content, like a Folder.

There is a "portlet" profile, which installs a portlet to show the contents of
an folderish type.

You can limit the types, which can be added to FolderishTypes by providing
a Generic Setup import type configuration.

The reason for this package is, that in my experience it's easier to group
related content together at one place. An article about something fancy might
have an image gallery associated with it as well as some pdf-downloads. With
this package you can put everything inside the article.
Another use case is that you can structure content hierarchically and don't need
to define "default pages" - a concept hard to understand and handle (see:
https://sixfeetup.com/blog/plone-drupal-features )

Alexander Limi also wished folderish content back in 2008:
"#10: Content re-use is overrated — people like folderish"
https://limi.net/things-plone


How to migrate Products.PloneArticle documents to Folderish Document
====================================================================

A upgrade step "PloneArticle to Folderish Document"	in the
``collective.folderishtypes`` default profile for migrating PloneArticle objects to
Folderish Document objects is provided. Note, this does not cover
PloneArticleMultiPage at the moment.


How to migrate non-folderishtypes to folderish ones
===================================================

Non-folderish content types are missing some BTree attributes, which folderish
content types have (See ``Products.BtreeFolder2.BTreeFolder2Base._initBtrees``
).

`plone.app.folder`_ provides an upgrade view to migrate pre-plone.app.folder (or
non-folderish) types to the new BTree based implementation (defined in:
``plone.app.folder.migration.BTreeMigrationView``).

To upgrade your non-folderish content types to folderish ones, just call
``@@migrate-btrees`` on your Plone site root, and you're done.


Translations
============

This product has been translated into

- German.

- Spanish.

You can contribute for any message missing or other new languages, join us at 
`Plone Collective Team <https://www.transifex.com/plone/plone-collective/>`_ 
into *Transifex.net* service with all world Plone translators community.


Installation
============

This addon can be installed has any other addons, please follow official
documentation_.

To use ``collective.folderishtypes`` with Archetypes, depend on the
``dexterity`` ``extras_require`` in ``setup.py`` or buildout like so::

    collective.folderishtypes [archetypes]

For the dexterity version, like so::

    collective.folderishtypes [dexterity]


Tested with
===========

Plone 4, Plone 5


Tests status
------------

This add-on is tested using Travis CI. The current status of the add-on is:

.. image:: https://img.shields.io/travis/collective/collective.folderishtypes/master.svg
    :target: https://travis-ci.org/collective/collective.folderishtypes

.. image:: http://img.shields.io/pypi/v/collective.folderishtypes.svg
   :target: https://pypi.org/project/collective.folderishtypes


Contribute
==========

Have an idea? Found a bug? Let us know by `opening a ticket`_.

- Issue Tracker: https://github.com/collective/collective.folderishtypes/issues
- Source Code: https://github.com/collective/collective.folderishtypes


TODO
====

- Depend on z3c.jbot, so that overriding folder_listing and folder_summary_view
  might also work at IPloneSite root.
- Write tests
- See, if this portlet is useful:
  https://github.com/RedTurtle/collective.portlet.localcontents


License
=======

The project is licensed under the GPLv2.

.. _Plone: https://plone.org/
.. _plone.app.folder: https://pypi.org/project/plone.app.folder/
.. _`opening a ticket`: https://github.com/collective/collective.folderishtypes/issues
.. _documentation: https://docs.plone.org/manage/installing/installing_addons.html
