from Products.CMFCore import utils
from Products.CMFCore.permissions import setDefaultRoles
from collective.folderishtypes import config
from zope.i18nmessageid import MessageFactory


try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

MsgFact = MessageFactory(config.PROJECTNAME)


ADD_PERMISSIONS = {
    "Folderish Event": "collective.folderishtypes: Add Folderish Event",
    "Folderish Document": "collective.folderishtypes: Add Folderish Document",
    "Folderish News Item": "collective.folderishtypes: Add Folderish News Item"
}
setDefaultRoles(
    ADD_PERMISSIONS["Folderish Event"],
    ('Manager', 'Owner', 'Contributor', )
)
setDefaultRoles(
    ADD_PERMISSIONS["Folderish Document"],
    ('Manager', 'Owner', 'Contributor', )
)
setDefaultRoles(
    ADD_PERMISSIONS["Folderish News Item"],
    ('Manager', 'Owner', 'Contributor', )
)


def initialize(context):
    """Register content types through Archetypes with Zope and the CMF.
    """
    from collective.folderishtypes.content import folderish_event  # nopep8
    from collective.folderishtypes.content import folderish_document  # nopep8
    from collective.folderishtypes.content import folderish_newsitem  # nopep8

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
            "%s: %s" % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
        ).initialize(context)
