from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content import event
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.interfaces import IATEvent


from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.config import PROJECTNAME

import pdb;pdb.set_trace()
# test = FolderishEvent()
# assert(IATEvent.providedBy(test))

class FolderishEvent(event.ATEvent, folder.ATFolder):
    # implements(IFolderishEvent)
    portal_type = "Folderish Event"

atapi.registerType(VenueFolder, PROJECTNAME)


