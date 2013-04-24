# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from trt13.portal.embedvideo.testing import TRT13_PORTAL_EMBEDVIDEO_INTEGRATION


class TestSample(unittest.TestCase):
    layer = TRT13_PORTAL_EMBEDVIDEO_INTEGRATION

    def setUp(self):
        self.qi_tool = api.portal.get_tool('portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'trt13.portal.embedvideo'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')


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
            title='v1',
            container=self.folder
        )

    #     v1 = self.folder['v1']
    #     self.assertTrue(IEmbedVideo.providedBy(v1))

    # def test_default_values_for_checkboxes(self):
    #     self.folder.invokeFactory('trt13.portal.embedvideo.video', 'p1')
    #     p1 = self.folder['p1']
    #     self.assertTrue(p1.allow_anonymous)
    #     self.assertTrue(p1.show_results)

    # def test_fti(self):
    #     fti = queryUtility(IDexterityFTI, name='trt13.portal.embedvideo.video')
    #     self.assertNotEquals(None, fti)

    # def test_schema(self):
    #     fti = queryUtility(IDexterityFTI, name='trt13.portal.embedvideo.video')
    #     schema = fti.lookupSchema()
    #     self.assertEquals(IEmbedVideo, schema)

    # def test_factory(self):
    #     fti = queryUtility(IDexterityFTI, name='trt13.portal.embedvideo.video')
    #     factory = fti.factory
    #     new_object = createObject(factory)
    #     self.assertTrue(IEmbedVideo.providedBy(new_object))