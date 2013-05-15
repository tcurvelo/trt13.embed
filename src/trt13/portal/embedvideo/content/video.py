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


@form.default_value(field=IVideo['height'])
@form.default_value(field=IVideo['width'])
@form.default_value(field=IVideo['url'])
@form.default_value(field=IVideo['mimetype'])
def defaultValue(data):
    context = data.context
    if IVideo.providedBy(context):
        return getattr(context, data.field.getName())
    else:
        return data.field.default


class Video(dexterity.Container):
    grok.implements(IVideo)


class View(grok.View):
    grok.context(IVideo)
    grok.require("zope2.View")
