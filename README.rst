Introduction
============

Provides the types "Folderish Event", "Folderish News Item" and
"Folderish Document" as replacements for their ATContentTypes equivalents.
Those types are able to hold any other content, like a Folder.

There is a "listing_viewlet" and "portlet" profile, which show the contents of
the folderish types in a viewlet or portlet respectively.

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

TODO
====

- Write tests
- The folderish content viewlet seems to be shown regardless if it was
  registered via Generic Setup. Fix that.
- Check, if folderish types implement all interfaces from the types they derive
  from. if not, implement them also.

Tested with
===========

Plone 4


Author
======

Johannes Raggam <johannes@raggam.co.at>, BlueDynamics Alliance
