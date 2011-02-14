# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import newsitem
from Products.ATContentTypes.content import folder

from collective.folderishtypes.interfaces import IFolderishNewsItem
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
ct_schema = newsitem.ATNewsItemSchema .copy()

class FolderishNewsItem(folder.ATFolder, newsitem.ATNewsItem):
    implements(IFolderishNewsItem)

    portal_type = 'Folderish News Item'
    _at_rename_after_creation = True
    schema = ct_schema + folder_schema

atapi.registerType(FolderishNewsItem, PROJECTNAME)
