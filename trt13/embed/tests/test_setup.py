# -*- coding: utf-8 -*-
import unittest

from plone import api
from trt13.embed.testing import TRT13_EMBED_INTEGRATION


class TestSetup(unittest.TestCase):
    layer = TRT13_EMBED_INTEGRATION

    def setUp(self):
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_is_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled('trt13.embed')
        )

    def test_uninstall(self):
        self.installer.uninstallProducts(['trt13.embed'])
        self.assertFalse(
            self.installer.isProductInstalled('trt13.embed')
        )

    def test_dependencies_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled('plone.app.dexterity')
        )

    def test_content_types_exist(self):
        types = api.portal.get_tool('portal_types')
        self.assertIn('trt13.embed', types.objectIds())
