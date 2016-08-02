from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.testing import z2

import trt13.embed


class Fixture(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=trt13.embed)
        z2.installProduct(app, 'Products.DateRecurringIndex')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'Products.DateRecurringIndex')

    def setUpPloneSite(self, portal):
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        self.applyProfile(portal, 'trt13.embed:default')
        self.applyProfile(portal, 'plone.app.contenttypes:plone-content')


TRT13_EMBED = Fixture()


TRT13_EMBED_INTEGRATION = IntegrationTesting(
    bases=(TRT13_EMBED, ),
    name="TRT13_EMBED_INTEGRATION")


TRT13_EMBED_FUNCTIONAL = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, TRT13_EMBED, z2.ZSERVER),
    name="TRT13_EMBED_FUNCTIONAL")
