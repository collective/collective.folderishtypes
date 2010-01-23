Introduction
============
Provides the types "Folderish Event", "Folderish News Item" and
"Folderish Document" as replacements for their ATContentTypes equivalents and
a "Folderish Subfolder" which can be added as a subfolder to the three ATCT
replacement types.

Those types are able to hold Images, Files and the Folderish Subfolders - which
itself can hold again Images, Files and Folderish Subfolders. The purpose of the
Folderish Subfolders is to limit the possible types which can be added to the
ATCT replacement types while allowing to build a nested hierachy.

You can override these limits by providing Generic Setup import steps for all
Folderish_* types.


Author
======
Johannes Raggam <johannes@raggam.co.at>


TODO
====
- Add "Folderish Event" to CalendarTool
- Write tests
- If needed: provide an alternative view for
  Products/CMFPlone/skins/plone_templates/events_listing


Changes to templates
====================
$ diff collective.folderishtypes/collective/folderishtypes/browser/folder_listing.pt Plone/Products/CMFPlone/skins/plone_content/folder_listing.pt
38,41c38,39
<              tal:attributes="class python:bool(context.Format() in
<                              ('text/structured', 'text/x-rst',)) and
<                              str('stx' + kss_class) or
<                              str('plain' + kss_class)">
---
>              tal:attributes="class python:test(context.Format() in ('text/structured',
>                                                    'text/x-rst', ), 'stx' + kss_class, 'plain' + kss_class)">
84c82
<                         tal:attributes="class python:bool(item_type in ('Event', 'Folderish Event')) and str('vevent') or ''">
---
>                         tal:attributes="class python:test(item_type == 'Event', 'vevent', '')">
90c88
<                                tal:attributes="href python:bool(item_type in use_view_action) and str(item_url+'/view') or str(item_url);
---
>                                tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);
99c97
<                             <span tal:condition="python:item_type in ('Event', 'Folderish Event') and item.location"
---
>                             <span tal:condition="python: item_type == 'Event' and item.location"
113c111
<                             <span tal:condition="python:item_type in ('Event', 'Folderish Event') and not item.location"
---
>                             <span tal:condition="python: item_type == 'Event' and not item.location"
148c146
<                                 <tal:modified condition="python: item_type not in ('Event', 'Folderish Event')">
---
>                                 <tal:modified condition="python: item_type != 'Event'">



$ diff collective.folderishtypes/collective/folderishtypes/browser/folder_summary_view.pt Plone/Products/CMFPlone/skins/plone_content/folder_summary_view.pt
38,41c38,39
<              tal:attributes="class python:bool(context.Format() in
<                              ('text/structured', 'text/x-rst',)) and
<                              str('stx' + kss_class) or
<                              str('plain' + kss_class)">
---
>              tal:attributes="class python:test(context.Format() in ('text/structured',
>                                                    'text/x-rst', ), 'stx' + kss_class, 'plain' + kss_class)">
84c82
<                        tal:attributes="href python:bool(item_type in use_view_action) and str(item_url+'/view') or str(item_url);">
---
>                        tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);">
95c93
<                            tal:attributes="href python:bool(item_type in use_view_action) and str(item_url+'/view') or str(item_url);"
---
>                            tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);"
103,104c101,102
<                     <tal:event condition="python:item_type in ('Event', 'Folderish Event')">
<                         <span tal:condition="python:item.location"
---
>                     <tal:event condition="python: item_type == 'Event'">
>                         <span tal:condition="python: item_type == 'Event' and item.location"
118c116
<                         <span tal:condition="python:not item.location"
---
>                         <span tal:condition="python: item_type == 'Event' and not item.location"
131c129
<                     <tal:newsitem condition="python:item_type in ('News Item', 'Folderish News Item')">
---
>                     <tal:newsitem condition="python: item_type == 'News Item'">
164c162
<                            tal:attributes="href python:bool(item_type in use_view_action) and str(item_url+'/view') or str(item_url);"
---
>                            tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);"


