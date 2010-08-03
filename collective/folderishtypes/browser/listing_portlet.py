# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from collective.folderishtypes import MsgFact as _
from collective.folderishtypes.interfaces import IFolderishType

class IListingPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(IListingPortlet)

    @property
    def title(self):
        return _(u"Folderish Contenttype Listing Portlet")

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IListingPortlet)
    label = _(u"Add portlet for folderish types")
    description = _(u"This portlet shows the contents of folderish types.")

    def create(self):
        return Assignment()

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('listing_portlet.pt')

    @property
    def show_me(self):
        if IFolderishType.providedBy(self.context): return True
        else: return False