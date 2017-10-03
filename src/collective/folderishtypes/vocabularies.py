# -*- coding: utf-8 -*-
try:
    from Products.CMFPlone.utils import getAllowedSizes
except ImportError:
    from plone.app.imaging.utils import getAllowedSizes
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def ImageScaleVocabulary(context):
    allowed_sizes = getAllowedSizes()
    items = [
        (u'%s(%s, %s)' % (key, value[0], value[1]), key)
        for key, value in allowed_sizes.items() if allowed_sizes
    ]
    return SimpleVocabulary.fromItems(items)
