from five import grok
from plone.directives import dexterity
from plone.directives import form
from trt13.portal.embedvideo import embedvideoMessageFactory as _
from zope import schema


class IVideo(form.Schema):
    """A embedded video"""

    height = schema.Int(
        title=_(u"Height"),
        required=False
    )

    width = schema.Int(
        title=_(u"Width"),
        required=False
    )

    url = schema.TextLine(
        title=_(u"URL"),
        required=False
    )

    mimetype = schema.TextLine(
        title=_(u"Mimetype"),
        required=False
    )


class Video(dexterity.Container):
    grok.implements(IVideo)


class View(grok.View):
    grok.context(IVideo)
    grok.require("zope2.View")
