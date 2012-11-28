Changelog
=========

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
