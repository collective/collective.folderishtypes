from zope.interface import Interface

class IFolderishType(Interface):
    """ Marker interface
    """

class IFolderishDocument(IFolderishType):
    """ Marker interface
    """

class IFolderishEvent(IFolderishType):
    """ Marker interface
    """

class IFolderishNewsItem(IFolderishType):
    """ Marker interface
    """
