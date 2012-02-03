Changelog
=========

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
