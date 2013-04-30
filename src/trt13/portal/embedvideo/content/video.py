from five import grok
from plone.directives import dexterity
from plone.directives import form
from trt13.portal.embedvideo import embedvideoMessageFactory as _
from zope import schema


class IVideo(form.Schema):
    """A embedded video"""
    pass
    # parameters = schema.TextLine(
    #     title=_(u"URL parameters"),
    #     description=_(u"URL parameters string (after '?')")
    # )

    # height = schema.Int(
    #     title=_(u"Height"),
    # )

    # width = schema.Int(
    #     title=_(u"Width"),
    # )
