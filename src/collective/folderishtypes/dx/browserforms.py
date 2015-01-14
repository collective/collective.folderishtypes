from Acquisition import aq_parent
from plone.dexterity.browser.add import DefaultAddForm
from plone.dexterity.browser.add import DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm
from plone.dexterity.interfaces import IDexterityEditForm
from plone.z3cform import layout
from zope.interface import classImplements


class AddForm(DefaultAddForm):

    def nextURL(self):
        return self.context.absolute_url()


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):

    def nextURL(self):
        return aq_parent(self.context).absolute_url()


EditView = layout.wrap_form(EditForm)
classImplements(EditView, IDexterityEditForm)
