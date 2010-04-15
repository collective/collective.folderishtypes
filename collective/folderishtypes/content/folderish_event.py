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
from Products.ATContentTypes.content import event
from Products.ATContentTypes.content import folder

from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
event_schema = event.ATEventSchema.copy()

class FolderishEvent(folder.ATFolder, event.ATEvent):
    implements(IFolderishEvent)
    portal_type = 'Folderish Event'
    archetype_name = 'Folderish Event'
    _at_rename_after_creation = True
    schema = event_schema + folder_schema

atapi.registerType(FolderishEvent, PROJECTNAME)