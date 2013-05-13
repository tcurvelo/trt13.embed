import robotsuite
import unittest

from plone.testing import layered
from trt13.portal.embedvideo.testing import TRT13_PORTAL_EMBEDVIDEO_FUNCTIONAL


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('test_embedvideo.robot'),
                layer=TRT13_PORTAL_EMBEDVIDEO_FUNCTIONAL),
    ])
    return suite
