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
type_schema = newsitem.ATNewsItemSchema.copy()

class FolderishNewsItem(folder.ATFolder, newsitem.ATNewsItem):
    implements(IFolderishNewsItem)

    portal_type = 'Folderish News Item'
    _at_rename_after_creation = True
    schema = type_schema + folder_schema

atapi.registerType(FolderishNewsItem, PROJECTNAME)
