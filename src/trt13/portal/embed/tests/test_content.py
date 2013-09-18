# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from trt13.portal.embed.content import embed
from trt13.portal.embed.testing import TRT13_PORTAL_EMBED_INTEGRATION


class TestContent(unittest.TestCase):
    layer = TRT13_PORTAL_EMBED_INTEGRATION

    def setUp(self):
        self.portal = api.portal.get()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(
            type='Folder',
            title='test-folder',
            container=self.portal
        )
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        api.content.create(
            type='trt13.portal.embed.embed',
            title=u"Motörhead",
            container=self.folder
        )
        e1 = self.folder['motorhead']
        self.assertTrue(embed.IEmbed.providedBy(e1))
        self.assertTrue(isinstance(e1, embed.Embed))
        self.assertEquals(u"Motörhead",  e1.title)
