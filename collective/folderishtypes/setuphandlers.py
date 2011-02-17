import logging
from Products.CMFCore.utils import getToolByName
from collective.folderishtypes.content.folderish_event import FolderishEvent

logger = logging.getLogger('collective.folderishtypes')

def isNotThisProfile(context, marker_file):
    return context.readDataFile(marker_file) is None

def setup(context):
    """ Configures Products.CMFPlone.CalendarTool
    """
    if isNotThisProfile(context,
                        'collective.folderishtypes-default.txt'): return
    site = context.getSite()
    calendar_tool = getToolByName(site, 'portal_calendar')
    calendar_tool.calendar_types += (FolderishEvent.portal_type,)
    logger.info('added type %s to calendar_types' % FolderishEvent.portal_type)
