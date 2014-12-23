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

try:
    from collective.contentleadimage.config import IMAGE_FIELD_NAME
    from collective.contentleadimage.config import IMAGE_CAPTION_FIELD_NAME
except ImportError:
    IMAGE_FIELD_NAME = None
    IMAGE_CAPTION_FIELD_NAME = None


class PloneArticleMigrator(ATItemMigrator):
    src_portal_type = 'PloneArticle'
    src_meta_type = 'PloneArticle'
    dst_portal_type = 'Folderish Document'
    dst_meta_type = 'FolderishDocument'

    def migrate_various(self):

        if IMAGE_FIELD_NAME:
            # Migrate contentleadimage
            new_img_field = self.new.getField(IMAGE_FIELD_NAME)
            if new_img_field:
                # Else: forgot to configure the type for it? or not supposed to
                # hold contentlead images
                img_field = self.old.getField(IMAGE_FIELD_NAME)
                img = img_field.get(self.old)
                if img:
                    new_img_field.set(self.new, img, mimetype=img.content_type)

                    cap_field = self.old.getField(IMAGE_CAPTION_FIELD_NAME)
                    cap = cap_field.get(self.old)
                    new_cap_field = self.new.getField(IMAGE_CAPTION_FIELD_NAME)
                    new_cap_field.set(self.new, cap)

                    logger.info('migrated contentleadimage for %s'
                                % self.new.absolute_url())

        logger.info('migrated PloneArticle %s' % self.new.absolute_url())

    def migrate_files(self):
        """Migrate files from PloneArticle to file contents within the
        folderish document.
        """
        for item in self.old.getFiles():

            if 'files' not in self.new.contentIds():
                self.new.invokeFactory('Folder', 'files', title='Files')

            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedFile.data

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.files.invokeFactory(
                "File",
                id_,
                title=title,
                description=description
            )
            item_new = self.new.files[id_]
            item_new.setFile(data)
            item_new.setFilename(item.attachedFile.filename)
            item_new.setContentType(item.attachedFile.content_type)

            item_new.creation_date = DateTime(creation_date)
            item_new.setModificationDate(DateTime(modification_date))

            logger.info(
                'migrated file %s for %s' % (id_, self.new.absolute_url()))

    def migrate_images(self):
        """Migrate images from PloneArticle to image contents within the
        folderish document.
        """
        for item in self.old.getImages():

            if 'images' not in self.new.contentIds():
                self.new.invokeFactory('Folder', 'images', title='Images')

            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedImage.data

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.images.invokeFactory(
                "Image",
                id_,
                title=title,
                description=description
            )
            item_new = self.new.images[id_]
            item_new.setImage(data)
            item_new.setFilename(item.attachedImage.filename)
            item_new.setContentType(item.attachedImage.content_type)

            item_new.creation_date = DateTime(creation_date)
            item_new.setModificationDate(DateTime(modification_date))

            logger.info(
                'migrated image %s for %s' % (id_, self.new.absolute_url()))

    def migrate_links(self):
        """Migrate links from PloneArticle to link contents within the
        folderish document.
        """
        for item in self.old.getLinks():

            if 'links' not in self.new.contentIds():
                self.new.invokeFactory('Folder', 'links', title='Links')

            id_ = item.id
            title = item.title
            description = item.description()
            data = item.attachedLink

            creation_date = item.CreationDate()
            modification_date = item.ModificationDate()

            self.new.links.invokeFactory(
                "Link",
                id_,
                title=title,
                description=description,
                remoteUrl=data
            )
            item_new = self.new.links[id_]
            item_new.creation_date = DateTime(creation_date)
            item_new.setModificationDate(DateTime(modification_date))

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
