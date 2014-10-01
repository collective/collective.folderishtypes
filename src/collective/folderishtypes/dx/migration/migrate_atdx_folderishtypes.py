from collective.folderishtypes.interfaces import IFolderishDocument
from collective.folderishtypes.interfaces import IFolderishEvent
from collective.folderishtypes.interfaces import IFolderishNewsItem
from plone.app.contenttypes.migration.migration import ATCTFolderMigrator
from plone.app.contenttypes.migration.migration import DocumentMigrator
from plone.app.contenttypes.migration.migration import EventMigrator
from plone.app.contenttypes.migration.migration import NewsItemMigrator
from plone.app.contenttypes.migration.migration import migrate
from plone.app.contenttypes.migration.utils import ATCT_LIST


class FolderishDocumentMigrator(DocumentMigrator, ATCTFolderMigrator):
    src_portal_type = 'Folderish Document'
    src_meta_type = 'FolderishDocument'
    dst_portal_type = 'Document'
    dst_meta_type = None  # not used


def migrate_folderishdocuments(portal):
    return migrate(portal, FolderishDocumentMigrator)


class FolderishEventMigrator(EventMigrator, ATCTFolderMigrator):
    src_portal_type = 'Folderish Event'
    src_meta_type = 'FolderishEvent'
    dst_portal_type = 'Event'
    dst_meta_type = None  # not used


def migrate_folderishevents(portal):
    return migrate(portal, FolderishEventMigrator)


class FolderishNewsItemMigrator(NewsItemMigrator, ATCTFolderMigrator):
    src_portal_type = 'Folderish News Item'
    src_meta_type = 'FolderishNewsItem'
    dst_portal_type = 'News Item'
    dst_meta_type = None  # not used


def migrate_folderishnewsitems(portal):
    return migrate(portal, FolderishNewsItemMigrator)


ATCT_LIST.update({
    "Folderish Document": {
        'iface': IFolderishDocument,
        'migrator': migrate_folderishdocuments,
        'extended_fields': [],
        'new_type_name': 'Document',
        'old_meta_type': 'FolderishDocument',
    },
    "Folderish Event": {
        'iface': IFolderishEvent,
        'migrator': migrate_folderishevents,
        'extended_fields': [],
        'new_type_name': 'Event',
        'old_meta_type': 'FolderishEvent',
    },
    "Folderish News Item": {
        'iface': IFolderishNewsItem,
        'migrator': migrate_folderishnewsitems,
        'extended_fields': [],
        'new_type_name': 'News Item',
        'old_meta_type': 'FolderishNewsItem',
    },
})
