# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

PROJECTNAME = "collective.folderishtypes"

ADD_PERMISSIONS = {
    "Folderish Event": "collective.folderishtypes: Add Folderish Event",
    "Folderish Document": "collective.folderishtypes: Add Folderish Document",
    "Folderish News Item": "collective.folderishtypes: Add Folderish News Item",
}

def schema_cleanup(schema):
    for key in ['id', 'title', 'description', 'subject', 'relatedItems',
              'location', 'language', 'effectiveDate', 'expirationDate',
              'creation_date', 'modification_date', 'creators', 'contributors',
              'rights', 'allowDiscussion', 'excludeFromNav']:
        if key in schema:
            del schema[key]
    return schema


