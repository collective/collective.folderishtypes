# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

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
