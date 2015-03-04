Changes
=======

2.0 (2015-03-04)
----------------

- Plone 5 + 4 safe call of the ``@@folder_listing`` ``listing_macro``.
  [thet]

- Provide a ``redirectparent.zcml`` file. When loading it the user is
  redirected to the parent folder after adding or editing. This avoids
  confusing behavior of creating nested content structures, while one might add
  multiple content items to one folder. For consistency reasons, this is done
  for all types.
  For Archetypes, this behavior is enabled by default.
  [thet]

- Add a browserlayer for collective.folderishtypes including the .at and .dx
  sub packages together with upgrade steps. Bind relevant browser views to
  these browser layers.
  [thet]

- Allow "Site Administrator" to add ATContentTypes based Folderish Content
  Types.
  [thet]

- Better PloneArticle migration: Set content_type and filename for files and
  images. Plus: migrate contentleadimage, if available.
  [thet]

- Update unsintall profiles.
  [thet]


2.0b2 (2014-10-17)
------------------

- Fix broken release
  [rnix]


2.0b1 (2014-10-02)
------------------

- Add ISelectableConstrainTypes to behaviors of Dexterity folderish types.
  [agitator]

- Add content listing viewlet.
  [agitator]

- Add migration step for Products.PloneArticle objects to Archetypes based
  foldersh document objects.
  [thet]

- Initialize permissions and roles for Archetypes foldersh types.
  [thet]

- Dexterity support.
  [thet]


1.8 (2013-11-23)
----------------

- In folder_summary_view do a more sane check, if an image is available.
  [thet]


1.7 (2013-08-23)
----------------

- Remove bobo_traverse in Foldersh News Item, since plone.app.imaging does the
  traversing.
  [thet]

- Remove vCalendar action entry from FTI config of Folderish Event.
  [thet]

- More documentation: How To create own content types based on
  collective.folderishtypes, How to migrate non-folderishtypes to folderish
  ones.
  [thet]


1.6 (2013-04-23)
----------------

- Update translations and translate folder_listing.
  [thet]

- Add z3c.autoinclude.plugin entry point.
  [thet]


1.5 (2012-11-30)
----------------

- Let the folderish types derive from Products.ATContentTypes ATFolder instead
  of plone.app.folder's implementation. It inherits some i18n classes. This
  fixes the issue that on translation of folderish types LinguaPlone's
  translation view wasn't shown.
  [thet]


1.4 (2012-11-28)
----------------

- Give the original, non-folderish types another title, so that they can be
  easily kept apart from the folderish ones.
  [thet]

- For folderish events, move the location field back to the main schemata.
  [thet]


1.3 (2012-11-26)
----------------

- Allow discussions from plone.app.discussion on Folderish Types.
  [thet]


1.2.1 (2012-09-06)
------------------

- CSS fix
  [rnix]


1.2 (2012-09-04)
----------------

- Removed folderish=True when finalizing the schema, which prevented
  relateditems from being displayed. Updated import to plone.app.folder.
  [agitator]

- Fix meta types in FTI to follow consistent conventions.
  [rnixx]

- For Folderish Event, use plone.app.event's ATEvent implementation if
  available.
  [thet]


1.1.1 (2012-02-05)
------------------

- Add a custom style class for the contextual contents portlet based on the
  portlet's name.
  [thet]


1.1 (2012-02-04)
----------------

- Add a contextual contents portlet, which shows the contents of folderish
  types in a portlet.
  [thet]


1.0 (2012-02-02)
----------------

- No Changes, release as 1.0 final.
  [thet]


1.0b5 (2011-09-07)
------------------

- Updated documentation: Missing viewlet issue.
  [thet]


1.0b4 (2011-09-07)
------------------

- Locales Update.
  [thet]

- Add types to image_types in portal_atct to allow image scale recreation.
  [thet]

- Add HistroyAwareMixin and configure types to be versionable.
  [thet]

- Remove folderish_listing_viewlet, since there is already a portlet which can
  be used.
  [thet]

- Include CSS via link instead of import, which can then be better processed by
  XML manipulation tools like Deliverance or Diazo.
  [thet]

- More explicit content-icons background styles which don't override
  background-color.
  [thet]

- Use plone.app.imaging scales - apply a schema patch to FolderishNewsItem.
  [thet]

- Fixed traversing to image scales for FolderishNewsItem. Subclasses should
  implement __bobo_traverse__ too.
  [thet]


1.0b3 (2011-03-22)
------------------

- Add rolemap.xml for generic setup to have proper configured permissions.
  [thet]


1.0b2 (2011-03-10)
------------------

- Make portlet registration optional and register portlets only for folderish
  types.
  [thet]

- Updated folder_listing.pt and folder_summary_view.pt to current Plone trunk.
  [thet]


1.0b1 (2011-02-18)
------------------

- Initial release
