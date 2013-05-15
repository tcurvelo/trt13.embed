# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from trt13.portal.embedvideo.content import video
from trt13.portal.embedvideo.testing import TRT13_PORTAL_EMBEDVIDEO_INTEGRATION


class TestContent(unittest.TestCase):
    layer = TRT13_PORTAL_EMBEDVIDEO_INTEGRATION

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
            type='trt13.portal.embedvideo.video',
            title=u"Motörhead",
            container=self.folder
        )
        v1 = self.folder['motorhead']
        self.assertTrue(video.IVideo.providedBy(v1))
        self.assertTrue(isinstance(v1, video.Video))
        self.assertEquals(u"Motörhead",  v1.title)

    def test_adding_a_video_inside_another_and_acquisition(self):
        api.content.create(
            type='trt13.portal.embedvideo.video',
            title=u"Audiência",
            url="http://plone.org",
            height=200,
            width=200,
            container=self.folder
        )
        video_pai = self.folder['audiencia']

        api.content.create(
            type='trt13.portal.embedvideo.video',
            title=u"Qualidade Baixa",
            height=50,
            width=50,
            container=video_pai
        )
        alternativo = video_pai['qualidade-baixa']
        self.assertTrue(video.IVideo.providedBy(alternativo))
        self.assertEquals(u"Qualidade Baixa",  alternativo.title)
        self.assertEquals(50,  alternativo.height)
        self.assertEquals(50,  alternativo.width)
        # URL adquirida do pai
        self.assertEquals("http://plone.org", alternativo.url)
