from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.testing import z2
import trt13.embed


TRT13_EMBED = PloneWithPackageLayer(
    zcml_package=trt13.embed,
    zcml_filename='configure.zcml',
    gs_profile_id='trt13.embed:default',
    name="TRT13_EMBED")

TRT13_EMBED_INTEGRATION = IntegrationTesting(
    bases=(TRT13_EMBED, ),
    name="TRT13_EMBED_INTEGRATION")

TRT13_EMBED_FUNCTIONAL = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, TRT13_EMBED, z2.ZSERVER),
    name="TRT13_EMBED_FUNCTIONAL")
