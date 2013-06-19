# -*- coding: utf-8 -*-
import unittest

from plone import api
from trt13.portal.embedvideo.testing import TRT13_PORTAL_EMBEDVIDEO_INTEGRATION
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestView(unittest.TestCase):
    layer = TRT13_PORTAL_EMBEDVIDEO_INTEGRATION

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
            type='trt13.portal.embedvideo.video',
            title=u"Audiencia",
            container=self.folder
        )
        self.video = self.folder['audiencia']

        api.content.create(
            type='trt13.portal.embedvideo.video',
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

        request = self.layer['request']
        request["QUERY_STRING"] = "ajax_load=true"

        player = api.content.get_view(
            "view",
            self.video['qualidade-baixa'],
            request)

        self.assertIn(
            """<object name="trt13_portal_embedvideo_player" standby="video com qualidade mais baixa" width="320" height="180" type="application/pdf">

          <param name="URL" value="mms://localhost/video.wmv">
          <param name="AnimationAtStart" value="false">
          <param name="AutoSize" value="0">
          <param name="AutoStart" value="true">
          <param name="ShowControls" value="true">
          <param name="ShowDisplay" value="0">
          <param name="ShowStatusBar" value="1">
          <param name="StretchToFit" value="True">
          <param name="TransparentAtStart" value="true">

          <embed id="trt13_portal_embedvideo_player_embed" name="trt13_portal_embedvideo_player_embed" src="mms://localhost/video.wmv" type="application/pdf" width="320" height="180" autosize="0" autostart="1" bgcolor="darkblue" displaysize="4" loop="0" showcontrols="1" showdisplay="0" showstatusbar="1" showtracker="0" stretchtofit="1" videoborder3d="0">
          </embed>
        </object>""",
            player()
        )
