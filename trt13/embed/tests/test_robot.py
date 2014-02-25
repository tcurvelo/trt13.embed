import robotsuite
import unittest

from plone.testing import layered
from trt13.embed.testing import TRT13_EMBED_FUNCTIONAL


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('test_embed.robot'),
                layer=TRT13_EMBED_FUNCTIONAL),
    ])
    return suite
