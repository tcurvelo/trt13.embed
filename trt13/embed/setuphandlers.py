# -*- coding: utf-8 -*-
import logging

from Products.CMFCore.utils import getToolByName

from Products.GenericSetup.upgrade import listUpgradeSteps


_PROJECT = 'trt13.embed'
_PROFILE_ID = 'trt13.embed:default'


def run_upgrades(context):
    ''' Run Upgrade steps
    '''
    if context.readDataFile('trt13.embed-default.txt') is None:
        return
    logger = logging.getLogger(_PROJECT)
    site = context.getSite()
    setup_tool = getToolByName(site, 'portal_setup')
    version = setup_tool.getLastVersionForProfile(_PROFILE_ID)
    upgradeSteps = listUpgradeSteps(setup_tool, _PROFILE_ID, version)
    sorted(upgradeSteps, key=lambda step: step['sortkey'])

    for step in upgradeSteps:
        oStep = step.get('step')
        if oStep is not None:
            oStep.doStep(setup_tool)
            msg = "Ran upgrade step %s for profile %s" % (oStep.title,
                                                          _PROFILE_ID)
            setup_tool.setLastVersionForProfile(_PROFILE_ID, oStep.dest)
            logger.info(msg)
