from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

try:
    from plone.app.event.at import content as event
except ImportError:
    from Products.ATContentTypes.content import event
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + event.ATEventSchema.copy()
schemata.finalizeATCTSchema(type_schema,
                            moveDiscussion=False)
type_schema.changeSchemataForField('location', 'default')
type_schema.moveField('location', before='attendees') # Move location back to
                                                      # main schemata

class FolderishEvent(folder.ATFolder, event.ATEvent):
    implements(IFolderishEvent)

    portal_type = 'Folderish Event'
    _at_rename_after_creation = True
    schema = type_schema

atapi.registerType(FolderishEvent, PROJECTNAME)
