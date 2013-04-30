from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import trt13.portal.embedvideo


TRT13_PORTAL_EMBEDVIDEO = PloneWithPackageLayer(
    zcml_package=trt13.portal.embedvideo,
    zcml_filename='configure.zcml',
    gs_profile_id='trt13.portal.embedvideo:default',
    name="TRT13_PORTAL_EMBEDVIDEO")

TRT13_PORTAL_EMBEDVIDEO_INTEGRATION = IntegrationTesting(
    bases=(TRT13_PORTAL_EMBEDVIDEO, ),
    name="TRT13_PORTAL_EMBEDVIDEO_INTEGRATION")

TRT13_PORTAL_EMBEDVIDEO_FUNCTIONAL = FunctionalTesting(
    bases=(TRT13_PORTAL_EMBEDVIDEO, ),
    name="TRT13_PORTAL_EMBEDVIDEO_FUNCTIONAL")
