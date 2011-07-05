from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from Acquisition import aq_inner
from zope.component import getMultiAdapter

from collective.folderishtypes import MsgFact as _
from collective.folderishtypes.interfaces import IFolderishType

class IListingPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(IListingPortlet)

    @property
    def title(self):
        return _(u"listingportlet_title", u"Folderish Contenttype Listing Portlet")

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IListingPortlet)
    label = _(u"listingportlet_label_add", u"Add portlet for folderish types")
    description = _(u"listingportlet_help_add", u"This portlet shows the contents of folderish types.")

    def create(self):
        return Assignment()

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('listing_portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        self.anonymous = portal_state.anonymous()

    @property
    def available(self):
        return not self.anonymous and IFolderishType.providedBy(self.context)
