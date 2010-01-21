from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content import event
from Products.ATContentTypes.content import folder

from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.config import PROJECTNAME

FolderishEventSchema = event.ATEventSchema.copy() + folder.ATFolderSchema.copy()

class FolderishEvent(folder.ATFolder, event.ATEvent):
    implements(IFolderishEvent)
    portal_type = "Folderish Event"
    _at_rename_after_creation = True
    schema = FolderishEventSchema

atapi.registerType(FolderishEvent, PROJECTNAME)
