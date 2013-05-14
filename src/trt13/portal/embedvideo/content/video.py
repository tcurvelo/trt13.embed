from five import grok
from plone.directives import dexterity
from plone.directives import form
from trt13.portal.embedvideo import embedvideoMessageFactory as _
from zope import schema


class IVideo(form.Schema):
    """A embedded video"""

    height = schema.Int(
        title=_(u"Height"),
    )

    width = schema.Int(
        title=_(u"Width"),
    )

    url = schema.TextLine(
        title=_(u"URL"),
    )

    mimetype = schema.TextLine(
        title=_(u"Mimetype"),
    )


class View(grok.View):
    grok.context(IVideo)
    grok.require("zope2.View")
