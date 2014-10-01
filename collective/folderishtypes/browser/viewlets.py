from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ListingViewlet(ViewletBase):
    index = ViewPageTemplateFile('listing_viewlet.pt')

    def available(self):
        return 'folder_contents' not in self.view.__name__
