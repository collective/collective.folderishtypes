from Products.ATContentTypes.content import document
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import newsitem
from Products.ATContentTypes.content import schemata
from collective.folderishtypes import PROJECTNAME
from collective.folderishtypes.interfaces import IFolderishDocument
from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.interfaces import IFolderishNewsItem
from zope.interface import implements

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

try:
    from plone.app.event.at import content as event
except ImportError:
    from Products.ATContentTypes.content import event


def schema_cleanup(schema):
    """Cleanup a schema to prepare it to be merged with another one.
       ATCT Schema definitions are not simple lists or dicts, so there is
       some manual interaction neccessary.
    """
    for key in [
        'id', 'title', 'description', 'subject', 'relatedItems', 'location',
        'language', 'effectiveDate', 'expirationDate', 'creation_date',
        'modification_date', 'creators', 'contributors', 'rights',
        'allowDiscussion', 'excludeFromNav'
    ]:
        if key in schema:
            del schema[key]
    return schema


# DOCUMENT

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + document.ATDocumentSchema.copy()
schemata.finalizeATCTSchema(type_schema,
                            moveDiscussion=False)


class FolderishDocument(folder.ATFolder, document.ATDocument):
    implements(IFolderishDocument)

    portal_type = 'Folderish Document'
    _at_rename_after_creation = True
    schema = type_schema
atapi.registerType(FolderishDocument, PROJECTNAME)


# EVENT

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + event.ATEventSchema.copy()
schemata.finalizeATCTSchema(type_schema,
                            moveDiscussion=False)
type_schema.changeSchemataForField('location', 'default')
type_schema.moveField('location', before='attendees')  # Move location back to
                                                       # main schemata


class FolderishEvent(folder.ATFolder, event.ATEvent):
    implements(IFolderishEvent)

    portal_type = 'Folderish Event'
    _at_rename_after_creation = True
    schema = type_schema
atapi.registerType(FolderishEvent, PROJECTNAME)


# NEWS ITEM

folder_schema = schema_cleanup(folder.ATFolderSchema.copy())
type_schema = folder_schema + newsitem.ATNewsItemSchema.copy()
type_schema['image'].sizes = None  # needed for plone.app.imaging
schemata.finalizeATCTSchema(type_schema,
                            moveDiscussion=False)


class FolderishNewsItem(folder.ATFolder, newsitem.ATNewsItem):
    implements(IFolderishNewsItem)

    portal_type = 'Folderish News Item'
    _at_rename_after_creation = True
    schema = type_schema
atapi.registerType(FolderishNewsItem, PROJECTNAME)
