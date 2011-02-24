from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import event
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + event.ATEventSchema.copy()
schemata.finalizeATCTSchema(type_schema,
                            folderish=True,
                            moveDiscussion=False)

class FolderishEvent(folder.ATFolder, event.ATEvent):
    implements(IFolderishEvent)

    portal_type = 'Folderish Event'
    _at_rename_after_creation = True
    schema = type_schema

atapi.registerType(FolderishEvent, PROJECTNAME)
