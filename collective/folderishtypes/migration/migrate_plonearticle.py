from DateTime import DateTime
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.utils import getToolByName
from Products.PloneArticle.interfaces import IPloneArticle
from Products.contentmigration.archetypes import ATItemMigrator
from Products.contentmigration.walker import CustomQueryWalker
from transaction import savepoint
from zope.component import queryUtility

import transaction
import logging

logger = logging.getLogger('collective.folderishtypes PloneArticle migration')


class PloneArticleMigrator(ATItemMigrator):
    src_portal_type = 'PloneArticle'
    src_meta_type = 'PloneArticle'
    dst_portal_type = 'Folderish Document'
    dst_meta_type = 'FolderishDocument'

    def migrate_files(self):
        """Migrate files from PloneArticle to file contents within the
        folderish document.
        """
        for item in self.old.getFiles():
            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedFile.data

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.invokeFactory(
                "File",
                id_,
                title,
                description=description
            )
            self.new[id_].setFile(data)

            self.new[id_].creation_date = DateTime(creation_date)
            self.new[id_].setModificationDate(DateTime(modification_date))

            logger.info(
                'migrated file %s for %s' % (id_, self.new.absolute_url()))

    def migrate_images(self):
        """Migrate images from PloneArticle to image contents within the
        folderish document.
        """
        for item in self.old.getImages():
            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedImage.data

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.invokeFactory(
                "Image",
                id_,
                title,
                description=description
            )
            self.new[id_].setImage(data)

            self.new[id_].creation_date = DateTime(creation_date)
            self.new[id_].setModificationDate(DateTime(modification_date))

            logger.info(
                'migrated image %s for %s' % (id_, self.new.absolute_url()))

    def migrate_links(self):
        """Migrate links from PloneArticle to link contents within the
        folderish document.
        """
        for item in self.old.getLinks():
            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedLink

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.invokeFactory(
                "Link",
                id_,
                title,
                description=description,
                remoteUrl=data
            )

            self.new[id_].creation_date = DateTime(creation_date)
            self.new[id_].setModificationDate(DateTime(modification_date))

            logger.info(
                'migrated link %s for %s' % (id_, self.new.absolute_url()))


def callBefore(oldobj):
    # Do a commit before each migration, commiting the previous changes to
    # avoid running out of space for large migrations.
    transaction.commit()

    if 'portal_factory' in oldobj.getPhysicalPath():
        logger.info('Skipping factory obj: {0}'.format(
            '/'.join(oldobj.getPhysicalPath())))
        return False
    return True


def migrate(context):
    # switch linkintegrity temp off
    ptool = queryUtility(IPropertiesTool)
    site_props = getattr(ptool, 'site_properties', None)
    linkintegrity = site_props.getProperty(
        'enable_link_integrity_checks',
        False
    )
    site_props.manage_changeProperties(enable_link_integrity_checks=False)

    # do migration
    portal = getToolByName(context, 'portal_url').getPortalObject()
    walker = CustomQueryWalker(
        portal, PloneArticleMigrator,
        query=dict(object_provides=IPloneArticle.__identifier__),
        callBefore=callBefore)
    savepoint(optimistic=True)
    walker.go()

    # switch linkintegrity back
    site_props.manage_changeProperties(
        enable_link_integrity_checks=linkintegrity
    )

    return walker.getOutput()
