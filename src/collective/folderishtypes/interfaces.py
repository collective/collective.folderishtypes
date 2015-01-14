from zope.interface import Interface


class IThemeSpecific(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IFolderishType(Interface):
    """Marker interface
    """


class IFolderishDocument(IFolderishType):
    """Marker interface
    """


class IFolderishEvent(IFolderishType):
    """Marker interface
    """


class IFolderishNewsItem(IFolderishType):
    """Marker interface
    """
