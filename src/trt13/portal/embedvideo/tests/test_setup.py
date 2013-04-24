# -*- coding: utf-8 -*-
import unittest

from plone import api
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
