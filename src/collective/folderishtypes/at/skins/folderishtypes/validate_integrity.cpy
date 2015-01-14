## Script (Python) "validate_integrity"
##title=Validate Integrity
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##

# REDIRECT TO PARENT FOLDER AFTER EDITING
# From: http://plonenotes.blogspot.co.at/2013/03/plone-redirection-after-archetypes.html
#       http://www.upfrontsystems.co.za/Members/francois/frankthetank/archetypes-redirection-after-creation 

from Acquisition import aq_parent
from Products.Archetypes import PloneMessageFactory as _
from Products.Archetypes.utils import addStatusMessage

request = context.REQUEST
errors = {}
errors = context.validate(REQUEST=request, errors=errors, data=1, metadata=0)

if errors:
    message = _(u'Please correct the indicated errors.')
    addStatusMessage(request, message, type='error')
    return state.set(status='failure', errors=errors)
else:
    message = _(u'Changes saved.')
    addStatusMessage(request, message)
    state.setNextAction(
        'redirect_to:string:%s' % (aq_parent(context).absolute_url()))
    return state.set(status='success')
