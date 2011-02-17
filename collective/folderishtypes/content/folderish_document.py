from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import document
from Products.ATContentTypes.content import folder

from collective.folderishtypes.interfaces import IFolderishDocument
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = document.ATDocumentSchema.copy()

class FolderishDocument(folder.ATFolder, document.ATDocument):
    implements(IFolderishDocument)

    portal_type = 'Folderish Document'
    _at_rename_after_creation = True
    schema = type_schema + folder_schema

atapi.registerType(FolderishDocument, PROJECTNAME)
