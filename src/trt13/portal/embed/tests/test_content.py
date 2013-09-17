# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from trt13.portal.embed.content import video
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
            type='trt13.portal.embed.video',
            title=u"Motörhead",
            container=self.folder
        )
        v1 = self.folder['motorhead']
        self.assertTrue(video.IVideo.providedBy(v1))
        self.assertTrue(isinstance(v1, video.Video))
        self.assertEquals(u"Motörhead",  v1.title)
