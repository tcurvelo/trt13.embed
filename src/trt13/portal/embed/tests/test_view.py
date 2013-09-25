# -*- coding: utf-8 -*-
import unittest

from plone import api
from trt13.portal.embed.testing import TRT13_PORTAL_EMBED_INTEGRATION
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestView(unittest.TestCase):
    layer = TRT13_PORTAL_EMBED_INTEGRATION

    def setUp(self):
        self.portal = api.portal.get()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        api.content.create(
            type='Folder',
            title='test-folder',
            container=self.portal
        )
        self.folder = self.portal['test-folder']

        api.content.create(
            type='trt13.portal.embed.embed',
            title=u"Audiencia",
            container=self.folder
        )
        self.video = self.folder['audiencia']

        api.content.create(
            type='trt13.portal.embed.embed',
            title=u"Qualidade Baixa",
            container=self.video
        )

        setRoles(self.portal, TEST_USER_ID, ['Member'])

    def test_player_subview(self):
        baixa = self.video['qualidade-baixa']

        baixa.description = "video com qualidade mais baixa"
        baixa.url = "mms://localhost/video.wmv"
        baixa.height = 180
        baixa.width = 320
        baixa.mimetype = "application/pdf"
        baixa.parameters = ["foo|bar"]

        request = self.layer['request']
        request["QUERY_STRING"] = "ajax_load=true"

        player = api.content.get_view(
            "view",
            self.video['qualidade-baixa'],
            request)

        self.assertIn(
            """<object id="trt13_portal_embed_object" standby="video com qualidade mais baixa" width="320" height="180" type="application/pdf" data="mms://localhost/video.wmv">

            <param name="foo" value="bar" />

            <embed id="trt13_portal_embed_embed"
                src="mms://localhost/video.wmv"
                width="320" height="180"
                type="application/pdf"
                foo="bar">
            </embed>

        </object>""",
            player()
        )
