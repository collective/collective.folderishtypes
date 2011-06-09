from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import newsitem
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.folderishtypes.interfaces import IFolderishNewsItem
from collective.folderishtypes.config import PROJECTNAME
from collective.folderishtypes.config import schema_cleanup

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + newsitem.ATNewsItemSchema.copy()
type_schema['image'].sizes = None # needed for plone.app.imaging
schemata.finalizeATCTSchema(type_schema,
                            folderish=True,
                            moveDiscussion=False)

class FolderishNewsItem(folder.ATFolder, newsitem.ATNewsItem):
    implements(IFolderishNewsItem)

    portal_type = 'Folderish News Item'
    _at_rename_after_creation = True
    schema = type_schema

    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image
        return newsitem.ATNewsItem.__bobo_traverse__(self, REQUEST, name)

atapi.registerType(FolderishNewsItem, PROJECTNAME)
