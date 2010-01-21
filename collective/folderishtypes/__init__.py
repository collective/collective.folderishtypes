from zope.i18nmessageid import MessageFactory
from collective.folderishtypes import config

from Products.Archetypes import atapi
from Products.CMFCore import utils

MsgFact = MessageFactory('collective.folderishtypes')

def initialize(context):
    """Register content types through Archetypes with Zope and the CMF.
    """
    from content import folderish_event #, folderish_document

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit("%s: %s" % (config.PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)