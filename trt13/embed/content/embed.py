from five import grok
from plone import api
from plone.directives import dexterity
from plone.directives import form
from trt13.embed import embedMessageFactory as _
from zope import schema


class IEmbed(form.Schema):
    """Um conteudo embarcado"""

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

    parameters = schema.List(
        title=_(u"Parameters"),
        description=_(u"Please inform the parameters, one per line, in the"
                      u"format 'name|value'"),
        value_type=schema.TextLine(),
        required=False
    )


@form.default_value(field=IEmbed['height'])
@form.default_value(field=IEmbed['width'])
@form.default_value(field=IEmbed['url'])
@form.default_value(field=IEmbed['mimetype'])
@form.default_value(field=IEmbed['parameters'])
def defaultValue(data):
    context = data.context
    if IEmbed.providedBy(context):
        return getattr(context, data.field.getName())
    else:
        return data.field.default


class Embed(dexterity.Container):
    grok.implements(IEmbed)

    def tag(self, scale, css_class):
        if self.image_thumb:
            return """
                <a href="{0}">
                    <img src="{0}/@@images/image_thumb" alt="{1}" title="{1}"
                        class="{2}"
                        height="84" width="128"/>
                </a>
            """.format(self.absolute_url(), self.image_caption, css_class)
        else:
            return

    def get_parameters(self):
        params = []
        if self.parameters:
            for param_line in self.parameters:
                param = param_line.split('|', 1)
                params.append({
                    "name": param[0],
                    "value": param[1] if len(param) > 1 else param[0]
                })
        return params


class View(grok.View):
    grok.context(IEmbed)
    grok.require("zope2.View")

    def alternatives(self):
        if not hasattr(self, '__alternatives') or not self.__alternatives:
            catalog = api.portal.get_tool(name='portal_catalog')
            folder_path = '/'.join(self.context.getPhysicalPath())

            self.__alternatives = [
                result.getObject()
                for result in catalog.searchResults(
                    path={'query': folder_path},
                    portal_type='trt13.embed.embed'
                )
                if result.getPath() != folder_path
            ]
        return self.__alternatives

    def embed_tag(self):

        parameters_as_atributtes = " ".join(
            '{}="{}"'.format(item["name"], item["value"])
            for item in self.context.get_parameters()
        )

        return """<embed class="trt13_embed"
                src="{}"
                width="{}" height="{}"
                type="{}"
                {}>
            </embed>""".format(
            self.context.url,
            self.context.width,
            self.context.height,
            self.context.mimetype,
            parameters_as_atributtes
        )
