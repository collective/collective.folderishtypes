from collective.folderishtypes.interfaces import IFolderishDocument
from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.interfaces import IFolderishNewsItem
from plone.app.contenttypes.interfaces import IDocument
from plone.app.contenttypes.interfaces import IEvent
from plone.app.contenttypes.interfaces import INewsItem
from plone.dexterity.content import Container
from zope.interface import implements


class FolderishDocument(Container):
    implements(IDocument, IFolderishDocument)


class FolderishEvent(Container):
    implements(IEvent, IFolderishEvent)


class FolderishNewsItem(Container):
    implements(INewsItem, IFolderishNewsItem)
