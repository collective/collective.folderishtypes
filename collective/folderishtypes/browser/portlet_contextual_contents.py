from Acquisition import aq_inner, aq_parent
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.formlib import form
from zope.interface import implements

from collective.folderishtypes import MsgFact as _


DEFAULT_ALLOWED_TYPES = (
    'Folderish News Item',
    'Folderish Document',
    'Folderish Event',
    'File',
    'Link',
    'Image',
)


class IContextualContentsPortlet(IPortletDataProvider):

    name = schema.TextLine(
            title=_(u"ctxcontents_label_title", default=u"Title"),
            description=_(u"ctxcontents_help_title",
                          default=u"The title of the Contextual Contents portlet."),
            default=u"",
            required=False)

    allowed_types = schema.Tuple(
        title=_(u"ctxcontents_label_allowed_types", u"Allowed Types"),
        description=_(u"ctxcontents_help_allowed_types", u"Select the content types that should be shown."),
        default=DEFAULT_ALLOWED_TYPES,
        required=True,
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.ReallyUserFriendlyTypes"
        )
    )

    display_images = schema.Bool(
        title=_(u"ctxcontents_label_display_images", u"Display Images"),
        description=_(u"ctxcontents_help_display_images", u"Display images inline."),
        default=False,
        required=False,
    )

    image_scale = schema.Choice(
        title=_(u'ctxcontents_label_image_scale', default=u'Image Scale'),
        description=_(u'ctxcontents_help_image_scale',
                      default=u'Select, which image scale should be used '
                              u'for the portlet.'),
        required=False,
        default=None,
        vocabulary="collective.folderishtypes.ImageScaleVocabulary",
    )

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('portlet_contextual_contents.pt')

    @property
    def items(self):
        context = aq_inner(self.context)
        if not ISiteRoot.providedBy(context):
            # get contents from parent, if it's a default view and the context
            # is not an ISiteRoot object
            parent = aq_parent(context)
            if parent.defaultView() == context.id:
                context = parent
        cat = getToolByName(context,'portal_catalog')
        query = {}
        query['portal_type'] = self.data.allowed_types
        query['path'] = {'query': '/'.join(context.getPhysicalPath())}
        query['sort_on'] = 'getObjPositionInParent'
        query['path']['depth'] = 1
        brains = cat(**query)
        return brains

class Assignment(base.Assignment):
    implements(IContextualContentsPortlet)

    def __init__(self, name = u"Contextual Contents",
            allowed_types=DEFAULT_ALLOWED_TYPES,
            display_images=False,
            image_scale=None):
        self.name = name
        self.allowed_types = allowed_types
        self.display_images = display_images
        self.image_scale = image_scale

    @property
    def title(self):
        return _(u'portlet_ctxcontents_title', default=u"Contextual Contents Portlet")

class AddForm(base.AddForm):
    form_fields = form.Fields(IContextualContentsPortlet)
    label = _(u'portlet_ctxcontents_label_add', default=u"Add Contextual Contents Portlet.")
    description = _(u'portlet_ctxcontents_help_add', default=u"This portlet shows items of a specific Type which are in the current folder.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IContextualContentsPortlet)
    label = _(u'portlet_ctxcontents_label_edit', default=u"Edit Contextual Contents Portlet.")
    description = _(u'portlet_ctxcontents_help_edit', default=u"This portlet shows items of a specific Type which are in the current folder.")
