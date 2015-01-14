from Products.CMFCore import utils
from Products.CMFCore.permissions import setDefaultRoles
from collective.folderishtypes import PROJECTNAME

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi


ADD_PERMISSIONS = {
    "Folderish Event": "collective.folderishtypes: Add Folderish Event",
    "Folderish Document": "collective.folderishtypes: Add Folderish Document",
    "Folderish News Item": "collective.folderishtypes: Add Folderish News Item"
}
setDefaultRoles(
    ADD_PERMISSIONS["Folderish Event"],
    ('Manager', 'Owner', 'Site Administrator', 'Contributor', )
)
setDefaultRoles(
    ADD_PERMISSIONS["Folderish Document"],
    ('Manager', 'Owner', 'Site Administrator', 'Contributor', )
)
setDefaultRoles(
    ADD_PERMISSIONS["Folderish News Item"],
    ('Manager', 'Owner', 'Site Administrator', 'Contributor', )
)


def initialize(context):
    """Register content types through Archetypes with Zope and the CMF.
    """
    from collective.folderishtypes.at import content  # nopep8

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECTNAME), PROJECTNAME
    )

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
            "%s: %s" % (PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
        ).initialize(context)
