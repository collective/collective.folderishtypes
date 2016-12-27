# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.folderishtypes import MsgFact as _
from collective.folderishtypes.interfaces import IFolderishType
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.interface import implementer


class IListingPortlet(IPortletDataProvider):
    pass


@implementer(IListingPortlet)
class Assignment(base.Assignment):

    @property
    def title(self):
        return _(
            u"listingportlet_title",
            default=u"Folderish Contenttype Listing Portlet"
        )


class AddForm(base.NullAddForm):
    label = _(u"listingportlet_label_add", u"Add portlet for folderish types")
    description = _(
        u"listingportlet_help_add",
        default=u"This portlet shows the contents of folderish types."
    )

    def create(self):
        return Assignment()


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('listing_portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)
        portal_state = getMultiAdapter(
            (context, self.request),
            name=u'plone_portal_state'
        )
        self.anonymous = portal_state.anonymous()

    @property
    def available(self):
        return not self.anonymous and IFolderishType.providedBy(self.context)
