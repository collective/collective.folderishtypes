Introduction
============

Provides the types "Folderish Event", "Folderish News Item" and
"Folderish Document" as replacements for their ATContentTypes equivalents.
Those types are able to hold any other content, like a Folder.

There is a "portlet" profile, which installs a portlet to show the contents of
an folderish type.

You can limit the types, which can be added to FolderishTypes by providing
a Generic Setup import type configuration.

The reason for this package is, that in my experience it's easier to group
related content together at one place. An article about something fancy might
have an image gallery associated with it as well as some pdf-downloads. With
this package you can put everyting inside the article.
Another use case is that you can structure content hierarchically and don't need
to define "default pages" - a concept hard to understand and handle (see:
http://www.sixfeetup.com/blog/plone-vs.-drupal-core-features-comparison )

Alexander Limi also wished folderish content back in 2008:
"#10: Content re-use is overrated — people like folderish"
http://limi.net/articles/18-things-i-wish-were-true-about-plone/

.. note::
  If you use plone.app.event, please configure the Folderish_Event type to use
  the @@event_view instead of the event_view.


How To create own content types based on collective.folderishtypes
==================================================================

You can subclass the content classes from ``collective.folderishtypes.content``
and use it's schema to create own content types based on
``collective.folderishtypes``, as you would do to subclass for any other
Archetypes based content type.


How to migrate non-folderishtypes to folderish ones
===================================================

Non-folderish content types are missing some btree attributes, which folderish
content types have (See ``Products.BtreeFolder2.BTreeFolder2Base._initBtrees``
).

plone.app.folder provides an upgrade view to migrate pre-plone.app.folder (or
non-folderish) types to the new Btree based implementation (defined in:
``plone.app.folder.migration.BTreeMigrationView``).

To upgrade your non-folderish content types to folderish ones, just call
``@@migrate-btrees`` on your Plone site root, and you're done.


TODO
====

- Depend on z3c.jbot, so that overriding folder_listing and folder_summary_view
  might also work at IPloneSite root.
- Write tests
- See, if this portlet is useful:
  https://github.com/RedTurtle/collective.portlet.localcontents


Tested with
===========

Plone 4+


Contributors
============

- Johannes Raggam <raggam-nl [at] adm [dot] at> (Author)

- Robert Niederrreiter <rnix [at] squarewave [dot] at>
